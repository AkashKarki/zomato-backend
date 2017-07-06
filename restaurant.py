restaurant_detail={"Domino's":{"Owner's name":"Tom Monaghan","rating":"0","Food":{"Margherita":"350","Peppy Paneer":"450","Veg Extravaganza":"500","Mexican Green Wave":"475"}},
                "pizza hut":{"Owner's name":"Virag Joshi","rating":"0","Food":{"Paneer & Capsicum":"370","Chicken keema & Corn":"480","Chicken Hot N Spicy":"500","Onion":"375"}}}

print"WELCOME"
type=raw_input("\npress 1 if you are customer\npress 2 if you are owner\nwaiting for your response::")
if type=="2":
        choice=raw_input("\npress 1 to update information \npress 2 to quit\nwaiting for your response::")
        if choice=="1":
            rest_name=raw_input("\npress 1 to update domino's information\npress 2 to update pizza hut information\nwaiting for your response::")
            if rest_name=="1":
                update_ch=raw_input("\npress 1 to update owner's information\npress 2 to update food information\nwaiting for your response::")
                if update_ch=="1":
                    new_name=raw_input("enter new name")
                    restaurant_detail["Domino's"]["Owner's name"] = new_name
                if update_ch=="2":
                    choice2=raw_input("\npress 1 to update price\npress 2 to add food\npress 3 to remove food\nwaiting for your response::")
                    if choice2=="1":
                        name=raw_input("enter the name of food item::")
                        if name in restaurant_detail["Domino's"]["Food"]:
                            price=raw_input("enter new price")
                            restaurant_detail["Domino's"]["Food"][name] = price
                        else:
                            print"Food item not found try again"
                            exit()
                    if choice2=="2":
                        new_item_name = raw_input("enter the name of new food item::")
                        new_item_price = raw_input("enter price of new food item::")
                        restaurant_detail["Domino's"]["Food"].update({new_item_name: new_item_price})
                        print"item added"
                        exit()
                    if choice2=="3":
                        name = raw_input("enter the name of food item you want to remove::")
                        if name in restaurant_detail["Domino's"]["Food"]:
                            del restaurant_detail["Domino's"]["Food"][name]
                            print"item deleted"
                            exit()
                        else:
                            print"Food item not found try again"
                            exit()
            if rest_name=="2":
                update_ch = raw_input("\npress 1 to update owner's information\npress 2 to update food information\nwaiting for your response::")
                if update_ch == "1":
                    new_name = raw_input("enter new name")
                    restaurant_detail["pizza hut"]["Owner's name"] = new_name
                    print "information updated"
                    exit()
                if update_ch == "2":
                    choice2 = raw_input("\npress 1 to update price\npress 2 to add food\npress 3 to remove food\nwaiting for your response::")
                    if choice2 == "1":
                        name = raw_input("enter the name of food item::")
                        if name in restaurant_detail["pizza hut"]["Food"]:
                            price = raw_input("enter new price")
                            restaurant_detail["pizza hut"]["Food"][name] = price
                            print"price updated"
                            exit()
                        else:
                            print"Food item not found try again"
                            exit()
                    if choice2 == "2":
                        new_item_name = raw_input("enter the name of new food item::")
                        new_item_price = raw_input("enter price of new food item::")
                        restaurant_detail["pizza hut"]["Food"].update({new_item_name: new_item_price})
                        print"item added"
                        exit()
                    if choice2 == "3":
                        name = raw_input("enter the name of food item you want to remove::")
                        if name in restaurant_detail["pizza hut"]["Food"]:
                            del restaurant_detail["pizza hut"]["Food"][name]
                            print"item deleted"
                            exit()
                        else:
                            print"Food item not found try again"
                            exit()
if type=="1":
    print"\nname of restaurant::Domino's"
    print"\nmenu of Domino's\n"
    for food in restaurant_detail["Domino's"]["Food"]:
        print"=>"+ food
    print"\nname of restaurant::pizza hut\n"
    print"\nmenu of pizza hut\n"
    for food in restaurant_detail["pizza hut"]["Food"]:
        print"=>"+ food
    choice=raw_input("\npress 1 to select Domino's\npress 2 to select pizza hut\nwaiting for your response::")
    if choice=="1":
        food_name=raw_input("enter name of the food you want to order::")
        if food_name in restaurant_detail["Domino's"]["Food"]:
            print "order successful"
        else:
            print "not available"
            exit()
    if choice=="2":
        food_name = raw_input("enter name of the food you want to order::")
        if food_name in restaurant_detail["pizza hut"]["Food"]:
            print "order successful"
        else:
            print "not available"
            exit()
    print"\npress 1 for walk-in\npress 2 for delievery\nwaiting for your response::"
    choice2=raw_input()
    if choice2=="1":
        print"order method walk-in"
        if choice=="1":
            cost=int(restaurant_detail["Domino's"]["Food"][food_name])
            bill=cost+(.1*cost)+(.06*cost)+(0.15*cost)
            print "your bill is::"+str(bill)
        elif choice=="2":
            cost = int(restaurant_detail["pizza hut"]["Food"][food_name])
            bill = cost + (.1 * cost) + (.06 * cost) + (0.15 * cost)
            print "your bill is::" + str(bill)
    if choice2=="2":
        print"order method delievery"
        if choice=="1":
            cost=int(restaurant_detail["Domino's"]["Food"][food_name])
            bill=cost+(.1*cost)+(.06*cost)+(0.15*cost)
            print "your bill is::"+str(bill)
        elif choice=="2":
            cost = int(restaurant_detail["pizza hut"]["Food"][food_name])
            bill = cost + (.1 * cost) + (.06 * cost) + (0.15 * cost)
            print "your bill is::" + str(bill)
    rating_ch=raw_input("\ndo you want to rate the restaurant::\npress 1 to rate\npress 2 to quit\nwaiting for your response::")
    if rating_ch=="1":
        rating=raw_input("rate the restaurant from 1-10::")
        if choice=="1":
            restaurant_detail["Domino's"]["rating"] = rating
        if choice=="2":
            restaurant_detail["pizza hut"]["rating"] = rating
        print "have a nice day"
    if rating_ch=="2":
        print "have a nice day"