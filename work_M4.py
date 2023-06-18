str = 'helloworld'
def palindrom_check(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        print('True')
        return True
    else: 
        print('False')
        return False
palindrom_check(str)