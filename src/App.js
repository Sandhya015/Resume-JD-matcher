import { useState } from "react";
import axios from "axios";

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [score, setScore] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("jd", jd);

    const res = await axios.post("http://localhost:5000/upload", formData);
    setScore(res.data.match_score);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Resume-JD Matcher</h1>
      <input type="file" onChange={(e) => setResume(e.target.files[0])} />
      <input type="file" onChange={(e) => setJd(e.target.files[0])} />
      <button onClick={handleUpload}>Check Match</button>
      {score !== null && <p>Match Score: {score}%</p>}
    </div>
  );
}

export default App;
