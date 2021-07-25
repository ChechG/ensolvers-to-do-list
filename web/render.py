#!/usr/bin/python3
from sys import argv
import MySQLdb
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
import MySQLdb.cursors
import re
import uuid
from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)
app.secret_key = '343434'

MY_HOST = "localhost"
MY_USER = "new_user"
MY_PASS = "todolist"
MY_DB = "todo_db"

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

@app.route('/', methods=['GET'])
def ini():
    """ First entry from app """
    if request.method == 'GET':
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", not_exist=not_exist, list_f=list_f, items=list_i, list_folders=dic_folders)

@app.route('/submit_add', methods=['POST'])
def submit_add():
    if request.method == "POST":
        new_task = request.form["new_task"]
        folder_task = request.form["task_folder"]
        folder_task = folder_task[11:]
        add_t = db.cursor()
        add_t.execute("INSERT INTO lists (todo, id_folder) VALUES ('{}', {})".format(new_task, int(folder_task)))
        db.commit()
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", list_folders=dic_folders)

@app.route('/submit_folder', methods=['POST'])
def submit_folder():
    if request.method == 'POST':
        new_folder = request.form["new_folder"]
        add_f = db.cursor()
        add_f.execute("INSERT INTO folders (name) VALUES ('{}')".format(new_folder))
        db.commit()
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", list_folders=dic_folders)


@app.route('/submit_delete', methods=['POST'])
def submit_delete():
    if request.method == 'POST':
        delete_task = request.form["task_id"]
        tasks = db.cursor()
        tasks.execute("DELETE FROM lists WHERE id=" + delete_task)
        db.commit()
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", list_folders=dic_folders)

@app.route('/submit_edit', methods=['POST'])
def submit_edit():
    if request.method == 'POST':
        edit_task = request.form['task_id']
        task_id = int(edit_task)
        new_task = request.form['new_task']
        edits = db.cursor()
        edits.execute("UPDATE lists SET todo='{}' WHERE id={}".format(new_task, task_id))
        db.commit()
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", list_folders=dic_folders)

@app.route('/delete_folder', methods=['POST'])
def delete_folder():
    if request.method == 'POST':
        folder = request.form['folder_id']
        items_list = db.cursor()
        items_list.execute("SELECT * FROM lists")
        items = items_list.fetchall()
        list_i = []
        not_exist = "You have no items on your to-do list"
        if items:
            for item in items:
                lista = []
                for i in item:
                    lista.append(i)
                list_i.append(lista)
            not_exist = ""
        folders_list = db.cursor()
        folders_list.execute("SELECT * FROM folders")
        folders = folders_list.fetchall()
        list_f = []
        if folders:
            for folder in folders:
                lista = []
                for f in folder:
                    lista.append(f)
                list_f.append(lista)
        dic_folders = {}
        for k in list_f:
            list_tasks = []
            for task in list_i:
                if task[2] == k[0]:
                    task[2] = k[1]
                    list_tasks.append(task)
            k[1] = k[1].replace(" ", "_")
            dic_folders[k[1]] = list_tasks
    return render_template("index.html", list_folders=dic_folders)
        

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)