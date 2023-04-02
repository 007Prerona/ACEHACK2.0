const audioContext = new AudioContext();
const audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
const audioSource = audioContext.createMediaStreamSource(audioStream);

const audioRecorder = new MediaRecorder(audioStream);
const audioChunks = [];
audioRecorder.addEventListener('dataavailable', (event) => {
  audioChunks.push(event.data);
});
audioRecorder.addEventListener('stop', () => {
  const audioBlob = new Blob(audioChunks);
  const audioUrl = URL.createObjectURL(audioBlob);
  transcribeAudio(audioBlob); // Call speech recognition function
});

audioRecorder.start();