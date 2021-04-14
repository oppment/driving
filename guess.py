import random
start = int(input('請輸入起始值'))
end = int(input('請輸入結束值'))
r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	num = int(input('請猜數字'))
	if num == r:
		print('恭喜你！你猜中了！！')
		print('這是你猜的第', count,'次')
		break
	elif num > r:
		print('數字太大，請重猜 ')
	elif num < r:
		print('數字太小，請重猜 ')
	print('這是你猜的第', count,'次')
