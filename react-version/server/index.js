const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express()
const mysql = require('mysql')

const db = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'todo_db',
});

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api/get", (req, res) => {
    const sqlSelect = "SELECT * FROM lists";
    db.query(sqlSelect, (err, result) => {
        res.send(result);
    });
});

app.post("/api/insert", (req, res) => {

    const new_task = req.body.new_task;
    const sel_folder = req.body.sel_folder;

    const sqlInsert = "INSERT INTO lists (todo) VALUES (?)";
    db.query(sqlInsert, new_task, (err, result) => {
        console.log(err);
    });
});

app.delete('/api/delete/:id_task', (req, res) => {
    const name = req.params.id_task;
    const sqlDelete = "DELETE FROM lists WHERE id=?";
    db.query(sqlDelete, name, (err, result) => {
        if (err) console.log(err);
    });
})

app.put('/api/update', (req, res) => {
    const id_task = req.body.upd_task;
    const name = req.body.task;
    const sqlUpdate = "UPDATE lists SET todo = ? WHERE id = ?";
    db.query(sqlUpdate, [name, id_task], (err, result) => {
        if (err) console.log(err);
    });
})

app.listen(3001, () => {
    console.log("running on port 3001");
})