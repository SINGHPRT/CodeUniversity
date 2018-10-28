from flask import Flask, render_template, json, request

app = Flask(__name__)

## URL Routes and their handlers

@app.route('/')
def main():
     return render_template('index.html')


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({
            "status":"success",
            "name":_name,
            "email":_email,
            "password":_password})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/signIn', methods=['POST'])
def signIn():
    # read the posted values from the UI
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _email and _password:
        return json.dumps({
            "status":"success",
            "email":_email,
            "password":_password})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


##Run the app  if it is main/entry point
if __name__ == '__main__':
   app.run(debug=True)






