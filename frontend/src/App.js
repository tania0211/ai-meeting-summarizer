import Navbar from "./components/Navbar";
import UploadForm from "./components/UploadForm";
import SummaryCard from "./components/SummaryCard";
import { useState } from "react";

function App() {
  const [summary, setSummary] = useState("");
  const [actions, setActions] = useState([]);
  const [transcript, setTranscript] = useState("");

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Navbar />
      <div className="p-6 max-w-3xl mx-auto">
        {/* Pass state setters down to UploadForm */}
        <UploadForm
          setSummary={setSummary}
          setActions={setActions}
          setTranscript={setTranscript}
        />

        {/* Only render card when summary is available */}
        {summary && (
          <SummaryCard
            summary={summary}
            actions={actions}
            transcript={transcript}
          />
        )}
      </div>
    </div>
  );
}

export default App;
