import shelve

def playerHighScore(player, score):
    """Compare players' previous high score to current score
    and record each player's high score."""

    f = shelve.open('v:\workspace\HighScore_Homework\src\scores.shelve')
   
    if not player in f.keys():	# if new player
        f[player] = score       # add that player
    elif score > f[player]:		# if new score is higher than previous best
        f[player] = score		# record new score

    return f[player]			# return the players best
 
    f.close()