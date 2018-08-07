import io
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
import glob
from pathlib import Path
import collections
import difflib


ps = PorterStemmer()

stop_words = set(stopwords.words('english'))


pages=[]
os.chdir('/home/royal/Documents/searchengine')
for file in glob.glob("*.txt"):
	pages.append(file)
index_map={}

for page in pages:
	with open(page) as f:
		l= f.read()# Use this to read file content as a stream:
		words = l.split()
	for r in words:
	    if not r in stop_words:
	    	path=Path('./filter')
	    	appendFile = open(f'{path}/homefil.txt','a')
	    	appendFile.write(" "+r)
	    	appendFile.close()

	with open(f'{path}/homefil.txt') as g:
		cont=g.read()
		filt_word=cont.split()
		os.remove(f'{path}/homefil.txt')


	stemmed=[]
	for f in filt_word:
		stemmed.append(ps.stem(f))
	c = collections.Counter(stemmed)
	final=[]

	for i in c.most_common(1):

		final.append(i[0])


	index_map[page]=final

a=input('Enter your search ')

dic={}
values=[]
for k,v in index_map.items():
	# print(v[0])
	dic[v[0]]=k
	# print(v)
	values.append(v[0])

key_to_search=difflib.get_close_matches(a, values)
found_key=dic[key_to_search[0]]

with open(found_key) as f:
	print(f.read())
		



