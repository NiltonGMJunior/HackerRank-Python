import re

def fun(s):
    pattern = r'^([a-zA-Z0-9\_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]{1,3})$'
    compiled_pattern = re.compile(pattern)
    matches = re.findall(compiled_pattern, s)
    if matches:
        return True
    return False

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