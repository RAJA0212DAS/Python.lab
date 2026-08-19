temp = float(input("Enter temperature: "))
choice = input("Enter unit (C/F/K): ").upper()

if choice == "C":
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15

    print("Fahrenheit =", fahrenheit)
    print("Kelvin =", kelvin)

elif choice == "F":
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15

    print("Celsius =", celsius)
    print("Kelvin =", kelvin)

elif choice == "K":
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32

    print("Celsius =", celsius)
    print("Fahrenheit =", fahrenheit)

else:
    print("Invalid unit")