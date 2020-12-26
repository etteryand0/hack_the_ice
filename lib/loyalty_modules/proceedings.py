class Proceedings:
    def __init__(self, company, calculate_score,
                 score, coefficient):
        self.company = company
        self.score = score
        self.coefficient = coefficient
        self.calculate_score = calculate_score

    def processe(self):
        proceedings = self.company[4]  # BV - номер исп права(str)
        if bool(proceedings):
            punishment = self.proceedings_value()
            if punishment:
                self.score -= self.proceedings_value()
                return True

        no_debt = self.calculate_score(100, 'no_debt')
        self.score += no_debt
        return False

    def proceedings_value(self):
        proceedings_value = self.company[6].strip()  # BY-сумма долга(list int)
        promiser = self.company[5]  # CE - должник(str)
        company_name = self.company[0]  # B-company_name(str)

        if company_name != promiser:
            return False

        values_obj = map(int, proceedings_value.split(';'))
        debt = sum(list(values_obj))

        punishment = self.calculate_score(debt, 'debt')

        return punishment
