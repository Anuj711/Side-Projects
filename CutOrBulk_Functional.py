import math, os, sys, random


def greeting():
    print(
        "Hello, welcome to the cut or bulk program. \nThis program is intended for adults who are working out for "
        "the first time.\nThis program uses metric units and will convert imperial to metric for you if needed.")
    main()

def main():
    # Taking weight input
    print(
        "\nIf you know your weight in killograms please press 1. If you do not know this weight in killograms and "
        "wish to enter it in pounds please press 2:")
    weight = 0.0
    height = 0.0
    choice1 = int(input())
    if choice1 == 1:
        print("Please enter your weight in kilograms")
        weight = float(input())
    elif choice1 == 2:
        print("Please enter your weight in pounds")
        weight = float(input()) * 0.45359237
    # Taking height input
    print(
        "\nIf you know your height in meters please press 1. If you do not know this height in meters and wish to "
        "enter it in feet please press 2:")
    choice2 = int(input())
    if choice2 == 1:
        print("Please enter your height in meters")
        height = float(input())
    elif choice2 == 2:
        print("Please enter your height in feet")
        height = float(input()) / 3.28
    BMI(height, weight)


def BMI(height, weight):
    bmi = 0.0
    bmi = round((weight / (height * height)))
    BFP(bmi)


def BFP(bmi):
    print("Your BMI:", bmi)
    print("Please enter your age")
    bfp = 0
    age = int(input())
    print("Please enter your gender by selecting 1 for Male and 2 for Female")
    gender = int(input())
    if gender == 1:
        bfp = round(1.20 * bmi + 0.23 * age - 16.2)
    elif gender == 2:
        bfp = round(1.20 * bmi + 0.23 * age - 5.4)
    print("Here is your body fat percentage: ", bfp, "%")
    CutOrBulk(bfp, bmi)


def CutOrBulk(bfp, bmi):
    print("\nHere are your results")
    if (bmi <= 18) & (bfp <= 6):
        print("You're pretty skinny, you need to build some mass. Try bulking!")
    elif (bmi >= 25) & (bfp >= 23):
        print("You're kind of heavy already, you need to get leaner. Try cutting!")
    elif (18 < bmi) & (bmi < 25) & (bfp <= 17):
        print("Your body composition is fine, however you might have some stubborn fat in minor areas and skinny "
              "arms. You need to build some mass overall. Try bulking!")
    elif (18 < bmi) & (bmi < 25) & (bfp > 17):
        print(
            "Your body composition is fine however, you might have some stubborn fat in more noticeable areas. You "
            "need to get leaner. Try cutting!")


greeting()
