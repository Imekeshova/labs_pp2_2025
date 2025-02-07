s=input()
def reversed_sentence(str):
    words=str.split()
    result=' '.join(reversed(words))
    print(result)
reversed_sentence(s)