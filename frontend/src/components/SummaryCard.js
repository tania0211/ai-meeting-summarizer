function SummaryCard({ summary, actions, transcript }) {
  return (
    <div className="bg-gray-800 p-6 rounded-2xl shadow-lg mt-6 space-y-6">
      {/* Summary Section */}
      <div>
        <h2 className="text-xl font-semibold mb-2 text-blue-400">Summary</h2>
        <p className="text-gray-200">{summary}</p>
      </div>

      {/* Action Items Section */}
      {actions && actions.length > 0 && (
        <div>
          <h2 className="text-xl font-semibold mb-2 text-green-400">Action Items</h2>
          <ul className="list-disc pl-5 space-y-1 text-gray-200">
            {actions.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Transcript Section */}
      <div>
        <h2 className="text-xl font-semibold mb-2 text-yellow-400">Transcript</h2>
        <p className="text-gray-300 text-sm leading-relaxed">{transcript}</p>
      </div>
    </div>
  );
}

export default SummaryCard;
