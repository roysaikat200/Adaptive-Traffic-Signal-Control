import numpy as np
import pandas as pd

np.random.seed(42)

num_data_points = 100000

cycle_length = 120
lane1_upcoming_num_vehicles = np.random.randint(5, 75, num_data_points)
lane2_upcoming_num_vehicles = np.random.randint(5, 75, num_data_points)
lane3_upcoming_num_vehicles = np.random.randint(5, 75, num_data_points)
lane4_upcoming_num_vehicles = np.random.randint(5, 75, num_data_points)

# Shift the upcoming to present for the next day (simulate this by copying the array)
lane1_present_num_vehicles = np.roll(lane1_upcoming_num_vehicles, 1)
lane2_present_num_vehicles = np.roll(lane2_upcoming_num_vehicles, 1)
lane3_present_num_vehicles = np.roll(lane3_upcoming_num_vehicles, 1)
lane4_present_num_vehicles = np.roll(lane4_upcoming_num_vehicles, 1)

# For the first day, you could copy the upcoming to present directly or initialize it differently
# Here, just copying for simplicity
lane1_present_num_vehicles[0] = np.random.randint(5, 75)
lane2_present_num_vehicles[0] = np.random.randint(5, 75)
lane3_present_num_vehicles[0] = np.random.randint(5, 75)
lane4_present_num_vehicles[0] = np.random.randint(5, 75)

# The rest of the vehicle-related data generation remains the same
ew_present_waiting_times = np.random.randint(10, 60, num_data_points)
ns_present_waiting_times = np.random.randint(10, 60, num_data_points)
ew_upcoming_waiting_times = np.random.randint(10, 60, num_data_points)
ns_upcoming_waiting_times = np.random.randint(10, 60, num_data_points)
flow_ratios = np.random.uniform(0.2, 1.0, num_data_points)
time_of_day = np.random.randint(0, 24, num_data_points)

def calculate_ew_present_green_time(lane1_present_num_vehicles, lane3_present_num_vehicles, cycle_length, ew_present_waiting_times, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
    
    ew_present_green_time = cycle_length * (max(lane1_present_num_vehicles, lane3_present_num_vehicles) / (flow_ratio * cycle_length)) + (ew_present_waiting_times * 0.05)
    
    return ew_present_green_time

def calculate_ns_present_green_time(lane2_present_num_vehicles, lane4_present_num_vehicles, cycle_length, ns_present_waiting_times, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
    
    ns_present_green_time = cycle_length * (max(lane2_present_num_vehicles, lane4_present_num_vehicles) / (flow_ratio * cycle_length)) + (ns_present_waiting_times * 0.05)
    
    return ns_present_green_time

def calculate_ew_upcoming_green_time(lane1_upcoming_num_vehicles, lane3_upcoming_num_vehicles, cycle_length, ew_upcoming_waiting_times, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
    
    ew_upcoming_green_time = cycle_length * (max(lane1_upcoming_num_vehicles, lane3_upcoming_num_vehicles) / (flow_ratio * cycle_length)) + (ew_upcoming_waiting_times * 0.05)
    
    return ew_upcoming_green_time

def calculate_ns_upcoming_green_time(lane2_upcoming_num_vehicles, lane4_upcoming_num_vehicles, cycle_length, ns_upcoming_waiting_times, time_of_day, flow_ratio):
    if 7 <= time_of_day <= 9 or 16 <= time_of_day <= 18:
        flow_ratio *= np.random.uniform(1.3, 1.8)
        
    ns_upcoming_green_time = cycle_length * (max(lane2_upcoming_num_vehicles, lane4_upcoming_num_vehicles) / (flow_ratio * cycle_length)) + (ns_upcoming_waiting_times * 0.05)
    
    return ns_upcoming_green_time
    
ew_present_green_time = np.zeros(num_data_points)
ns_present_green_time = np.zeros(num_data_points)

ew_upcoming_green_time = np.zeros(num_data_points)
ns_upcoming_green_time = np.zeros(num_data_points)

for i in range(num_data_points):
    ew_present_green_time[i] = calculate_ew_present_green_time(lane1_present_num_vehicles[i], lane3_present_num_vehicles[i], cycle_length, ew_present_waiting_times[i], time_of_day[i], flow_ratios[i])
    ns_present_green_time[i] = calculate_ns_present_green_time(lane2_present_num_vehicles[i], lane4_present_num_vehicles[i], cycle_length, ew_present_green_time[i], time_of_day[i], flow_ratios[i])

    ew_upcoming_green_time[i] = calculate_ew_upcoming_green_time(lane1_upcoming_num_vehicles[i], lane3_upcoming_num_vehicles[i], cycle_length, ns_present_green_time[i], time_of_day[i], flow_ratios[i])
    ns_upcoming_green_time[i] = calculate_ns_upcoming_green_time(lane2_upcoming_num_vehicles[i], lane4_upcoming_num_vehicles[i], cycle_length, ew_upcoming_green_time[i] ,time_of_day[i], flow_ratios[i])

data = pd.DataFrame({
    'cycle_length': cycle_length,
    'lane1_present_num_vehicles': lane1_present_num_vehicles,
    'lane2_present_num_vehicles': lane2_present_num_vehicles,
    'lane3_present_num_vehicles': lane3_present_num_vehicles,
    'lane4_present_num_vehicles': lane4_present_num_vehicles,
    'lane1_upcoming_num_vehicles' : lane1_upcoming_num_vehicles,
    'lane2_upcoming_num_vehicles' : lane2_upcoming_num_vehicles,
    'lane3_upcoming_num_vehicles' : lane3_upcoming_num_vehicles,
    'lane4_upcoming_num_vehicles' : lane4_upcoming_num_vehicles,
    'ew_present_waiting_times': ew_present_waiting_times,
    'ns_present_waiting_times': ew_present_green_time,
    'ew_upcoming_waiting_times': ns_present_green_time,
    'ns_upcoming_waiting_times': ew_upcoming_green_time,
    'time_of_day' : time_of_day,
    'flow_ratios' : flow_ratios,
    'ew_present_green_time': ew_present_green_time,
    'ns_present_green_time': ns_present_green_time,
    'ew_upcoming_green_time': ew_upcoming_green_time,
    'ns_upcoming_green_time': ns_upcoming_green_time,
})

print(data.head())

data.to_csv('traffic_signal_data.csv', index=False)