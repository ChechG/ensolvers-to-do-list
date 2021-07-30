# To-Do list APP
## React version

This is a simple web application that allows you to create to-do items and folders to
group them. The development was divided in two phases:
- Phase 1: to-do item creation

## Description

With this app you can create your tasks, whatever they are, and those will be stored in a local database. Every time you add a new task. You can add, update or delete tasks as you want. Each task can be checked so you can follow your progress through the day!

## Features
* Add, update, delete tasks.
* Check every finished task.
* Tasks will be stored in a database for later use.
* Single-page app.

## Getting Started

### Dependencies

In order to download it and run it, you will need:
* Program: MySQL Workbench
    [this](https://dev.mysql.com/downloads/workbench/)
    Once Workbench is downloaded and installed:
        - File > Run SQL Script > (select dump.sql)
        - Query > Execute (All or selection)
        - In Schemas section, refresh
    You've got now your database configured.

* Terminal 1
You need npm previously installed.
[this](https://nodejs.org/en/)
```
$ cd /react-version/client
$ npm install express body-parser mysql nodemon cors
$ npm install
$ npm i axios
$ npm start
```

* Terminal 2
```
$ cd /react-version/server
$ npm run devStart
```

In your default browser refresh so that the database is updated.

### Installing

* This To-Di List APP can be downloaded from [this](https://github.com/ChechG/ensolvers-to-do-list.git) repo.
* The database should be populated in order for results to be visible and the application to run as it should so you need to run the script as it follows:
```
$ ./open_todo_list
```
* Open your browser of choice (I recommend [Google Chrome](https://www.google.com/intl/es-419/chrome/) for now) and type `http://localhost:5000/`
* Enjoy creating new lists!

## Database

One of the most crucial parts of the overall performance of the app is the database mapping implemented. To better understand and start using the app, a dump.sql file is used to populate the database. Once you get the hang of it, the user can delete the default tasks.

Use your root password to dump the dump file in the mysql database (MySQL Workbench).

## Author

Cecilia Giudice 
[Github](https://github.com/ChechG)
