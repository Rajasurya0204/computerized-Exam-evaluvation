from flask import Flask, render_template, request
from v3 import main

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/calc')
def calc():
	question = request.args['q']
	image = request.args['i']
	keys = request.args['e'].split(',')
	marks = request.args['m']
	if marks:
		marks= float(marks)
		mark = main(question,image,keys,marks)
	else:
		mark = main(question,image,keys,0.25)
	return render_template("result.html",mark = mark)

if __name__ == '__main__':
   app.run(debug = True)