
# function for year of interest(yoi)
def yoi():  
    # variables
    country = ''
    year = 0
    age = 0
    ymaxage = 0
    yminage = 100
    ymaxcountry = ''
    ymincountry = ''
    ysumage = 0
    ycount = 0
    # open file and split and strip all words after line 1
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for index, line in enumerate(file):
            if index > 1:
                words = line.strip().split(',')
                country = words[0]
                year = int(words[2])
                age = float(words[3])
                # find min and max years for yoi
                if year == int(choice):
                    ysumage += age
                    ycount += 1
                    if age > ymaxage:
                        ymaxage = age 
                        ymaxcountry = country
                    if age < yminage:   
                        yminage = age
                        ymincountry = country
        # find average life expectancy for yoi
        yaveage = ysumage / ycount
        print(f'\nFor the year {choice}:')
        print(f'The min life expectancy was in {ymincountry} with {yminage:.2f} years.')
        print(f'The max life expectancy was in {ymaxcountry} with {ymaxage:.2f} years.')
        print(f'The average life expectancy across all countries in {choice} was {yaveage:.2f}.\n')

# function for country of interest(coi)                  
def coi():
    # variables
    cmaxage = 0
    cminage = 100
    csumage = 0
    ccount = 0
    cmaxyear = 0
    cminyear = 3000
    country = ''
    # open file and split and strip all words after line 1
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for index, line in enumerate(file):
            if index > 1:
                words = line.strip().split(',')
                country = words[0]
                year = int(words[2])
                age = float(words[3])
                # find min and max years for coi
                if country == choice:
                    ccount += 1
                    csumage += age
                    if age > cmaxage:
                        cmaxage = age 
                        cmaxyear = year
                    if age < cminage:
                        cminage = age
                        cminyear = year
        #find average life expectancy for coi
        try:
            caveage = csumage / ccount
        except ZeroDivisionError:
            countryerror(choice)
        print(f'\nFor the country of {choice.capitalize()}:')
        print(f'The min life expectancy was {cminage:.2f} years in {cminyear}.')
        print(f'The max life expectancy was {cmaxage:.2f} years in {cmaxyear}.')
        print(f'The overall average life expectancy in {choice} is {caveage:.2f} years.\n')

# function for overall ages                 
def overall():
    # variables
    maxage = 0
    minage = 100
    maxcountry = ' '
    mincountry = ' '
    maxyear = 0
    minyear = 3000
    latest = 0
    earliest = 3000
    maxagedrop = 0
    # open file and split and strip all words after line 1 again
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for index, line in enumerate(file):
            if index > 1:
                words = line.split(',')
                country = words[0].strip()
                year = int(words[2].strip())
                age = float(words[3].strip())
                # find overall min and max years
                if age > maxage:
                    maxage = age 
                    maxcountry = country
                    maxyear = year
                if age < minage:
                    minage = age
                    mincountry = country
                    minyear = year
                # find earliest and latest years
                if year > latest:
                    latest = year
                if year < earliest:
                    earliest = year
                # find overall average life expectancy
                sumage = 0
                for i in words:
                    sumage += age
                count = 0
                for i in words:
                    count += 1
                aveage = sumage / count
    print(f'The overall max life expectancy is {maxage:.2f} years from {maxcountry} in {maxyear}')
    print(f'The overall min life expectancy is {minage:.2f} years from {mincountry} in {minyear}')
    print(f'The ovreall average life expectancy across all countries from {earliest} to {latest} is {aveage:.2f} years.')
    
# function to find greatest age drop
def agedrop():
    #create list for all ages and for all decreases
    agelist = []
    decrease = []
    # open file and split and strip all words after line 1 and append to agelist
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for index, line in enumerate(file):
            if index > 1:
                words = line.strip().split(',')
                country = words[0]
                year = int(words[2])
                age = float(words[3])
                agelist.append(age)
        # find age drops and append to decrease list
        highest = agelist[0]
        largest = 0
        for age in agelist:
            drop = highest - age
            largest = max(largest, drop)
            decrease.append(largest)
        # find max age drop
        maxagedrop = 0
        for drop in decrease:
            if drop > maxagedrop:
                maxagedrop = drop
                countrydrop = country
                year1 = year
                year2 = year+1
    print(f'The country with the greatest age drop was {countrydrop} from {year1} {year2} with a drop of {maxagedrop:.2f} years.\n')

# function to split and strip all words and add all lines with chosen word into list
results = []
def choices(choice):
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for line in file:
            if line == choice:
                results.append(line.strip().split(','))             

# function for division error
def countryerror(choice):
    choice = input(f'"{choice}" is not a valid country, please try another country: ').capitalize()  
    choices(choice)
    coi()

# loop to run functions again
yes = 'yes'
while yes.lower().startswith('y'):
    # enter valid year of interest(yoi) or country of interest(coi)
    choice = input('\nPlease enter a year or country: ').capitalize()
    with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
        for line in file:
            if line == choice:
                results.append(line.strip().split(','))  
    if choice.isdigit():
        while int(choice) < 1543 or int(choice) > 2019:
            choice = input('That is not a valid year, please try another year: ')
        yoi()
    else:
        choices(choice)
        coi()
    yes = input('Would you like to search again? ')
else:
    print('\nHere is the overall information from around the world:')
    overall()
    agedrop()
    print('Goodbye now!\n')
    exit
