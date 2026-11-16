
print("===== PHYSICS FORMULA SOLVER =====")
print("1. Speed")
print("2. Force")
print("3. Density")
print("4. Work Done")
print("5. Pressure")

choice = int(input("Choose a formula (1-5): "))

if choice == 1:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    answer = distance / time
    print("Speed =", answer, "m/s")

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    answer = mass * acceleration
    print("Force =", answer, "N")

elif choice == 3:
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))
    answer = mass / volume
    print("Density =", answer, "kg/m³")

elif choice == 4:
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    answer = force * distance
    print("Work Done =", answer, "J")

elif choice == 5:
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m²): "))
    answer = force / area
    print("Pressure =", answer, "Pa")

else:
    print("Invalid choice!")
