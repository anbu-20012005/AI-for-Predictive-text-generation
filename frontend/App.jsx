function App() {
  const [inputText, setInputText] = React.useState('');
  const [prediction, setPrediction] = React.useState('');
  const [history, setHistory] = React.useState([]);

  // Handle input change
  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  // Handle prediction request
  const handlePredict = async () => {
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText }),
      });
      const data = await response.json();
      setPrediction(data.prediction);
      // Update history
      setHistory([...history, { input: inputText, prediction: data.prediction }]);
    } catch (error) {
      console.error('Error:', error);
      setPrediction('Error fetching prediction');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-4">AI Predictive Text</h1>
      <div className="mb-4">
        <input
          type="text"
          value={inputText}
          onChange={handleInputChange}
          placeholder="Enter text (e.g., The sun is)"
          className="w-full p-2 border rounded"
        />
        <button
          onClick={handlePredict}
          className="mt-2 bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          Predict
        </button>
      </div>
      {prediction && (
        <div className="mb-4">
          <h2 className="text-xl font-semibold">Prediction:</h2>
          <p>{prediction}</p>
        </div>
      )}
      <div>
        <h2 className="text-xl font-semibold">History:</h2>
        <ul className="list-disc pl-5">
          {history.map((item, index) => (
            <li key={index}>
              Input: {item.input} → Prediction: {item.prediction}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));