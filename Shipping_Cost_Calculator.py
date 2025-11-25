# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the weight in kilograms(kg): "))
rate = float(input("Enter the shipping rate per kg: "))

## Calculate Shipping Cost
shipping_cost = weight * rate

## Display Result
print(f"Weight: {weight} | Rate: {rate}")
print("--------------------------------")
print(f"Shipping Cost: ${shipping_cost}")
