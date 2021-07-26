# To-Do list APP

This is a simple web application that allows you to create to-do items and folders to
group them. The development was divided in two phases:
- Phase 1: to-do item creation
- Phase 2: folder creation to group the to-do items

## Description

With this app you can create your tasks, whatever they are, and those will be stored in a local database. Every time you add a new task, you also need to add it to a folder, which you can also create and store in the same database. You can add, update or delete tasks as you want. You can also delete the folders once you are finished. Each task can be checked so you can follow your progress through the day!

## Features
* Add, update, delete tasks.
* Check every finished task.
* Create new folders.
* Delete folders, including the tasks you assigned said folder.
* Tasks and folders will be stored in a database for later use.
* Single-page app.

## Getting Started

### Dependencies

In order to download it and run it, you will need:
* Python3
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

* Flask - Python module, web framework
```
$ sudo pip3 install Flask
```

* Jinja2
```
$ sudo pip3 install Jinja2
```

* MySQL
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
```
* JavaScript 3.2.1

* Bootstrap

### Installing

* This To-Di List APP can be downloaded from [this](https://github.com/ChechG/ensolvers-to-do-list.git) repo.
* The database should be populated in order for results to be visible and the application to run as it should so you need to run the script as it follows:
```
$ ./open_todo_list
```
* Open your browser of choice (I recommend [Google Chrome](https://www.google.com/intl/es-419/chrome/) for now) and type `http://localhost:5000/`
* Enjoy creating new lists!

## Database

One of the most crucial parts of the overall performance of the app is the database mapping implemented. To better understand and start using the app, a dump.sql file is used to populate the database when you run the script. Once you get the hang of it, the user can delete the default tasks and folders.


### Screenshots

User Login:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_login.png?raw=true)

Player Daily Input:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_player_view.png?raw=true)

Staff Dashboard:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_dash.png?raw=true)

Staff View - Player Profile:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_profile.png?raw=true)

Staff View - Advanced Stats:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_adv.png?raw=true)

Staff View - Injuries:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_injury.png?raw=true)

Staff View - Compare:
![login](https://github.com/sfrechou/PlayerTrack/blob/main/dist/README_src/screen_compare.png?raw=true)


## Author

Cecilia Giudice 
[Github](https://github.com/ChechG)
