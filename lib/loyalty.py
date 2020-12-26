from lib.loyalty_modules import Check_Status
from lib.loyalty_modules import Proceedings


class Loyalty:
    def __init__(self, company):
        # company = ['B-company_name(str)', 'D-ИНН(int)', 'AL-недействующая(bool)', 'AM-на стадии ликвидации(bool)',
        #            'BV-номер исп права(str)', 'CE-должник(str)', 'BY-сумма долга(list int)'
        #           ]
        self.company = company  # list
        self.score = 10000
        self.coefficient = {
            'inoperative': 1,
            'liquidated': 1,
            'debt': 1.5
        }  # коэффиценты для вычитания\прибавления баллов

    def calculate_score(self, score, reason):
        # Единая функция для вычисления суммы баллов с коэффициентами
        return int(score * self.coefficient[reason])

    def check_status(self):
        # Проверяем компвнию на статус
        # (недейстующая, находится на стадии разработки)
        # Колонки: AL, AM
        check_status = Check_Status(self.company, self.calculate_score,
                                    self.score, self.coefficient)
        status = check_status.processe()
        self.score = check_status.score
        del check_status  # clear memory

        return status

    def check_proceedings(self):
        # Проверяем компанию на испольнительные производства
        # Колонки: BV, B, CE, BY
        check_proceedings = Proceedings(self.company, self.calculate_score,
                                        self.score, self.coefficient)
        proceedings = check_proceedings.processe()
        self.score = check_proceedings.score
        del check_proceedings

        return proceedings
