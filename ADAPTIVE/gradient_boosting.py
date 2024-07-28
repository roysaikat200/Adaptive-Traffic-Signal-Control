import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Read the data
data = pd.read_csv('traffic_signal_data.csv')

# Define features and target variables
X = data[['cycle_length', 'lane1_num_vehicles', 'lane2_num_vehicles', 'lane3_num_vehicles', 'lane4_num_vehicles', 'ew_waiting_times', 'time_of_day', 'flow_ratios']]
y_ew = data['ew_green_time']  # East-West green time
y_ns = data['ns_green_time']  # North-South green time

# Split the data into training and testing sets
X_train, X_test, y_ew_train, y_ew_test, y_ns_train, y_ns_test = train_test_split(X, y_ew, y_ns, test_size=0.2, random_state=42)

# Define and train the Gradient Boosting Regressor models for EW and NS directions
model_ew = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model_ns = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

model_ew.fit(X_train, y_ew_train)
model_ns.fit(X_train, y_ns_train)

# Predict green times for EW and NS directions
y_ew_pred = model_ew.predict(X_test)
y_ns_pred = model_ns.predict(X_test)

# Compute mean squared error for EW and NS directions
mse_ew = mean_squared_error(y_ew_test, y_ew_pred)
mse_ns = mean_squared_error(y_ns_test, y_ns_pred)

print(f'Mean Squared Error (EW): {mse_ew}')
print(f'Mean Squared Error (NS): {mse_ns}')

# Create new data for prediction
new_data = pd.DataFrame({
    'cycle_length': [120],
    'lane1_num_vehicles': [78],
    'lane2_num_vehicles': [52],
    'lane3_num_vehicles': [82],
    'lane4_num_vehicles': [54],
    'ew_waiting_times': [40],
    'time_of_day': [10],
    'flow_ratios': [1.0]
})

# Predict green times for the new data
predicted_ew_green_time = model_ew.predict(new_data)
predicted_ns_green_time = model_ns.predict(new_data)

print(f'Predicted EW Green Time: {predicted_ew_green_time[0]} seconds')
print(f'Predicted NS Green Time: {predicted_ns_green_time[0]} seconds')



