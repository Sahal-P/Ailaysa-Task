import { Avatar } from "@mui/material";
import "./App.css";
import { Blurhash } from "react-blurhash";
import { useEffect, useState } from "react";

function App() {
  const [sentence, setSentence] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);

  const handleStreamButtonClick = () => {
    setIsStreaming(true);
    const eventSource = new EventSource('http://127.0.0.1:8000/api/users/stream')

    eventSource.onmessage = function(event) {
      console.log("yesss",event.data);
      
      setSentence(prevSentence => prevSentence + event.data);
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
      <div className="rounded-full inline-block" style={{ overflow: 'hidden' }}>
        <Blurhash
          hash="LEHV6nWB2yk8pyo0adR*.7kCMdnj"
          width={156}
          height={156}
          resolutionX={32}
          resolutionY={32}
          punch={1}
        />
        </div>
        <Avatar
          alt="Remy Sharp"
          src="https://hips.hearstapps.com/digitalspyuk.cdnds.net/17/05/1486135181-avatar.jpg?crop=0.564xw:1.00xh;0.436xw,0&resize=1200:*"
          sx={{ width: 156, height: 156 }}
        />
        {sentence}
        <button onClick={() => handleStreamButtonClick()} disabled={isStreaming}>
        Start Streaming
      </button>
      </div>
    </>
  );
}

export default App;
