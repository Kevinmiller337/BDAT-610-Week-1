for tempConversions in range(3):
    inputFahrenheitString = input("Enter temperature in Fahrenheit: ")
    tempInF = float(inputFahrenheitString)
    tempInC = (tempInF - 32) * 5.0/9.0
    print( "The temperature in C is", tempInC, "degrees" )

