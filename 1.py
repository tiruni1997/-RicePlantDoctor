
from flask import Flask,render_template,request, jsonify, session, sessions,url_for,redirect
from werkzeug.utils import redirect
#import mysql.connector

#connection =mysql.connector.connect(host='localhost',port='3306', database='rice_plant_doctor',user='root',password='')
#cursor =connection.cursor()

from main import chatWithBot

app = Flask(__name__)


@app.route('/get', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.args.get('msg')
    return jsonify(chatBotReply=chatWithBot(chatInput))


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index/sign')
def signin():
	return render_template('Signin.html')

@app.route('/index/homepage')
def homepage():
	return render_template('HomePage.html')

@app.route('/index/bot')
def bot():
	return render_template('bot.html')

#@app.route('/login', methods=['GET','POST'])
#def login():
	#msg=''
	#if request.methode=='POST':
		#username=request.form.get('Email')
		#password=request.form.get('Password')
		##record =cursor.fetchone()
		#return "The email is {} and the password is{}".format(email,password).render_template('bot.html')
		#if record:
			#session['loggedin']=True
			#session['username']=record[1]
			#return redirect(url_for('home'))
		#else:
			#msg='Error'
	#return render_template('index.html',msg=msg) 
if __name__ == '__main__':
    app.run()