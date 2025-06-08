import ollama
from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__, static_folder='static', static_url_path='/')

# Global context
context = "We will play a RPG(role play game).In this game will be sections." \
"There will be 4 options at the end of each section, they will be 1 and 2 and 3 and 4." \
"The players or player will make choice for each section." \
"If the user has made a choice that does not exist, warn them and make them choose again." \
"Make the chapter of stories long" \
"You will be Narrator for the game. The topic and other point will come at second prompt. Wait for them." \
"If second prompt doesn't give information you will create the story line on your own."

# Memory system - keeps last 30 interactions (60 messages total: 30 user + 30 assistant)
conversation_memory = deque(maxlen=60)  # 30 pairs of user/assistant messages
MEMORY_LIMIT = 30  # Number of user prompts to remember

@app.route('/api/response', methods=['POST'])
def handle_prompt():
    global conversation_memory
    try:
        data = request.json
        question = data.get("prompt", "")

        # Build messages with memory
        messages = [
            {"role": "system", "content": context}
        ]
        
        # Add conversation history from memory
        messages.extend(list(conversation_memory))
        
        # Add current user message
        messages.append({"role": "user", "content": question})

        # Get response from LLaMA
        result = ollama.chat(model="llama3.1", messages=messages)
        answer = result['message']['content']

        # Add current exchange to memory
        conversation_memory.append({"role": "user", "content": question})
        conversation_memory.append({"role": "assistant", "content": answer})

        # Debug: Print memory status
        print(f"Memory status: {len(conversation_memory)//2} conversations stored (max: {MEMORY_LIMIT})")

        return jsonify({"response": answer, "status": "success"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route('/api/memory/status', methods=['GET'])
def memory_status():
    """Endpoint to check memory status"""
    return jsonify({
        "conversations_stored": len(conversation_memory) // 2,
        "max_conversations": MEMORY_LIMIT,
        "total_messages": len(conversation_memory),
        "status": "success"
    })

@app.route('/api/memory/clear', methods=['POST'])
def clear_memory():
    """Endpoint to clear conversation memory"""
    global conversation_memory
    conversation_memory.clear()
    return jsonify({
        "message": "Conversation memory cleared",
        "status": "success"
    })

@app.route('/api/memory/export', methods=['GET'])
def export_memory():
    """Endpoint to export conversation history"""
    conversations = []
    for i in range(0, len(conversation_memory), 2):
        if i + 1 < len(conversation_memory):
            conversations.append({
                "user": conversation_memory[i]["content"],
                "assistant": conversation_memory[i + 1]["content"]
            })
    
    return jsonify({
        "conversations": conversations,
        "total_conversations": len(conversations),
        "status": "success"
    })

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)