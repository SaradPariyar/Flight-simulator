class Score:
    def __init__(self, player, attempt):
        self.player = player
        self.attempt = attempt

class Earn:
    def gain(self, score, earn):
        score.earn = earn

income = Earn()
score = Score("ABC-123", "2")
print("The car is " + score.earn)
income.gain(score, "red")
print("The car is now " + score.earn)
