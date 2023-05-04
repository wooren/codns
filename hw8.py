shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    total = input('수량은? ')
    shopping_bag[item] = total
    print(f'장바구니에 {item} {total}개가 담겼습니다')

print(f'>>>장바구니 보기: {shopping_bag}')

print('[검색]')
identify = input('장바구니에서 확인하고자 하는 상품은? ')
if identify in shopping_bag:
    print(f'{identify}(는) {shopping_bag[identify]}개 있습니다')
else:
    print(f'장바구니에 {identify}는 없습니다')