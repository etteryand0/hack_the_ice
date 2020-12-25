class Check_Status:
    def __init__(self, company, save_score,
                 score, coefficient):
        self.company = company
        self.score = score
        self.coefficient = coefficient
        self.save_score = save_score

    def processe(self):
        if self.operative():
            if self.not_liquidated():
                return self.score
            else:
                self.score -= self.save_score(self.score, 'liquidated')
                return self.score
        else:
            self.score -= self.save_score(self.score, 'inoperative')
            return self.score

    def operative(self):
        # Проверяем, является ли компание действующей
        invalid = self.company[$] # [AL]
        if invalid == 'True':
            return False

        return True

    def not_liquidated(self):
        liquidated = self.company[$] # [AM]
        if liquidated == 'True':
            return False

        return True