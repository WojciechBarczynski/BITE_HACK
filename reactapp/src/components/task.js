import React, { useState } from 'react';
import taskService from '../services/taskService';
import '../style/task.css';
const TaskComponent = () => {

    const [currentTask, setCurrentTask] = useState(null);
    const [taskImage, setTaskImage] = useState("");

    const generate = () => {
        taskService.generate().then((res) => {
            setCurrentTask(res.data.taskid)
            setTaskImage(res.data.taskurl)
        })
    }

    if(currentTask == null) {
        return (
            <div className='task'>
                <h2>Aktualnie nie rozwiązujesz żadnego zadania!</h2>
                <button onClick={generate} className="niceButton">Kliknij tutaj aby rozpocząć...</button>
            </div>
        )
    }

    return (
        <div className='task'>
            <h2>Rozwiązujesz zadanie: #{currentTask}</h2>
            <img className="taskImage" src={taskImage} alt="Zdjęcie nie wczytało się poprawnie..." />
            <input placeholder="Wpisz odpowiedź..." className="taskInput" type="text" /><br />
            <button onClick={generate} className="niceButton" style={{marginTop: "10px"}}>Wyślij rozwiązanie</button>
        </div>
    );
};

export default TaskComponent;