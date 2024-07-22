Insurance Charges Analysis:

Thank you for visiting! This repository contains a CSV file and a Python script for analyzing insurance charges.

Contents:

insurance.csv: This file contains a table with insurance information including age, sex, BMI, number of children, smoker status, and charges.

insurance_analysis.py: Python script used to analyze the difference in charges between smokers and non-smokers.

Analysis Summary:
The script calculates that smokers pay an average of $17,000 more in insurance charges compared to non-smokers. Further analysis was conducted to determine if smoker status alone significantly influences insurance payments. A linear regression was performed with varying parameters (m from -10 to 10, b from -20 to 20), revealing high errors across all tested configurations. This indicates that smoker status alone does not provide a reliable estimate for insurance charges.

Dependencies:
This project utilizes built-in functionalities of the latest Python version, with only the csv module imported for handling the data file.
