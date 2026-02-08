class Loan:
    def __init__(self, loan_amount,annual_interest_rate, number_of_years):
        self._loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.number_of_years = number_of_years
    def get_monthly_rate(self):
        monthly_rate = self.annual_interest_rate / 1200
        total_months = self.number_of_years * 12
        numerator = monthly_rate * (1 + monthly_rate) ** total_months
        denominator = (1 + monthly_rate) ** total_months - 1
        monthly_payment = self._loan_amount * (numerator / denominator)
        return monthly_payment
    def get_total_payment(self):
        return self.get_monthly_rate() * (self.number_of_years * 12)
