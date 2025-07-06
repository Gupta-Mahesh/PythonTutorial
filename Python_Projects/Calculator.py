"""Calculator program using exception handling (try and except) """


def isNumeric(*value2):
    try:
        for val in value2:
            float(val)
        return True
    except (ValueError, TypeError) as e:
        print("Enter Valid value", e)
        return False, exit(1)

def add(*value2):
    temp = 0 
    if isNumeric(*value2):
        for val in value2:
            temp += float(val)
        return "The Addition of these value are "+ str(temp)

def sub(*value2):
    count = 0
    temp = 0 
    if isNumeric(*value2):
        for val in value2:
            count +=1
            if count == 2:
                result = "The Subtraction of this value is " + str (float(value2[0]) - float(value2[1]))
        if count > 2:
            message = result + " [Note: Only first two value were considered for the substraction result.]"
            return message
        else:
            return result

def multiply(*value2):
    temp =1
    if isNumeric(*value2):
        for val in value2:
            temp *= float(val)
        return "The Multiplication of these values are "+ str(temp)

def div(*value2):
    count = 0
    if isNumeric(*value2):
        try:
            for val in value2:
                count +=1
                if count == 2:
                    result = "The Division of the value is " + str (int(value2[0]) / int(value2[1]))
            if count > 2:
                message = result + " [Note: Only first two value were considered for the division result.]"
                return message
            else:
                return result
        except ZeroDivisionError:
            return "The Value can not divide by the Zero"


#number = None
number = [i for i in input("Enter the numbers by giving space : ").split()]
operation = input("Enter which operation do you want to proceed : +, -,*, / or All : ").strip()

if len(number) < 2:
    print("Please enter the value")
    exit(1)
elif operation == '+':
    print("\n",add(*number))

elif operation == '-':
    print("\n",sub(*number))

elif operation == '*':
    print("\n",multiply(*number))

elif operation == '/':
    print("\n",div(*number))

elif operation == 'all':
    print("\n",add(*number))
    print("\n",sub(*number))
    print("\n",multiply(*number))
    print("\n",div(*number))
else:
    print("operation not supported")
