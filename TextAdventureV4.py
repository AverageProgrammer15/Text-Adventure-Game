import random
import time
import json
from datetime import date, datetime


CusEnemyName = None
CusEnemyHp = None
CusEnemyMoves = None
Player_Moveset = []
Player_Limit = []
PlayerXP = 0
PlayerLVL = 0
PlayerHP = None
PlayerEffects = []
Kills = 0
TURN = None
MoveUsed = None
Status = "Alive"
CodeActivated = False
Acheivements = {"First Kill":False, "Novice Hunter":False, "Experienced Hunter":False}
AchievementHistory = []
# Mage_Stats:
Mage_Set = {"Fireball": [35, 'None'], "Barrage": [25, 'None']}
Mage_Limit = [15, 45]
# Barbarian_Stats:
Barbarian_Set = {"Axe Stab": [65, 'None'], "Rampage": [25, 'None']}
Barbarian_Limit = [3, 25]
# Archer_Stats
Archer_Set = {"Arrow": [15, 'None'], "Arrow Rain": [25, 'None']}
Archer_Limit = [55, 10]
# Swordmaster_Stats
Swordmaster_Set = {"Sword Throw": [15, 'None'], "Sword Combo": [35, 'None']}
Swordmaster_Limit = [45, 10]
#[ADMIN ONLY]
ADMIN_Set = {"Go Random Bullshit": [999,None], "Go Even Better Randomm Bullshit": [9999,None]}
ADMIN_Limit = [99999999, 999999999]
PlayerName = input("Insert a name for your character: ")
Race = input("Choose your fighting style (Barbarian, Archer, Mage, Swordmaster): ")

if Race not in ["Barbarian", "Archer", "Mage", "Swordmaster","Admin"]:
    while Race not in ["Barbarian", "Archer", "Mage", "Swordmaster","Admin"]:
        Race = input("Please choose a valid race (Barbarian, Archer, Mage, Swordmaster): ")

if Race == "Mage":
    Player_Moveset = Mage_Set
    PlayerHP = 150
    Player_Limit = Mage_Limit.copy()
elif Race == "Barbarian":
    Player_Moveset = Barbarian_Set
    PlayerHP = 350
    Player_Limit = Barbarian_Limit.copy()
elif Race == "Archer":
    Player_Moveset = Archer_Set
    PlayerHP = 150
    Player_Limit = Archer_Limit.copy()
elif Race == "Swordmaster":
    Player_Moveset = Swordmaster_Set
    PlayerHP = 250
    Player_Limit = Swordmaster_Limit.copy()
elif Race == "Admin":
    Player_Moveset = ADMIN_Set
    Player_Limit = ADMIN_Limit.copy()
    PlayerHP = 9999999
def OnGameEnd():
    global Player_Moveset, Player_Limit, PlayerHP, Status
    Status = "Alive"

    if Race == "Mage":
        Player_Moveset = Mage_Set
        PlayerHP = 150
        Player_Limit = Mage_Limit.copy()
    elif Race == "Barbarian":
        Player_Moveset = Barbarian_Set
        PlayerHP = 350
        Player_Limit = Barbarian_Limit.copy()
    elif Race == "Archer":
        Player_Moveset = Archer_Set
        PlayerHP = 150
        Player_Limit = Archer_Limit.copy()
    elif Race == "Swordmaster":
        Player_Moveset = Swordmaster_Set
        PlayerHP = 250
        Player_Limit = Swordmaster_Limit.copy()

new_name = None
new_moves = None
new_hp = None

# Enemies:
#1.)Dummy
Dummy_Name = "Dummy"
Dummy = 50
Dummy_Moves = {"Nothing": (0, 'None')}
#2.) Goblin
Goblin_Name = "Goblin"
Goblin = 65
Goblin_Moves = {'Slash': (15, "Bleeding"), 'Rush': (20, 'None')}
#3.) Witch
Witch_Name = "Witch"
Witch = 55
Witch_Moves = {'Spell': (10, 'None'), 'Deadly Spell': (50, 'Curse')}
#4.)Ogre
Ogre_Name = "Ogre"
Ogre = 100
Ogre_Moves = {'Slam': (35, 'None'), 'Throw': (55, 'None'), 'Stomp': (25, 'None')}
#5.) Buff Goblin
BG_Name = "Buff Goblin"
BG = 130
BG_Moves = {'Cannon Ball': (55, 'None'), 'Rush': (40, 'None'), 'Spam sword hits (idk)': (30, 'None')}
#6.) Wind Spirit
WS_Name = "Wind Spirit"
WS = 125
WS_Moves = {"Air Hole": (35, 'None'), "Mininado": (45, 'None'), "Air Waves": (40, 'None')}
#7.) Titan
Titan_Name = "Titan"
Titan = 250
Titan_Moves = {"Shockwaves": (65, 'None'), "Rock Throw": (45, 'None'), "Arising": (35, 'Crystalize')}
#8.) ???
MB_Name = "???"
MB = 500
MB_Moves = {"Shadow Attack": (50,'Curse'), "Cast Away":(55,"Cystalize")}

FirstDialogue = ["Some kingdom is starting to fall from the hands of a very powerful (and scary I think) villain", "And your job is to free the kingdom from this villain", f"{PlayerName}: Uhhh yep I'm def dead", f"{PlayerName}: Oh look! An enemy! Guess we gotta fight it :/"]
SecondDialogue = [f"{PlayerName}: Yey we defeated the stupid goblin!", "Giga Goblin: YOU WILL PAY FOR WHAT YOU DID", f"{PlayerName}: Well shit"]
ThirdDialogue = [f"{PlayerName}: Surely that's it right?", f"{PlayerName}: Welp guess I'll be on my way now..."]

First2Dialogue = [f"{PlayerName}: Just walkin to the (dying) kingdom", "Some witch: HeY wAnT sOmE dEfInItLeY nOrMaL dRiNkS?", f"{PlayerName}: I think I'll pass...", "Some witch: HoW dArE yOu NoW yOu MuSt DiE >:(", f"{PlayerName}: Here we go again...", "Some witch: I SUMMON A FUCKING GIGA CHAD GOBLIN", f"{PlayerName}: Hell nah an even more buffed goblin..."]
Second2Dialogue = ["Some witch: grrrr this isn't over", f"{PlayerName}: lol ez", "Some witch: summons a wind spirit and gtfo", f"{PlayerName}: Bruh"]
Third2Dialogue = [f"{PlayerName}: Dang I think it's over now...", f"{PlayerName}: Welp I guess the adventure continues"]

First3Dialogue = [f"{PlayerName}: I wonder why I made the witch mad...", "Insert very strong stomping*", f"{PlayerName}: Holy shit what did I just hear", f"{PlayerName}: looks up* yep I'm fucked"]
Second3Dialogue = [f"{PlayerName}: Dang I wonder how this guy got here...", f"{PlayerName}: Don't tell me there is another one...", f"{PlayerName}: Oh it's an ogre..", f"{PlayerName}: Well better than a titan I guess"]
Third3Dialogue = [f'{PlayerName}: I think that is all of them for now.. atleast', "???: [INSERT SOME RANDOM SOUND]"]

Encountered = "You've encountered... "

def save_player_data(filename="player_data.json"):
    data = {
        "Name": PlayerName,
        "Class": Race,
        "Health": PlayerHP,
        "Moveset": Player_Moveset,
        "Limit": Player_Limit,
        "XP": PlayerXP,
        "Kills": Kills
    }
    with open(filename, "w") as file:
        json.dump(data, file)

    print("Game saved successfully!")

def load_player_data(filename="player_data.json"):
    global PlayerName, Race, PlayerHP, Player_Moveset, Player_Limit, PlayerXP
    try:
        with open(filename, 'r') as file:
            player_data = json.load(file)
            for x in range(15):
             PlayerName = player_data["Name"]
             Race = player_data["Class"]
             PlayerHP = player_data["Health"]
             Player_Moveset = player_data["Moveset"]
             Player_Limit = player_data["Limit"]
             PlayerXP = player_data["XP"]
             Kills = player_data["Kills"]
            print("Successful")
    except FileNotFoundError:
        print("Load data failed :(")

def CheckTableForString(table, requirement):
    Status = False
    for x in table:
        if x == requirement:
            Status = True
            break
    
    return Status

def Effect(InsertEffect, VictimHP, VictimName, VictimMoves):
    if InsertEffect == "Bleeding":
        #Similar to poison
        VictimHP -= 10
        print(f"{VictimName} lost 10 HP!")
        print(f"{VictimName} HP: {VictimHP}")
    elif InsertEffect == 'Curse':
        #Similar to poison(2)
        VictimHP -= 15
        print(f"{VictimName} lost 15 HP!")
        print(f"{VictimName} HP: {VictimHP}")
    elif InsertEffect == 'Crystalize':
        #Weaken Player
        for move in VictimMoves:
            VictimMoves[move][0] /= 2
            if VictimMoves[move] <= 10:
                VictimMoves[move] = 10
                VictimMoves += 5
        print(f"{VictimName}'s moves are weakened!")
    return VictimHP

def Give_XP(Multiplier):
    global PlayerXP, PlayerLVL
    PlayerXP += (10 * Multiplier)
    print(f"You received {10 * Multiplier} XP")
    if PlayerXP >= 300:
        PlayerLVL += 1
        PlayerXP -= 300
        while PlayerXP >= 300:
            PlayerLVL += 1
            PlayerXP -= 300
        print(f"You are now Level: {PlayerLVL}")

def GetMove(ChosenMoves, Damage, AddTo):
    for Move, Attack in ChosenMoves.items():
        if Attack[0] == Damage:
            return Move
    return "Unknown Move"

def EnemyMaker():
    custom_name = input("Insert a name for your enemy: ")
    custom_health = int(input("Insert the amount of health of your enemy: "))
    custom_moves = {}
    amount_of_moves = int(input("How many moves does this enemy have?: "))
    
    for _ in range(amount_of_moves):
        move_name = input("Name of move: ")
        move_damage = int(input("How much damage: "))
        move_effect = input("Bleeding, Curse, Crystalize")
        custom_moves[move_name] = [move_damage, move_effect]
    
    return custom_name, custom_health, custom_moves

def Use_Move(Moves, Name, Target, NumOfMoves):
    global PlayerName, MoveUsed, PlayerHP, Player_Limit, PlayerEffects
    if Name == PlayerName:
        print("-------YOUR TURN--------")
        time.sleep(2)
        ChooseMove = input(f"Choose move to use (0 (Uses: {Player_Limit[0]}) or 1 (Uses: {Player_Limit[1]}) or 'Heal'): ")
        if ChooseMove != 'Heal':
            ChooseMove = int(ChooseMove)
            if Player_Limit[ChooseMove] > 0:
                DamageDealt = list(Moves.values())[ChooseMove][0]
                Target -= DamageDealt
                Player_Limit[ChooseMove] -= 1
                print(f"Damage Dealt: {DamageDealt}")
                time.sleep(1)
            else:
                print("You can't use this move anymore")
                time.sleep(1)
        else:
            Healed = random.randint(0, 150)
            PlayerHP += Healed
            print(f"You healed {Healed}")
    else:
        print("-------ENEMY TURN--------")
        PlayerEffects = []
        EnemyMoveChosen = list(Moves.values())[random.randint(0, NumOfMoves)]
        EnemyDamageDealt = EnemyMoveChosen[0]
        EnemyEffectDealt = EnemyMoveChosen[1]
        
        MoveUsed = GetMove(Moves, EnemyDamageDealt, MoveUsed)
        time.sleep(random.randint(1, 3))
        print(f"Enemy used {MoveUsed}")
        if EnemyEffectDealt != 'None':
            PlayerEffects.append(EnemyEffectDealt)
            print(f"Enemy gave the player: {PlayerEffects}")
        time.sleep(1)
        Target -= EnemyDamageDealt
        print(f"Enemy dealt: {EnemyDamageDealt}")
        time.sleep(1)
    return Target

def Game(Enemy_Name, Enemy, Enemy_Moves, TF):
    global TURN, Player_Moveset, PlayerName, PlayerHP, Status, PlayerEffects, Kills
    GetEnemyHealth = Enemy
    print(f"A wild {Enemy_Name} appeared")
    time.sleep(2)
    TURN = random.randint(0, 1)
    
    TotalMoves = len(Enemy_Moves) - 1
    
    while Enemy > 0 and PlayerHP > 0:
        if TURN == 1:
            PlayerHP = Use_Move(Enemy_Moves, Enemy_Name, PlayerHP, TotalMoves)
            print(f"Player HP: {PlayerHP}")
        else:
            Enemy = Use_Move(Player_Moveset, PlayerName, Enemy, 1)
            print(f"Enemy HP: {Enemy}")
        TURN = 1 - TURN
        if PlayerEffects:
            PlayerHP = Effect(PlayerEffects[0], PlayerHP, PlayerName, Player_Moveset)

    if Enemy <= 0:
        print("Enemy defeated!")
        if TF == True:
            Give_XP(GetEnemyHealth)
            Kills += 1
            

        
    if PlayerHP <= 0:
        print("Game over")
        time.sleep(1)
        print("Restart the program")
        Status = "Dead"

def Tutorial():
    global AchievementHistory
    print("---Tutorial Start---")
    print("Hello player!")
    time.sleep(2)
    print("It seems your name is...")
    time.sleep(2)
    print(PlayerName)
    time.sleep(2)
    print("Well, welcome to the game!")
    time.sleep(2)
    print("Today I will teach you how to play this game!")
    time.sleep(2)
    print("Every class has two moves but serve different purposes")
    time.sleep(2)
    print("You can only use your abilities when it's your turn")
    time.sleep(2)
    print("If it's your turn you can either type 0 or 1 to use an ability")
    time.sleep(2)
    print("But be careful for you only have a limit on each move you use")
    time.sleep(2)
    print("You can also heal but you will sacrifice your turn")
    time.sleep(2)
    print("Let's practice!")
    time.sleep(2)
    print("Try fighting this dummy!")
    time.sleep(2)
    Game(Dummy_Name, Dummy, Dummy_Moves, True)
    print("---TUTORIAL COMPLETE!---")
    time.sleep(2)
    if CheckTableForString(AchievementHistory, "Welcome!") == False:
        print("Achievement Unlocked: Welcome!")
        AchievementHistory.append("Welcome!")


def Reincarnate(Name, HP, MovesChosen,Multiplier):
    new_name = Name + "(Buffed)"
    new_hp = int(HP * Multiplier)
    new_moves = {move: [dmg[0] + Multiplier, dmg[1]] for move, dmg in MovesChosen.items()}
    return new_name, new_hp, new_moves

def Chapter1():
    for Dialogue in FirstDialogue:
        print(Dialogue)
        time.sleep(1)
    Game(Goblin_Name, Goblin, Goblin_Moves, True)
    if Status == "Alive":
        OnGameEnd()
        for Dialogue in SecondDialogue:
            print(Dialogue)
            time.sleep(1)
            
        if Status == "Alive":
            Game(BG_Name, BG, BG_Moves, True)
            for Dialogue in ThirdDialogue:
                print(Dialogue)
                time.sleep(1)
            input("CHAPTER 1 COMPLETED (Press enter to continue)")
            if CheckTableForString(AchievementHistory,"Complete Chapter 1") == False:
                        AchievementHistory.append("Complete Chapter 1")
                        print("Achievement: COMPLETE CHAPTER 1!")
    Main_Menu()

def Chapter2():
    global new_hp, new_name, new_moves, Status
    
    for Dialogue in First2Dialogue:
        print(Dialogue)
    new_name, new_hp, new_moves = Reincarnate(BG_Name, BG, BG_Moves,2)
    Game(new_name, new_hp, new_moves, True)
    if Status == "Alive":
        OnGameEnd()
        for Dialogue in Second2Dialogue:
            print(Dialogue)
            time.sleep(1)
        if Status == "Alive":
            Game(WS_Name, WS, WS_Moves, True)
            for Dialogue in Third2Dialogue:
                print(Dialogue)
                time.sleep(1)
                if CheckTableForString(AchievementHistory,"Complete Chapter 2") == False:
                        AchievementHistory.append("Complete Chapter 2")
                        print("Achievement: COMPLETE CHAPTER 2!")
            input("CHAPTER 2 COMPLETED (Press enter to continue)")
    Main_Menu()
    
def Chapter3():
    global Status, AchievementHistory
    for Dialogue in First3Dialogue:
        print(Dialogue)
        time.sleep(1)
    Game(Titan_Name, Titan, Titan_Moves, True)
    if Status == "Alive":
        OnGameEnd()
        for Dialogue in Second3Dialogue:
            print(Dialogue)
            time.sleep(1)
        if Status == "Alive":
            Game(Ogre_Name, Ogre, Ogre_Moves, True)
            if Status == "Alive":
                for Dialogue in Third3Dialogue:
                    print(Dialogue)
                    time.sleep(1)
                    print("Chapter 3 COMPLETED")
                    if CheckTableForString(AchievementHistory,"Complete Chapter 3") == False:
                        AchievementHistory.append("Complete Chapter 3")
                        print("Achievement: COMPLETE CHAPTER 3!")
    Main_Menu()

def Enemy_Rush():
    global PlayerHP, AchievementHistory
    OnGameEnd()
    Wave = 1
    WaveMultiplier = 1
    AvailableEnemies = ["Goblin", "Witch", "Ogre"]
    WaveCounter = 1
    while PlayerHP > 0:
        print(PlayerHP)
        ChoosingEnemy = random.choice(list(AvailableEnemies))
                
        if ChoosingEnemy == "Goblin":
            new_name,new_hp,new_moves = Reincarnate(Goblin_Name,Goblin,Goblin_Moves,WaveMultiplier)
            Game(new_name,new_hp,new_moves,False)
        elif ChoosingEnemy == "Witch":
            new_name,new_hp,new_moves = Reincarnate(Witch_Name,Witch,Witch_Moves,WaveMultiplier)
            Game(new_name,new_hp,new_moves, False)
        elif ChoosingEnemy == "Ogre":
            new_name,new_hp,new_moves = Reincarnate(Ogre_Name,Ogre,Ogre_Moves,WaveMultiplier)
            Game(new_name,new_hp,new_moves, False)
        if PlayerHP >= 0:
         print("Wave completed...")
         time.sleep(2.5)
         Wave += 1
         WaveCounter += 1
        if WaveCounter >= 5:
            if WaveMultiplier == 1:
                print("Easy so far?")
                time.sleep(1)
                print("Let's make it a little bit harder!")
                time.sleep(1)
                print("Every few waves the difficulty of the enemies increase!")
            WaveMultiplier += 1   
        time.sleep(2.5)
        print(f"Wave {Wave}")
    print(f"Survived {Wave} waves...")
    Give_XP(Wave)
    time.sleep(3)
    if Wave >= 25:
        if CheckTableForString(AchievementHistory, "Reach Wave 25!") == False:
            AchievementHistory.append("Reach Wave 25!")
            print("Achievement Unlocked: Reach Wave 25!")
    if Wave >= 50:
        if CheckTableForString(AchievementHistory, "Reach Wave 50!") == False:
            AchievementHistory.append("Reach Wave 50!")
            print("Achievement Unlocked: Reach Wave 50!")
    if Wave == 69:
        if CheckTableForString(AchievementHistory, "69") == False:
            AchievementHistory.append("69")
            print("Achievement Unlocked: 69")
    if Wave >= 100:
        if CheckTableForString(AchievementHistory, "Reach Wave 100!") == False:
            AchievementHistory.append("Reach Wave 100!")
            print("Achievement Unlocked: Reach Wave 100!")
    Main_Menu()






def CheckAchIfTrue():
    global Kills, Acheivements, AchievementHistory
    if Kills >= 1:
        if CheckTableForString(AchievementHistory, "First Kill") == False:
         print("Achievement: First Kill!")
         Acheivements["First Kill"] = True
         AchievementHistory.append("First Kill")
    if Kills >= 10:
        if CheckTableForString(AchievementHistory, "Novice Hunter") == False:
         print("Achievement: Novice Hunter!")
         Acheivements["Novice Hunter"] = True
         AchievementHistory.append("Novice Hunter")
    if Kills >= 100:
        if CheckTableForString(AchievementHistory, "Experienced Hunter") == False:
         print("Achievement: Experienced Hunter!")
         Acheivements["Experienced Hunter"] = True
         AchievementHistory.append("Experienced Hunter")
        
    

def Main_Menu():
    global  Acheivements, AchievementHistory
    OnGameEnd()
    CheckAchIfTrue()
    global CusEnemyName, CusEnemyHp, CusEnemyMoves, PlayerXP, PlayerLVL, CodeActivated
    Option = input("('PVE', 'Enemy Maker', 'Adventure', 'Save', 'Stats','Tutorial', 'Enemy Rush', 'Achievements')[Exit]: ")
    if Option not in ['PVE', 'Enemy Maker', 'Adventure', 'Exit', 'Save', 'Stats', 'Tutorial', '51990', 'Enemy Rush', 'Achievements']:
        print("Not valid")
        Main_Menu()
    elif Option == "PVE":
        AllEnemies = ["Dummy", "Goblin", "Witch", "Ogre", "Buff Goblin", "Wind Spirit", "Titan"]
        if CodeActivated == True:
            AllEnemies.append("Your God")
        ChooseEnemy = input(f"Choose from the enemies: {AllEnemies}: ")
        if ChooseEnemy in AllEnemies:
            if ChooseEnemy == "Dummy":
                Game(Dummy_Name, Dummy, Dummy_Moves, True)
            elif ChooseEnemy == "Goblin":
                Game(Goblin_Name, Goblin, Goblin_Moves, True)
            elif ChooseEnemy == "Witch":
                Game(Witch_Name, Witch, Witch_Moves, True)
            elif ChooseEnemy == "Ogre":
                Game(Ogre_Name, Ogre, Ogre_Moves, True)
            elif ChooseEnemy == "Buff Goblin":
                Game(BG_Name, BG, BG_Moves, True)
            elif ChooseEnemy == "Wind Spirit":
                Game(WS_Name, WS, WS_Moves, True)
            elif ChooseEnemy == "Titan":
                Game(Titan_Name, Titan, Titan_Moves, True)
            if CodeActivated == True:
                if ChooseEnemy == "Your God":
                    print("So you finally found me...")
                    time.sleep(1)
                    print("Nobody in the last century has anyone found me before...")
                    time.sleep(1)
                    print("Now lets see how strong you truly are...")
                    time.sleep(2)
                    Game(MB_Name, MB, MB_Moves, True)
        Main_Menu()
        
    elif Option == "Enemy Maker":
        CusEnemyName, CusEnemyHp, CusEnemyMoves = EnemyMaker()
        print(f"Custom Enemy Created: {CusEnemyName} with HP: {CusEnemyHp} and Moves: {CusEnemyMoves}")
        Game(CusEnemyName, CusEnemyHp, CusEnemyMoves, False)
        Main_Menu()
    elif Option == "Adventure":
        ChooseChapter = input("Choose Chapter: (1-3)[Available: 1&2]: ")
        ChooseChapter = int(ChooseChapter)
        if ChooseChapter == 1:
            Chapter1()
        elif ChooseChapter == 2:
            Chapter2()
        elif ChooseChapter == 3:
            Chapter3()
    elif Option == "Exit":
        if input("Stop the game? (Yes/No): ") == "Yes":
            print("Game stopped")
        else:
            Main_Menu()
    elif Option == 'Save':
        if input("Would you like to save your data? (Yes/No): ") == "Yes":
            save_player_data()
            Main_Menu()
        else:
            Main_Menu()
    elif Option == 'Stats':
        print(f'Level: {PlayerLVL}')
        print(f'XP: {PlayerXP}')
        print(f'Kills: {Kills}')
        Main_Menu()
    elif Option == 'Tutorial':
        if input("Would you like to redo the tutorial (Yes/No): ") == "Yes":
            Tutorial()
            Main_Menu()
        else:
            Main_Menu()
    elif Option == '51990':
        if CodeActivated == False:
            CodeActivated = True
            print("Something appeared..")
            time.sleep(2)
            print("But I don't know what..")
            time.sleep(2)
            print("Maybe check the main menu?")
            time.sleep(2)
        Main_Menu()
    elif Option == 'Enemy Rush':
        if input("Would you like to start an endless run? (Yes/No)") == "Yes":
            Enemy_Rush()
        else:
            Main_Menu()
    elif Option == 'Achievements':
        print("---Achievement History---")
        Counter = 1
        for Achievement in AchievementHistory:
            print(f"{Counter}.) {Achievement}")
            Counter += 1
        
        Main_Menu()


if input("Would you like to load your data? (Yes/No): ") == "Yes":
    load_player_data()
    Main_Menu()
else:
    if input("Would you like to do the tutorial (Yes/No):") == "Yes":
        Tutorial()
        Main_Menu()
    else:
        Main_Menu()
