from lib.loyalty_modules import Check_Status

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
        check_status = Check_Status(self.company, self.save_score, 
                                    self.score, self.coefficient)
        self.score = check_status.processe()

