import { useState } from "react";

function App() {
  const [video, setVideo] = useState(null);
  const [seconds, setSeconds] = useState(5);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!video) return alert("Select a video");

    const formData = new FormData();
    formData.append("video", video);
    formData.append("keep_seconds", seconds);

    setLoading(true);

    const response = await fetch("http://localhost:8000/trim", {
      method: "POST",
      body: formData,
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "trimmed.mp4";
    a.click();

    setLoading(false);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Simple Video Trimmer</h2>

      <input
        type="file"
        accept="video/*"
        onChange={(e) => setVideo(e.target.files[0])}
      />

      <br /><br />

      <label>Keep first (seconds): </label>
      <input
        type="number"
        value={seconds}
        onChange={(e) => setSeconds(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {loading ? "Processing..." : "Trim Video"}
      </button>
    </div>
  );
}

export default App;
