
# Farming Made Easy

**Farming Made Easy** is a web application designed to help farmers by providing crop recommendations, prediction models, and other useful information. The system uses machine learning to predict the best crops based on various factors like soil, climate, and weather data.

## Features

- **Crop Recommendation System**: Suggests suitable crops based on the user's location and preferences.
- **Predictive Modeling**: Uses a decision tree regression model to predict the yields of various crops.
- **Appwrite Integration**: Utilizes Appwrite for authentication and file storage.
- **Error Handling**: Custom error pages (e.g., for 404 errors) for a better user experience.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Jinja2**: Template engine for rendering HTML.
- **Appwrite**: Cloud platform for backend services (e.g., file storage and authentication).
- **scikit-learn**: Machine learning library used for building prediction models.
- **Pandas**: Data manipulation library used for handling datasets.
- **NumPy**: Library used for numerical computations.

## Project Structure

```
Farming_Made_Easy/
│
├── app.py             # Main Flask application
├── api/               # API routes and logic
├── static/            # Static files (images)
├── templates/         # Jinja2 templates (HTML files)
│   └── 404.html       # Custom error page for 404
├── venv/              # Virtual environment
├── config.py          # Configuration settings
├── requirements.txt   # Python dependencies
└── .env               # Environment variables
```

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/athrocks/Farming-Made-Easy.git
cd Farming-Made-Easy
```

### Step 2: Set up a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

- **Windows**:

```bash
venv\Scripts\activate
```

- **Mac/Linux**:

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Set up environment variables

Create a `.env` file in the root directory and add the necessary environment variables. For example:

```bash
APPWRITE_ENDPOINT="your endpoint"
APPWRITE_PROJECT_ID="your-appwrite-project-id"
APPWRITE_BUCKET_ID="your-appwrite-bucket-id"
```

### Step 6: Run the application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to see the app in action.

## Contributing

Feel free to fork this project, make changes, and submit pull requests. If you find any bugs or want to suggest improvements, please open an issue.

## License

This project is licensed under the MIT License.
