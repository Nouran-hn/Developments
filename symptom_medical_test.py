#INTRODUCTION
print("Hello patient. Today I will ask you to chose symptoms that you are going through and I will tell you what sickness or illnesses you may have.")
print(" ")
#AGE
age= int(input("How old are you? "))
#IF STATEMENTS
if age >=50:
  print("Please read the following symptoms:")
  print("a)Coughing")
  print("b)Dry/sore throat")
  print("c)Runny nose")
  print("d)Sneezing")
  print("e)Swelling")
  print("f)Dizziness")
  print("g)Headache")
  print("h)Fatigue")
  print("i)High temperature")
  print("j)Migraine")
  print("k)Nausea")
  print("l)Stomach Cramp")
  print("m)Vomiting")
  print("n)Itchiness ")
  print("o)Stiffness")
  print("p)Redness")
  print("q)Joint Pain")
  print("r)Heaviness ")

#CALCULATIONS
  s=input("What are your symptoms (e.g. a,h,n): ")
  symp1= s.lower()
  symptoms = symp1.split(",")
  
  disease1=""
  disease2=""
  disease3=""
  disease4=""
  disease5=""
  disease6=""
  disease7=""
  disease8=""
  
  for symp in symptoms:
    if symp in ["a", "b", "c", "d'"]:
      disease1 = "cold"
    if symp in ["i","f","a","m","h"]:
      disease2 = "flu"
    if symp in ["e","f","g","k"]:
      disease3 = "allergic reaction"
    if symp in ["l","m","g",]:
      disease4 = "Food poisoning"
    if symp in ["o","q","r","e","p"]:
      disese5 = "Arthritis"
    if symp in ["i","n"]:
      disease6 = "Rash"
    if symp in ["r", "f","p"]:
      disease7 = "Heart problem"
    if symp in ["f", "g", "j", "r", "h"]:
      disease8 = "narcolepsy"
 
  print("Possible illnesses are: ")
  if disease1 =="":
    print(disease)
  if disease2 =="":
    print(disease)
  if disease3 =="":
    print(disease)
  if disease4 =="":
    print(disease)
  if disease5 =="":
    print(disease)
  if disease6 =="":
    print(disease)
  if disease7 =="":
    print(disease)
  if disease8 =="":
    print(disease)
 
#NOT ABOVE 50
else:
  print("Please read the following symptoms:")
  print("a)Coughing")
  print("b)Dry/sore throat")
  print("c)Runny nose")
  print("d)Sneezing")
  print("e)Swelling")
  print("f)Dizziness")
  print("g)Headache")
  print("h)Fatigue")
  print("i)High temperature")
  print("j)Migraine")
  print("k)Nausea")
  print("l)Stomach Cramp")
  print("m)Vomiting")
  print("n)Itchiness")
  S=input("What are your symptoms (e.g. a,h,n): ")
  symp1= S.lower()
  symptoms = symp1.split(",")
 
  disease1=""
  disease2=""
  disease3=""
  disease4=""
  disease5=""
 
  for symp2 in symptoms:
    if symp2 in ["a", "b", "c", "d'"]:
      disease1 = "cold"
    if symp2 in ["i","f","a","m", "h"]:
      disease2 = "flu"
    if symp2 in ["e","f","g","k"]:
      disease3 = "allergic reaction"
    if symp2 in ["l","m","g", "j"]:
      disease4 = "Food poisoning"
    if symp2 in ["i","n"]:
      disease5 = "Rash"
    
 
  print("Possible illnesses are: ")
  if disease1 =="":
    print(disease1)
  if disease2 =="":  
    print(disease2)
  if disease3 =="":
    print(disease3)
  if disease4 =="":
    print(disease4)
  if disease5 =="":
    print(disease5)


