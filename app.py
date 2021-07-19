from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login_page.html')

@app.route('/loginresult', methods=['GET', 'POST'])
def loginresult():

    if request.method == 'POST':
        typeofuser = request.form['typeofuser']
        emp_id = request.form['empid']
        email = request.form['email']
        password = request.form['password']

        if typeofuser == '1':
            conn = pymysql.connect(database = 'employees', host='localhost', user = 'susmita', password = 'susmita12')
            cursor = conn.cursor()
            cursor.execute('select *from employees where employee_id = %s;',(emp_id))
            if cursor.rowcount == 1:
                record = cursor.fetchall()
                for x in record:
                    empid = x[0]
                    emailid = x[1]
                    passw = x[2]
                    if emp_id == empid and email == emailid and password == passw:
                        return render_template('homepage.html')

        #else
            #return 'Hello %s %s %s %s have fun learning python <br/> <a href="/">Back Home</a>' % (typeofuser,emp_id, email,password)

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/tasks.html')
def tasks():
    return render_template('tasks.html')

@app.route('/customerrecommendations.html')
def customerrecommendations():
    return render_template('customerrecommendations.html')

@app.route('/promotions.html')
def promotions():
    return render_template('promotions.html')

@app.route('/performance.html')
def performance():
    return render_template('performance.html')

@app.route('/product.html')
def product():
    return render_template('product.html')

@app.route('/activityhistory.html')
def activityhistory():
    return render_template('activityhistory.html')

@app.route('/reminders.html')
def reminders():
    return render_template('reminders.html')

@app.route('/events.html')
def events():
    return render_template('events.html')

@app.route('/login_page.html')
def login_page():
    return render_template('login_page.html')










#if __name__ == "__index__":
    #app.run()
