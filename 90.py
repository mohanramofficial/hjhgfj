def onlyint():
	s=input()
	l=list(s)
	a=''
	for i in l:
		if i.isnumeric():
			a+=i
	print(a)
try:
	onlyint()
except:
	print('invalid')
  p
