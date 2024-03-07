import "./App.css";
import { useEffect, useState } from "react";
import { Button } from "./components/ui/button";

function App() {
  const [sentence, setSentence] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);

  const handleStreamButtonClick = () => {
    setIsStreaming(true);
    const eventSource = new EventSource('http://127.0.0.1:8000/api/users/stream')

    eventSource.onmessage = function(event) {
      console.log("yesss",event.data);
      
      setSentence(prevSentence => prevSentence + event.data + " ");
    };
    eventSource.onerror = function() {
      eventSource.close();
  };

    return () => {
      eventSource.close();
      setIsStreaming(false)
    };
  };
  useEffect(() => {
    
  },[sentence])
  

  return (
    <>
      <div className="flex content-center items-center">
      <div className="flex row">
        {sentence}
      </div>
        <div>
        <Button onClick={() => handleStreamButtonClick()} disabled={isStreaming}>
        Start Streaming
      </Button>
        </div>
        
      </div>
    </>
  );
}

export default App;
