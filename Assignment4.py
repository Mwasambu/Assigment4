#Enter the price of the House you wish to Buy
print("Enter the House Price")
price = float(input())
#Enter the credit score
print("Enter the Credit Score")
CreditScore = float(input())
#Enter the first name
print("Enter the first name")
first_name = input()
#Enter the last name
print("Enter the last name")
last_name = input()
fullnames = first_name + " " + last_name
#Enter the email
print("Enter the email address")
email = input()
#Enter the phone number
print("Enter the phone number")
phone = input()
#Enter the mailing
print("Enter the mailing address")
mailing = input()
#Enter the City
print("Enter the City")
city = input()
print("Enter the State")
state = input()
#Enter the mailing
print("Enter the zip code")
zipcode = input()
#Qualify for loans with the best interest rates

if CreditScore >= 780 and CreditScore <=850:
    CreditStatus="Excent Credit"
    print("Zero Down Payment")
    downPayment = 0.0 * price
#Usually qualify for loans with the best interest rates
elif CreditScore >= 740 and CreditScore <= 779:
    CreditStatus="Very Good"
    downPayment = 0.2 * price
    #May face slightly higher loan Interest rates
elif CreditScore >= 720 and CreditScore <=739:
    CreditStatus="Above Average"
    downPayment = 0.3 * price
#May qualify for most loans of higher interest rates
elif CreditScore >= 680 and CreditScore <=719:
    CreditStatus ="Average"
    downPayment = 0.6 * price
#May qualify for most loans at significant higher Interest rates
elif CreditScore >= 620 and CreditScore <=679:
    CreditStatus="Below Average"
    downPayment = 0.18 * price
#Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580 and CreditScore <=619:
    CreditStatus="Poor Credit Score"
    downPayment = 0.20 * price
#Facing extreme credit issue
else:
    CreditScore < 520
    CreditStatus="Poor Credit Score"
    downPayment = 0.25 * price


print("Name: " + fullnames )
print("Physical Address: ")
print("City: " + city + " State: " + state + " Zipcode: " + zipcode)
print()
print("New House Price: " + '' + str(price))
print("Down Payment: " + str(downPayment))
print("Credit Score: " + str(CreditScore))
print("Credit Status: " + CreditStatus)