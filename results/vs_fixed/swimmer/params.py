import numpy as np
import matplotlib.pyplot as plt
import json
import sys

times = []
rewards = []
t = []
r = []

trials = ["Swimmer-v1-adaptive-margin-1000.000000-0.001000-300.000000-0.000500",
"Swimmer-v1-adaptive-1000.000000-0.001000-300.000000-0.000500",
"Swimmer-v1-adaptive-1000.000000-0.001000-300.000000-0.000000",
"Swimmer-v1-adaptive-20000.000000-0.001000-0.000000-0.000500",
"Swimmer-v1-none-5000.000000-0.001000-0.000000-0.000000",
"Swimmer-v1-none-20000.000000-0.005000-0.000000-0.000000",
"Swimmer-v1-none-20000.000000-0.001000-0.000000-0.000000"]

names = ["Adapt both w/ margin","Adapt both", "Adapt steps", "Adapt KL", "Optimal steps (5,000)", "Optimal KL (0.005)", "Original steps/KL"]
for i in xrange(len(trials)):
    with open(trials[i]) as data_file:
        data = json.load(data_file)

    times.append([])
    rewards.append([])
    totaltime = 0

    time_since = 0
    avg = 0
    avgcount = 0

    for e in xrange(len(data["mean_reward"])):
        totaltime += data["timesteps"][e]

        time_since += data["timesteps"][e]
        avg += data["timesteps"][e]
        avgcount += 1

        if time_since > 10000:
            time_since = 0
            # totaltime += 1
            if i == 0:
                times[i].append(totaltime)
            else:
                times[i].append(totaltime)
            rewards[i].append(avg/avgcount)

            avg = 0
            avgcount = 0

    t.append(np.array(times[i]))
    r.append(np.array(rewards[i]))

    lin, = plt.plot(t[i],r[i],label=names[i])
    # if i == 0:
        # lin.remove()

plt.xlabel("Environment Steps Seen")
plt.ylabel("Average return")
leg = plt.legend(loc=4)
for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0)
plt.title("Swimmer-v1")
plt.show()
