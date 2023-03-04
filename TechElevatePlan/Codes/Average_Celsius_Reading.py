def average_celsius(fahrenheit_readings):
    # Create an empty array to store the Celsius readings
    celsius_numbers = []
    # Convert each Fahrenheit reading to Celsius and add to the array
    for fahrenheit_reading in fahrenheit_readings:
        celsius_conversion = (fahrenheit_reading - 32) / 1.8
        celsius_numbers.append(celsius_conversion)

    # Calculate the sum of all Celsius readings
    sum = 0.0
    for celsius_number in celsius_numbers:
        sum += celsius_number

    # Calculate and return the mean average
    return sum / len(celsius_numbers)

