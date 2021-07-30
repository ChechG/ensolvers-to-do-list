import React, { useState, useEffect } from 'react';
import './App.css';
import Axios from 'axios';

function App() {
	const [new_task, setNewTask] = useState('');
	const [task_list, setTask_list] = useState([]);
	const [upd_task, setUpdate] = useState('');

	useEffect(() => {
		Axios.get('http://localhost:3001/api/get').then((response) => {
			setTask_list(response.data);
		});
	}, []);


	const submit_add = () => {
		Axios.post('http://localhost:3001/api/insert', {
			new_task: new_task,
		});

		setTask_list([
			...task_list,
			{ new_task: new_task},
		]);

		window.location.reload();
	};

	const delete_task = (id_task) => {
		Axios.delete(`http://localhost:3001/api/delete/${id_task}`);

		window.location.reload();
	}

	const update_task = (id_task) => {
		Axios.put('http://localhost:3001/api/update', {
			upd_task: id_task,
			task: upd_task,
		});
		setUpdate("");
		window.location.reload();
	}

  return (
    <div className="App">
        <h1>This is my To-Do List App</h1>
        <div className="add_task_section">
            <label><h2>Add new task</h2></label>
            <div className="input-group mb-3">
                <input type="text" className="form-control" id="new_task" name="new_task" onChange={(e) => {
					setNewTask(e.target.value);
				}}/>
            </div>
            <button onClick={submit_add} value="Save changes" id="save_new" className="btn btn-outline-success flota">Save task</button>
        </div>
		<div className="table_section">
			<h1>All my tasks</h1>
			<table className="display dataTable table" role="grid">
				<thead className="thead-dark">
                    <tr className="header">
						<th>Check</th>
						<th className="min_th">To_do</th>
						<th>#</th>
						<th>#</th>
						<th>#</th>
                    </tr>
                </thead>
				<tbody>
				{task_list.map((val) => {
						return (
						<tr>
							<td><input type="checkbox" /></td>
							<td>{val.todo}</td>
							<td><input type="text" onChange={(e) => {
								setUpdate(e.target.value)
							}} /></td>
							<td><button onClick={() => {update_task(val.id)}}>Update</button></td>
							<td><button onClick={() => {delete_task(val.id)}}>Delete</button></td>
						</tr>
						);
					})}
				</tbody>
			</table>
			
		</div>
    </div>
  );
}

export default App;
