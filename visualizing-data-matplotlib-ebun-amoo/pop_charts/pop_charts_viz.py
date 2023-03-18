
import matplotlib.pyplot as pyplot
from pop_charts_exploration import *

def getDurations():
    durations = []
    exploration = PopChartsExploration('pop_charts_exploration.db')
    rows = exploration.session.query(PopCharts).all()
    for row in rows:
        durations.append(row.duration)
    
    return durations

def go():
    number_of_bins = 20
    durations = getDurations()

    pyplot.hist(durations, bins=number_of_bins)
    pyplot.show()
        
if __name__ == '__main__':
    go()
