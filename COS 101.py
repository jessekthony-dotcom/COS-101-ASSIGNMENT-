import math

# Constants
G = 6.67430e-11  # Universal gravitational constant (N·m²/kg²)
g = 9.81         # Standard acceleration due to gravity on Earth (m/s²)

while True:
    print("\n--- Physics Formula Calculator ---")
    print("1. Newton's Second Law (F = m * a)")
    print("2. Kinetic Energy (E = 0.5 * m * v^2)")
    print("3. Ohm's Law (V = I * R)")
    print("4. Universal Gravitational Force (F = G * (m1 * m2) / R^2)")
    print("5. Simple Pendulum Period (T = 2 * pi * sqrt(L / g))")

    choice = input("\nSelect a formula (1-5): ").strip()

    if choice == "1":
        m = float(input("Enter mass (m) in kg: "))
        a = float(input("Enter acceleration (a) in m/s²: "))
        force = m * a
        print(f"Force (F) = {force:.4f} N")

    elif choice == "2":
        m = float(input("Enter mass (m) in kg: "))
        v = float(input("Enter velocity (v) in m/s: "))
        energy = 0.5 * m * (v ** 2)
        print(f"Kinetic Energy (E) = {energy:.4f} J")

    elif choice == "3":
        i = float(input("Enter current (I) in Amperes: "))
        r = float(input("Enter resistance (R) in Ohms: "))
        voltage = i * r
        print(f"Voltage (V) = {voltage:.4f} V")

    elif choice == "4":
        m1 = float(input("Enter first mass (m1) in kg: "))
        m2 = float(input("Enter second mass (m2) in kg: "))
        r = float(input("Enter distance between centers (R) in meters: "))
        if r == 0:
            print("Error: Distance (R) cannot be zero.")
        else:
            force = G * (m1 * m2) / (r ** 2)
            print(f"Gravitational Force (F) = {force:.4e} N")

    elif choice == "5":
        length = float(input("Enter pendulum length (L) in meters: "))
        if length < 0:
            print("Error: Length (L) cannot be negative.")
        else:
            period = 2 * math.pi * math.sqrt(length / g)
            print(f"Pendulum Period (T) = {period:.4f} seconds")

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

    # Loop control: ask user whether to continue or end
    while True:
        again = input("\nDo you want to continue? (Yes/No): ").strip().lower()
        if again in ("yes", "y"):
            break
        elif again in ("no", "n"):
            print("Program ended. Goodbye!")
            exit()
        else:
            print("Please type 'Yes' or 'No'.")
