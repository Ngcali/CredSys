# take user input for loan application
name = input("Name: ")
age = int(input("Age: "))
income = float(input("Income: "))
credit_score = int(input("Credit Score: "))
loan_amount = float(input("Loan Amount: "))
loan_duration = ""

if loan_amount < 5000:
    loan_duration = "6 Months"
    interest_rate = 15
elif loan_amount > 5000 and loan_amount == 1000:
    loan_duration = "3 Months"
    interest_rate = 20
elif loan_amount > 1000 and loan_amount == 10000:
    loan_duration = "12 Months"
    interest_rate = 10

# print out the user's inputs for confirmation
print("\nYour loan application details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Income: {income}")
print(f"Credit Score: {credit_score}")
print(f"Loan Amount: {loan_amount}")
print(f"Loan Duration: {loan_duration}")
print(f"Interest Rate: {interest_rate}% per annum")

print("Calculating your credit score...")
if credit_score > 650:
    print("Congratulations, you are eligible for a loan!")
else:
    print("Sorry, your credit score is too low to be eligible for a loan!")
    
# Display the loan details to the user
print("\n\nPlease confirm the following loan details:")
print(f"Loan Amount: {loan_amount}")
print(f"Loan Duration: {loan_duration} months")
print(f"Interest Rate: {interest_rate}% per annum")

# Ask the user to confirm the loan details
confirmation = input("Do you confirm these loan details? (Y/N) ")

# Process user confirmation
if confirmation.lower() == 'y':
    print("Loan application confirmed.")
    # Call function to process the loan application
else:
    print("Loan application cancelled.")


#Would you like to proceed with the loan application? (Y/N)
    
