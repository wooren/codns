num = int(input('세자리 정수 입력'))
number = '영일이삼사오육칠팔구'
def read_single_digit(one):
    han = number[one]
    return han
def read_number(thr):
    a = thr//100 #100의 자리수
    b = thr%100 #남은 수
    c = b//10 #10의 자리수
    d = b%10 #1의 자리수
    res1 = read_single_digit(a)
    res2 = read_single_digit(c)
    res3 = read_single_digit(d)
    print(res1 , res2 , res3)
read_number(num)
    
    
