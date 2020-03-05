def callnum(digits):
    callnumbers = {'0': ' ', '1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}
    output = [key for key in callnumbers[digits[0]]]
    for index in range(1, len(digits)):
        number = digits[index]
        if number in [0, 1]:
            break
        options = []
        for key in callnumbers[number]:
            options += [option + key for option in output]
        output = options
        output.sort()
    print(output)


if __name__ == '__main__':
    a = input('Input:\n')
    a = a.split(',')
    print('Output:')
    callnum(a)
