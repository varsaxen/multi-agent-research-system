import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [logs, setLogs] = useState([]);
  const [finalResult, setFinalResult] = useState("");
  const [waitingApproval, setWaitingApproval] = useState(false);
  const [feedback, setFeedback] = useState("");
const [isLoading, setIsLoading] = useState(false);
  // ✅ Normal API
  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:8000/research", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query })
    });

    const data = await res.json();
    setResult(data);
  };

  // ✅ Streaming API (SSE)
  const startStream = () => {
    setLogs([]);
    setFinalResult("");
    setWaitingApproval(false);
    setFeedback("");
    setIsLoading(true);

    const evtSource = new EventSource(
      `http://127.0.0.1:8000/research/stream?query=${query}`
    );

    evtSource.onmessage = (event) => {
let clean = event.data.replace(/^data:\s*/, "").trim();

      // ✅ detect review
      if (clean.toLowerCase().includes("review")) {
setIsLoading(false);
        setLogs((prev) => {
          if (prev.includes("⏸️ Review required (awaiting approval)")) return prev;
          return [...prev, "⏸️ Review required (awaiting approval)"];
        });

        setWaitingApproval(true);
        evtSource.close();
        return;
      }

      setLogs((prev) => {
        if (prev.includes(clean)) return prev;
        return [...prev, clean];
      });
    };

    evtSource.onerror = () => {
      console.error("SSE error");
      evtSource.close();
    };
  };

  // ✅ Resume after approval
 const handleApprove = async () => {
  const res = await fetch("http://127.0.0.1:8000/research/resume", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      query,
      feedback
    })
  });

  const data = await res.json();

  setFinalResult(data.synthesis);
  setWaitingApproval(false);
setIsLoading(false);

  // ✅ Remove "awaiting approval" log
  setLogs((prev) =>
    prev.filter((log) => !log.includes("Review required"))
  );

  // ✅ Add completion message
  setLogs((prev) => [
    ...prev,
    "✅ Review approved — summary generated"
  ]);
};


  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>🚀 AI Research Agent (Live)</h1>

      {/* ✅ Input */}
      <input
        style={{ width: "300px", padding: "8px" }}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your research query..."
      />

      <br /><br />

      {/* ✅ Buttons */}
      <button onClick={handleSubmit}>Run Research</button>

<button onClick={startStream} style={{ marginLeft: "10px" }}>
  🌐 Stream Research
</button>

{isLoading && (
  <p style={{
    marginTop: "10px",
    color: "#555",
    fontStyle: "italic"
  }}>
    🔄 Agents working...
  </p>
)}
      {/* ✅ Timeline */}
      <div style={{
        marginTop: "20px",
        border: "1px solid #ccc",
        padding: "15px",
        backgroundColor: "#f5f7fa",
        borderRadius: "6px"
      }}>
        <h3>🧠 Agent Timeline</h3>
       {logs.map((log, i) => (
  <div
    key={i}
    style={{
      fontWeight: i === logs.length - 1 ? "bold" : "normal",
      color: i === logs.length - 1 ? "#2c7be5" : "#333",
      marginBottom: "6px"
    }}
  >
    • {log}
  </div>
))}
      </div>

      {/* ✅ HITL */}
      {waitingApproval && (
        <div style={{
          marginTop: "20px",
          padding: "10px",
          border: "1px solid orange",
          backgroundColor: "#fff8e1"
        }}>
          <h3>⚠️ Human Review Required</h3>

          <textarea
            style={{ width: "300px", height: "80px" }}
            placeholder="Enter feedback (optional)"
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
          />

          <br /><br />

          <button onClick={handleApprove}>
            ✅ Approve & Continue
          </button>
        </div>
      )}

      {/* ✅ FINAL RESULT */}
      {finalResult && (
        <div style={{
          marginTop: "20px",
          padding: "10px",
          border: "1px solid green",
          backgroundColor: "#e8f5e9"
        }}>
          <h2>✅ Streamed Summary</h2>
          <p>{finalResult}</p>
        </div>
      )}

      {/* ✅ Sub Questions */}
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Sub Questions</h2>

          <ul style={{
            listStylePosition: "inside",
            display: "inline-block",
            textAlign: "left",
            lineHeight: "1.8"
          }}>
            {result.sub_questions.map((q, i) => (
              <li key={i}>{q}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
