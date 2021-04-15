# 讀取檔案
data=[]
count = 0
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
#		if count % 1000 == 0:
#			print(len(data))
		print(count)
print('總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('流言的平均長度為',sum_len/len(data))
