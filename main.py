#The purpose of this program is to randomly select certain or all aspects of character creation in Guild Wars 2

#TO DO
#Add option to return to main menu
#Add case handling

import random

#Variables
gw2_races = ["Asura", "Sylvari", "Human", "Norn", "Charr"]
gw2_genders = ["Male", "Female"]
gw2_base_professions = ["Mesmer", "Guardian", "Necromancer", "Ranger", "Elementalist", "Warrior", "Thief", "Engineer", "Revenant"]
mesmer_elite_specialization = ["Chronomancer", "Mirage", "Virtuoso"]
guardian_elite_specialization = ["Dragonhunter", "Firebrand", "Willbender"]
necromancer_elite_specialization = ["Reaper", "Scourge", "Harbinger"]
ranger_elite_specialization = ["Druid", "Soulbeast", "Untamed"]
elementalist_elite_specialization = ["Tempest", "Weaver", "Catalyst"]
warrior_elite_specialization = ["Berserker", "Spellbreaker", "Bladesworn"]
thief_elite_specialization = ["Daredevil", "Deadeye", "Specter"]
engineer_elite_specialization = ["Scrapper", "Holosmith", "Mechanist"]
revenant_elite_specialization = ["Herald", "Renegade", "Vindicator"]

#Functions

def race_selector():
    random_race = random.choice(gw2_races)
    return(random_race)

def gender_selector():
    random_gender = random.choice(gw2_genders)
    return(random_gender)

def profession_selector():
    random_base_profession = random.choice(gw2_base_professions)
    return(random_base_profession)    

#Import parts from main to this function
#Do a while loop with true or false to tell if they want to reroll or not
def elite_specialization_selector():
        random_base_profession = random.choice(gw2_base_professions)
        if random_base_profession == "Mesmer":
            random_elite_specialization = random.choice(mesmer_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Guardian":
            random_elite_specialization = random.choice(guardian_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Necromancer":
            random_elite_specialization = random.choice(necromancer_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Ranger":
            random_elite_specialization = random.choice(ranger_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Elementalist":
            random_elite_specialization = random.choice(elementalist_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Warrior":
            random_elite_specialization = random.choice(warrior_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Thief":
            random_elite_specialization = random.choice(thief_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Engineer":
            random_elite_specialization = random.choice(engineer_elite_specialization)
            return random_elite_specialization
        elif random_base_profession == "Revenant":
            random_elite_specialization = random.choice(revenant_elite_specialization)
            return random_elite_specialization
        
def random_character():
    print(race_selector())
    print(gender_selector())
    print(elite_specialization_selector())

def creation_menu():
    seconary_menu_active = True
    while seconary_menu_active == True:
        print("Enter 1 to pick just a random profession")
        print("Enter 2 to randomize the whole character")
        creation_option = input()
        if creation_option == "1":
            rand_prof_selec_loop = True
            seconary_menu_active = False
            while rand_prof_selec_loop == True:
                print(elite_specialization_selector())
                print("Enter 1 to reroll")
                print("Enter q to quit")
                reroll_choice = input()
                if reroll_choice == "1":
                        elite_specialization_selector()
                elif reroll_choice == "q":
                        rand_prof_selec_loop = False
                        print("Program halted")
                else:
                        print("Please make a selection of 1 or 2")
        elif creation_option == '2':
            random_character_loop = True
            seconary_menu_active = False
            while random_character_loop:
                random_character()
                print("Enter 1 to reroll")
                print("Enter q to quit")
                reroll_choice = input()
                if reroll_choice == "1":
                    print(random_character())
                elif reroll_choice == "q":
                    random_character_loop = False
                    print("Program halted")
                else:
                    print("Please make a selection of 1 or 2")
        else:
             print("Make a selection of 1 or 2 only")

#The main program
def main_program():
    menu_active = True
    while menu_active == True:
        print("Enter 1 to create a new character")
        print("Enter q to quit")
        main_option_one = input()
        if main_option_one == "1":
            creation_menu()
            menu_active = False
        elif main_option_one == "q":
            print("Program halted")
            menu_active = False
        else:
            print("Please enter 1 or q only")


print("Welcome to GW2Random")
main_program()