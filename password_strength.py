import re, getpass

date_format_ru     = r'\d{2}[\.-]\d{2}[\.-]\d{2,4}'                    # Russian date format
date_format_en     = r'\d{4}-\d{2}-\d{2}'                              # English date format
license_plate      = r'[a-zA-Z]{1}\d{3}[a-zA-Z]{2}\d{2,3}'             # license format

def get_password_rating(password):
    password_rating = 0
    standard_formats = re.compile('{}|{}|{}'.format(date_format_ru, date_format_en, license_plate)) 
    if not standard_formats.findall(password):                         # Standard form serachs
        if (re.compile(r'[A-Z]').findall(password) and                 # Upper case search
            re.compile(r'[a-z]').findall(password)):                   # Lower case search
            letter_weight = 3
            password_rating += letter_weight
        if re.compile(r'\d').findall(password):                        # Digit search
            digit_weight = 3
            password_rating += digit_weight
        if re.compile(r'@|\^|#|\$|\*|&|-|_|\+|=|:|;|!|<|>|~|`|\.|,|%|(|)|"|\\|/|\?').findall(password): # Special symbols search
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