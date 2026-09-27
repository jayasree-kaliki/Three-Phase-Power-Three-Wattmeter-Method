# three_wattmeter_method.py
# Program to calculate three-phase power
# using the Three-Wattmeter Method

print("=== Three-Wattmeter Method ===")

# Input wattmeter readings
W1 = float(input("Enter Wattmeter 1 reading (W): "))
W2 = float(input("Enter Wattmeter 2 reading (W): "))
W3 = float(input("Enter Wattmeter 3 reading (W): "))

# Calculate total active power
total_power = W1 + W2 + W3

# Display results
print("\n--- Three-Wattmeter Results ---")
print(f"Wattmeter 1 = {W1:.2f} W")
print(f"Wattmeter 2 = {W2:.2f} W")
print(f"Wattmeter 3 = {W3:.2f} W")
print(f"Total Three-Phase Power = {total_power:.2f} W")
print(f"Total Three-Phase Power = {total_power / 1000:.3f} kW")
