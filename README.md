# 🚗 Parking Revenue Growth Prediction API

An end-to-end Machine Learning solution designed to forecast daily revenue and analyze growth trends for parking facilities. This project demonstrates a full data pipeline: from **PostgreSQL** data extraction and **Time-Series Feature Engineering** to a production-ready **FastAPI** deployment.



## 🌟 Business Value
Predicting parking revenue allows management to:
* **Optimize Staffing:** Align workforce with predicted high-volume days.
* **Financial Planning:** Forecast monthly growth and identify underperforming locations.
* **Dynamic Decision Making:** Use data-driven insights to adjust parking rates or marketing efforts.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Machine Learning:** XGBoost (Gradient Boosting Regressor)
* **API Framework:** FastAPI, Uvicorn
* **Data Handling:** Pandas, SQLAlchemy, Scikit-learn
* **Database:** PostgreSQL
* **Environment:** Dotenv for secure credential management

## 📂 Project Structure
```text
parking-revenue-ai/
├── models/             # Saved model artifacts (.pkl)
├── notebooks/          # Training & Exploratory Data Analysis (EDA)
├── src/                # Core logic (Database & Processing)
│   ├── database.py     # SQL Connection engine
│   └── processor.py    # Feature engineering logic
├── main.py             # FastAPI entry point
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 📊 Feature Engineering Logic

The model's accuracy (approx. 92% MAPE) is driven by specialized time-series features:

Lag Features (rev_lag_1, rev_lag_7): Captures daily momentum and weekly seasonality.

Rolling Mean (rev_rolling_7): Smooths out random noise to identify the underlying trend.

Temporal Indicators: Day of week, Month, and Weekend flags to capture human behavior patterns.

## 🚀 Getting Started
1. Setup Environment
git clone [https://github.com/your-username/parking-revenue-ai.git](https://github.com/your-username/parking-revenue-ai.git)
cd parking-revenue-ai
pip install -r requirements.txt

2. Database Configuration
Create a .env file in the root directory:
DB_SERVER=your_host:port
DB_USER=your_user
DB_PASSWORD=your_password
DB_DATABASE=your_db

3. Training & Deployment
Open notebooks/train_model.ipynb and run all cells to train and export the model to /models.

Launch the API:
python main.py
Visit http://localhost:8000/docs to test the API via Swagger UI.