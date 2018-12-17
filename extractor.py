import pyperclip,re

text = str(pyperclip.paste())   #Used to get content directly from clipboard
result = []                     #Empty list to store results

def PhoneNumberCheck():
    PhnNumCheck = re.compile(r'''
        (\d{3}|\(\d{3}\))    #first three-digit
        (\s|-|\.)?           #separator or space
        (\d{3}|\(\d{3}\))    #second three-digits
        (\s|-|\.)?           #separator or space
        (\d{4}|\(\d{4}\))    #last four-digits
    ''', re.VERBOSE)
    for num in PhnNumCheck.findall(text):
        result.append(num[0] + num[2] + num[4])

def EmailCheck():
    emailCheck = re.compile(r'''
        [a-zA-Z0-9.+_-]+  #username
        @                 #@ character
        [a-zA-Z0-9.+_-]+  #domain name
        \.                #first .(dot) 
        [a-zA-Z]          #domain type like-- com
        \.?               #second .(dot) for domains like co.in
        [a-zA-Z]*         #second part of domain type like 'in' in  co.in 
    ''',re.VERBOSE)

    for emails in emailCheck.findall(text):
        result.append(emails)

def PrintResult():
    if len(result)>0 :
        print('Found ' + str(len(result)) + ' results:')
        for n in range(0,len(result)):
            print(result[n])
    else:
        print('No phone number or email address found.')

def main():
    PhoneNumberCheck()
    EmailCheck()
    PrintResult()

if __name__ == '__main__':
    main()






