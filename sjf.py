#bt - burst time, wt - wait time
def findAvgTime(bursttime, x):
    i = 0
    wt = 0
    turnaround_time = 0
    empty1 = []
    empty2 = []
    sjfOutput = list()

    while(i < len(bursttime)):
        turnaround_time += bursttime[i]

        sjfOutput.append({"process": str(x.index(
            bursttime[i])+1), "burstTime": str(bursttime[i]), "waitingTime": str(wt), "turnAroundTime": str(turnaround_time)})

        x[x.index(bursttime[i])] = -1
        empty1.append(wt)
        empty2.append(turnaround_time)
        wt += bursttime[i]
        i += 1

    avgwait = round(sum(empty1)/len(empty1), 5)
    avgturn = round(sum(empty2)/len(empty2), 5)
    return sjfOutput, str(avgwait), str(avgturn)
