# Display the menu
print("Physics Formula Calculator")
print("Choose one of the following options:")
print("A: Calculate Force (F = m * a)")
print("B: Calculate Kinetic Energy (KE = 0.5 * m * v^2)")
print("C: Calculate Potential Energy (PE = m * g * h)")
print("D: Calculate Pressure (P = F / A)")
print("E: Calculate Work Done (W = F * d)")

# Get the user's choice
choice = input("Enter your choice (A, B, C, D, E): ").strip().upper()

# Perform the appropriate calculation based on the user's choice
if choice == "A":
    m = float(input("Enter mass (m) in kg: "))
    a = float(input("Enter acceleration (a) in m/s^2: "))
    F = m * a
    print(f"Force (F) = {F} N")
elif choice == "B":
    m = float(input("Enter mass (m) in kg: "))
    v = float(input("Enter velocity (v) in m/s: "))
    KE = 0.5 * m * v**2
    print(f"Kinetic Energy (KE) = {KE} J")
elif choice == "C":
    m = float(input("Enter mass (m) in kg: "))
    g = 9.8  # Acceleration due to gravity in m/s^2
    h = float(input("Enter height (h) in meters: "))
    PE = m * g * h
    print(f"Potential Energy (PE) = {PE} J")
elif choice == "D":
    F = float(input("Enter force (F) in N: "))
    A = float(input("Enter area (A) in m^2: "))
    P = F / A
    print(f"Pressure (P) = {P} Pa")
elif choice == "E":
    F = float(input("Enter force (F) in N: "))
    d = float(input("Enter distance (d) in meters: "))
    W = F * d
    print(f"Work Done (W) = {W} J")
else:
    print("Invalid choice. Please select A, B, C, D, or E.")