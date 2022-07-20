import imp
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
"""fig.show()"""

mean = statistics.mean(data)
stdDeviation = statistics.stdev(data)
print("Mean of population", mean)
print("Standard Deviation of population", stdDeviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

standard_deviation = statistics.stdev(mean_list)
print("Standard Deviation of Sampling Distribution", standard_deviation)

sampling_mean = statistics.mean(mean_list)
print("Mean of Sampling Distribution", sampling_mean)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2], mode = "lines", name="Mean"))

First_std_start, First_std_end = sampling_mean-standard_deviation, sampling_mean+standard_deviation
Second_std_start, Second_std_end = sampling_mean-(2*standard_deviation), sampling_mean+(2*standard_deviation)
Third_std_start, Third_std_end = sampling_mean-(3*standard_deviation), sampling_mean+(3*standard_deviation)

fig.add_trace(go.Scatter(x = [First_std_start,First_std_start], y = [0,0.2], mode = "lines", name="First Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [First_std_end,First_std_end], y = [0,0.2], mode = "lines", name="First Standard Deviation End"))

fig.add_trace(go.Scatter(x = [Second_std_start,Second_std_start], y = [0,0.2], mode = "lines", name="Second Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [Second_std_end,Second_std_end], y = [0,0.2], mode = "lines", name="Second Standard Deviation End"))

fig.add_trace(go.Scatter(x = [Third_std_start,Third_std_start], y = [0,0.2], mode = "lines", name="Third Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [Third_std_end,Third_std_end], y = [0,0.2], mode = "lines", name="Third Standard Deviation End"))

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample 1", mean_of_sample1)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean_list,mean_list], y = [0,0.2], mode = "lines", name="Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample1,mean_of_sample1],y = [0, 0.2], mode = "lines", name = "Mean of Sample 1"))

fig.add_trace(go.Scatter(x = [First_std_end,First_std_end], y = [0,0.2], mode = "lines", name="First Standard Deviation End"))

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of sample 2", mean_of_sample2)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean_list,mean_list], y = [0,0.2], mode = "lines", name="Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample2,mean_of_sample2],y = [0, 0.2], mode = "lines", name = "Mean of Sample 2"))

fig.add_trace(go.Scatter(x = [Second_std_end,Second_std_end], y = [0,0.2], mode = "lines", name="Second Standard Deviation End"))

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("Mean of sample 3", mean_of_sample3)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean_list,mean_list], y = [0,0.2], mode = "lines", name="Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample3,mean_of_sample3],y = [0, 0.2], mode = "lines", name = "Mean of Sample 3"))

fig.add_trace(go.Scatter(x = [Third_std_end,Third_std_end], y = [0,0.2], mode = "lines", name="Third Standard Deviation End"))

fig.show()

z_score1 = (mean_of_sample1 - mean)/standard_deviation
print("z_score1:-", z_score1)

z_score2 = (mean_of_sample2 - mean)/standard_deviation
print("z_score2:-", z_score2)

z_score3 = (mean_of_sample3 - mean)/standard_deviation
print("z_score3:-", z_score3)
print("If z<1 or z<2, the impact of intervation might not be statistically significant, that's why dataset 3 is the good intervation")