import React, { useState } from 'react';
import ReactPlayer from 'react-player';
import ytdl from 'ytdl-core';
import { saveAs } from 'file-saver';

const App = () => {
 const [url, setUrl] = useState('');
 const [audioUrl, setAudioUrl] = useState('');

 const downloadAudio = async () => {
    try {
      const info = await ytdl.getInfo(url);
      const audioFormats = ytdl.filterFormats(info.formats, 'audioonly');
      const audioFormat = ytdl.chooseFormat(audioFormats);

      if (audioFormat) {
        const audioStream = ytdl(url, { format: audioFormat });
        const blob = await new Promise((resolve, reject) => {
          const chunks = [];
          audioStream.on('data', chunk => chunks.push(chunk));
          audioStream.on('end', () => resolve(new Blob(chunks, { type: 'audio/mpeg' })));
          audioStream.on('error', reject);
        });
        saveAs(blob, `${info.videoDetails.title}.mp3`);
        setAudioUrl('');
      } else {
        throw new Error('No suitable audio format found');
      }
    } catch (error) {
      console.error('Error downloading audio:', error);
    }
 };

 return (
    <div>
      <input type="text" placeholder="Enter YouTube video URL" value={url} onChange={e => setUrl(e.target.value)} />
      <button onClick={downloadAudio}>Download as Audio</button>
      {audioUrl && (
        <ReactPlayer url={audioUrl} controls />
      )}
    </div>
 );
};

export default App;