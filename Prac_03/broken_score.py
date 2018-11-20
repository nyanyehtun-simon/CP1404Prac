def main():
    score = float(input("Enter score: "))

    result = determine_score(score)
    print(result)

def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"

main()


