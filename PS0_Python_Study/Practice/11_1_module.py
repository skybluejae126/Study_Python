# 필요한 것들끼리 부품처럼 잘 만들어진 파일
# 부품만 교체하거나 추가할 수 있게 (확장자.py)

# import theater_module_11_1
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 영화 보러 갔을 때 가격
# theater_module.price_solider(5) # 4명이서 군인이 영화 보러 갔을 때 가격

# import theater_module_11_1 as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module_11_1 import*
# price(3)
# price_morning(4)
# price_solider(5)

# from theater_module_11_1 import price, price_morning # 어떤 함수만 가져다 쓸지 선택 가능
# price(5)
# price_morning(6)
# # price_solider(7) # 오류남

from theater_module_11_1 import price_solider as price
price(5)