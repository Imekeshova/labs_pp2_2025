def unique_list(lst): 
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

user_input = input()
user_list = [int(i) for i in user_input.split()]

print(unique_list(user_list))
