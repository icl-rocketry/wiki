'''
Script to plot and analyse the data collected during the radio test
Written by Daniele Valentino Bella for ICLR
December 2019
'''

import numpy as np
from datetime import datetime
import re
import matplotlib.pyplot as plt


DATA_FILE='./uncorruptedRadioData.txt'
MAX_DISTANCE=1000 # in m, assuming constant velocity
DATA_START=41 # Array value where the data becomes useful
EXAMPLE_DISTANCES=np.array([500, 1000, 1500, 2000, 2500, 3000])


def packet_information(data_file_name):
  '''
  Function to read range test data from file and convert it to the appropriate format

  '''

  def seconds_diff(time_diff):
    # Explicitly define method so that it can be used on numpy array
    return time_diff.total_seconds()

  array_total_seconds=np.vectorize(seconds_diff)

  packet_times = np.array([])
  packet_nums = np.array([])
  packet_rssis = np.array([])

  with open(data_file_name) as data_file:
    lines = data_file.readlines()

    for line in lines:
      packet_time = re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}(?= -> Received packet 'Data Packet [0-9]{1,4}' with RSSI -[0-9]{1,4})", line)
      packet_num = re.findall("[0-9]{1,4}(?=' with RSSI -[0-9]{1,4})", line)
      packet_rssi = re.findall("(?<=with RSSI )-[0-9]{1,4}", line)

      if packet_time and packet_num and packet_rssi:
        # Convert the data from the current line to the appropriate format
        packet_time = datetime.strptime(packet_time[0], '%H:%M:%S.%f')
        packet_num = int(packet_num[0])
        packet_rssi = int(packet_rssi[0])

        packet_times = np.append(packet_times, packet_time)
        packet_nums = np.append(packet_nums, packet_num)
        packet_rssis = np.append(packet_rssis, packet_rssi)

  experiment_times = packet_times-min(packet_times)
  experiment_times = array_total_seconds(experiment_times) 

  return experiment_times, packet_nums, packet_rssis 

def distance(time_array, final_distance, double_speed_stop=0):
  '''
  Function to evaluate the distance at an array, given final_distance occuring at the end
  double_speed_stop is the index of where the subjects stop moving apart at double the speed
  '''
  switch_time = time_array[double_speed_stop]

  walking_speed = final_distance/(time_array.max()+2*switch_time)
  
  distance_array=np.zeros_like(time_array)
  distance_array[:double_speed_stop]=2*walking_speed*time_array[:double_speed_stop]
  distance_array[double_speed_stop:]=walking_speed*(time_array[double_speed_stop:]+switch_time)

  return distance_array

def trim(packet_rssis, packet_nums, packet_times):
  '''
  Function to trim data to get rid of all the data before the experiment started
  '''
  experiment_start_index = np.where(packet_rssis == np.amax(packet_rssis))

  experiment_times=packet_times[int(experiment_start_index[0])+1:]-packet_times[int(experiment_start_index[0])+1]
  experiment_nums=packet_nums[int(experiment_start_index[0])+1:]
  experiment_rssis=packet_rssis[int(experiment_start_index[0])+1:]

  return experiment_rssis, experiment_nums, experiment_times

def best_fit_line_params(x, y, data_start):
  '''
  Function that returns a and b for the line of best fit y=ax+b
  '''
  coeffs = np.polyfit(x[data_start:], y[data_start:], 1)

  return coeffs

def RSSI_eval(coeffs, distance):
  '''
  Function to apply line of best fit to find RSSI based on distance
  '''
  return -np.square(np.log10(coeffs[0]*distance+coeffs[1]))

packet_times, packet_nums, packet_rssis = packet_information(DATA_FILE)

experiment_rssis, experiment_nums, experiment_times = trim(packet_rssis, packet_nums, packet_times)
experiment_distance=distance(experiment_times, MAX_DISTANCE, double_speed_stop=DATA_START)

best_line_coeffs = best_fit_line_params(experiment_distance, 10**(np.sqrt(-experiment_rssis)), DATA_START)
print(f"The coefficients of the line of best fit, from highest order of x to lowest are: {best_line_coeffs}")

for distance in EXAMPLE_DISTANCES:
  print(f"RSSI at {distance} m:       {RSSI_eval(best_line_coeffs,distance)} dBm")

plt.scatter(experiment_distance, experiment_rssis, marker='o', s=10, label='Experimental Data')
plt.plot(experiment_distance, RSSI_eval(best_line_coeffs, experiment_distance), color='red', label='Curve of best fit')
plt.xlabel('Distance (m)')
plt.ylabel('RSSI (dBm)')
plt.title('RSSI against Distance for the Range Test')
plt.legend()

plt.show()
