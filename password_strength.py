import re, getpass

STANDARD_FORMATS  = re.compile(r'\d{2}[\.-]\d{2}[\.-]\d{2,4}|\d{4}-\d{2}-\d{2}|[a-zA-Z]{1}\d{3}[a-zA-Z]{2}\d{2,3}')
"""
Standard formats 
\d{2}[\.-]\d{2}[\.-]\d{2,4}        - Date format
\d{4}-\d{2}-\d{2}                  - Date format
[a-zA-Z]{1}\d{3}[a-zA-Z]{2}\d{2,3} - license plate 
"""
def get_password_rating(password):
    password_rating = 0
    if not (re.compile(r'HumanFactorLabs|HFLabs|HFL').findall(password) or
            STANDARD_FORMATS.findall(password)):
        if (re.compile(r'[A-Z]').findall(password) and
            re.compile(r'[a-z]').findall(password)):
            letter_weight = 3
            password_rating += letter_weight
        if re.compile(r'\d').findall(password):
            digit_weight = 3
            password_rating += digit_weight
        if re.compile(r'@|\^|#|\$|\*|&|-|_|\+|=|:|;|!|<|>|~|`|\.|,|%|(|)|"|\\|/|\?').findall(password):
            spec_symbol_weight = 4
            password_rating += spec_symbol_weight
    return password_rating

def result_out_put(password_rating):
    if password_rating:
        print('\n\nYour password rating is: ', password_rating)
    else:               
        print('\n\nSuch password can not be approved, try again')

if __name__ == '__main__':
    password = getpass.getpass()
    password_rating = get_password_rating(password)
    result_out_put(password_rating)