from PyCharmMiscProject.Loan import Loan
class LoanCalculator:
    def __init__(self):
        self.loan = None
    def input_data(self):
        while True:
            try:
                loan = float(input("Enter loan amount: "))
                rate = float(input("Enter loan rate: "))
                years = int(input("Enter number of years: "))
                break
            except ValueError:
                print("Введите корректные значения")
        self.loan_amount = loan
        self.annual_interest_rate = rate
        self.number_of_years = years
    def calculate(self):
        self.input_data()
        self.loan = Loan(self.loan_amount, self.annual_interest_rate, self.number_of_years)
    def display(self):
        mp = self.loan.get_monthly_rate()
        tp = self.loan.get_total_payment()
        print(f"Monthly payment: {mp:.2f}")
        print(f"Total payment: {tp:.2f}")
if __name__ == "__main__":
    calculator = LoanCalculator()
    calculator.calculate()
    calculator.display()


