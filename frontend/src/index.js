import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      const { data } = await axios.get('/api/tasks');
      setTasks(data);
    };
    fetchTasks();
  }, []);

  return (
    <div>
      <h1>Tasks</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.title}</li>
        ))}
      </ul>
    </div>
  );
}