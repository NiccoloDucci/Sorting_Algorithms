def countingSort(alist):
	
	#lista output
	result = [0]*len(alist)
	
	#trovo massimo e minimo
	mx = alist[0]
	mn = alist[0]
	for i in alist[1:]:
		if i > mx:
			mx=i
		elif i<mn:
			mn=i
	
	#creo vettore occorrenze per valore nell'intervalo [mn,mx]
	counts=[0]*(mx-mn+1)
	
	#calcolo occorrenze
	for i in range( len(alist) ):
		counts[ alist[i]-mn ] = counts[ alist[i]-mn ] + 1
	
	#Ordinamento in base al contenuto dell'array delle frequenze counts
	k=0
	for j in range(len(counts)):
		while counts[j] > 0:
			result[k] = j + mn
			k=k+1
			counts[j]=counts[j]-1
			
	return result    

a=[0,2,3,4,1,5]
print(countingSort(a))