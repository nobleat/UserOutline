from flask import Flask, render_template, request, redirect, session
from user import usercls

app = Flask(__name__)

@app.route('/')
def index():
    userlist = usercls.get_all()
    return render_template("index.html", userlist=userlist )

@app.route('/create_user')
def create_user():
    return render_template('/adduser.html')

@app.route('/adduserpg',  methods=['POST'])
def adduserpg():
        usercls.create(request.form)
        return redirect('/')


if __name__=="__main__":
    app.run(debug=True)