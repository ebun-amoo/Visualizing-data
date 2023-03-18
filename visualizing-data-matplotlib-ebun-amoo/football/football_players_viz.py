from numpy import corrcoef as corr
import matplotlib.pyplot as pyplot
from football_players_exploration import *

def iteratePlayers(position):
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football_players_exploration.db')
    rows = exploration.session.query(Player).filter(Player.position == position).all()
    for row in rows:
        caps.append(row.caps)
        goals.append(row.goals)
    
    return caps, goals
    
def go(position):
    caps, goals = iteratePlayers(position)
    pyplot.scatter(caps, goals)
    correlation = (corr(caps, goals))[0][1]
    pyplot.title(f"{position} - {correlation}")
    pyplot.show()
    
if __name__ == '__main__':
    go('GK')
    go('DF')
    go('MF')
    go('FW')
    

