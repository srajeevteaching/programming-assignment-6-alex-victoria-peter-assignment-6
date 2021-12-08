# Team Members: Alex, Peter, Victoria
# Course: CS151, Dr. Rajeev
# Programming Assignment 6
# Inputs: storm2000.csv, menu choice, output file,
# Outputs: question 1 to file (difference in deaths and injuries for each storm, significance)
#          question 2 to graph (number of types of storms)
#          question 3 to terminal (avg # of days)
#          question 4 output_______________


#                ****** put info about q4 into outputs and menu options *******


START_MONTH = 0 #The year and month in the format YYYYMM in which the storm started
START_DAY = 1 #The day of the month in which the storm started
START_TIME = 2 #The time at which the storm started
END_MONTH = 3 #The year and month in the format YYYYMM in which the storm ended
END_DAY = 4  #The day of the month in which the storm ended
END_TIME = 5 #The time at which the storm ended
STATE = 6 #The name of the state where storm occurred
TYPE = 7 #The type of storm
DIRECT_INJURIES = 8 #The number of injuries directly caused by the storm
INDIRECT_INJURIES = 9 #The number of injuries indirectly caused by the storm
DIRECT_DEATHS = 10 #The number of deaths directly caused by the storm
INDIRECT_DEATHS = 11 #The number of deaths indirectly caused by the storm
PROPERTY_DAMAGE = 12 #The amount of damage to property
CROP_DAMAGE = 13 #The amount of damage to crops

def load_storm_data ():
    storms = []
    try:
        #open the file for reading
        file = open("storm2000.csv", "r")
        #run through each storm in the file
        for line in file:
            #split the storm into its different parts, add it to a list
            storm = line.split(",")
            #casts the data to appropriate type
            storm[START_MONTH] = int(storm[START_MONTH])
            storm[START_DAY] = int(storm[START_DAY])
            storm[START_TIME] = int (storm[START_TIME])
            storm[END_MONTH] = int(storm[END_MONTH])
            storm[END_DAY] = int(storm[END_DAY])
            storm[END_TIME] = int(storm[END_TIME])
            storm[DIRECT_INJURIES] = int(storm[DIRECT_INJURIES])
            storm[INDIRECT_INJURIES] = int(storm[INDIRECT_INJURIES])
            storm[DIRECT_DEATHS] = int(storm[DIRECT_DEATHS])
            storm[INDIRECT_DEATHS] = int(storm[INDIRECT_DEATHS])
            storm[PROPERTY_DAMAGE] = int(storm[PROPERTY_DAMAGE])
            storm[CROP_DAMAGE] = int(storm[CROP_DAMAGE])
            #add the strom to list of storms
            storms.append(storm)
        file.close()
    #try/except for if the above code runs into an error such as not finding file
    except FileNotFoundError:
        print ("file does not exist")
    return storms

def menu(storms):
    choice = 0
    while choice != "5":
        choice = input ("SELECT QUESTION:\n 1: Deaths and Injuries Data \n 2: Property Damage Graph \n 3: Average Duration \n 4: \n 5: quit\n ")
        if choice == "1":
            death_and_injury_data (storms)
        elif choice == "2":
            property_damage_graph (storms)
        elif choice == "3":
            average_duration (storms)
        elif choice == "4":
            question_four (storms)
        elif choice == "5":
            print ("quiting menu")
        else:
            print ("input a valid choice\n")

def death_and_injury_data (storms):
    print("death")
def property_damage_graph (storms):
    print("damage")
def average_duration(storms):
    print("duration")
def question_four (storms):
    print("4")
def main():
    storms = load_storm_data()
    menu(storms)

main()