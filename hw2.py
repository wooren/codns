def exchange(m):
    a = m//500; #500원 짜리의 개수
    b = m%500; #500원 주고 남은 나머지
    c = b//100; #100원 짜리의 개수
    d = b%100; #100원도 주고 남은 나머지
    e = d//50; #50원 짜리의 개수
    f = d%50; #50원 주고 남은 나머지
    g = f//10; #10원 짜리의 개수
    print('500원수=',a);
    print('100원수=',c);
    print('50원수=',e);
    print('10원수=',g);

def get_integer(prompt):
    res = float(input(prompt));
    return res;

r = get_integer('반환하고하 하는 금액?'); exchange(r);
