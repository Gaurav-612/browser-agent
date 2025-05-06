document.getElementById('send-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) return;
  
    addMessageToChat(userInput, 'user-message');
    document.getElementById('user-input').value = '';
  
    try {
      const res = await fetch('http://localhost:8000/parse-command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: userInput }),
      });
  
      const data = await res.json();
      const botMessage = data.message;
      addMessageToChat(botMessage, 'bot-message');
  
      if (data.action === 'forecast' && data.raw_message) {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
          chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            func: (text) => {
              const textarea = document.getElementById('forecast_input_message_text');
              if (textarea) {
                textarea.value = text;
                textarea.dispatchEvent(new Event('input', { bubbles: true }));
              }
              const button = document.getElementById('forecast_input_message_submit_button');
              if (button) button.click();
            },
            args: [data.raw_message],
          });
        });
      }
    } catch (error) {
      console.error('Error communicating with backend:', error);
      addMessageToChat('Error: Unable to process your request.', 'bot-message');
    }
  });
  
  function addMessageToChat(message, className) {
    const chatContainer = document.getElementById('chat-container');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = `message ${className}`;
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }
  