def total_amount(billamount,tip_per):
    total_tip=(billamount/100)*tip_per
    total_bill=billamount+total_tip
    print("Please pay",total_bill,"to the restaurant")
bill=int(input("Enter your bill amount:"))
tip=int(input("Enter your tip percentage:"))
total_amount(bill,tip)