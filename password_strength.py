import re

# For password rating evaluatuon
# 1. Upper- and lower-case:
lower_case = re.compile(r'[a-z]')
upper_case = re.compile(r'[A-Z]')
# 2. Digits
digits     = re.compile(r'\d')
# 3. Special symbols
spec_symb  = re.compile(r'@|\^|#|\$|\*|&|-|_')
# For password denying
# 4. Bad passwordlist (depends on used (may be old) passwords, etc.)
bad_password_list = ['vasya123', 'irina 1974', 'uryuk']
# 5. Persosnel information words 
pers_inf     = re.compile(r'ILIA|PETROV|IRINA|NIKITENKO')
# 6. Company name (both full and acronim)
company_name = re.compile(r'HumanFactorLabs|HFLabs|HFL')
# 7. Standard formats
standard_formats  = re.compile(r'\d{2}[\.-]\d{2}[\.-]\d{2,4}|\d{4}-\d{2}-\d{2}|[a-zA-Z]{1}\d{3}[a-zA-Z]{2}\d{2,3}')
# Password strenth evaluation

def get_password_rating(password):
    #     pass
    password_rating = 0
    if not (password in bad_password_list or
                    pers_inf.findall(password) or
                    company_name.findall(password) or
                    standard_formats.findall(password)):
        if (upper_case.findall(password) and
            lower_case.findall(password)):
            password_rating += 3
        if digits.findall(password):
            password_rating += 3
        if spec_symb.findall(password):
            password_rating += 4
    return password_rating

def result_out_put(password_rating):
    if password_rating:
        print('\n\nYour password rating is: ', password_rating)
    else:               
        print('\n\nSuch password can not be approved, try again')

if __name__ == '__main__':
    password = input('\nPlease, input your password:\n\n')
    password_rating = get_password_rating(password)
    result_out_put(password_rating)