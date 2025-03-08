def check_for_palindrom(s):
    if s == s[::-1]:
        print("PASS")
    else:
        print("DON'T PASS")
    
s = input().replace(" ", "").lower()
check_for_palindrom(s)
    