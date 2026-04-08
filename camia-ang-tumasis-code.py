import json
import time
#use
def main():
    try:
        # READING from the file
        filename = "projectCS.json"
        with open(filename, 'r') as file:
            # Load the JSON data from the file
            data = json.load(file)
        mainloop = 1
        historynumber = 1
        while mainloop != 0:
            first = int(
                input("Welcome to the Accountantulator\nWhat do you want to calculate?\n1.VAT\n2.Income\n3.Exit "))
            time.sleep(0.5)
            print("In this software you will be able to calculate either your VAT of a product or your Income Tax")
            if first == 1:
                loop = 1
                while loop != 0:
                    option = int(input(
                        "Welcome to the VAT part of the Accountantulator\nPlease pick the number of the  option that you want  to do\n1. Calculate VAT of product\n2. History of your Accountantulator\n3. How to use Accountantulator\n4. Find Product\n5. Alter Product\n6. Exit "))
                    if option == 1:
                        historynumber = historynumber + 1
                        newdict = {}
                        newdict["username"] = input("What is your name? ")
                        newdict["name"] = input("What is the name of the product ")
                        while True:
                            newdict["price"] = input(f"Enter value of {newdict["name"]} ")
                            try:
                                newdict["price"] = float(newdict["price"])
                                break
                            except ValueError:
                                print(f"Please input a number")
                        newdict["vatofproduct"] = newdict["price"] * 0.12
                        print(f"The VAT is {newdict["vatofproduct"]:.2f} ")
                        newdict["minimumpriceforsale"] = newdict["vatofproduct"] + newdict["price"] + 0.1
                        print(f"The minimum price to gain profit is {newdict["minimumpriceforsale"]:.2f} ")
                        while True:
                            newdict["marketprice"] = input("Enter the value you want to sell the product at")
                            try:
                                newdict["marketprice"] = float(newdict["marketprice"])
                                break
                            except ValueError:
                                print(f"Please input a number")
                        newdict["profit"] = newdict["marketprice"] - newdict["minimumpriceforsale"]
                        print(f"The profit from one {newdict["name"]} is {newdict["profit"]:.2f}")
                        newdict["creation"] = "Created by User"
                        newdict["historyno"] = historynumber
                        newdict["type"] = "VAT"
                        data.append(newdict)

                    elif option == 2:
                        checkhistory = 1
                        while checkhistory == 1:
                            for produce in data:
                                for i in produce:
                                    time.sleep(0.1)
                                    print(f"{i.capitalize()}: {produce[i]}")
                                print("")
                            while True:
                                try:
                                    checkhistory = (input("Return to Menu?\n1. No\n2. Yes"))
                                    checkhistory = int(checkhistory)
                                    if checkhistory == 1  or checkhistory == 2:
                                        break
                                except:
                                    print("Use only 1 or 2")


                    elif option == 3:
                        sampledict = {"username": "", "name": "", "price": 0, "vatofproduct": 0,
                                      "minimumpriceforsale": 0,
                                      "marketprice": 0, "profit": 0, "creation": "Sample", "historyno": 0}
                        print("Welcome to the Tutorial for using the Accountantulator")
                        print("We will give a quick run down on how the Accountantulator works")
                        time.sleep(1)
                        sampledict["username"] = input("First input your username")
                        print("We then get the name of your product")
                        sampledict["name"] = input("Input the name of your product")
                        print(f"The name of your product is {sampledict["name"]}")
                        time.sleep(0.5)
                        while True:
                            sampledict["price"] = input(f"Enter value of {sampledict["name"]} ")
                            try:
                                sampledict["price"] = float(sampledict["price"])
                                break
                            except ValueError:
                                print(f"Please input a number")
                        time.sleep(0.5)
                        sampledict["vatofproduct"] = sampledict["price"] * 0.12
                        print(f"You will now recieve the VAT of your product, which is {sampledict["vatofproduct"]}")
                        time.sleep(0.5)
                        sampledict["minimumpriceforsale"] = sampledict["vatofproduct"] + sampledict["price"] + 0.1
                        time.sleep(0.5)
                        print(
                            f"Now the Accountantulator will solve for the minimum price for you to have a profit, which is {sampledict["minimumpriceforsale"]}")
                        time.sleep(0.5)
                        sampledict["marketprice"] = float(
                            input("Now you can appoint the price you are going to sell the product for accounting VAT"))
                        sampledict["profit"] = sampledict["marketprice"] - sampledict["minimumpriceforsale"]
                        while True:
                            sampledict["marketprice"] = input(f"Enter the price that you want to sell {sampledict["name"]} ")
                            try:
                                sampledict["marketprice"] = float(sampledict["marketprice"])
                                break
                            except ValueError:
                                print(f"Please input a number")
                        time.sleep(2)
                        print(
                            f"Lastly, the Accountantulator will give you the profit per product sold, for the sample you provided it is {sampledict["profit"]}")
                        time.sleep(1)
                        print(
                            "When using the Accountantulator you will also get a history number to track the history of usage of the Accountantulator.")
                        sampledict["creation"] = "Sample test by User"
                        sampledict["historyno"] = 0
                        sampledict["type"] = "VAT"
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
                            while True:
                                try:
                                    alternativeloop = (input("Continue Searching?\n1. Yes\n2. No "))
                                    alternativeloop = int(alternativeloop)
                                    if alternativeloop == 1  or alternativeloop == 2:
                                        break
                                except:
                                    print("Use only 1 or 2")


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
                                            while True:
                                                produce["price"] = input("Please enter a new price: ")
                                                try:
                                                    produce["price"] = float(produce["price"])
                                                    break
                                                except ValueError:
                                                    print(f"Please input a number")
                                            produce["vatofproduct"] = produce["price"] * 0.12
                                            print(f"The VAT is {produce["vatofproduct"]:.2f} ")
                                            produce["minimumpriceforsale"] = produce["vatofproduct"] + produce[
                                                "price"] + 0.1
                                            print(
                                                f"The minimum price to gain profit is {produce["minimumpriceforsale"]:.2f} ")
                                            produce["creation"] = "Altered"
                                        elif alteration == 4:
                                            while True:
                                                produce["marketprice"] = input("Please enter a valid price: ")
                                                try:
                                                    produce["price"] = float(produce["marketprice"])
                                                    break
                                                except ValueError:
                                                    print(f"Please input a number")
                                            produce["profit"] = produce["marketprice"] - produce["minimumpriceforsale"]
                                            print(f"The new profit from one {produce["name"]} is {produce["profit"]}")
                                            produce["creation"] = "Altered"
                                        elif alteration == 5:
                                            print("To check alterations go to the History of Accountantulator")
                                            alterloop = 1
                                        else:
                                            print("Select one of the valid")
                            if foundname == False:
                                print("No product with that name")
                            while True:
                                try:
                                    alternativeloop = (input("Return to Menu?\n1. No\n2. Yes"))
                                    alternativeloop = int(checkhistory)
                                    if alternativeloop == 1 or alternativeloop == 2:
                                        break
                                except:
                                    print("Use only 1 or 2")

                    elif option == 6:
                        print("Back to Main loop")
                        loop = 0
                    else:
                        print("Use a valid input")
            elif first == 2:
                loop = 0
                while loop == 0:
                    option = int(input(
                        "Welcome to the Income Tax part of the Accountantulator, what do you want to do \n1.Calculate Income tax\n2.History of Accountantulator\n3.Find Income tax\n4.Alter Income tax\n5.Exit"))
                    if option == 1:
                        historynumber = historynumber + 1
                        newdict = {}
                        newdict["username"] = input("What is your name? ")

                        try:
                            newdict["income"] = int(input("What is your income, format is numbers only no commas or spaces"))
                            test= newdict["income"]+ 1
                        except ValueError:
                            newdict["income"] = int(input('Please use a valid input'))

                        if newdict["income"] <= 250000:
                            newdict["incometax"] = 0
                            newdict["newincome"] = newdict["income"]

                        elif newdict["income"] >= 250001 and newdict["income"] <= 400000:
                            newdict["incometax"] = (newdict["income"] - 250000) * 0.15
                            newdict["newincome"] = newdict["income"] - newdict["incometax"]

                        elif newdict["income"] >= 400001 and newdict["income"] <= 800000:
                            newdict["incometax"] = ((newdict["income"] - 400000) * 0.2) + 22500
                            newdict["newincome"] = newdict["income"] - newdict["incometax"]

                        elif newdict["income"] >= 800001 and newdict["income"] <= 2000000:
                            newdict["incometax"] = ((newdict["income"] - 800000) * 0.25) + 102500
                            newdict["newincome"] = newdict["income"] - newdict["incometax"]

                        elif newdict["income"] >= 2000001 and newdict["income"] <= 8000000:
                            newdict["incometax"] = ((newdict["income"] - 2000000) * 0.3) + 402500
                            newdict["newincome"] = newdict["income"] - newdict["incometax"]

                        elif newdict["income"] > 8000000:
                            newdict["incometax"] = ((newdict["income"] - 8000000) * 0.35) + 2202500
                            newdict["newincome"] = newdict["income"] - newdict["incometax"]

                        newdict["historyno"] = historynumber + 1
                        newdict["type"] = "Income Tax"
                        data.append(newdict)
                        print(
                            f"You have {newdict["incometax"]} income tax, meaning your income after tax is {newdict["newincome"]}")

                    elif option == 2:
                        checkhistory = 1
                        while checkhistory == 1:
                            for produce in data:
                                for i in produce:
                                    time.sleep(0.1)
                                    print(f"{i.capitalize()}: {produce[i]}")
                                print("")
                            while True:
                                try:
                                    checkhistory = (input("Return to Menu?\n1. No\n2. Yes"))
                                    checkhistory = int(checkhistory)
                                    if checkhistory == 1 or checkhistory == 2:
                                        break
                                except:
                                    print("Use only 1 or 2")

                    elif option == 3:
                        foundname = False
                        alternativeloop = 1
                        while alternativeloop != 2:
                            nameofindinctax = input("Please input the name of the person you want to find")
                            for person in data:
                                if person["username"] == nameofindinctax and person["type"] == "Income Tax":
                                    foundname = True
                                    print("Found it!")
                                    print(f"Printing Data for {nameofindinctax}")
                                    time.sleep(3)
                                    for i in person:
                                        print(f"{i.capitalize()}: {person[i]}")
                            if foundname == False:
                                print("No product with that name")
                            while True:
                                try:
                                    alternativeloop = (input("Continue Searching?\n1. Yes\n2. No "))
                                    alternativeloop = int(alternativeloop)
                                    if alternativeloop == 1 or alternativeloop == 2:
                                        break
                                except:
                                    print("Use only 1 or 2")

                    elif option == 4:
                        alternation = 0
                        alterloop = 0
                        foundname = False
                        alternativeloop = 1
                        while alternativeloop != 2:
                            nameofindinctax = input("Please input the name of the person you want to find")
                            for person in data:
                                if person["username"] == nameofindinctax and person["type"] == "Income Tax":
                                    foundname = True
                                    print("Found it!")
                                    print(f"Printing Data for {nameofindinctax}")
                                    while alterloop == 0:
                                        alteration = int(input("What do you want to alternate\n1.Username\n2.Income"))
                                        if alteration == 1:
                                            person["username"] = input("What is you name?")
                                        elif alteration == 2:
                                            while True:
                                                person["income"] = input("Please enter a new price: ")
                                                try:
                                                    person["icome"] = float(person["income"])
                                                    break
                                                except ValueError:
                                                    print(f"Please input a number")
                                            if person["income"] <= 250000:
                                                person["incometax"] = 0
                                                person["newincome"] = person["income"]

                                            elif person["income"] >= 250001 and person["income"] <= 400000:
                                                person["incometax"] = (person["income"] - 250000) * 0.15
                                                person["newincome"] = person["income"] - person["incometax"]

                                            elif person["income"] >= 400001 and person["income"] <= 800000:
                                                person["incometax"] = ((person["income"] - 400000) * 0.2) + 22500
                                                person["newincome"] = person["income"] - person["incometax"]

                                            elif person["income"] >= 800001 and person["income"] <= 2000000:
                                                person["incometax"] = ((person["income"] - 800000) * 0.25) + 102500
                                                person["newincome"] = person["income"] - person["incometax"]

                                            elif person["income"] >= 2000001 and person["income"] <= 8000000:
                                                person["incometax"] = ((person["income"] - 2000000) * 0.3) + 402500
                                                person["newincome"] = person["income"] - person["incometax"]

                                            elif person["income"] > 8000000:
                                                person["incometax"] = ((person["income"] - 8000000) * 0.35) + 2202500
                                                person["newincome"] = person["income"] - person["incometax"]
                                        person["creation"] = "Altered"
                                    else:
                                        print(" Please use a valid input")
                                if foundname == False:
                                    print("No product with that name")
                    else:
                        print("Please use a valid input")
            elif first == 3:
                mainloop = 0
            else:
                print("Please use a valid input")

    except FileNotFoundError:
        print("Error: The file 'projectCS.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

main()
