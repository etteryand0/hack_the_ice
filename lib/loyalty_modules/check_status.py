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
                return True
            else:
                self.score -= self.save_score(self.score, 'liquidated')
                return False
        else:
            self.score -= self.save_score(self.score, 'inoperative')
            return False

    def operative(self):
        # Проверяем, является ли компание действующей
        invalid = self.company[0] # [AL]
        if invalid == 'True':
            return False

        return True

    def not_liquidated(self):
        # Проверяем, назодится ли компания на стадии ликвидации
        liquidated = self.company[1] # [AM]
        if liquidated == 'True':
            return False

        return True