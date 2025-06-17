window.onload = function () {
  const sendButton = document.getElementById("send-prompt");
  const promptInput = document.getElementById("prompt");
  const responseBox = document.getElementById("response-box");

  const chatName = "new_chat";

  sendButton.addEventListener("click", async function (event) {
    event.preventDefault();

    const prompt = promptInput.value.trim();
    if (!prompt) return;

    responseBox.innerHTML += `<p><strong>You:</strong> ${prompt}</p>`;

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, chatName })
      });

      const data = await res.json();
      responseBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
      promptInput.value = "";
      responseBox.scrollTop = responseBox.scrollHeight;
    } catch (err) {
      console.error("Fetch error:", err);
    }
  });
};