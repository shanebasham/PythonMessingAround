
from datetime import datetime

#main function
def main():
    #get user input
    gender = input("Please enter your gender (M or F): ")
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))

    #run functions using users input
    years = find_age(birth_str)
    kg = lb_to_kg(pounds)
    cm = in_to_cm(inches)
    bmi = find_bmi(kg, cm)
    bmr = find_bmr(gender, kg, cm, years)

    #print results
    print(f"\nAge (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

#find users birthday
def find_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

#convert a mass in pounds to kilograms
def lb_to_kg(pounds):
    kg = pounds * 0.45359237
    return kg

#convert a length in inches to centimeters
def in_to_cm(inches):
    cm = inches * 2.54
    return cm

#find users body mass index
def find_bmi(weight, height):
    bmi = weight / (height ** 2) * 10000
    return bmi

#find users basal metabolic rate
def find_bmr(gender, weight, height, age):
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

main()