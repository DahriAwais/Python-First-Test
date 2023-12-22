Number_of_people=int(input("Enter Number of Peoples:"))
Total_Meals=int(input("Enter Number Of Meals:"))
Cost_of_each_meal=int(input("Enter price of one meal:"))
Sales_tax_percentage=int(input("Enter sales tax:"))
Tip_percentage=int(input("Enter Tip:"))
Sales_Tax=Sales_tax_percentage*Cost_of_each_meal*Total_Meals//100
Tip_Amount=Tip_percentage*Cost_of_each_meal*Total_Meals//100



print(f"Total Cost Of Food Is:",Cost_of_each_meal*Total_Meals)
print(f"Total Sales Tax:",Sales_Tax)
print(f"Total tip Amount:",Tip_Amount)
print(f"Total Bill Amount per Person:",Cost_of_each_meal*Total_Meals//Number_of_people)