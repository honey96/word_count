from django.http import HttpResponse
from django.shortcuts import render
import operator
def start(request):
	return render(request,'start.html')


def count(request):
	fulltext=request.GET['parabox']
	words=fulltext.split()
	worddict={}
	for i in words:
		if i in worddict:
			worddict[i]+=1
		else:
			worddict[i]=1
	#print(fulltext)
	sort=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

	return render(request,'count.html',{'parabox':fulltext,'count':len(words),'sorted_words':sort})


def about(request):
	return render(request,'about.html')
