import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Read the data
data = pd.read_csv('traffic_signal_data.csv')

X = data[['cycle_length', 'lane1_present_num_vehicles', 'lane2_present_num_vehicles', 
          'lane3_present_num_vehicles', 'lane4_present_num_vehicles',
          'lane1_upcoming_num_vehicles', 'lane2_upcoming_num_vehicles',
          'lane3_upcoming_num_vehicles', 'lane4_upcoming_num_vehicles',
          'ew_present_waiting_times', 'time_of_day', 'flow_ratios']]
y_p_ew = data['ew_present_green_time']  
y_p_ns = data['ns_present_green_time']  
y_u_ew = data['ew_upcoming_green_time']  
y_u_ns = data['ns_upcoming_green_time'] 

X_train, X_test, y_p_ew_train, y_p_ew_test = train_test_split(X, y_p_ew, test_size=0.2, random_state=42)
_, _, y_p_ns_train, y_p_ns_test = train_test_split(X, y_p_ns, test_size=0.2, random_state=42)
_, _, y_u_ew_train, y_u_ew_test = train_test_split(X, y_u_ew, test_size=0.2, random_state=42)
_, _, y_u_ns_train, y_u_ns_test = train_test_split(X, y_u_ns, test_size=0.2, random_state=42)

model_p_ew = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model_p_ns = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model_u_ew = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model_u_ns = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

model_p_ew.fit(X_train, y_p_ew_train)
model_p_ns.fit(X_train, y_p_ns_train)
model_u_ew.fit(X_train, y_u_ew_train)
model_u_ns.fit(X_train, y_u_ns_train)

y_p_ew_pred = model_p_ew.predict(X_test)
y_p_ns_pred = model_p_ns.predict(X_test)
y_u_ew_pred = model_u_ew.predict(X_test)
y_u_ns_pred = model_u_ns.predict(X_test)

mse_p_ew = mean_squared_error(y_p_ew_test, y_p_ew_pred)
mse_p_ns = mean_squared_error(y_p_ns_test, y_p_ns_pred)
mse_u_ew = mean_squared_error(y_u_ew_test, y_u_ew_pred)
mse_u_ns = mean_squared_error(y_u_ns_test, y_u_ns_pred)

print(f'Mean Squared Error (P_EW): {mse_p_ew}')
print(f'Mean Squared Error (P_NS): {mse_p_ns}')
print(f'Mean Squared Error (U_EW): {mse_u_ew}')
print(f'Mean Squared Error (U_NS): {mse_u_ns}')

new_data = pd.DataFrame({
    'cycle_length': [120],
    'lane1_present_num_vehicles': [46],
    'lane2_present_num_vehicles': [48],
    'lane3_present_num_vehicles': [52],
    'lane4_present_num_vehicles': [54],
    'lane1_upcoming_num_vehicles': [78],  
    'lane2_upcoming_num_vehicles': [14],
    'lane3_upcoming_num_vehicles': [82],
    'lane4_upcoming_num_vehicles': [12],
    'ew_present_waiting_times': [40],
    'time_of_day': [10],
    'flow_ratios': [1.0]
})

predicted_ew_present_green_time = model_p_ew.predict(new_data)
predicted_ns_present_green_time = model_p_ns.predict(new_data)
predicted_ew_upcoming_green_time = model_u_ew.predict(new_data)
predicted_ns_upcoming_green_time = model_u_ns.predict(new_data)

print(f'Predicted Present  EW Green Time: {predicted_ew_present_green_time[0]} seconds')
print(f'Predicted Present  NS Green Time: {predicted_ns_present_green_time[0]} seconds')
print(f'Predicted Upcoming EW Green Time: {predicted_ew_upcoming_green_time[0]} seconds')
print(f'Predicted Upcoming NS Green Time: {predicted_ns_upcoming_green_time[0]} seconds')

if (predicted_ew_upcoming_green_time[0] > predicted_ew_present_green_time[0]):
    ew_green_time = (predicted_ew_present_green_time[0] * 0.5) + (predicted_ew_upcoming_green_time[0] * 0.5)
else:
    ew_green_time = predicted_ew_present_green_time[0]
    
if (predicted_ns_upcoming_green_time[0] > predicted_ns_present_green_time[0]):
    ns_green_time = (predicted_ns_present_green_time[0] * 0.5) + (predicted_ns_upcoming_green_time[0] * 0.5)
else:
    ns_green_time = predicted_ns_present_green_time[0]
    
print(f'EW Green Time: {ew_green_time} seconds')
print(f'NS Green Time: {ns_green_time} seconds')

