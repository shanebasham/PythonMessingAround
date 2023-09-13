
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
        #find age drops and append to decrease list
        highest = agelist[0]
        largest = 0
        for age in agelist:
            drop = highest - age
            largest = max(largest, drop)
            decrease.append(largest)
        maxagedrop = 0
        for drop in decrease:
            if drop > maxagedrop:
                maxagedrop = drop
                countrydrop = country
                year1 = year
                year2 = year+1
    print(f'The country with the greatest age drop was {countrydrop} from {year1}-{year2} with a drop of {maxagedrop:.2f} years.\n')

agedrop()

# agelist = []
# with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#     for index, line in enumerate(file):
#         if index > 1:
#             words = line.strip().split(',')
#             country = words[0]
#             year = int(words[2])
#             age = float(words[3])
#             if age:
#                 agelist.append(age)
# decrease = []
# for i in range(len(agelist)):
#     try:
#         if agelist[i] - agelist[i+1] > 0:
#             decrease.append(agelist[i] - agelist[i+1])
#     except:
#         if agelist[-2] - agelist[-1] > 0:
#             decrease.append(agelist[-2] - agelist[-1])
# maxdrop = 0
# for i in range(0, len(decrease)):
#     decrease[i] = int(decrease[i])
#     for i in range(0, len(decrease)):
#         if maxdrop > decrease:
#             maxdrop = decrease
# print(maxdrop)

            #find greatest age drop
            # maxagedrop = -1
            # for i in range(len(ages)):
            #     for j in range(i + 1 , len(ages)):
            #         agedrop = ages[i] - ages[j]
            #         if agedrop > maxagedrop:
            #             maxagedrop = agedrop
            #             countrydrop = country
            #             year1 = year
            #             year2 = year1 + 1
#print(f'The country with the greatest age drop was countrydrop from year1-year2 with a drop of {maxage:.2f} years.\n')

# list = []
# with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#     for index, line in enumerate(file):
#         if index > 1:
#             words = line.strip().split(',')
#             list.append(words)
# choice = input('\nEnter country: ').capitalize()
# while not str(choice) in list[0]:
#     choice = input(f'"{choice}" is not a valid country, please try another country: ').capitalize()
# print(f'{choice} In list')

# import time
# for x in range (0,4):  
#     b = "Loading" + "." * x
#     print (b, end="\r")
#     time.sleep(.5)
# from itertools import repeat

# vowel = ["a", "e", "i", "o", "u"]
# consonant = ["h", "s", "t"]
# for x in vowel:
#   for y in consonant:
#     s = (x + y)
#     n = 5
#     print(list(repeat(s, n)))
# print()

#BEST
# import time
# for x in range (0,4):  
#     b = "Loading" + "." * x
#     print (b, end="\r")
#     time.sleep(.3)

# print()
# import sys
# import time
# a = 0  
# for x in range (0,3):  
#     a = a + 1  
#     b = ("Loading" + "." * a)
#     # \r prints a carriage return first, so `b` is printed on top of the previous line.
#     sys.stdout.write('\r'+b)
#     time.sleep(0.5)
# print(a)

# from itertools import repeat
# twister_list = []
# place = ["right hand", "left hand", "right foot", "left foot"]
# color = ["red", "yellow", "blue", "green"]
# for x in place:
#   for y in color:
#     s = (x + " " + y)
#     n = 1
#     list = (list(repeat(s, n)))
