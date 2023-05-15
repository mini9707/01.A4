from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ssvirwm.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/song')
def team1():
   return render_template('song.html')

@app.route("/team", methods=["POST"])
def member_post():
    name_receive = request.form['name_give']
    mbti_receive = request.form['mbti_give']
    intro_receive = request.form['intro_give']
    adv_receive = request.form['adv_give']
    style_receive = request.form['style_give']
    address_receive = request.form['address_give']

    doc = {
       'name':name_receive,
       'mbti':mbti_receive,
       'intro':intro_receive,
       'adv':adv_receive,
       'style':style_receive,
       'address':address_receive
    }
    db.members.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/team", methods=["GET"])
def member_get():
    all_members = list(db.members.find({},{'_id':False}))
    return jsonify({'result': all_members})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)