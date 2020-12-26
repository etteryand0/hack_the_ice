class License:
    def __init__(self, company, 
                 calculate_score, score):
        self.company = company
        self.score = score
        self.calculate_score = calculate_score

    def processe(self):
        if not self.have_license():
            return False

        self.score += self.calculate_score(100, 'have_license')
        return True

    def have_license(self):
        license_ = self.company[7]
        if bool(license_):
            return True
        else:
            return False