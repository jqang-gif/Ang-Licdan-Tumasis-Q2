import json
import time
#use
try:
    # READING from the file
    filename = "projectCS.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)
    loop = 1
    historynumber=1
    while loop != 0:
        option = int(input("Welcome to the Accountantulator\nPlease pick the number of the  option that you want  to do\n1. Calculate VAT of product\n2. History of your Accountantulator\n3. How to use Accountantulator\n4. Find Product\n5. Alter Product\n6. Exit"))
        if option == 1:
            historynumber= historynumber + 1
            newdict = {}
            newdict["username"] = input("What is your name? ")
            newdict["name"] = input("What is the name of the product ")
            newdict["price"] = float(input(f"Enter value of {newdict["name"]} "))
            newdict["vatofproduct"] = newdict["price"]*0.12
            print(f"The VAT is {newdict["vatofproduct"]:.2f} ")
            newdict["minimumpriceforsale"] = newdict["vatofproduct"] + newdict["price"]+0.1
            print(f"The minimum price to gain profit is {newdict["minimumpriceforsale"]:.2f} ")
            newdict["marketprice"]=float(input("Enter the value you want to sell the product at" ))
            newdict["profit"] = newdict["marketprice"]-newdict["minimumpriceforsale"]
            print(f"The profit from one {newdict["name"]} is {newdict["profit"]}")
            newdict["creation"] = "Created by User"
            newdict["historyno"] = historynumber
            data.append(newdict)

        elif option == 2:
            for produce in data:
                for i in produce:
                    print(f"{i.capitalize()}: {produce[i]}")
                print("")

        elif option == 3:
            sampledict ={"username": "","name": "", "price": 0,"vatofproduct": 0,"minimumpriceforsale": 0,"marketprice": 0,"profit": 0,"creation": "Sample","historyno": 0}
            print("Welcome to the Tutorial for using the Accountantulator")
            print("We will give a quick run down on how the Accountantulator works")
            time.sleep(1)
            sampledict["username"]= input("First input your username")
            print("We then get the name of your product")
            sampledict["name"] = input("Input the name of your product")
            print(f"The name of your product is {sampledict["name"]}")
            time.sleep(0.5)
            sampledict["price"]= float(input("Now input the price of the product you have "))
            time.sleep(0.5)
            sampledict["vatofproduct"] = sampledict["price"] * 0.12
            print(f"You will now recieve the VAT of your product, which is {sampledict["vatofproduct"]}")
            time.sleep(0.5)
            sampledict["minimumpriceforsale"] = sampledict["vatofproduct"] + sampledict["price"]+0.1
            time.sleep(0.5)
            print(f"Now the Accountantulator will solve for the minimum price for you to have a profit, which is {sampledict["minimumpriceforsale"]}")
            time.sleep(0.5)
            sampledict["marketprice"] =float(input("Now you can appoint the price you are going to sell the product for accounting VAT" ))
            sampledict["profit"] = sampledict["marketprice"] - sampledict["minimumpriceforsale"]
            time.sleep(2)
            print(f"Lastly, the Accountantulator will give you the profit per product sold, for the sample you provided it is {sampledict["profit"]}")
            time.sleep(1)
            print("When using the Accountantulator you will also get a history number to track the history of usage of the Accountantulator.")
            sampledict["creation"] = "Sample test by User"
            sampledict["historyno"] = 0
            time.sleep(1)
            print("Here is all the data gathered by the Accountantulator")
            time.sleep(2)
            for produce in data:
                for i in produce:
                    print(f"{i.capitalize()}: {produce[i]}")
                    time.sleep(0.25)
            print("Now that you understand how to use it try a real test by typing 1 into the menu.")
            time.sleep(0.25)

        elif option == 4:
            foundname = False
            alternativeloop = 1
            while alternativeloop != 2:
                productnametofind = input("Please input the name of the product you want to find")
                for produce in data:
                    if produce["name"] == productnametofind:
                        foundname = True
                        print("Found it!")
                        print(f"Printing Data for {productnametofind}")
                        time.sleep(3)
                        for i in produce:
                            print(f"{i.capitalize()}: {produce[i]}")
                if foundname == False:
                    print("No product with that name")
                alternativeloop = int(input("Continue Searching?\n1. Yes\n2. No "))


        elif option == 5:
            foundname = False
            alternativeloop = 1
            while alternativeloop != 2:
                productnametoalter = input("Please input the name of the product you want to alter")
                for produce in data:
                    if produce["name"] == productnametoalter:
                        foundname = True
                        print(f"Printing Data for {productnametoalter}")
                        time.sleep(3)
                        for i in produce:
                            print(f"{i.capitalize()}: {produce[i]}")
                        alterloop = 0
                        while alterloop == 0:
                            alteration = int(input(
                                "What do you want to alter?\n1. Username\n2. Product Name\n3. Price of Product\n4. Market Price of Product\n5. Finish Alterations"))

                            if alteration == 1:
                                produce["username"] = input("Input a new Username")
                                produce["creation"] = "Altered"
                            elif alteration == 2:
                                produce["name"] = input("Input new product name")
                                produce["creation"] = "Altered"
                            elif alteration == 3:
                                produce["price"] = float(int("Input the new Price of Product"))
                                produce["vatofproduct"] = produce["price"] * 0.12
                                print(f"The VAT is {produce["vatofproduct"]:.2f} ")
                                produce["minimumpriceforsale"] = produce["vatofproduct"] + produce["price"] + 0.1
                                print(f"The minimum price to gain profit is {produce["minimumpriceforsale"]:.2f} ")
                                produce["creation"] = "Altered"
                            elif alteration == 4:
                                produce["marketprice"] = float(
                                    input("Enter the new value you want to sell the product at"))
                                produce["profit"] = produce["marketprice"] - produce["minimumpriceforsale"]
                                print(f"The new profit from one {produce["name"]} is {produce["profit"]}")
                                produce["creation"] = "Altered"
                            elif alteration == 5:
                                print("To check alterations go to the History of Accountantulator")
                                alterloop = 1
                            else:
                                print("Select one")
                if foundname == False:
                    print("No product with that name")
                alternativeloop = int(input("Continue Searching?\n1. Yes\n2. No "))

        elif option == 6:
            print("Goodbye")
            loop = 0
        else:
            print("Use a valid input")


except FileNotFoundError:
    print("Error: The file 'projectCS.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")