sale = int(input("할인률은?"))
def get_fixed_price(price):
    fixed = price * 100/(100-sale)
    return fixed
A = int(input("a상품의 할인된 가격은?"))
B = int(input("b상품의 할인된 가격은?"))
A_price = get_fixed_price(A)
B_price = get_fixed_price(B)
print("A상품의 정가는",A_price)
print("B상품의 정가는",B_price)

