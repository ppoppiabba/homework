burger_prices = [int(input("햄버거 값: ")) for _ in range(3)]

drink_prices = [int(input("음료 값: ")) for _ in range(2)]

set_menu_prices = [burger + drink - 50 for burger in burger_prices for drink in drink_prices]

print(min(set_menu_prices))

