#Tumasis, Bleuzette Albrielle Felenash M. 
#Ang, Juneau Jazz Q.

#Add needed libraries
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

    #Main Menu Loop. The program runs here
    while loop != 0:

        #Shows the menu and asks the user what they want to do
        option = int(input("Welcome to the Accountantulator\nPlease pick the number of the  option that you want  to do\n1. Calculate VAT of product\n2. History of your Accountantulator\n3. How to use Accountantulator\n4. Find Product\n5. Alter Product\n6. Exit"))
        #Option 1: Calculate VAT
        if option == 1:
            #Increases history count
            historynumber= historynumber + 1
            #Dictionary to store product information
            newdict = {}
            #Asks the user for basic product details
            newdict["username"] = input("What is your name? ")
            newdict["name"] = input("What is the name of the product ")
            #Gets the product price
            newdict["price"] = float(input(f"Enter value of {newdict["name"]} "))
            #Calculates VAT
            newdict["vatofproduct"] = newdict["price"]*0.12
            print(f"The VAT is {newdict["vatofproduct"]:.2f} ")
            #Calculates the minimum selling price
            newdict["minimumpriceforsale"] = newdict["vatofproduct"] + newdict["price"]+0.1
            print(f"The minimum price to gain profit is {newdict["minimumpriceforsale"]:.2f} ")
            #Asks user what price they want to sell it at
            newdict["marketprice"]=float(input("Enter the value you want to sell the product at: " ))
            #Calculates profit
            newdict["profit"] = newdict["marketprice"]-newdict["minimumpriceforsale"]
            print(f"The profit from one {newdict["name"]} is {newdict["profit"]}")
            #Marks that this was created by the user
            newdict["creation"] = "Created by User"
            #Saves history number 
            newdict["historyno"] = historynumber
            #Adds this product to data list
            data.append(newdict)
            
        #Option 2: Show history
        elif option == 2:
            #Loops through every saved product 
            for produce in data:
                #Prints each detail of the product
                for i in produce:
                    print(f"{i.capitalize()}: {produce[i]}")
                print("")
        #Option 3: Tutorial or How to use
        elif option == 3:
            #Quick Print statement for greeting
            print("Welcome to the Tutorial for using Accountalator! \n We will give a quick run down on how it works")
            #Creates a sample product to demonstrate
            sampledict ={"username": "","name": "", "price": 0,"vatofproduct": 0,"minimumpriceforsale": 0,"marketprice": 0,"profit": 0,"creation": "Sample","historyno": 0}
            print("Welcome to the Tutorial for using the Accountantulator")
            print("We will give a quick run down on how the Accountantulator works")
            time.sleep(1)
            #Step by step demo
            sampledict["username"]= input("First input your username")
            print("We then get the name of your product")
            sampledict["name"] = input("Input the name of your product")
            print(f"The name of your product is {sampledict["name"]}")
            time.sleep(0.5)
            sampledict["price"]= float(input("Now input the price of the product you have "))
            time.sleep(0.5)
            #Calculates VAT
            sampledict["vatofproduct"] = sampledict["price"] * 0.12
            print(f"You will now recieve the VAT of your product, which is {sampledict["vatofproduct"]}")
            time.sleep(0.5)
            #Calculates minimum selling price 
            sampledict["minimumpriceforsale"] = sampledict["vatofproduct"] + sampledict["price"]+0.1
            time.sleep(0.5)
            print(f"Now the Accountantulator will solve for the minimum price for you to have a profit, which is {sampledict["minimumpriceforsale"]}")
            time.sleep(0.5)
            #Asks the user for their selling price
            sampledict["marketprice"] =float(input("Now you can appoint the price you are going to sell the product for accounting VAT" ))
            #Calculates the profit and records the history number
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
        #Option 4: Find product 
        elif option == 4:
            foundname = False
            alternativeloop = 1
            while alternativeloop != 2:
                productnametofind = input("Please input the name of the product you want to find")
                #Searches through saved data
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

        #Option 5: Alter Product
        #This option allows user to edit or update information about a product
        elif option == 5:
            #Helps us check if the product name provided actually exists
            foundname = False
            #Controls whether the user wants to keep searching for products to alter
            alternativeloop = 1
            #Loops until option 2 is chosen
            while alternativeloop != 2:
                #Asks the user which product they want to change
                productnametoalter = input("Please input the name of the product you want to alter")
                #Loops through every product stored in the data list
                for produce in data:
                    #Checks if the product's name matches the one user provided
                    if produce["name"] == productnametoalter:
                        foundname = True
                        print(f"Printing Data for {productnametoalter}")
                        time.sleep(3)
                        for i in produce:
                            print(f"{i.capitalize()}: {produce[i]}")
                        alterloop = 0
                        while alterloop == 0:
                            #Asks the user what part of the product they would like to modify
                            alteration = int(input(
                                "What do you want to alter?\n1. Username\n2. Product Name\n3. Price of Product\n4. Market Price of Product\n5. Finish Alterations"))
                            #Option 1: Change Username
                            if alteration == 1:
                                #Updates the username and marks that this was altered
                                produce["username"] = input("Input a new Username")
                                produce["creation"] = "Altered"
                            #Option 2: Change Product Name
                            elif alteration == 2:
                                #Updates the product name and marks as altered
                                produce["name"] = input("Input new product name")
                                produce["creation"] = "Altered"
                            #Option 3: Change product price
                            elif alteration == 3:
                                #Updates base price and recalculates VAT and minimum selling price
                                produce["price"] = float(int("Input the new Price of Product"))
                                produce["vatofproduct"] = produce["price"] * 0.12
                                print(f"The VAT is {produce["vatofproduct"]:.2f} ")
                                produce["minimumpriceforsale"] = produce["vatofproduct"] + produce["price"] + 0.1
                                print(f"The minimum price to gain profit is {produce["minimumpriceforsale"]:.2f} ")
                                #Marks as Altered
                                produce["creation"] = "Altered"
                                #Option 4: Change Market Price
                            elif alteration == 4:
                                #Updates selling price and recalculates profit
                                produce["marketprice"] = float(
                                    input("Enter the new value you want to sell the product at"))
                                produce["profit"] = produce["marketprice"] - produce["minimumpriceforsale"]
                                print(f"The new profit from one {produce["name"]} is {produce["profit"]}")
                                #Marks as Altered
                                produce["creation"] = "Altered"
                            #Option 5: Finish Editing
                            elif alteration == 5:
                                #Informs the user that the alteration is complete and exits the editing loop
                                print("Alterations complate. To check alterations go to the History of Accountantulator")
                                alterloop = 1
                            else:
                                print("Select one")
                #If no name matched what the user typed
                if foundname == False:
                    print("No product with that name")
                #Asks the user if they want to search and alter another product
                alternativeloop = int(input("Continue Searching?\n1. Yes\n2. No "))
        #Option 6: Exit Program
        elif option == 6:
            print("Goodbye")
            loop = 0
        else:
            print("Use a valid input")

#Error Handling
except FileNotFoundError:
    print("Error: The file 'projectCS.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
