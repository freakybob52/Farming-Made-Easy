from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    # Appwrite settings
    APPWRITE_ENDPOINT = os.getenv("APPWRITE_ENDPOINT")
    APPWRITE_PROJECT_ID = os.getenv("APPWRITE_PROJECT_ID")
    APPWRITE_BUCKET_ID = os.getenv("APPWRITE_BUCKET_ID")


    # Commodity IDs (optional)
    ARHAR_ID = os.getenv("ARHAR_ID")
    BAJRA_ID = os.getenv("BAJRA_ID")
    BARLEY_ID = os.getenv("BARLEY_ID")
    COPRA_ID = os.getenv("COPRA_ID")
    COTTON_ID = os.getenv("COTTON_ID")
    SESAMUM_ID = os.getenv("SESAMUM_ID")
    GRAM_ID = os.getenv("GRAM_ID")
    GROUNDNUT_ID = os.getenv("GROUNDNUT_ID")
    JOWAR_ID = os.getenv("JOWAR_ID")
    MAIZE_ID = os.getenv("MAIZE_ID")
    MASOOR_ID = os.getenv("MASOOR_ID")
    MOONG_ID = os.getenv("MOONG_ID")
    NIGER_ID = os.getenv("NIGER_ID")
    PADDY_ID = os.getenv("PADDY_ID")
    RAGI_ID = os.getenv("RAGI_ID")
    RAPE_ID = os.getenv("RAPE_ID")
    JUTE_ID = os.getenv("JUTE_ID")
    SAFFLOWER_ID = os.getenv("SAFFLOWER_ID")
    SOYABEAN_ID = os.getenv("SOYABEAN_ID")
    SUGARCANE_ID = os.getenv("SUGARCANE_ID")
    SUNFLOWER_ID = os.getenv("SUNFLOWER_ID")
    URAD_ID = os.getenv("URAD_ID")
    WHEAT_ID = os.getenv("WHEAT_ID")
