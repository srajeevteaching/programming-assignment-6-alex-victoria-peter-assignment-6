import matplotlib.pyplot as plt

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
            storm[PROPERTY_DAMAGE] = float(storm[PROPERTY_DAMAGE])
            storm[CROP_DAMAGE] = float(storm[CROP_DAMAGE])
            #add the strom to list of storms
            storms.append(storm)
        file.close()
    #try/except for if the above code runs into an error such as not finding file
    except FileNotFoundError:
        print ("file does not exist")
    return storms

# presents options and calls the appropriate functions based off user input
def menu(storms):
    choice = 0
    while choice != "5":
        choice = input ("SELECT QUESTION:\n 1: Deaths and Injuries Data \n 2: Property Damage Graph \n 3: Average Duration \n 4: Storm Type Frequency \n 5: quit\n ")
        if choice == "1":
            death_and_injury_data (storms)
        elif choice == "2":
            prop (storms)
        elif choice == "3":
            average_duration (storms)
        elif choice == "4":
            storm_type_frequency (storms)
        elif choice == "5":
            print ("quiting menu")
        else:
            print ("input a valid choice\n")

# compares direct injuries to direct deaths of each storm and prints results to user chosen file
def death_and_injury_data (storms):
    print ("This function will compare the direct injuries to direct deaths of each storm and print the results to a file ")
    # asks user for filename and opens it for writing
    filename = input("input output file name: ")
    file = open("filename", "w")
    print ("Difference between Direct Injuries and Direct Deaths (injuries - deaths)", file=file)
    # runs through each storm
    for storm in storms:
        # finds the difference
        diff = storm[DIRECT_INJURIES] - storm[DIRECT_DEATHS]
        # finds which comparison to use and prints the difference and comparison to the file
        if diff <= -5:
            print (diff, "Significantly Less", file= file)
        elif diff > -5 and diff <-1:
            print(diff, "Less", file=file)
        elif diff >= -1 and diff <= 1:
            print(diff, "Same", file=file)
        elif diff > 1 and diff < 5:
            print(diff, "More", file=file)
        else:
            print(diff, "Significantly More", file=file)

def prop(storms):
    # Initialize low, medium, and high property damage
    n = 0
    l = 0
    m = 0
    h = 0
    for data in storms:
        #change data of properties damaged to float
        d = data[12]
        if d == 0:
            n += 1 #none
        elif d > 10000:
            h += 1 # high
        elif d < 1000:
            l += 1 # low
        else:
            m += 1 # medium
    # make a list of total high, low, and medium damage
    dam = [n,l,m,h]
    #ask for file name
    filename = input ('Insert name of graph file: ') # name of graph file
    print('\tNone: ', n,'\n \tLow: ', l, '\n \tModerate: ', m, '\n \tHigh: ', h) #printing to console
    plt.bar (['none', 'low', 'moderate', 'high'], dam, color ='red')
    plt.xlabel("Property Damage")
    plt.ylabel("Number of Storms")
    plt.title("Property Damage Caused By Storms")
    plt.show()
    plt.savefig(filename)



# finds the average duration of all storms and prints it
def average_duration(storms):
    count = 0
    total = 0
    # runs through each storm, finds duration, adds it to total, increase count by 1
    for storm in storms:
        duration = storm[END_DAY] - storm[START_DAY]
        if duration == 0:
            duration = 1
        total += duration
        count += 1
    # calculate the average
    avg = float(total / count)
    print ("Average duration of all storms: %.2f" %avg, " days\n")

def storm_type_frequency (storms):
    count_type = {}
    # Count each storm type
    for storm in storms:
        if storm[TYPE] in count_type:
            count_type[storm[TYPE]] += 1
        elif not storm[TYPE] in count_type:
            count_type[storm[TYPE]] = 1
    most_common = max(count_type)
    print(count_type)
    print("The most common type is: " + str(most_common))


def main():
    try:
        storms = load_storm_data()
        menu(storms)
        #ask for storm data file and open file
    #    file = input('Enter the name of storm data file: ')
    #    storm = open(file)
        #op = menu(storm)
    #    print()
    #    if op == 1: #injuries vs deaths
    #        death_and_injury_data(storm)
    #    if op == 2: #property damage graph
    #        print('Property Damage Graph')
    #        prop(storm)
    #    if op == 3: #average duration
    #        average_duration(storm)
    #    if op == 4: #most frequent storm
    #        question_four(storm)

    except FileNotFoundError:
        print ('Invalid file name. Please try again.')


main()
