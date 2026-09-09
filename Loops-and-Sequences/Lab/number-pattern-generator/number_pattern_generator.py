def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value."
    
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    secret_code = ""
    for i in range(1, n + 1):
        if i == 1:
            secret_code += str(i)
        else:
            secret_code += " " + str(i)
            
    return secret_code
#print(number_pattern(5))