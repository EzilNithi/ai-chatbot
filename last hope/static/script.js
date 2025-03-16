function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    fetch(`/chatbot?query=${encodeURIComponent(userInput)}`)
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
}
