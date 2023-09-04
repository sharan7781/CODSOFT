import tkinter as tk

# Define chatbot rules
rules = {
    "What's the weather like today?": "The weather is sunny and warm.",
    "Will it rain tomorrow?": "Yes, there is a chance of rain tomorrow.",
    "How's the weather this weekend?": "The weather this weekend will be partly cloudy.",
    "Goodbye": "Goodbye! Have a great day."
}

def get_response(user_input):
    user_input = user_input.strip().lower()
    for pattern, response in rules.items():
        if pattern.lower() in user_input:
            return response
    return "I'm sorry, I don't understand that."

def send_message():
    user_input = entry.get()
    if user_input:
        response = get_response(user_input)
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, f"You: {user_input}\n")
        chat.insert(tk.END, f"ChatBot: {response}\n\n")
        chat.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple ChatBot")

chat = tk.Text(root, state=tk.DISABLED)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
