document.addEventListener('DOMContentLoaded', () => {
  const socket = new WebSocket('ws://' + window.location.host + '/ws/subscribe/');

  socket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      const messageTextArea = document.querySelector("#message");
      messageTextArea.value += `Received Message: ${data.message} On topic: ${data.topic}\r\n`;
  };

  document.querySelector("#subscribe").addEventListener("click", () => {
      const topic = document.querySelector("#topic").value.trim();
      if (topic) {
          socket.send(JSON.stringify({ 'topic': topic }));
          document.querySelector("#status").style.color = "green";
          document.querySelector("#status").value = "SUBSCRIBED";
      } else {
          alert("Please enter a topic.");
      }
  });

  document.querySelector("#unsubscribe").addEventListener("click", () => {
      const topic = document.querySelector("#topic").value.trim();
      if (topic) {
          socket.send(JSON.stringify({ 'topic': topic }));
          document.querySelector("#status").style.color = "red";
          document.querySelector("#status").value = "UNSUBSCRIBED";
      } else {
          alert("Please enter a topic.");
      }
  });
});

