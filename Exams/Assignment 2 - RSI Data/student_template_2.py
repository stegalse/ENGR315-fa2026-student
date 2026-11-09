"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
import pandas as pd
import numpy as np
from scipy.stats import ttest_rel, norm, chisquare, t
import matplotlib.pyplot as plt

# Utilize print() functions to clearly provide an output response for each question. 


# First, I need to use the panda read .csv function to convert the data 
# into a dataframe so it can be used in each task.
# Add a relative path to all_participant_data_rsi.csv file 
# Go up two folders, then find us-counties data
data = pd.read_csv('../../data/drop-jump/all_participant_data_rsi.csv')


# Add a variable for each column in the dataset
trial = data['trial']
force_plate_rsi = data['force_plate_rsi']
accelerometer_rsi = data['accelerometer_rsi']
percent_error = data['percent_error']


#Task 1: For the new dataset of RSI values (all_participant_data_rsi.csv), 
# conduct a paired t-test comparing all the force plate and accelerometer RSI values. 
# Clearly report the t-value, p-value, null and alternative hypotheses, and decide whether 
# the null hypothesis can be rejected or not. In your report: What can we conclude about the two measurement methods?

print("Task 1:")
print("Null hypothesis: There is no difference in the RSI values measured in on the force plate and the accelerometer. ")
print("Alternative hypothesis: There is a significant difference in the RSI values measured on the force plate and \n                        the accelerometer; each measurement method produces different or skewed results.")

# an alpha of 0.05 is suitable for all tests (stated in Canvas)
alpha = 0.05

# paired t-test function on rsi data comparing the force plase and accelerometer rsi means
statistic, pvalue = ttest_rel(force_plate_rsi, accelerometer_rsi)

# print the results from the t-test
print("p-value:", pvalue)
print("t-value:", statistic)

if pvalue < alpha:
    print("Reject null hypothesis\n")
elif pvalue > alpha:
    print("Fail to reject null hypothesis\n")


#Task 2: For the RSI values gathered using an accelerometer, fit a normal distribution and 
# conduct a Chi2 Goodness of Fit Test. Clearly print out the chi2 stat, p-value, and an indication 
# of whether it is a good fit or not. Plot a histogram of the accelerometer data with the normal 
# distribution curve overlaid. In your report: what factors in the data cause this to be a good fit or not?

print("Task 2:")

mean_a = np.average(accelerometer_rsi)
std_a = np.std(accelerometer_rsi)
print("The mean of is", mean_a, "and the standard deviation is", std_a)

# Find the fitted mean and standard distribution using norm.fit
mu, sigma = norm.fit(accelerometer_rsi)
print("The fitted mean is", mu, "and the fitted standard deviation is", sigma)

# Create bins for the Chi-square test
observed, bin_edges = np.histogram(accelerometer_rsi, bins=10)

# Calculate expected frequencies
expected = len(accelerometer_rsi) * np.diff(norm.cdf(np.concatenate(([-np.inf], bin_edges[1:-1], [np.inf])),mu, sigma))

# Perform Chi-square Goodness of Fit Test
chi_stat, p2value = chisquare(observed, expected, ddof=2)

print("Chi-square Statistic:", chi_stat)
print("P-value:", p2value)

if p2value < alpha:
    print("This is a good fit.\n")
elif p2value > alpha:
    print("This is not a good fit.\n")

# Create histogram of accelerometer RSI data
plt.hist(accelerometer_rsi, bins=10, density=True,
         alpha=0.6, label='Accelerometer RSI')

# Generate x values for the normal distribution curve
x = np.linspace(min(accelerometer_rsi), max(accelerometer_rsi), 100)

# Calculate normal distribution probability density
y = norm.pdf(x, mu, sigma)

# Plot normal distribution curve
plt.plot(x, y, label='Fitted Normal Distribution', linewidth=2)

# Add labels, title, and legend
plt.xlabel('RSI')
plt.ylabel('Probability Density')
plt.title('Accelerometer RSI Distribution')
plt.legend()
plt.show()

#Task 3: From the force plate and accelerometer-based RSI data for all participants, 
# create and print() a dataframe containing only the trials from Participant ‘F’. 
# Calculate the 95% confidence intervals for Participant F’s RSI for both the force plate and 
# accelerometer measurements. In your report: What can we conclude about the two measurement methods from these?

print("Task 3:")

# Filter data to only include Participant F
participant_f = data[data['trial'].str.startswith('F_trial_')]

# Store Participant F's RSI measurements
fp_f = participant_f['force_plate_rsi']
a_f = participant_f['accelerometer_rsi']

# Calculate 95% confidence intervals for force plate measurements
fp_ci = t.interval(0.95, df=len(fp_f)-1, loc=np.mean(fp_f), scale=np.std(fp_f, ddof=1)/np.sqrt(len(fp_f)))

#Calculate 95% confidence intervals for accelerometer measurements
a_ci = t.interval(0.95, df=len(a_f)-1, loc=np.mean(a_f), scale=np.std(a_f, ddof=1)/np.sqrt(len(a_f)))

# Round and print results
print("Force Plate Mean:", round(float(np.mean(fp_f)), 4))
print("Force Plate 95% Confidence Interval:",
      tuple(round(float(x), 4) for x in fp_ci))

print("Accelerometer Mean:", round(float(np.mean(a_f)), 4))
print("Accelerometer 95% Confidence Interval:",
      tuple(round(float(x), 4) for x in a_ci))