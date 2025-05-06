# Limbik Browser Agent: Chrome Extension

This folder contains the **Chat Automator** Chrome extension, which provides a chat-like interface for interacting with a backend API and automating tasks on web pages.

---

## **Folder Structure**

---

## **How It Works**

1. **Popup Interface**:
   - Provides a chat UI for user commands.
   - Sends commands to the backend API (`http://localhost:8000/parse-command`).
   - Displays responses and automates actions on the active webpage.

2. **Background Script**:
   - Listens for messages from the popup.
   - Executes scripts in the active browser tab to automate tasks.

3. **Content Script**:
   - Directly manipulates the DOM of the active webpage (if needed).

---

## **Setup Instructions**

1. Open Chrome and navigate to `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `chrome-extension` folder.

---

## **Key Files**

### **1. `manifest.json`**
Defines the extension's metadata and permissions:
- **Permissions**: `scripting`, `tabs`, `activeTab`.
- **Host Permissions**: Allows communication with the backend API.

### **2. `popup.html`**
HTML structure for the chat interface.

### **3. `popup.js`**
Handles user input, communicates with the backend, and automates browser actions.

### **4. `popup.css`**
Styles for the chat interface, including user and bot message formatting.

### **5. `background.js`**
Executes scripts in the active tab based on user commands.

---

## **Usage**

1. Open the extension by clicking its icon in the Chrome toolbar.
2. Type a command in the chat interface and click **Send**.
3. The extension communicates with the backend and automates tasks on the active webpage.

---

## **Example Command**

- **Forecast a Message**:
`forecast for this message: Hello world`
- The backend processes the command and returns a response.
- The extension automates input and submission on the active webpage.

---

## **Future Improvements**

- Add support for more commands.
- Improve error handling and user feedback.
- Enhance the chat interface with richer UI elements.