from pklearn import Table
from pklearn.templates import simulate, BasicPlayer
from sklearn.ensemble import GradientBoostingRegressor

if __name__ == '__main__':

    t = Table(smallBlind=1, bigBlind=2, maxBuyIn=200)

    players = []
    for i in range(6):
        
        #create BasicPlayer that uses GradientBoostingRegressor as machine learning model
        #with wealth of 1 million and 10 discrete choices for raising,
        #with each raise choice .7 times the next largest raise choice
        #Player forgets training samples older than 100,000
        r = GradientBoostingRegressor()
        name = 'Player ' + str(i+1)
        p = BasicPlayer(name=name, reg=r, bankroll=10**6, nRaises=10, rFactor=.7, memory=10**5)
        players.append(p)

    for p in players: t.addPlayer(p)

    #simulate 'nHands' hands
    #begin training after 'firstTrain' hands
    #before which players take random actions and explore state space
    #players train every 'nTrain' hands after 'firstTrain'
    #players cash out/ buy in every 'nBuyIn' hands
    #table narrates each hands if 'vocal' is True
    simulate(t, nHands=10000, firstTrain=2000, nTrain=1000, nBuyIn=10)
    #train all players 10 times for 1000 hands each
    for i in range(40):
        #train Player 1 for 10000 hands, training once
        players[0].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[0].stopTraining()
        
        #train Player 2 for 2000 hands, training every 1000 hands
        players[1].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[1].stopTraining()

        players[2].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[2].stopTraining()

        players[3].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[3].stopTraining()

        players[4].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[4].stopTraining()

        players[5].startTraining()
        simulate(t, nHands=1000, nTrain=1000, nBuyIn=10)   
        players[5].stopTraining()
    
    simulate(t, nHands=20, nBuyIn=10, vocal=True)

    