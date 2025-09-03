function SummaryCard({ summary, actions, transcript }) {
  return (
    <div className="bg-gray-800 p-6 rounded-2xl shadow-lg mt-6">
      <h2 className="text-2xl font-bold mb-4 text-blue-400">Meeting Summary</h2>
      <p className="mb-4">{summary}</p>

      <h3 className="text-xl font-semibold text-green-400 mb-2">
        Action Items
      </h3>
      {actions.length > 0 ? (
        <ul className="list-disc list-inside mb-4">
          {actions.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      ) : (
        <p className="mb-4">No action items found.</p>
      )}

      <h3 className="text-xl font-semibold text-purple-400 mb-2">Transcript</h3>
      <p className="whitespace-pre-wrap">{transcript}</p>
    </div>
  );
}

export default SummaryCard;
