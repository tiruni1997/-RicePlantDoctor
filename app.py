from flask import Flask, request, jsonify,render_template

#import mysql.connector

from main import chatWithBot

#from flaskext.mysql import MYSQL
#import pymysql


app = Flask(__name__)

#conn= mysql.connector.connect(host="localhost", user="root", password='', database="rice_plant_doctor")
#cursor=conn.cursor()

#mysql = MYSQL()

#MYSQL configeration

#app.config['MYSQL_DATABWSE_USER']='root'
##app.config['MYSQL_DATABWSE_PASSWORD']='rice_plant_doctor'
#app.config['MYSQL_DATABWSE_DB']='root'
#app.config['MYSQL_DATABWSE_HOST']='localhost'
#mysql.init_app(app)



@app.route('/get', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.args.get('msg')
    return jsonify(chatBotReply=chatWithBot(chatInput))


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/index/Login')
def Login():
	return render_template('Login.html')

    
@app.route('/index/bot')
def bot():
	return render_template('bot.html')


@app.route('/index/SignIn')
def SignIn():
	return render_template('SignIn.html')

@app.route('/index/ContactUS')
def ContactUS():
	return render_template('ContactUS.html')

@app.route('/index/AboutUs')
def AboutUs():
	return render_template('AboutUs.html')


	

#@app.route("/login_validation", methods=['POST', 'GET'])
#def login_validation():
	#email=request.form.get('email')
	#password=request.form.get('password')

	#cursor.execute("""SELECT * FROM 'farmer_details' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}' '""".format(email,password))
	
	#farmer_details=cursor.fetchall()

	#if len(farmer_details)>0:
		#return render_template('Home.html')
	#else:
		#return render_template('index.html')


#@app.route('/add_user' , method=['POST'])
#def add_user():
	#name=request.form.get('uname')
	#district=request.form.get('uDistrict')
	#email=request.form.get('uemail')
	#password=request.form.get('upassword')
	#cursor.execute("""INSERT INTO 'farmer_details' ('F_ID','FullName','District','email','password') VALUES
	 #(NULL,'{}','{}','{}','{}')""".format(name,district,email,password))
	
	#conn.commit()
	#return "register Success"



if __name__ == '__main__':
    app.run()