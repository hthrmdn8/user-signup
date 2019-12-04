from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])

def display_form():
    password_errors= ['','']
    return render_template('register.html', title="We Don't Want Your Buisness", password_errors=password_errors)
    

def password_check(password, password2):   
    password_error= ''
    password2_error='' 

    if password != password2:
        password2_error = "Passwords Don't Match"   
              
    if len(password) >20 or len(password) <3:
        password_error = "Does Not Meet Password Requirements (Between 3-20 Characters)"
    return [password_error, password2_error]   



@app.route('/', methods=['POST'])
def validate():
    username = request.form["Username"]
    username_error = ''
    email = request.form["Email"]
    email_error = ''
    password = request.form["Password"]
    password2 = request.form["Verify Password"]   
    password_errors = password_check(password, password2)

    if len(username) >20 or len(username) <3 or username.count(' ') > 0:
        username_error = "Does Not Meet Username Requirements (Between 3-20 Characters, and No Spaces)"
    
    if email != '' and (not 3 <= len(email) <= 20 or email.count("@") != 1 or email.count(".") != 1 or email.count(' ') > 0): 
        email_error = "Does Not Meet Email Requirements Hoe"
    
    if not email_error and not username_error and not password_errors[0] and not password_errors[1]:
        return render_template("page.html", username= username)

    return render_template("register.html", username= username, username_error=username_error, password_errors=password_errors, email=email, email_error=email_error)








app.run()