#bt - burst time, wt - wait time
def findwtingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findAvgTime(processes, n, bt):
    fcfsOutput = []
    wt = [0] * n
    tat = [0] * n
    totalwtingTime = 0
    total_tat = 0
    findwtingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)

    for i in range(n):
        burstData = str(bt[i])
        wtData = str(wt[i])
        tatData = str(tat[i])
        totalwtingTime = totalwtingTime + wt[i]
        total_tat = total_tat + tat[i]

        fcfsOutput.append(
            {"process": str(i+1), "burstTime": burstData, "wtingTime": wtData, "turnAroundTime": tatData})

    avgwt = round(totalwtingTime / n, 5)
    avgturn = round(total_tat / n, 5)
    return fcfsOutput, str(avgwt), str(avgturn)
