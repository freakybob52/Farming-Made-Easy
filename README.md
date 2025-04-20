# Agro Genius

Agro Genius is a comprehensive agricultural assistance web application designed to empower farmers with data-driven insights, predictions, and recommendations to optimize their farming practices and increase productivity.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Authentication](#authentication)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)

## Overview

Agro Genius leverages machine learning, real-time weather data, and agricultural expertise to provide farmers with a powerful toolset for making informed decisions about their crops, fertilizers, and farming practices.


## Key Features

### 🌱 Crop Recommendation
Suggests optimal crops based on soil analysis, climate conditions, and historical yield data.

![Crop Recommendation Screenshot](/readmeImgs/cropRecom.png)

### 📊 Crop Price Prediction
Analyzes market trends to forecast future crop prices, helping farmers plan harvests for maximum profit.

![Price Prediction Screenshot](/readmeImgs/cropPricePred.png)

### 🌤️ Weather Prediction
Provides localized weather forecasts essential for crop management and planning farming activities.

![Weather Forecast Screenshot](/readmeImgs/weatherPred.png)

### 📚 Information Guide
Comprehensive knowledge base offering best practices for various crops, pest management, and sustainable farming techniques.

![Information Guide Screenshot](/readmeImgs/guide.png)

### 🧪 Fertilizer Recommendation
Suggests optimal fertilizer usage based on crop needs and soil conditions to maximize yield while minimizing environmental impact.

![Fertilizer Recommendation Screenshot](/readmeImgs/fertilizerRecom.png)

### 🛒 Agriculture Shops
Locates nearby agricultural supply stores based on the user's location, making it easy to source necessary farming inputs.

![Agriculture Shops Screenshot](/readmeImgs/shops.png)

## Architecture

Agro Genius follows a modular architecture designed for scalability and maintainability

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Jinja2 Templates
- **Appwrite Cloud**:
  - Authentication (including Google OAuth2)
  - Database
  - Storage for files and assets
- **Machine Learning**: scikit-learn, TensorFlow, Pandas, NumPy
- **Weather API**: OpenWeatherMap API
- **Geolocation**: Google Maps API

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment
- Appwrite account and project

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

### Step 5: Set up Appwrite
1. Create an Appwrite project in the [Appwrite Console](https://appwrite.io/)
2. Set up authentication methods (Email/Password and Google OAuth2)
3. Create necessary database collections
4. Create a storage bucket for file uploads

### Step 6: Set up environment variables
Create a `.env` file in the root directory and add the necessary environment variables:
```bash
# Appwrite Configuration
APPWRITE_ENDPOINT=your_appwrite_endpoint
APPWRITE_PROJECT_ID=your_appwrite_project_id
APPWRITE_BUCKET_ID=your_appwrite_bucket_id

```

### Step 7: Run the application
```bash
pyhon app.py
```

Visit `http://localhost:5000` in your browser to access Agro Genius.

## Authentication

Agro Genius leverages Appwrite's authentication service to provide:

### Google OAuth2 
Users can quickly sign in with their Google accounts for seamless access.

![Google OAuth Screenshot](/readmeImgs/login.png)

### Traditional Login/Signup
Users can also create dedicated accounts using email and password authentication.

![Login/Signup Screenshot](/readmeImgs/signup.png)

## Modules

### Crop Recommendation Module
- Takes soil parameters, location data, and season information as inputs
- Uses a trained linear regression model to predict suitable crops
- Displays recommendations with expected yield values

### Crop Price Prediction Module
- Collects and pre-processes historical price data
- Builds prediction models using time-series analysis
- Provides forecasted prices for selected crops

### Weather Prediction Module
- Integrates with weather APIs to fetch real-time and forecasted weather data
- Extracts location information for precise forecasts
- Presents easy-to-understand weather information relevant to farming decisions

### Information Guide
- Offers multilingual support for accessibility
- Provides comprehensive guides on various farming techniques and crop management

### Fertilizer Recommendation Module
- Analyzes crop needs and soil conditions
- Finds optimal fertilizer compositions from a comprehensive database
- Provides detailed recommendations with application guidelines

### Agriculture Shops Module
- Uses location data to find nearby agricultural supply stores
- Displays shop information with directions and available products

## Contributing

We welcome contributions to Agro Genius! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
