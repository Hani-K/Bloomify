#! /usr/bin/python

import math
import os
import subprocess

# Function to calculate the optimal false positive rate based on the number of passwords
def calculate_optimal_false_positive_rate(num_passwords):
    return math.pow(0.6185, math.log(num_passwords))

def p_Select(num_lines):
    # Calculate the optimal false positive rate
    optimal_false_positive_rate = calculate_optimal_false_positive_rate(num_lines)

    # Ask the user if they want to use the optimal false positive rate or set one manually
    user_choice = input(f"The optimal false positive rate caculated is {optimal_false_positive_rate:.10f}. Do you want to use this value? (Y/n) ")

    if user_choice.lower() == 'y' or not user_choice:
        false_positive_rate = optimal_false_positive_rate
    else:
        false_positive_rate = float(input("Enter the desired false positive rate (e.g., 0.001): "))
    
    return false_positive_rate