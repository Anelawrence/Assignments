# Using the structures we explained during the course of this week’s sessions:
# Create a BankAccount class
# It should have similar attributes of a conventional bank
# It should have methods that implement the deposit and withdrawal functionality of a bank account
# Test that your code is working properly
# Push your code to github

class BankAccount:
    acct_bal = 0
    def __init__(self, acct_name, acct_number, deposit, withdrawal):
        self.acct_name = acct_name
        self.acct_number = acct_number
        self.depost = deposit
        self.withdrawal = withdrawal

        if deposit > withdrawal:
            self.acct_bal = deposit - withdrawal
        elif deposit == withdrawal:
            self.acct_bal = BankAccount.acct_bal
        else:
            BankAccount.acct_bal = "Sorry, you cannot withdraw more than what you have."
       

customer_1 = BankAccount("Shola", "001", 5000, 5000)
customer_2 = BankAccount("John", "002", 10000, 15000)

print(customer_1.acct_bal)
print(customer_2.acct_bal)



