import random

r = random.randint(1,100)
while True:
	num = int(input('請猜數字'))
	if num == r:
		print('恭喜你！你猜中了！！')
		break
	elif num > r:
		print('數字太大，請重猜 ')
	elif num < r:
		print('數字太小，請重猜 ')
