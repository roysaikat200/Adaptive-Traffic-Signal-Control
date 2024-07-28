import numpy as np
import pandas as pd

np.random.seed(42)

num_data_points = 100000

cycle_length = 120
lane1_num_vehicles = np.random.randint(5, 75, num_data_points)
lane2_num_vehicles = np.random.randint(5, 75, num_data_points)
lane3_num_vehicles = np.random.randint(5, 75, num_data_points)
lane4_num_vehicles = np.random.randint(5, 75, num_data_points)
ew_waiting_times = np.random.randint(10, 60, num_data_points)
flow_ratios = np.random.uniform(0.2, 1.0, num_data_points)
time_of_day = np.random.randint(0, 24, num_data_points)

def calculate_ew_green_time(lane1_num_vehicles, lane3_num_vehicles, cycle_length, prev_waiting_time, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
    
    ew_green_time = cycle_length * (max(lane1_num_vehicles, lane3_num_vehicles) / (flow_ratio * cycle_length)) + (prev_waiting_time * 0.05)
    
    return ew_green_time

def calculate_ns_green_time(lane2_num_vehicles, lane4_num_vehicles, cycle_length, prev_waiting_time, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
    
    ns_green_time = cycle_length * (max(lane2_num_vehicles, lane4_num_vehicles) / (flow_ratio * cycle_length)) + (prev_waiting_time * 0.05)
    
    return ns_green_time
    
ew_green_time = np.zeros(num_data_points)
ns_green_time = np.zeros(num_data_points)

for i in range(num_data_points):
    ew_green_time[i] = calculate_ew_green_time(lane1_num_vehicles[i], lane3_num_vehicles[i], cycle_length, ew_waiting_times[i], time_of_day[i], flow_ratios[i])
    ns_green_time[i] = calculate_ns_green_time(lane2_num_vehicles[i], lane4_num_vehicles[i], cycle_length, ew_green_time[i], time_of_day[i], flow_ratios[i])

data = pd.DataFrame({
    'cycle_length': cycle_length,
    'lane1_num_vehicles': lane1_num_vehicles,
    'lane2_num_vehicles': lane2_num_vehicles,
    'lane3_num_vehicles': lane3_num_vehicles,
    'lane4_num_vehicles': lane4_num_vehicles,
    'ew_waiting_times': ew_waiting_times,
    'ns_waiting_times': ew_green_time,
    'time_of_day' : time_of_day,
    'flow_ratios' : flow_ratios,
    'ew_green_time': ew_green_time,
    'ns_green_time': ns_green_time,
})

print(data.head())

data.to_csv('traffic_signal_data.csv', index=False)