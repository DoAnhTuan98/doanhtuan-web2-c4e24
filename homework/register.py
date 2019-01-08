import mlab
from mongoengine import Document,StringField,IntField,EmailField
from flask import Flask,render_template,redirect,request
app = Flask(__name__)

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        mlab.connect()
        class users(Document):
            name = StringField()
            email = EmailField()
            user = StringField()
            password = StringField()
        m = users(
            name = request.form["name"],
            email = request.form["email"],
            user = request.form["user"],
            password = request.form["password"],
        )
        m.save()
        return("WElcom")
if __name__ == "__main__":
    app.run(debug=True)
 

        




