class Check_Status:
    def __init__(self, company, calculate_score,
                 score):
        self.company = company
        self.score = score
        self.calculate_score = calculate_score

    def processe(self):
        if self.operative():
            if self.not_liquidated():
                return True
            else:
                self.score -= self.calculate_score(self.score, 'liquidated')
                return False
        else:
            self.score -= self.calculate_score(self.score, 'inoperative')
            return False

    def operative(self):
        # Проверяем, является ли компание действующей
        invalid = self.company[2]  # [AL]
        if bool(invalid):
            return False

        return True

    def not_liquidated(self):
        # Проверяем, назодится ли компания на стадии ликвидации
        liquidated = self.company[3]  # [AM]
        if bool(liquidated):
            return False

        return True
