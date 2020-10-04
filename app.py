#!/usr/bin/env python

# coding: utf-8


# In[ ]:





from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/")

def xyz():

    return render_template("power.html")

@app.route("/userinput",methods=['GET','POST'])

def abc():

    if(request.method=='POST'):
        num=int(request.form['n'])

        power=int(request.form['p'])

        r=(num**power)

        return render_template("power.html",result=r)

if __name__=="__main__":

    app.run()







