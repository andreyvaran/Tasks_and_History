def simb_in_str(st : str , sub : str) -> bool:
    set1 = set(list(st))
    subset = set(list(sub))
    for i in subset:
        if i not in set1 : return False
    return True




if __name__ == '__main__':
    s = input()
    t1 = input()
    t2 = input()

    # Test1
    # if simb_in_str(s , t1) and simb_in_str(s ,t2):
    #     print('hui')




'''



ez 

huila
hui
la

stopgame
sam
topge

Можно попытаться описать что если в 2 словах есть одинаковая последовательность 
gaharaghr
grh
aaagrh

sam
topge


'''