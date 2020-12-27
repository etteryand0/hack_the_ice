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
        # HK - неуплата налогов
        nonpayment = self.company[8]
        if bool(nonpayment):
            punishment = self.calculate_score(1000, 'taxes_debt')
            self.score -= punishment
            return True

        bonus = self.calculate_score(1000, 'no_taxes_debt')
        self.score += bonus

        return False

    def taxes_history(self):
        # HL - нет истории налогов
        no_history = self.company[9]
        if bool(no_history):
            punishment = self.calculate_score(1000, 'no_taxes_history')
            self.score -= punishment
            return False

        bonus = self.calculate_score(1000, 'taxes_history')
        self.score += bonus

        return True

    def massive_founder(self):
        # HH - массовый учредитель
        massive = self.company[10]
        if bool(massive):
            punishment = self.calculate_score(1000, 'massive_founder')
            self.score -= punishment
            return True

        bonus = self.calculate_score(1000, 'not_massive')
        self.score += bonus

        return False

    def massive_leader(self):
        # HG - массовый руководитель
        massive = self.company[11]
        if bool(massive):
            punishment = self.calculate_score(1000, 'massive_leader')
            self.score -= punishment
            return True

        bonus = self.calculate_score(1000, 'not_massive')
        self.score += bonus

        return False

    def banned_founder(self):
        # HE - бан учредителя
        banned = self.company[12]
        if bool(banned):
            punishment = self.calculate_score(1000, 'banned_founder')
            self.score -= punishment
            return True

        return False
