def check_clothing_suitability(temp):
    if temp >= 25:  # Temperature in Celsius, you can adjust this value
        print("It's hot enough for light clothes.")
    else : 
         print("It's cold, you can wear heavy clothes.")
    


temperature = float(input("Enter the current temperature in Celsius: "))
result = check_clothing_suitability(temperature)
print(result)