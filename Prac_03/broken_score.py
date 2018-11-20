score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif 0 <= score <= 100:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")

