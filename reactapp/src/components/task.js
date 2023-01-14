import React, { useState } from 'react';
import answerService from '../services/answerService';
import taskService from '../services/taskService';
import '../style/task.css';

const TaskComponent = (props) => {

    const [currentTask, setCurrentTask] = useState(null);
    const [taskImage, setTaskImage] = useState("");
    const [answer, setAnswer] = useState("");
    const [showingAnswer, setShowingAnswer] = useState(false);
    const [isCorrect, setIsCorrect] = useState(false);
    const [ranking, setRanking] = useState(0);

    const generate = () => {
        taskService.generate().then((res) => {
            setCurrentTask(res.data.taskid)
            setTaskImage(res.data.taskurl)
            setShowingAnswer(false)
        })
    }

    const handleAnswer = () => {
        answerService.answer(localStorage.getItem("userid"), currentTask, answer)
            .then(res => {
                props.fixStuff();
                setShowingAnswer(true);
                setTaskImage(res.data.link);
                setAnswer(res.data.answer);
                setIsCorrect(parseInt(res.data.result) == 0 ? false : true);
                setRanking(res.data.pointdelta);
            })
    }

    const getResultHeader = () => {
        if(isCorrect) return <h2>Twoje rozwiązanie jest poprawne! (Ranking +{ranking})</h2>
        else return <h2>Popełniłeś błąd (Ranking -{ranking*(-1)})</h2>
    }

    if(showingAnswer) {
        return (
            <div className='task'>
                {getResultHeader()}
                <img className="taskImage" src={taskImage} alt="Zdjęcie nie wczytało się poprawnie..." />
                Poprawna odpowiedź: <b>{answer}</b><br />
                <button onClick={generate} className="niceButton" style={{marginTop: "10px"}}>Przejdź do następnego zadania</button>
            </div>
        );
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
            <input placeholder="Wpisz odpowiedź..." className="taskInput" type="text" onChange={(e) => setAnswer(e.target.value)}/><br />
            <button onClick={handleAnswer} className="niceButton" style={{marginTop: "10px"}}>Wyślij rozwiązanie</button>
        </div>
    );
};

export default TaskComponent;