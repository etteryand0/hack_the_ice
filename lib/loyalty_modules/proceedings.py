class Proceedings:
    def __init__(self, company, calculate_score,
                 score, coefficient):
        self.company = company
        self.score = score
        self.coefficient = coefficient
        self.calculate_score = calculate_score

    def processe(self):
        proceedings = self.company[4]  # BV
        if bool(proceedings):
            self.score -= self.proceedings_value()
            return True
        else:
            return False

    def proceedings_value(self):
        proceedings_value = self.company[6]  # BY
        promiser = self.company[5]  # CE
        company_name = self.company[0]  # B

        if company_name != promiser:
            punishment = 0
            return punishment

        values_obj = map(int, proceedings_value.split(';'))
        debt = sum(list(values_obj))

        punishment = self.calculate_score(debt, 'debt')

        return punishment
