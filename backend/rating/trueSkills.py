class TrueSkills:
    def __init__(self, mu=25, sigma=8.333, beta=4.167, tau=0.0833):
        self.mu = mu
        self.sigma = sigma
        self.beta = beta
        self.tau = tau

    def includeTime(self, expectedTime, time, outcome):
        if outcome:
            return 1
        else:
            if time > expectedTime:
                return max(0, 1 - ((1.04**(time-expectedTime))/expectedTime))
            else:
                return (2 - ((time)/expectedTime))


    def update(self, player_rating, task_rating, outcome, time, expectedTime):
        expected_outcome = self.expected_outcome(player_rating, task_rating)
        new_rating = player_rating + self.tau * self.sigma * (outcome - expected_outcome) * self.includeTime(expectedTime, time, outcome)
        return new_rating

    def expected_outcome(self, player_rating, task_rating):
        delta = task_rating - player_rating
        expected_outcome = 1 / (1 + 10 ** (-delta / (self.beta * self.sigma)))
        return expected_outcome

    def predict(self, player_rating, task_rating):
        expected_outcome = self.expected_outcome(player_rating, task_rating)
        predicted_outcome = 1 - expected_outcome
        return predicted_outcome
