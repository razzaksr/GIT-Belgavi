from API import *

health1 = gHealth.getHealth()
input("Welcome to gHealth Dashboard! Press Enter to continue...")
while True:
    print("\n1. Add Weigh-In\n2. Update Weigh-In\n3. View Weigh-In\n4. Filter Weigh-Ins\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age in years: "))
        gender = input("Enter gender (male/female): ")
        height = int(input("Enter height in cm: "))
        weight = float(input("Enter weight in kg: "))
        health1.initialize(name, age, gender, height)
        print(health1.makeWeighIn(id=str(len(retrieve())+1), weight=weight))
    elif choice == "2":
        weId = input("Enter Weigh-In ID to update: ")
        weight = float(input("Enter new weight in kg: "))
        print(health1.updateWeighIn(id=weId, weight=weight))
    elif choice == "3":
        weId = input("Enter Weigh-In ID to view: ")
        print(health1.readWeighIn(weId))
    elif choice == "4":
        metric = input("Enter metric to filter by (bmi/bmr/fat-rate/muscle-rate/body-age): ")
        value = float(input("Enter value to compare: "))
        operator = input("Enter comparison operator (gt/ge/lt/le/eq): ")
        print(health1.filter(metric, value, operator))
    elif choice == "5":
        print("Exiting gHealth Dashboard. Stay healthy!")
        break
# health1.initialize("Sabarinathan",34,"male",172)
# health1.makeWeighIn(id="1",weight=82.9)
# health1.initialize("Razak Mohamed",34,"male",158)
# health1.makeWeighIn(id="2",weight=71.02)
# health1.initialize("Nithya",24,"female",142)
# health1.makeWeighIn(id="3",weight=52.9)
# health1.initialize("Rakshana",33,"female",160)
# health1.makeWeighIn(id="4",weight=62.9)
# print(health1.filter("bmr",1400,"ge"))
# health1.updateWeighIn(id="4",weight=78)