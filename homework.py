password = '9487'
t=3
while  True:
	p2 = input('輸入密碼:')
	if p2 == password:
		print('登入成功!')
		break
	else:
		t=t-1
		if t<1:
			print('密碼錯誤')
			break
		print('還有',t,'次機會')
		
