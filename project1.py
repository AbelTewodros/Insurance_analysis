import csv

smoker=[]
charges=[]
with open("python-portfolio-project-starter-files/insurance.csv") as insurance:
    insurance_dic=csv.DictReader(insurance)
    for individual in insurance_dic:
        smoker+=[individual["smoker"]]
        charges+=[individual["charges"]]

#Function to change a list of strings to float for manipulation
def number(strings):
    floatified=[]
    for i in strings:
        new=float(i)
        floatified.append(new)
    return floatified

zipped_smoker_charges= list(zip(smoker,number(charges)))
print(f"The following is a list made from the columns smoker and charges that are found on the insurance.csv files: \n{zipped_smoker_charges}\n")


#function to calculate average charge, where charges is a list of tuples and the second value is the charge
def calculate_average_charges(charges):
    total=0
    for i in charges:
        total=total+i[1]
    return total/len(charges)

print(f"The average charge for this dataset is ${calculate_average_charges(zipped_smoker_charges)}\n")


#This function calculates the average charges for smokers or non smokers,
#where smoker is a string of yes or no and zipped_smoker_charges is a 
#list of a tuple containing information if the individual smokes and the charges
def calculate_charges_smoker(smoker,zipped_smoker_charges):
    total=0
    length=0
    for i in zipped_smoker_charges:
        if i[0]== smoker:
            length+=1
            total+=i[1]
    return total/length

print("Average charges for a smoker: ${0}.\n".format(calculate_charges_smoker("yes",zipped_smoker_charges)))
print("Average charges for a non smoker: ${0}\n".format(calculate_charges_smoker("no",zipped_smoker_charges)))

def calculate_difference(charges_for_smoker,charges_for_non_smokers):
    return abs(charges_for_smoker-charges_for_non_smokers)

difference=calculate_difference(calculate_charges_smoker("yes",zipped_smoker_charges),calculate_charges_smoker("no",zipped_smoker_charges))
print(f"The difference in charges between smokers and non smokers is ${difference}\n")
print(f"This means that on average smokers tend to pay ${difference} more than non-smokers.\n")
print("We can conclude the importance that smoking plays when it comes to insurance payments\n")

def transform_zipped(zipped_smoker_charges):
    new=[]
    for i in zipped_smoker_charges:
        if i[0]=="yes":
            new.append((1,i[1]))
        else:
            new.append((0,i[1]))
    return new

def get_y(m,b,x):
    return m*x +b

def calculate_error(m,b,points):
    x_point=points[0]
    y_point=points[1]
    return abs(get_y(m,b,x_point)-y_point)

def calculate_all_error(m,b,data):
    total=0
    for i in data:
        total+=calculate_error(m,b,i)
    return total
possible_ms=[i for i in range(-10,11)]
possible_bs=[j for j in range(-20,21)]


lowest_error=int("inf")
best_ms=0
best_bs=0
for i in range(len(possible_ms)):
        for j in range(len(possible_bs)):
            if calculate_all_error(possible_ms[i],possible_bs[j],transform_zipped(zipped_smoker_charges))<lowest_error:
                lowest_error=calculate_all_error(possible_ms[i],possible_bs[j],transform_zipped(zipped_smoker_charges))
                best_ms=possible_ms[i]
                best_bs=possible_bs[i]
print(f"The best possible formula for calculating insurance based on this csv focusing on smokers or not is: y={best_ms}x+{best_bs}, with an error of {lowest_error}")


