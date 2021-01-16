import discord
import random
import os
import time
NewEmbed=discord.Embed(title="_", description="_", color=0x00fff0)
ClientID = []
thievery = []
luck = []
charisma = []
strength = []

godkey = str(random.randint(100000, 999999));
print("godkey is " +str(godkey))
clients = []
balances = []
souls = []
inventory = []
client = discord.Client()
market = ["soul","GodSoul","TitanSoul","burrito", "golden burrito", ]
marketPrices = [100, 500, 1000, 10, 10000000]
marketTypes = ["soul", "GodSoul", "TitanSoul", "food", "award"]
BlackMarket = []
BlackMarketPrices = []
BlackMarketTypes = []
SaltyP1Bet = []
SaltyP1Name = []
SaltyP1Numeric = []
SaltyP2Bet = []
SaltyP2Name = []
SaltyP2Numeric = []
SaltyProcess = False
SaltyBet = False
SaltyCoin = []
SaltyVote = False
SaltyMatch = 1;
SaltyPlayers = []
SaltyMessage = 0;
SaltyEmbed = 0;
SaltyWait = False;
SaltyCombatants = ["carl", "jonas", "mario", "batman", "iron man", "kyng"];
P1 = "compile"
P2 = "compile"
timer = False;
Time = 10

def Pay(money, index):
  balances[index] += money

def decryptInv(word):
    return word.split(",")

def getInt(word, StartIndex):
  print("getInt")
  wordList = split(word)
  wordList.reverse()
  searching = True
  indexOfSearch = 0;
  indexOfLoop = 1;
  final = 0;
  #print("mod first num " +str(int(wordList[indexOfSearch])*indexOfLoop))
  #print("mod second num " +str(int(wordList[indexOfSearch])*indexOfLoop + int(wordList[indexOfSearch+1])*indexOfLoop*10))
  #print("first num " + str(int(wordList[indexOfSearch])))
  
  
  for x in range(0, len(wordList) - StartIndex):
    print("iteration " +str(x) +" with a num of " +str(int(wordList[x])) +", a character of " +str(wordList[x]) +"and a current final of " +str(final) +" will be " +str(final + int(wordList[x])*(10**(x))))
    indexOfSearch = indexOfSearch-10
    final = final + int(wordList[x])*(10**(x))
    print(str(x) +" iteration is " +str(final))
  print("final string " +str(final))
  return final

def AddList(listofstuff):
  final = 0
  for x in range(0, len(listofstuff)):
    final = listofstuff[x] + final
    return final

def Search(listofstuff, item):
    checker = True;
    index = -1;
    for u in range (0, len(listofstuff)):
        if listofstuff[u] == item:
            checker = False
    if(checker == False):
        return index
    else:
        return -1
def Remove(listofstuff, item):
    listofstuff.remove(item)
    # for u in range(0, len(listofstuff)):
    #     if listofstuff[u] == item:
    #         listofstuff.remove(u - 1)


def split(word):
    return [char for char in word]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  
    T = False
    global thievery
    global luck
    global charisma
    global strength
    global P1
    global P2
    global Time
    global godkey
    global SaltyBet
    global SaltyCoin
    global SaltyVote
    global SaltyMatch
    global SaltyEmbed
    global SaltyP1Bet
    global SaltyP1Name
    global SaltyP2Bet
    global SaltyP2Name
    global SaltyP1Numeric
    global SaltyP2Numeric
    global SaltyProcess
    global SaltyMessage
    global SaltyCombatants
    for x in range(0, len(clients)):
        #print(clients)
        if clients[x] == str(message.author.name):
            T = True
    if message.content.startswith("$register"):
        if T == False:
            NewEmbed=discord.Embed(title="Register", description="we will now register your account as " +str(message.author.name), color=0x00fff0)

            await message.channel.send(embed = NewEmbed)
            clients.append(str(message.author.name))
            balances.append(0)
            souls.append(10);
            thievery.append(1)
            strength.append(1)
            luck.append(1)
            charisma.append(1)
            inventory.append("market_pass")
            #global godkey
            #godkey = random.randint(100000,999999)
            print("new godkey: " +str(godkey))
            #ClientID.append(message.author.user.id)
            T = True
        else:
            await message.channel.send("your account is already registered")



    if T == True:
      


      if message.author.name == client.user:
        return

      if message.content.startswith("$stats read"):
        NewEmbed = discord.Embed(title= str(message.author.name) +"'s stats!", description = "Say '$stats upgrade [number of the stat you would like to upgrade]'")
        NewEmbed.add_field(name = "1: thievery", value = "level " +str(thievery[x]))
        NewEmbed.add_field(name = "2: luck", value = "level " +str(luck[x]))
        NewEmbed.add_field(name = "3: charisma", value = "level " +str(charisma[x]))
        NewEmbed.add_field(name = "4: strength", value = "level " +str(strength[x]))
        await message.channel.send(embed = NewEmbed)

      if message.content.startswith("$stats upgrade "):
        NewEmbed = discord.Embed(title = "Stats", description = "That is not a viable option")
        if(split(message.content)[15] == "1"):
          if(balances[x] >= 500):
            thievery[x] += 1
            NewEmbed = discord.Embed(title= str(message.author.name) +"'s stats!", description = str(message.author.name) +" has upgraded their thievery skills! :spy:")
        elif(split(message.content)[15] == "2"):
          if(balances[x] >= 500):
            luck[x] += 1
            NewEmbed = discord.Embed(title= str(message.author.name) +"'s stats!", description = str(message.author.name) +" has become even more lucky! :shamrock:")
        elif(split(message.content)[15] == "3"):
          if(balances[x] >= 500):
            charisma[x] += 1
            NewEmbed = discord.Embed(title= str(message.author.name) +"'s stats!", description = str(message.author.name) +" has become more attractive and desireable! :hot_face:")
        elif(split(message.content)[15] == "3"):
          if(balances[x] >= 500):
            strength[x] += 1
            NewEmbed = discord.Embed(title= str(message.author.name) +"'s stats!", description = str(message.author.name) +" has become more attractive and desireable! :hot_face:")
        await message.channel.send(embed = NewEmbed)


      if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
      if message.content.startswith('$balance'):
        T = False
        for x in range(0, len(clients)):
            print(clients)
            if clients[x] == str(message.author.name):
                T = True
                print ('true')
                NewEmbed=discord.Embed(title="Balance", description="your balance is " +str(balances[x]), color=0x00fff0)
                await message.channel.send(embed = NewEmbed)



      if message.content.startswith('$clients'):
        NewEmbed=discord.Embed(title="Clients", description="active users of the bot" +str(balances[x]), color=0x00fff0)
        for y in range (0, len(clients)):
            NewEmbed.add_field(name = str(str(y+1)+ ": " +str(clients[y])), value = "______________________", inline = False)

        await message.channel.send(embed = NewEmbed);



      if message.content.startswith('$soul check'):
        NewEmbed=discord.Embed(title="Soul Level", description='@' +str(message.author.name) + ', your soul is at ' +str(souls[x]) +' integrity.', color=0x00fff0)
        await message.channel.send(embed = NewEmbed)



      if message.content.startswith('$soul sell'):
        NewEmbed=discord.Embed(title="Soul Sell", description=str("a piece of " +str(message.author.name) +"'s soul is on the market for " + str((11 - souls[x]) * 100)), color=0x0ffff0)
        await message.channel.send(embed = NewEmbed)
        market.append(str(message.author.name) +"'s soul")
        marketPrices.append((11- souls[x]) * 100)
        marketTypes.append("soul")
        souls[x] = souls[x] - 1;
        balances[x] = balances[x] + (11 - souls[x]) * 100



      if message.content.startswith('$market'):
        NewEmbed=discord.Embed(title="Market", description="buy using $buy [item number]", color=0x00fff0)
        for x in range(0, len(market)):
            NewEmbed.add_field(name=str(str(x+1) +": " +str(market[x])), value=str(marketPrices[x]), inline=False)
        #embed.addField('soul', '1',True)
        await message.channel.send(embed=NewEmbed)
        #embed.addField('**> Result 1:**', '1')
      if message.content.startswith('$buy'):
        Item = split(str(message.content))
        if(int(marketPrices[int(Item[5])-1]) <= balances[x]):
            NewEmbed=discord.Embed(title="BUY", description= str(message.author.name) +" bought " +str(market[int(Item[5])-1]) +"!", color=0x0ffff0)
            print(int(Item[5])-1)
            inventory[x] = str(inventory[x]) + "," + str(marketTypes[int(Item[5])-1])
            balances[x] = balances[x] - marketPrices[int(Item[5])-1];
        else:
            if(int(marketPrices[int(Item[5])-1]) > balances[x]):
                NewEmbed=discord.Embed(title="BUY", description= "you do not have enough coins to purchase a " +str(market[int(Item[5])-1]), color=0x00fff0)
            else:
                NewEmbed=discord.Embed(title="ERROR", description= "an error has occured, this may be a bug in the software or it may just be an uneeded message. Check if you can afford the item you are buying, if you can, contact the developer and describe your situation.", color = 0xff0000)
        await message.channel.send(embed=NewEmbed)


      if message.content.startswith('$inventory'):
        NewEmbed=discord.Embed(title="Inventory", description= str(message.author.name) +"'s inventory'", color = 0x00fff0)
        invList = decryptInv(inventory[x]);

        for e in range (0, len(invList)):
            NewEmbed.add_field(name = str(invList[e]), value = "______", inline = False)

        await message.channel.send(embed=NewEmbed)




      if message.content.startswith('$ActualGod'):
        #global godkey
        key = str(split(message.content)[11])+str(split(message.content)[12])+str(split(message.content)[13])+str(split(message.content)[14])+str(split(message.content)[15])+str(split(message.content)[16])
        print("input key is " +str(key))
        if(key == godkey):
            NewEmbed=discord.Embed(title="GOD", description= str(message.author.name) +"IS NOW A GOD", color = 0xffffff)
            balances[x] = 99999999999999999999
        else:
            NewEmbed=discord.Embed(title="GOD FAILED", description= str(key) +" is not the actual godkey. The godkey is " +str(godkey), color = 0xff0000)
            balances[x] = 99999999999999999999
        print ('god')
        godkey = random.randint(100000,999999)
        print("godkey is " +str(godkey))
        await message.channel.send(embed=NewEmbed)


      if message.content.startswith('$game saltyBet'):
        #global SaltyBet
        if(SaltyBet == False):
            SaltyBet = True;

            NewEmbed=discord.Embed(title="Salty bet!", description = "Starting a new game of saltybet, say 'SM join' to join and 'SM start' to start!", color = 0xff0000)
            NewEmbed.add_field(name = str(message.author.name), value = 1, inline = True)
            SaltyPlayers.append(message.author.name)
            SaltyEmbed = NewEmbed
            SaltyMessage = await message.channel.send(embed=NewEmbed)
            '\N{THUMBS UP SIGN}'
        else:
            NewEmbed=discord.Embed(title="Salty bet!", description = "There is already a game in progress hosted by " +str(SaltyPlayers[0]), color = 0xff0000)
            await message.channel.send(embed=NewEmbed)


      if(SaltyBet == True):
        if message.content.startswith('SM join'):
            #global SaltyBet
            if SaltyBet == True:
                SaltyPlayers.append(message.author)
                NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" joined saltybet hosted by " +str(SaltyPlayers[0]), color = 0xff0000)
                j = await message.channel.send(embed=NewEmbed)
                SaltyEmbed.add_field(name = str(message.author.name), value = str(len(SaltyPlayers)+1), inline = True)
                await SaltyMessage.edit(embed = SaltyEmbed)
                await message.delete()
                #time.sleep(2)
                await j.delete()

        if message.content.startswith('SM leave'):
            if(Search(SaltyPlayers, message.author.name) != -5):
                j = 0;
                Remove(SaltyPlayers, message.author.name)
                NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" left saltybet hosted by " +str(SaltyPlayers[0]), color = 0xff0000)
                j = await message.channel.send(embed=NewEmbed)
                SaltyEmbed = discord.Embed(title="Salty bet!", description = "Starting a new game of saltybet, say 'SM join' to join and 'SM start' to start!", color = 0xff0000)
                for c in range(0, len(SaltyPlayers)):
                    SaltyEmbed.add_field(name = str(SaltyPlayers[c]), value = str(c), inline = True)
                await SaltyMessage.edit(embed=SaltyEmbed)
                await message.delete()
                #time.sleep(2)
                await j.delete()

            else:
                NewEmbed=discord.Embed(title="Salty bet!", description = "you are not in the salty bet game so we cannot make you leave", color = 0xff0000)





        if message.content.startswith('SM start'):
          if(str(message.author.name) == str(SaltyPlayers[0])):
            if(SaltyProcess == False):
              Timer = True
              SaltyProcess = True
              TempP = SaltyCombatants
              P1 = TempP[random.randint(0,len(TempP)-1)]
              TempP.remove(P1)
              P2 = TempP[random.randint(0,len(TempP)-1)]
              TempP.remove(P2)
              NewEmbed=discord.Embed(title="Salty bet!", description = "match " +str(SaltyMatch) +": " +str(P1) +" V " +str(P2) +'.', footer = 'Say "P1 [money you will bet]" for ' +str(P1) +' or "P2 [money you will bet]" for ' +str(P2) +'.' , color = 0xff0000)
              NewEmbed.add_field(name = str(P1), value = str(P1) +' money pool: ' +str(AddList(SaltyP1Bet)))
              NewEmbed.add_field(name = str(P2), value = str(P2) +' money pool: ' +str(AddList(SaltyP2Bet)))
              NewEmbed.add_field(name = str(Time), value = "time remaining",inline = False)
              SaltyMessage = await message.channel.send(embed = NewEmbed)
              for r in range(0, 10):
                time.sleep(1)
                Time = Time -1
              
                NewEmbed=discord.Embed(title="Salty bet!", description = "match " +str(SaltyMatch) +": " +str(P1) +" V " +str(P2) +'.', footer = 'Say "P1 [money you will bet]" for ' +str(P1) +' or "P2 [money you will bet]" for ' +str(P2) +'.' , color = 0xff0000)
                NewEmbed.add_field(name = str(P1), value = str(P1) +' money pool: ' +str(AddList(SaltyP1Bet)))
                NewEmbed.add_field(name = str(P2), value = str(P2) +' money pool: ' +str(AddList(SaltyP2Bet)))
                NewEmbed.add_field(name = str(Time), value = "time remaining", inline = False)
                await SaltyMessage.edit(embed = NewEmbed)
              P1win = False;
              if(random.randint(0,1) == 1):
                P1win = True
              if P1win == True:
                NewEmbed=discord.Embed(title="Salty bet!", description = str(P1) +" won!" , color = 0xff0000)
                for b in range (0,len(SaltyP1Bet)):
                  NewEmbed.add_field(name = str(SaltyP1Name[b]) + " won", value = str(SaltyP1Bet[b]))
                  balances[SaltyP1Numeric[b]] = balances[SaltyP1Numeric[b]] + int(SaltyP1Bet[b])


                for b in range (0,len(SaltyP2Bet)):
                  NewEmbed.add_field(name = str(SaltyP1Name[b]) + " lost", value = str(SaltyP2Bet[b]))
                  balances[SaltyP2Numeric[b]] = balances[SaltyP2Numeric[b]] - int(SaltyP2Bet[b])
                

              else:
                NewEmbed=discord.Embed(title="Salty bet!", description = str(P2) +" won!" , color = 0xff0000)
                for b in range (0,len(SaltyP1Bet)):
                  NewEmbed.add_field(name = str(SaltyP1Name[b]) + " lost", value = str(SaltyP1Bet[b]))
                  balances[SaltyP1Numeric[b]] = balances[SaltyP1Numeric[b]] - int(SaltyP1Bet[b])

                for b in range (0,len(SaltyP2Bet)):
                  NewEmbed.add_field(name = str(SaltyP1Name[b]) + " won", value = str(SaltyP2Bet[b]))
                  balances[SaltyP2Numeric[b]] = balances[SaltyP2Numeric[b]] + int(SaltyP2Bet[b])
              await SaltyMessage.edit(embed = NewEmbed)
              SaltyProcess = False
              SaltyBet = False
              Time = 10
              
        
        if(SaltyProcess == True):
          if message.content.startswith("P1 "):
            getInt(str(message.content), 3)
            NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" has bet " +str(getInt(str(message.content), 3)) +" on " +str(P1), color = 0xff0000)
            #await message.channel.send("ppl have bet stuff")
            SaltyP1Numeric.append(x)
            SaltyP1Bet.append(getInt(str(message.content), 3))
            SaltyP1Name.append(message.author.name)
            NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" has bet " +str(getInt(str(message.content), 3)) +" on " +str(P1), color = 0xff0000)
            msg = await message.channel.send(embed = NewEmbed)
            SEMP2=discord.Embed(title="Salty bet!", description = "match " +str(SaltyMatch) +": " +str(P1) +" V " +str(P2) +'.', footer = 'Say "P1 [money you will bet]" for ' +str(P1) +' or "P2 [money you will bet]" for ' +str(P2) +'.' , color = 0xff0000)
            SEMP2.add_field(name = str(P1), value = str(P1) +' money pool: ' +str(AddList(SaltyP1Bet)))
            SEMP2.add_field(name = str(P2), value = str(P2) +' money pool: ' +str(AddList(SaltyP2Bet)))
            SEMP2.add_field(name = str(Time), value = "time remaining",inline = False)
            await SaltyMessage.edit(embed = SEMP2)
            await message.delete()
            #time.sleep(3)
            await msg.delete()
          
          if message.content.startswith("P2 "):
            getInt(str(message.content), 3)
            NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" has bet " +str(getInt(str(message.content), 3)) +" on " +str(P2), color = 0xff0000)
            #await message.channel.send("ppl have bet stuff")
            SaltyP2Numeric.append(x)
            SaltyP2Bet.append(getInt(str(message.content), 3))
            SaltyP2Name.append(message.author.name)
            NewEmbed=discord.Embed(title="Salty bet!", description = str(message.author.name) +" has bet " +str(getInt(str(message.content), 3)) +" on " +str(P2), color = 0xff0000)
            msg = await message.channel.send(embed = NewEmbed)
            SEMP2=discord.Embed(title="Salty bet!", description = "match " +str(SaltyMatch) +": " +str(P1) +" V " +str(P2) +'.', footer = 'Say "P1 [money you will bet]" for ' +str(P1) +' or "P2 [money you will bet]" for ' +str(P2) +'.' , color = 0xff0000)
            SEMP2.add_field(name = str(P1), value = str(P1) +' money pool: ' +str(AddList(SaltyP1Bet)))
            SEMP2.add_field(name = str(P2), value = str(P2) +' money pool: ' +str(AddList(SaltyP2Bet)))
            SEMP2.add_field(name = str(Time), value = "time remaining",inline = False)
            await SaltyMessage.edit(embed = SEMP2)
            await message.delete()
            #time.sleep(3)
            await msg.delete()


        











client.run(os.getenv('TOKEN'))
