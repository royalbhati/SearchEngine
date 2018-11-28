from flask import Flask, request, render_template
import io
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
import glob
from pathlib import Path
import collections
import difflib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
	return render_template('home.html')

@app.route('/result', methods=['POST'])
def my_form_post():
	text = request.form['text']
	ps = PorterStemmer()
	stop_words = set(stopwords.words('english'))
	pages=[]
	os.chdir('/home/royal/Desktop/searchengine')
	for file in glob.glob("*.txt"):
		pages.append(file)
	index_map={}

	for page in pages:
		with open(page) as f:
			l= f.read()
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
			stemmed.append(f)
		c = collections.Counter(stemmed)
		final=[]

		for i in c.most_common(10):

			final.append(i[0])


		index_map[page]=final

	
	dic={}
	values=[]
	for k,v in index_map.items():
		dic[k]=v
		values.append(v)



	key_to_search=[]

	for i in values:
		if text in i:
				key_to_search.append(i)

	# print("dic===",values)
	print(key_to_search)
	kts=[]
	for k,v in dic.items():
		for ks in key_to_search:
			if ks==v:
				kts.append(k)

	print(kts)
	aa=[]
	for k in kts:
		with open(k) as f:
			aa.append(f.read())


	ll=aa
	link=['https://en.wikipedia.org/wiki/Cat','https://en.wikipedia.org/wiki/Dog','https://en.wikipedia.org/wiki/Aeroplane']	
	return render_template('result.html',result=ll,txt=text,kts=kts,link=link)

if __name__ == "__main__":
	app.debug = True
	app.run()	