import { useState } from "react";

function UploadForm({ setSummary, setActions, setTranscript }) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (event) => {
    event.preventDefault();
    const file = event.target.fileInput.files[0];
    if (!file) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/process-audio/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      setSummary(data.summary);
      setActions(data.action_items);
      setTranscript(data.transcript);
    } catch (error) {
      console.error("Upload failed:", error);
    }

    setLoading(false);
  };

  return (
    <>
      <form
        onSubmit={handleUpload}
        className="bg-gray-800 p-6 rounded-2xl shadow-lg flex flex-col items-center gap-4"
      >
        <input
          type="file"
          name="fileInput"
          accept="audio/*"
          className="text-white"
        />

        <button
          type="submit"
          disabled={loading}
          className={`px-6 py-2 rounded-xl shadow-md transition ${
            loading
              ? "bg-gray-600 cursor-not-allowed"
              : "bg-blue-600 hover:bg-blue-700"
          }`}
        >
          {loading ? "Uploading..." : "Upload & Summarize"}
        </button>
      </form>

      {/* Full screen overlay loader */}
      {loading && (
        <div className="fixed inset-0 bg-black bg-opacity-80 flex flex-col items-center justify-center z-50">
          <div className="w-14 h-14 border-4 border-white border-t-transparent rounded-full animate-spin"></div>
          <p className="mt-4 text-white text-lg font-semibold">
            Processing your audio...
          </p>
        </div>
      )}
    </>
  );
}

export default UploadForm;
