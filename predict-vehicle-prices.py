import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("dataset.csv")

# Drop rows where price is missing (target variable)
df = df.dropna(subset=['price'])

# Handle missing values
num_cols = ['cylinders', 'mileage', 'doors']
imputer = SimpleImputer(strategy='median')
df[num_cols] = imputer.fit_transform(df[num_cols])

cat_cols = ['engine', 'fuel', 'transmission', 'trim', 'body', 'exterior_color', 'interior_color']
df[cat_cols] = df[cat_cols].fillna('Unknown')

# One-hot encoding
encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
encoded_features = encoder.fit_transform(df[cat_cols])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(cat_cols))

# Combine processed data
df_processed = pd.concat([df[['year', 'cylinders', 'mileage', 'doors', 'price']], encoded_df], axis=1)

# Fill remaining NaNs (if any)
df_processed = df_processed.fillna(0)

# Split data
X = df_processed.drop(columns=['price'])
y = df_processed['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Print results
print(f"Mean Absolute Error: ${mae:.2f}")
print(f"Root Mean Squared Error: ${rmse:.2f}")
print(f"R² Score: {r2:.3f}")
