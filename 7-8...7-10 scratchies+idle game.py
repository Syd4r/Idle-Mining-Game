#idlegame?
#wht to do
#exception aversion
import time
import random
import blackjack
def mine(inventory,inventory_price,items,money,rarity_list,cells_mined):
    mines_cost =[0,25,100,500]
    mine = []
    visual_mine = []
    while True:
        print()
        which_mine = input("Which mine do you want to pick (1 Basic: 0g, 2 Beginner: 25g, 3 Intermediate: 100g, 4 Expert: 500g): ")
        if which_mine in ["1","2","3","4"]:
            if mines_cost[int(which_mine)-1] > money:
                print("Too expensive")
            else:
                money -= mines_cost[int(which_mine) - 1]
                break
        else:
            print("Not a valid input")
    rarity = rarity_list[int(which_mine)-1]
    for i in range(int(which_mine)+3):
        row = []
        row_2 = []
        for j in range(int(which_mine)+3):
            thing_picked = random.uniform(0,1)
            for k in range(len(rarity)):
                if thing_picked <= rarity[k]:
                    row.append(items["name"][k])
                    row_2.append("X")
                    break
        mine.append(row)
        visual_mine.append(row_2)
    testing = []
    for i in range(len(mine)):
        testing.append(str(i+1))
    for i in range((int(which_mine)+2)*2+cells_mined):
        for p in range(len(mine)):
            print(visual_mine[p])
        print("You have "+str(((int(which_mine)+2)*2)-i+cells_mined)+" more tiles to uncover.")
        while True:
            print()
            down_amount = input("How far down do you want to mine?: ")
            right_amount = input("How far right do you want to mine?: ")
            if down_amount in testing and right_amount in testing:
                if visual_mine[int(down_amount)-1][int(right_amount)-1] == "X":
                    inventory.append(mine[int(down_amount)-1][int(right_amount)-1])
                    print()
                    print("You uncovered a "+mine[int(down_amount)-1][int(right_amount)-1]+" worth "+str(items["worth"][items["name"].index(mine[int(down_amount)-1][int(right_amount)-1])]))
                    inventory_price.append(items["worth"][items["name"].index(mine[int(down_amount)-1][int(right_amount)-1])])
                    visual_mine[int(down_amount) - 1][int(right_amount) - 1] = "O"
                    break
                else:
                    print("Already uncovered")
            else:
                print("Not a valid input")
    print()
    print("You've finished this mine")
    return inventory, inventory_price,money
money = 500
upgrade_variables = [0,0,0,0,0]
upgrades_name = ["Reduce Auto-Miner Mining Time", "More Uncovers While Mining", "Better Coinflip Odds",
                 "Everything Sells for 1 More Money", "Everything Sells for 1% More Money"]
upgrades_max = [30,5,50,100,100]
upgrades_price = [250,500,500,1000,2000]
items = {
        "name": ["dirt","stone","coal","iron","gold","diamond","ruby","emerald","sapphire","rose diamond","fossil", "ancient civilization", "temple of gold","hidden gold dimension","wormhole to gold universe","king midas","boobs"],
        "worth": [1,1,2,4,8,16,16,32,64,128,256,512,1024,2048,4096,8192,100000]
    }
rarity = [[0.25,0.5,0.7,0.9,0.95,0.99,1],[0.2,0.4,0.55,0.7,0.8,0.9,0.95,0.99,1], [0.15,0.3,0.4,0.5,0.6,0.7,0.75,0.8,0.85,0.9,0.94,0.98,0.99,1], [0.15,0.3,0.375,0.45,0.525,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.94,0.98,0.99,1]]
items_name = ["Old Sock","Hamburger","Wedding Ring", "2003 Honda Civic", "Trophy","Infinity Gauntlet","Infinite Money","No Money","IRL BOOBS"]
lore = ["Woo, you have money", 'The importance of disposable income',"For the love in your dreams", "Flex your wealth with transportation","Flex your wealth","Flex your wealth with power","Flex your wealth with wealth","Flex your wealth with no wealth","Redeem your wealth for actual profit"]
item_price = [100,1000,10000,100000,1000000,10000000,100000000,1000000000,1000000000000]
inventory = []
inventory_price = []
auto_miner_created = [[],[],[],[]]
auto_miners = [[],[],[],[]]
auto_miners_inv = [[],[],[],[]]
while True:
    how_long_mine = upgrade_variables[0]
    cells_mined = upgrade_variables[1]
    coin_flip_odds = upgrade_variables[2]
    plus_money = upgrade_variables[3]
    multiply_money = upgrade_variables[4]
    print("You have "+str(money)+" money.")
    whatdo = input("What do you want to do (Mine: M, Sell: S, Buy: B, Collect: C, View Inventory: I): ")
    if whatdo == "M":
        stuffies = mine(inventory,inventory_price,items,money,rarity,cells_mined)
        inventory = stuffies[0]
        inventory_price = stuffies[1]
        money = stuffies[2]
    elif whatdo == "S":
        print()
        whatdo_2 = input("Check price: (C), Sell One: (S1), or Sell All: (SA)?: ")
        print()
        if whatdo_2 == "C":
            while True:
                print()
                which_price = input("Which do you want to check "+str(items["name"])+"?: ")
                if which_price in items["name"]:
                    print("The price of "+which_price+" is "+str(items["worth"][items["name"].index(which_price)]))
                else:
                    print("Not a valid input")
        elif whatdo_2 == "S1":
            print("Your items are "+str(inventory))
            while True:
                print()
                which_item = input("What item do you want to sell? (1-"+str(len(inventory))+"): ")
                if which_item in inventory:
                    print("You sold a "+inventory[int(which_item)-1]+ " for "+str(inventory_price[int(which_item)-1])+" money")
                    inventory.pop(int(which_item)-1)
                    money += inventory_price[int(which_item)-1]
                    inventory_price.pop(int(which_item)-1)
                    break
                else:
                    print("Not a valid input")
        elif whatdo_2 == "SA":
            print("You sold everything")
            money += sum(inventory_price)
            inventory = []
            inventory_price = []
        else:
            print("Not a valid input")
    elif whatdo == "B":
        whatbuy = input("What do you want to buy? Auto-Miners: (M), Upgrades: (U), Gambles (G), Items (I): ")
        if whatbuy == "M":
            priceautominers = [50,250,750,2500]
            while True:
                print()
                whichmine = input("Which mine do you want to buy an autominer for? (1 Basic: 50g, 2 Beginner: 250g, 3 Intermediate: 750g, 4 Expert: 2500g): ")
                if whichmine in ["1","2","3","4"]:
                    if priceautominers[int(whichmine)-1] <= money:
                        money -= priceautominers[int(whichmine)-1]
                        auto_miners[int(whichmine)-1].append(int(time.time()))
                        auto_miner_created[int(whichmine)-1].append(False)
                        break
                    else:
                        print("Cant afford")
                else:
                    print("Not a valid input")
        elif whatbuy == "G":
            print()
            whichgamble = input("Do you want to do a coin flip or play blackjack? (C or B): ")
            while True:
                howmuch = input("How much do you want to bet?: ")
                if int(howmuch) <= money:
                    break
                else:
                    print()
                    print("Not enough money")
            if whichgamble == "C":
                print()
                print("Coin flip in...")
                for i in range(3):
                    time.sleep(1)
                    print(str(3-i))
                if random.randint(1,500) <= 250+coin_flip_odds:
                    returnvalue = 1
                    print("YOU WIN")
                else:
                    returnvalue = -1
                    print("YOU LOSE")
            elif whichgamble == "B":
                returnvalue = blackjack.run()
            else:
                print("Not a valid input")
                returnvalue = 0
            print()
            money += int(howmuch)*int(returnvalue)
        elif whatbuy == "U":
            print()
            print("Upgrades: ")
            for i in range(len(upgrades_name)):
                print(str(i+1)+" "+upgrades_name[i]+"   Price: "+str(upgrades_price[i])+"  Max Purchasable: "+str(upgrades_max[i])+"  Current Purchased: "+str(upgrade_variables[i]))
            while True:
                print()
                which_upgrade = input("Which do you want to upgrade? (1-5)(E to exit): ")
                if which_upgrade in ["1","2","3","4",'5']:
                    save = int(which_upgrade)-1
                    if upgrades_price[save] <= money:
                        if upgrade_variables[save] < upgrades_max[save]:
                            upgrade_variables[save] += 1
                            money -= upgrades_price[save]
                            break
                        else:
                            print("Upgrade Already Maxed")
                    else:
                        print("Not Enough Money")
                elif which_upgrade == "E":
                    break
                else:
                    print("Not a Valid Input")
        elif whatbuy == "I":
            print()
            print("Items:")
            check = []
            for i in range (len(items_name)):
                print(str(i+1)+": "+items_name[i]+":  "+lore[i]+"   Price: "+str(item_price[i]))
                check.append(str(i+1))
            while True:
                print()
                whatitem = input("Which item do you want to buy? (1-"+str(len(items_name))+"}(E to exit): ")
                if whatitem in check:
                    if item_price[int(whatitem)-1] <= money:
                        inventory.append(items_name[int(whatitem)-1])
                        inventory_price.append(item_price[int(whatitem)-1])
                        money -= item_price[int(whatitem)-1]
                        break
                    else:
                        print("Too expensive")
                elif whatitem == "E":
                    break
                else:
                    print("Not a valid input")
        else:
            print("Not a valid input")
    elif whatdo == "C":
        print()
        whichcollect = input("Do you want to collect all (CA) or collect one auto-miner (C): ")
        for i in range(len(auto_miner_created)):
            for j in range(len(auto_miner_created[i])):
                miner_inv = []
                for k in range(int((int(time.time())-auto_miners[i][j])/60-how_long_mine)):
                    thing_picked = random.uniform(0, 1)
                    for l in range(len(rarity[i])):
                        if thing_picked <= rarity[i][l]:
                            miner_inv.append(items["name"][l])
                            break
                auto_miners[i][j] = int(time.time())
                if whichcollect == "CA":
                    for k in range(len(miner_inv)):
                        inventory.append(miner_inv[k])
                        inventory_price.append(items["worth"][items["name"].index(miner_inv[k])])
                else:
                    if not auto_miner_created[i][j]:
                        auto_miners_inv[i].append(miner_inv)
                    else:
                        for k in range(len(miner_inv)):
                            auto_miners_inv[i][j].append(miner_inv[k])
                    auto_miner_created[i][j] = True
        if whichcollect == "CA":
            for l in range(len(auto_miners_inv)):
                for m in range(len(auto_miners_inv[l])):
                    for n in range(len(auto_miners_inv[l][m])):
                        inventory.append(auto_miners_inv[l][m][n])
                        inventory_price.append(items["worth"][items["name"].index(auto_miners_inv[l][m][n])])
                    auto_miners_inv[l][m] = []
        else:
            for i in range(len(auto_miners_inv)):
                for j in range(len(auto_miners_inv[i])):
                    print()
                    print("Auto-Miner for Mine "+str(i+1)+" which has "+str(auto_miners_inv[i][j]))
            variableforthisonesituation = 0
            for i in range(len(auto_miners_inv)):
                if len(auto_miners_inv[i]) > 0:
                    variableforthisonesituation += 1
            while True:
                print()
                whichautominerlevel = input("Which mine level auto-miner do you want to collect? Mine Level (1-4): ")
                if whichautominerlevel in ["1","2","3","4"]:
                    break
                else:
                    print("Not a valid input")
            whichautominer = input("Which auto-miner from that level? (1-"+str(len(auto_miners_inv[int(whichautominerlevel)-1]))+"): ")
            for i in range(len(auto_miners_inv[int(whichautominerlevel)-1][int(whichautominer)-1])):
                inventory.append(auto_miners_inv[int(whichautominerlevel) - 1][int(whichautominer)-1][i])
                inventory_price.append(items["worth"][items["name"].index(auto_miners_inv[int(whichautominerlevel)-1][int(whichautominer)-1][i])])
            auto_miners_inv[int(whichautominerlevel) - 1][int(whichautominer)-1] = []
            print()
            print("You collected from an auto-miner")
    elif whatdo == "I":
        different_things_in_inv = []
        for i in range(len(inventory)):
            if inventory[i] not in different_things_in_inv:
                different_things_in_inv.append(inventory[i])
        for i in range(len(different_things_in_inv)):
            print("You have "+str(inventory.count(different_things_in_inv[i]))+" "+different_things_in_inv[i])
    else:
        print("Not a valid input")
    print()