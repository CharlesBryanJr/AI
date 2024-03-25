import re

def find_regex_match(text, pattern):
    match = re.search(pattern, text)
    return match.group() if match else None


print(f'match_string1 = {find_regex_match("all time is relative", "a.*e")}')
print(f'match_string2 = {find_regex_match("all time is relative", "a.*?e")}')
print(f'match_string3 = {find_regex_match("aabababa", "a(ab)*a")}')
print(f'match_string4 = {find_regex_match("bbc", "ab+c")}')
print(f'match_string5 = {find_regex_match("ac", "a.[bc]+")}')
print(f'match_string6 = {find_regex_match("axbycz", "abc|xyz")}')
print(f'match_string7 = {find_regex_match("Brittle =", "[a-zA-Z]*[^,]=")}')
print(f'match_string8 = {find_regex_match("very very tall monster", "(very )+(fat )?(tall|ugly) monster")}')
html_string = '<h1 attribute="77">'
pattern = "<[^>]+>"
print(f'match_string9 = {find_regex_match(html_string, pattern)}')
mystr = "foo=99andfoo"
pattern = r"(\w+)=(\d+)and\1"
print(f'match_string10 = {find_regex_match(mystr, pattern)}')
mystr = "mello drama"
pattern = r"\w+\s*\d+"
print(f'match_string11 = {find_regex_match(mystr, pattern)}')
mystr = "mello drama"
pattern = r"\w+\s*\D+"
print(f'match_string12 = {find_regex_match(mystr, pattern)}')
