chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'automateMessage') {
      chrome.scripting.executeScript({
        target: { tabId: sender.tab.id },
        func: (msg) => {
          const inputBox = document.querySelector('input[type="text"]');
          const sendButton = document.querySelector('button');
          if (inputBox && sendButton) {
            inputBox.value = msg;
            sendButton.click();
          } else {
            console.error('Input box or send button not found.');
          }
        },
        args: [message.payload],
      });
    }
  });
// This code listens for messages from the popup and executes the script in the context of the current tab.   d