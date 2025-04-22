import { useState } from "react";
import axios from "axios";
import "./App.css";
function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("jd", jd);

    const res = await axios.post("http://localhost:5000/upload", formData);
    setResult(res.data);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Resume-JD Matcher</h1>

      <input type="file" onChange={(e) => setResume(e.target.files[0])} />
      <input type="file" onChange={(e) => setJd(e.target.files[0])} />
      <button onClick={handleUpload} className="mt-2 bg-blue-600 text-white px-4 py-2 rounded">
        Check Match
      </button>

      {result && (
        <div className="mt-4 p-4 border rounded bg-gray-50">
          <h2 className="text-xl font-semibold">Result</h2>
          <p><strong>Match Score:</strong> {result.score}%</p>
          <p className="mt-2 whitespace-pre-line">{result.report}</p>
        </div>
      )}
    </div>
  );
}

export default App;
