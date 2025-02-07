def spy_game(nums):
    code = [0, 0, 7]  
    index = 0 
    for num in nums:
        if num == code[index]:  
            index += 1  
            
            if index == len(code):  
                return True

    return False  
