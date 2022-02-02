import statistics 
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

score_list = df["reading score"].to_list()

mean = statistics.mean(score_list)
median = statistics.median(score_list)
mode = statistics.mode(score_list)
sD = statistics.stdev(score_list)

print("Mean :",mean)
print("Median :",median)
print("Mode :",mode)
print("Standard Deviation :",sD)

first_stddev_start , first_stddev_end = mean-sD , mean+sD
second_stddev_start , second_stddev_end = mean-2*sD , mean+2*sD
third_stddev_start , third_stddev_end = mean-3*sD , mean+3*sD

first_stddev_list = [num for num in score_list if first_stddev_start<num<first_stddev_end]
second_stddev_list = [num for num in score_list if second_stddev_start<num<second_stddev_end]
third_stddev_list = [num for num in score_list if third_stddev_start<num<third_stddev_end]

print(len(first_stddev_list)/len(score_list)*100,"% of data lies within 1st standard deviation")
print(len(second_stddev_list)/len(score_list)*100,"% of data lies within 2nd standard deviation")
print(len(third_stddev_list)/len(score_list)*100,"% of data lies within 3rd standard deviation")

