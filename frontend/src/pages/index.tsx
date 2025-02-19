import React, { useState } from "react";

export default function Home() {
    const [taskId, setTaskId] = useState("");

    const startTask = async () => {
        const response = await fetch(`/api/tasks/${taskId}`, { method: "POST" });
        const data = await response.json();
        alert(data.message);
    };

    return (
        <div>
            <h1>Code Fusion</h1>
            <input type="text" onChange={(e) => setTaskId(e.target.value)} placeholder="Task ID"/>
            <button onClick={startTask}>Start Task</button>
        </div>
    );
}
