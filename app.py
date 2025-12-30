import os
import pandas as pd
import numpy as np
import joblib

print("Real Estate Price Predictor")

# 1️ Load trained Random Forest model

model_path = os.path.join(os.path.dirname(__file__), "data", "model", "house_price_model.pkl")
model = joblib.load(model_path)


# 2️ Load dataset

data_path = os.path.join(os.path.dirname(__file__), "data", "California_housing.csv")
df = pd.read_csv(data_path)


# 3️ User input

longitude = float(input("Enter longitude: "))
latitude = float(input("Enter latitude: "))
median_income = float(input("Enter median income: "))
housing_median_age = float(input("Enter housing median age: "))
total_rooms = float(input("Enter total rooms: "))
population = float(input("Enter population: "))
households = float(input("Enter households: "))


# 4️ Feature engineering (same as training)

rooms_per_household = total_rooms / households
population_per_household = population / households

input_data = np.array([[median_income, housing_median_age,
                        rooms_per_household, population_per_household,
                        longitude, latitude]])


# 5️ Random Forest Prediction

predicted_price = model.predict(input_data)
print(f"\n Predicted House Price using ML model: ${round(predicted_price[0], 2)}")


# 6️ Location-based Average Price

# Distance from user location
df['distance'] = np.sqrt((df['longitude'] - longitude)**2 +
                         (df['latitude'] - latitude)**2)

# Nearest 100 houses
nearest_houses = df.sort_values('distance').head(100)

# Average price
average_price = nearest_houses['median_house_value'].mean()

print(f" Estimated Average House Price for nearby houses: ${round(average_price, 2)}")





