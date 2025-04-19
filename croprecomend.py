import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import pickle
import io
from appwrite.services.storage import Storage
from appwrite.exception import AppwriteException

def read_csv_from_appwrite(storage, bucket_id, file_id):
    try:
        response = storage.get_file_download(bucket_id=bucket_id, file_id=file_id)
        return pd.read_csv(io.BytesIO(response))
    except AppwriteException as e:
        print(f"Failed to read CSV from Appwrite: {e}")
        return None

def apply(client,bucket_id):
    try:
        # Load the pickled feature input
        with open("feature.pickle", "rb") as pickle_in:
            feature = pickle.load(pickle_in)

        Day = int(feature[0])
        Month = int(feature[1])
        District = feature[2]

        # Setup Appwrite storage
        storage = Storage(client)

        # Replace with your actual file IDs
        cropdb_file_id = '6802209b0008c93e197f'
        climate_file_id = '680220a9002d1ffda549'
        regressiondb_file_id = '6802204e002477a8bc95'
        # bucket_id = bucket_id

        df_crops = read_csv_from_appwrite(storage, bucket_id, cropdb_file_id)
        df_climate = read_csv_from_appwrite(storage, bucket_id, climate_file_id)
        dataset = read_csv_from_appwrite(storage, bucket_id, regressiondb_file_id)

        if df_crops is None or df_climate is None or dataset is None:
            print("Could not load required CSV files.")
            return

        crops = set()
        available_crops = set()

        for _, row in df_crops.iterrows():
            if Month == row['Month'] and (row['Day'] >= Day or row['Day'] == 0):
                if row['Crop'] in ['Aus', 'Aman', 'Boro']:
                    available_crops.add(row['Crop'])
                    crops.add('Rice')
                else:
                    available_crops.add(row['Crop'])
                    crops.add(row['Crop'])

        Ph = df_climate[(df_climate.City == District) & (df_climate.Month == Month)]["PH"].values
        Avg_temp = 0
        Avg_rainfall = 0
        n = 5

        for i in range(n):
            rainfall = df_climate[(df_climate.City == District) & (df_climate.Month == Month)]["Rainfall"].values
            max_temp = df_climate[(df_climate.City == District) & (df_climate.Month == Month)]["Max Temp"].values
            min_temp = df_climate[(df_climate.City == District) & (df_climate.Month == Month)]["Min Temp"].values
            Avg_temp += (max_temp + min_temp) / 2
            Avg_rainfall += rainfall
            Month += 1
            if Month > 12:
                Month = Month % 12 + 1

        Avg_temp = Avg_temp / n

        df_user = pd.DataFrame({
            'Rainfall': [Avg_rainfall[0] if len(Avg_rainfall) else 0],
            'Temp': [Avg_temp[0] if len(Avg_temp) else 0],
            'Ph': [Ph[0] if len(Ph) else 7]  # default to 7 if no data
        })

        highly_rec = []
        rec = []
        not_rec = []

        for crop in crops:
            temp_df = dataset[dataset['Crop'] == crop]
            X = temp_df[['Rainfall', 'Temperature', 'Ph']].values
            y = temp_df[['Production']].values

            X_train, _, y_train, _ = train_test_split(X, y, test_size=0.1, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)

            y_pred = regressor.predict(df_user)
            res = float(y_pred)

            if res > 3:
                highly_rec.append(crop)
            elif 0 < res <= 3:
                rec.append(crop)
            else:
                not_rec.append(crop)

        # Reset Month to original for output
        Month = int(feature[1])
        final_output = [available_crops, highly_rec, rec, not_rec, Day, Month, District]

        with open("model_output.pickle", "wb") as pickle_out:
            pickle.dump(final_output, pickle_out)

        return

    except Exception as e:
        print(f"Unexpected error in apply(): {e}")
        return
