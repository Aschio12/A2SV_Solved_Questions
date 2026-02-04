def swap_case(s):
    ans=""
    for char in s:
        if char.isalpha():
            if char==char.upper():
                ans+=char.lower()
            else:
                ans+=char.upper()
        else:
            ans+=char
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)