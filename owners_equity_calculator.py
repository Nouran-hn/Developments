#INTRODUCTION
print("Hello, welcome to Nouran's Partnership Equity Calculator! Today I will be asking you for two of you and your partners Assets and then two of you and your partners Liabilites. I will then tell you how much equity each of you own in the company!")
print("~ "*40)
print(" ")
print("~ "*40)
#INPUTS
CO=(input("What is the name of your company?"))
WS=(input("What do you sell?"))
print(" ")
#Person Number 1
print("The following is for PERSON NUMBER 1!")
#ASSESTS
A1=(input("What is the worth of your first biggest asset? (round to nearest dollar) $"))
while A1.isdigit()==False:
  print("This is not a valid number")
  A1=(input("What is the worth of your first biggest asset? (round to nearest dollar) $"))
A2=(input("What is the worth of your second biggest asset? (round to nearest dollar) $"))
while A2.isdigit()==False:
  print("This is not a valid number")
  A2=(input("What is the worth of your second biggest asset? (round to nearest dollar) $"))
print(" ")
#LIABILITIES
L1=(input("What is the cost of your first biggest liability? (round to nearest dollar) $"))
while L1.isdigit()==False:
  print("This is not a valid number")
  L1=(input("What is the cost of your first biggest liability? (round to nearest dollar) $"))
L2=(input("What is the cost of your second biggest liability? (round to nearest dollar) $"))
while L2.isdigit()==False:
  print("This is not a valid number")
  L2=(input("What is the cost of your second biggest liability? (round to nearest dollar) $"))
print(" ")
#Person Number 2
print("The following is for PERSON NUMBER 2!")
#ASSETS
a1=(input("What is the worth of your first biggest asset? (round to nearest dollar) $"))
while a1.isdigit()==False:
  print("This is not a valid number")
  a1=(input("What is the worth of your first biggest asset? (round to nearest dollar) $"))
a2=(input("What is the worth of your second biggest asset? (round to nearest dollar) $"))
while a2.isdigit()==False:
  print("This is not a valid number")
  a2=(input("What is the worth of your second biggest asset? (round to nearest dollar) $"))
print(" ")
#LIABILITIES
l1=(input("What is the cost of your first biggest liability? (round to nearest dollar) $"))
while l1.isdigit()==False:
  print("This is not a valid number")
  l1=(input("What is the cost of your first biggest liability? (round to nearest dollar) $"))
l2=(input("What is the cost of your biggest liability? (round to nearest dollar) $"))
while l2.isdigit()==False:
  print("This is not a valid number")
  l2=(input("What is the cost of your biggest liability? (round to nearest dollar) $"))
print("~ "*40)
print(" ")
print("~ "*40)
#CALCULATIONS
TotalAp1=float(A1)+float(A2)
TotalLp1=float(L1)+float(L2)
Totalap2=float(a1)+float(a2)
Totallp2=float(l1)+float(l2)
OEF=int(round(float((TotalAp1)+float(Totalap2))-(float(TotalLp1)+float(Totallp2)),2))
OEP1=int(float(TotalAp1)-float(TotalLp1))
OEP2=int(float(Totalap2)-float(Totallp2))
print("Here are each of the equities:")
print(" ")
print(("  The total equity of the company is"),str("$")+str(OEF))
print(" ")
print(("  The total equity of PERSON NUMBER 1 is"),str("$")+str(OEP1))
print(" ")
print(("  The total equity of PERSON NUMBER 2 is"),str("$")+str(OEP2))
print(" ")
#CALCULATIONS AS PERCENTAGES
print("~ "*40)
print("Here are  each of the equities as a percent of the company's total equity:")
print(" ")
PP1=int(round((float(OEP1)/float(OEF))*100,1))
PP2=int(round((float(OEP2)/float(OEF))*100,1))
print(("  PERSON 1 holds"),str(PP1)+str("%"),"of the company's equity")
print(" ")
print(("  PERSON 2 holds"),str(PP2)+str("%"),"of the company's equity")
print("~ "*40)
print(" ")
print("~ "*40)
#OUTRO
print("Thank you for using Nouran's Partnership Equity Calculator! I hope it was helpful and that",str(CO),"does very well and you sell many",str(WS), "! If you need more help or information visit this website, http://smallbusiness.chron.com/partnership-equity-64265.html. Have a good day!")

