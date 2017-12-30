from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os
from sklearn import tree


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])

#[height, weight, shoe size]
# give data set
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [166, 65, 40], [190,90,47], [175,64,39], [177,70,40], [159, 55, 37], [171, 75, 42], [181, 85,43]]

# what it can be 
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male',
      'female', 'male', 'female'] 

# we are gonna use a Decision Tree 
# https://en.wikipedia.org/wiki/Decision_tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[180, 79, 44]])

print prediction


def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
