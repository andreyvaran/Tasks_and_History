from math import factorial, ceil


def cnk(n: int, k: int) -> int:
    return ceil(factorial(n) / (factorial(k) * factorial(n - k)))


def result(n: int, m: int) -> int:
    res = 0
    if ((n + m - 2) % 3 == 0):
        line_ = (n + m - 2) // 3
        num_ = min(n, m) - line_ - 1
        res = cnk(line_, num_)
    return res


if __name__ == '__main__':
    n, m = map(int, input().split())

    print(result(n, m))
'''

									
									
									1
									
								1	
									8
							1		
								7	
						1			21
							6		
					1			15	
						5			20
				1			10		
					4			10	
			1			6			5
				3			4		
		1			3			1	
			2			1			
	1			1					
		1							
1									

'''
