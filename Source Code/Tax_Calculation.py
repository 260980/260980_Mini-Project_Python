# Calculating tax for a particular person
def tax_payment(age, gender, income):
    if age < 60 and gender == 'female':
        if income < 250000:
            return 'NO TAX'
        elif 250000 <= income <= 5000000:
            t1 = income
            t2 = (5 / 100) * t1
            tax = t2
            return abs(tax)
        elif 500000 <= income <= 1000000:
            t1 = income
            t2 = (20 / 100) * t1
            tax = t2
            return abs(tax)
        else:
            t1 = income
            t2 = (30 / 100) * t1
            tax = t2
            return abs(tax)
    elif age < 60 and gender == 'male':
        if income < 250000:
            return "No TAX"
        elif 250000 <= income <= 500000:
            t1 = income
            t2 = (6 / 100) * t1
            tax = t2
            return abs(tax)
        elif 500000 <= income <= 1000000:
            t1 = income
            t2 = (21 / 100) * t1
            tax = t2
            return abs(tax)
        else:
            t1 = income
            t2 = (31 / 100) * t1
            tax = t2
            print(abs(tax))
    elif 60 < age < 80:
        if income < 300000:
            return "No TAX"
        if 300000 <= income <= 500000:
            t1 = income
            t2 = (5 / 100) * t1
            tax = t2
            return abs(tax)
        elif 500000 <= income <= 1000000:
            t1 = income
            t2 = (20 / 100) * t1
            tax = t2
            return abs(tax)
        else:
            t1 = income
            t2 = (30 / 100) * t1
            tax = t2
            return abs(tax)
    elif age > 80:
        if income < 500000:
            return "No TAX"
        if 500000 <= income <= 1000000:
            t1 = income
            t2 = (20 / 100) * t1
            tax = t2
            return abs(tax)
        elif income > 1000000:
            t1 = income
            t2 = (30 / 100) * t1
            tax = t2
            return abs(tax)


def main():
    print("\n-------------------------------------------------\n")
    print("---------Welcome to Tax Calculation System--------\n")
    print("--------------------------------------------------\n")
    f = open("tax.txt", "a")
    age_in = int(input("Enter Age: \n"))
    gender_in = input("ENTER GENDER: \n")
    income_in = int(input("ENTER YEARLY INCOME: \n"))
    x = tax_payment(age_in, gender_in, income_in)
    print('Enter yes if you have applied for any policy')
    option = input(' ')
    if option == 'yes':
        print("Select any policy")
        # Reduces tax for policies
        print('1.car loan\n2.home loan\n3.Lic policy')
        policy = input('')
        if policy == '1':
            tax = (1 / 100) * x
            x = x - tax
        elif policy == '2':
            tax = (2 / 100) * x
            x = x - tax
        elif policy == '3':
            tax = (2 / 100) * x
            x = x - tax
    else:
        x = x
    print("Tax to be paid: \n" + str(x))
    # Stores the data into a file
    f.write(str(age_in) + "\t" + gender_in + "\t" + str(income_in) + "\t" + option + "\t" + str(x) + "\n")
    f.close()


if __name__ == "__main__":
    main()


# Pytest
def test_method():
    assert tax_payment(35, 'female', 1000000) == 50000
    assert tax_payment(65, 'male', 20000000) == 6000000
