
# variables
country = ''
year = 0
age = 0
ymaxage = 0
yminage = 100
ymaxcountry = ''
ymincountry = ''
cmaxage = 0
cminage = 100
ysumage = 0
ycount = 0
csumage = 0
ccount = 0
# open file and split and strip all words after line 1
with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
    yoi = input('\nPlease enter a year or country: ')
    if yoi.isdigit():
        while int(yoi) < 1543 or int(yoi) > 2019:
            yoi = input('That is not a valid year, please try another year: ')
        for index, line in enumerate(file):
            if index > 1:
                words = line.strip().split(',')
                country = words[0]
                year = int(words[2])
                age = float(words[3])
            # find min and max years for yoi
            if year == int(yoi):
                ysumage += age
                ycount += 1
                if age > ymaxage:
                    ymaxage = age 
                    ymaxcountry = country
                if age < yminage:   
                    yminage = age
                    ymincountry = country
        #find average life expectancy for yoi
        yaveage = ysumage / ycount
        print(f'\nFor the year {yoi}:')
        print(f'The min life expectancy was in {ymincountry} with {yminage:.2f} years.')
        print(f'The max life expectancy was in {ymaxcountry} with {ymaxage:.2f} years.')
        print(f'The average life expectancy across all countries in {yoi} was {yaveage:.2f} years.\n')

    else:
        country = ''
        coi = yoi
        for index, line in enumerate(file):
            if index > 1:
                words = line.strip().split(',')
                country = words[0]
                year = int(words[2])
                age = float(words[3])
                #find min and max years for coi
                while not coi.capitalize() in words:
                    coi = input('That is not a valid country, please try another country: ')
            if country == coi:
                ccount += 1
                csumage += age
                if age > cmaxage:
                    cmaxage = age 
                if age < cminage:
                    cminage = age
        #find average life expectancy for coi
        #caveage = csumage / ccount
        print(f'\nFor the country of {coi}:')
        print(f'The min life expectancy was {cminage:.2f} years.')
        print(f'The max life expectancy was {cmaxage:.2f} years.')
        #print(f'The overall average life expectancy in {coi} is {caveage:.2f} years.\n')
            


# # #get all the variables
# # maxage = 0
# # minage = 100
# # maxcountry = ' '
# # mincountry = ' '
# # maxyear = 0
# # minyear = 3000
# # yoi_maxage = 0
# # yoi_minage = 100
# # yoi_maxcountry = ' '
# # yoi_mincountry = ' '
# # yoi_list = []
# # yoi = int(input('What is the year? '))
# # while yoi < 1543 or yoi > 2019:
# #         yoi = int(input('That is not a valid year, please try another year: '))
# # with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
# #     for line in file.readlines():
# #         if str(yoi) in line:
# #             yoi_list.append(line)
# #     for index, line in enumerate(file):
# #         if index > 1:
# #             words = line.split(',')
# #             country = words[0].strip()
# #             year = int(words[2].strip())
# #             age = float(words[3].strip())
# #             if age > maxage:
# #                 maxage = age 
# #                 maxcountry = country
# #                 maxyear = year
# #             if age < minage:
# #                 minage = age
# #                 mincountry = country
# #                 minyear = year
# #             sumage = 0
# #             for i in words:
# #                 sumage += age
# #             count = 0
# #             for i in words:
# #                 count += 1
# #             aveage = sumage / count
            
# #             # if yoi == year:
# #             #     if age > maxage:
# #             #         yoi_maxage = age
# #             #         yoi_maxcountry = country
# #             #     if age < minage:    
# #             #         yoi_minage = age
# #             #         yoi_mincountry = country
# #             #     yoi_sumage = sum(yoi_list)
# #             #     yoi_count = 0
# #             #     for i in yoi_list:
# #             #         yoi_count += 1
# #             #     yoi_aveage = yoi_sumage / yoi_count
            
# # print(f"The country with the maxage is: {maxcountry} with {maxage} years in {maxyear}.")
# # print(f"The country with the minage is: {mincountry} with {minage} years in {minyear}.")
# # #print(f'The average life expectancy across all countries from 1543 to 2019 is {aveage}')
# # print(f'\nFor the year of {yoi}:')
# # print(f'The min life expectancy was {yoi_mincountry} with {yoi_minage} years.')
# # print(f'The max life expectancy was {yoi_maxcountry} with {yoi_maxage} years.')
# # #print(f'The average life expectancy across all countries is {yoi_aveage}')
    

# def yoi():
#     yoi = '2000'
#     ymaxage = 0
#     yminage = 100
#     ymaxcountry = ''
#     ymincountry = ''
#     with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#         for index, line in enumerate(file):
#             if index > 1:
#                 words = line.split(',')
#                 country = words[0].strip()
#                 year = int(words[2].strip())
#                 age = float(words[3].strip())
#                 if year == int(yoi):
#                     if age > ymaxage:
#                         ymaxage = age 
#                         ymaxcountry = country
#                     if age < yminage:
#                         yminage = age
#                         ymincountry = country
#                 sumage = 0
#                 for i in words:
#                     sumage += age
#                 count = 0
#                 for i in words:
#                     count += 1
#                 aveage = sumage / count
#     print(f'\nFor the year {yoi}:')
#     print(f'The min life expectancy was in {ymincountry} with {yminage} years.')
#     print(f'The max life expectancy was in {ymaxcountry} with {ymaxage} years.')
#     print(f'The average life expectancy across all countries from 1543 to 2019 is {aveage}\n')
        
# def life_expectancy():
#     maxage = 0
#     minage = 100
#     maxcountry = ' '
#     mincountry = ' '
#     maxyear = 0
#     minyear = 3000
#     with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#         for index, line in enumerate(file):
#             if index > 1:
#                 words = line.split(',')
#                 country = words[0].strip()
#                 year = int(words[2].strip())
#                 age = float(words[3].strip())
#                 if age > maxage:
#                     maxage = age 
#                     maxcountry = country
#                     maxyear = year
#                 if age < minage:
#                     minage = age
#                     mincountry = country
#                     minyear = year
#                 sumage = 0
#                 for i in words:
#                     sumage += age
#                 count = 0
#                 for i in words:
#                     count += 1
#                 aveage = sumage / count
#     print(f'\nThe overall max life expectancy is: {maxage} from {maxcountry} in {maxyear}')
#     print(f'The overall min life expectancy is: {minage} from {mincountry} in {minyear}')
#     print(f'The average life expectancy across all countries from 1543 to 2019 is {aveage}\n')
        
# yoi(), life_expectancy()


# # #open file and add all info to list
# # filelist = []
# # filelistfloat = [float(i) for i in filelist]
# # #fileliststr' '.join(map(str,filelist))
# # #cfilelistfloat = [float(x.replace(',', '')) for x in filelist]
# # life_expectancy = 'C:\\Users\\shane\\OneDrive\\Desktop\\PythonMessingAround\\Week 11 + 12\\life-expectancy.csv'
# # with open(life_expectancy) as file:
# #     for index, line in enumerate(file):
# #         line = line.strip()
# #         newline = line.split(',')
# #         filelist.append(newline)
# #         # if index == 0:
# #         #     continue
# #         # else:
# #         #     filelist.append(newline)

# #     #country = fileliststr[0]
# #     country = filelistfloat[0]
# #     #year = float(fileliststr[2])
# #     year = 0
# #     #age = float(fileliststr[3])
# #     age = 0

# #     maxage = 100
# #     minage = 0
# #     yoi_count = 0
# #     yoi_sum = 0

# # #enter valid year of interest(yoi)
# #     yoi = float(input('Enter the year of interest: '))
# #     while yoi < 1543 or yoi > 2019:
# #         yoi = float(input('That is not a valid year, please try another year: '))
# # #find min and max age, country, and year
# #     for word in (filelistfloat):
# #         if float(word[age]) > float(maxage):
# #             maxage = float(word[age])
# #             maxyear = word[year]
# #             maxcountry = word[country]
# #         if float(word[age]) < float(minage):    
# #             minage = float(word[age])
# #             minyear = word[year]
# #             mincountry = word[country]
# # #find min and max age, country, and year for yoi
# #         if filelistfloat[year] == yoi:
# #             yoi_count += 1
# #             yoi_sum += float(word[age])
# #             if float(word[age]) > float(maxage):
# #                 yoi_maxage = float(word[age])
# #                 yoi_maxyear = word[year]
# #                 yoi_maxcountry = word[country]
# #             if float(word[age]) < float(minage):    
# #                 yoi_minage = float(word[age])
# #                 yoi_minyear = word[year]
# #                 yoi_mincountry = word[country]
# # #find total average age overall
# #         sumage = sum(filelistfloat[age])
# #         count = 0
# #         for i in filelistfloat:
# #             count += 1
# #         aveage = sumage / count
# # #find total average age of yoi
# #         yoi_aveage = yoi_sum / yoi_count

# #     print(f'The overall max life expectancy is: {maxage} from {maxcountry} in {maxyear}')
# #     print(f'The overall min life expectancy is: {minage} from {mincountry} in {minyear}')
# #     print(f'The average life expectancy across all countries from 1543 to 2019 is {aveage}')
# #     print(f'\nFor the year of {yoi}:')
# #     print(f'The average life expectancy across all countries is {aveage}')
# #     print(f'The min life expectancy was in with {yoi_minage} years.')
# #     print(f'The max life expectancy was in with {yoi_maxage}years.')



# def life_expectancy():
#     maxage = 0
#     minage = 100
#     maxcountry = ' '
#     mincountry = ' '
#     maxyear = 0
#     minyear = 3000
#     with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#         for index, line in enumerate(file):
#             if index > 1:
#                 words = line.split(',')
#                 country = words[0].strip()
#                 year = int(words[2].strip())
#                 age = float(words[3].strip())
#                 if age > maxage:
#                     maxage = age 
#                     maxcountry = country
#                     maxyear = year
#                 if age < minage:
#                     minage = age
#                     mincountry = country
#                     minyear = year
#                 sumage = 0
#                 for i in words:
#                     sumage += age
#                 count = 0
#                 for i in words:
#                     count += 1
#                 aveage = sumage / count
#     print(f'\nThe overall max life expectancy is: {maxage} from {maxcountry} in {maxyear}')
#     print(f'The overall min life expectancy is: {minage} from {mincountry} in {minyear}')
#     print(f'The average life expectancy across all countries from 1543 to 2019 is {aveage}\n')
        
# def yoi():
#     yoi = int(input('Please enter a year: '))
#     while yoi < 1543 or yoi > 2019:
#             yoi = int(input('That is not a valid year, please try another year: '))
#     yoi_maxage = 200
#     yoi_minage = 0
#     yoi_maxcountry = ' '
#     yoi_mincountry = ' '
#     yoi_list = []
#     with open(r'C:\Users\shane\OneDrive\Desktop\PythonMessingAround\Week 11 + 12\life-expectancy.csv', 'r') as file:
#         # for line in file.readlines():
#         #     if str(yoi) in line:
#         #         yoi_list.append(line)
#         for index, line in enumerate(file):
#             if index > 1:
#                 words = line.split(',')
#                 country = words[0].strip()
#                 year = int(words[2].strip())
#                 age = float(words[3].strip())
#                 if year == int(yoi):
#                     if age > yoi_maxage:
#                         yoi_maxage = age
#                         yoi_maxcountry = country
#                     if age < yoi_minage:    
#                         yoi_minage = age
#                         yoi_mincountry = country
#             # yoi_sumage = sum(age)
#             # yoi_count = 0
#             # for i in yoi_list:
#             #     yoi_count += 1
#             # yoi_aveage = yoi_sumage / yoi_count
#     print(f'\nFor the year {yoi}:')
#     print(f'The min life expectancy was in {yoi_mincountry} with {yoi_minage} years.')
#     print(f'The max life expectancy was in {yoi_maxcountry} with {yoi_maxage} years.')
#     #print(f'The average life expectancy across all countries is {yoi_aveage}')
    

# yoi(), life_expectancy()