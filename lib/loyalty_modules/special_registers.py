class Special_Registers:
    def __init__(self, company, 
                 calculate_score, score):
        self.company = company
        self.score = score
        self.calculate_score = calculate_score

    def processe(self):
        self.banned_founder()
        self.massive_founder()
        self.massive_leader()
        self.taxes_debt()
        self.taxes_history()

        return True

    def taxes_debt(self):
        pass

    def taxes_history(self):
        pass

    def massive_founder(self):
        pass

    def massive_leader(self):
        pass

    def banned_founder(self):
        # HE - бан учредителя
        banned = self.company[12].strip()
        if bool(banned):
            punishment = self.calculate_score(1000, 'banned_founder')
            self.score -= punishment
            return True
        
        return False