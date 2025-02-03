temperature = 17
result = "Cold" if temperature < 15 else ("Warm" if 15 <= temperature <= 30 else "Hot")
print(result)