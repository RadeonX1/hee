import random
score = 1
while not score == "0":
    print("Main Menu")
    print(9 * "=")
    print("""1. Input Number of Score
2. Random Score and Check Grade
3. Exit""")
    choice = int(input("Enter Choice : "))
    if 0 < choice <=3:
        match choice:
            case 1:
                score = int(input("Enter number of score : "))
            case 2:
                print("Start Random Score ...")
                print("Check Grade...")
                print(14 * "-")
                print("|Grade| Total|")
                print(14 * "-")
                totalScore = 0
                A = 0
                B = 0
                C = 0
                D = 0
                F = 0
                for num in range(score):
                    ranscore = random.randrange(40, 90)
                    if ranscore >= 80:
                        A += 1
                    elif ranscore >= 70:
                        B += 1
                    elif ranscore >= 60:
                        C += 1
                    elif ranscore >= 50:
                        D += 1
                    else:
                        F += 1
                    totalScore = A + B + C + D + F
                print("|" + "A".center(5) + "|"f"{A:5d} |")
                print("|" + "B".center(5) + "|"f"{B:5d} |")
                print("|" + "C".center(5) + "|"f"{C:5d} |")
                print("|" + "D".center(5) + "|"f"{D:5d} |")
                print("|" + "F".center(5) + "|"f"{F:5d} |")
                print(14 * "-")
                print(f"|Total|{totalScore:5d} |")
                print(14 * "-")
            case 3:
                print("Exit Program")
                break
    else:
        print("Invalid choice, please try again.")
        