document.addEventListener('DOMContentLoaded', () => {
  const socket = new WebSocket('ws://' + window.location.host + '/ws/publish/');

  document.querySelector(".publish").addEventListener("click", () => {
      const topic = document.querySelector("#topic").value.trim();
      const message = document.querySelector("#message").value.trim();

      if (topic && message) {
          socket.send(JSON.stringify({
              'topic': topic,
              'message': message
          }));
      } else {
          alert("Please enter both topic and message.");
      }
  });
});
