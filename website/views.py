from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import  login_required, current_user
from .models import User
from . import collection
import json
from bson import ObjectId
from datetime import datetime




views = Blueprint("views", __name__)

@views.route("/", methods = ["GET","POST"])
@login_required
def home():
    
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short",category = "error")

        else:
            userID = current_user.get_id()
            current_datetime = datetime.now().strftime("%m/%d/%Y")
            collection.update_one(
            {'_id': ObjectId(userID)},
            {'$push': {'notes': {'note': note, 'date': current_datetime}}})

            
            

            flash("Lift added",category = "success")

            
        
    

    return render_template("home.html", user=current_user, notes = collection.find_one({"_id": ObjectId(current_user.get_id())})['notes'])

@views.route('/delete-note', methods=['POST'])
def delete_note():
    
  
    data = json.loads(request.data)  
    note = data['note']
    date = data['date']

    if data:
        collection.update_one(
        {'_id': ObjectId(current_user.get_id())},
        {'$pull': {'notes': {'note': note, 'date': date}}})

    return jsonify({})

@views.route("/settings")
def settings():

    
    return render_template("settings.html", user = current_user)



@views.route("/settings/resetAccount",methods=['POST'])
def resetAccount():

    collection.update_one(
        {'_id': ObjectId(current_user.get_id())},  
        {'$set': {'notes': []}}  
    )
        
    flash("Account Sucessfully Reset")

    return redirect(url_for('views.settings'))




@views.route('/data')
def get_data():
    
    users= list(collection.find())
    

    for user in users:
        user['_id'] = str(user['_id'])
    
    return (jsonify(users))




@views.route("/progressTracker")
def Tracker():
    user = current_user.get_id()
    pass
    
            
        
        


