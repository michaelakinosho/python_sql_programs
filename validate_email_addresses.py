import re

def fun(s):
    if s.count('@') != 1 and s.count('.') != 1:
        print('1')
        return False
    elif s.find('@') > s.find('.') or s.find('@') == 0:
        print('2')
        return False
    else:
        at_index = s.find('@')
        username = s[0:s.find('@')]
        website = s[s.find('@')+1:s.find('.')]
        extension = s[s.find('.'):len(s)+1]

        if len(re.findall("[^a-zA-Z0-9_-]",username)) > 0:
            print('3')
            return False
        if len(re.findall("[^a-zA-Z0-9]",website)) > 0:
            print('4')
            return False
        print(extension)
        if len(re.findall("[^a-zA-Z.]",extension)) > 0:
            print('5')
            return False
        elif len(extension) < 2 or len(extension) > 4:
            return False

    return True

    #print(s, 'just testing again')
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
