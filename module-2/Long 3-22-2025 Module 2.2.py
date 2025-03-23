#calculate number of year to get a double on an investment
def years_to_double(investment, interest_rate):
    years = 0
    goal = investment * 2 #goal amount(double the investment)
    # Set a breakpoint here to inspect initial values
    while investment < goal:
        investment += investment * interest_rate
        years += 1 #increment the number of years
    # Removed return statement to introduce an error
#Get the investment amount and interest rate from the user
investment = float(input("Enter the investment amount: "))  #convert the input to a float
interest_rate = float(input("Enter the interest rate: "))  #convert the input to a float

#implement calcualation and display outcome to the user
years = years_to_double(investment, interest_rate)
print("The investment will double after", years, "years.")