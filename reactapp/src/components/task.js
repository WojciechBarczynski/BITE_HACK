import React from 'react';
import '../style/task.css';
const TaskComponent = () => {

    const [content, setContent] = React.useState("")
    return (
        <div className='task'>
            {content}
        </div>
    );
};

export default TaskComponent;