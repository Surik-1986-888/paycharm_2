number_1=int(input("Enter_number_1 "))
number_2=int(input("Enter_number_2 "))
if number_1<number_2:
	smol_number=number_1
else:
	smol_number=number_2
print("smol_number=",smol_number)
i=2
k=1
while i<smol_number+1:
	k=smol_number%i
	if k==0:
		print("devisible=",i)
		break
	i+=1
