##Inputs we need from the user
#total rent
#total food ordered for snacking
#Electricity units Spend
#charge per unit
#persons sharing the room

## Outputs
#Total amount you've  to pay is

rent=int(input("Enter yourtotal rent: "))
food = int(input("Enter the amount spend on food : "))
electricity_spend =int(input("Enter the total Electricity units spend: "))
charge_per_unit = int(input("Enter the Charge per Unit: "))
persons = int(input("Enter the number of persons sharing the room: "))

total_bill = electricity_spend * charge_per_unit

total_amount = (rent + food + total_bill)//persons

print("each persons total amount to pay: ",total_amount)


