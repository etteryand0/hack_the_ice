class Loyalty:
    def __init__(self, company):
        self.company = company # list
        self.score = 10000
        self.coefficient = {
            'inoperative': 1,
            'liquidated': 1
        } # коэффиценты для вычитания\прибавления баллов
    
    def save_score(self, score, reason):
        return score * self.coefficient[reason]

    def check_status(self):
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
        invalid = self.company[$] # [AL]
        if invalid == 'True':
            return False

        return True

    def not_liquidated(self):
        liquidated = self.company[$] # [AM]
        if liquidated == 'True':
            return False

        return True