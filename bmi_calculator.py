def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class 1"
    elif 35 <= bmi < 39.9:
        return "Obesity Class 2"
    else:
        return "Obesity Class 3"

def main():
    print("BMI Calculator")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")

if __name__ == "__main__":
    main()

