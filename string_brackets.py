def check_string_brackets(input_string):
    count = 0
    for char in input_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            print('NO')
            return
    if count == 0:
        print('YES')
    else:
        print('NO')
            
            
check_string_brackets('{}}{}))')
check_string_brackets('[](){}')
