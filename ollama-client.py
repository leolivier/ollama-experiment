import ollama
import gradio as gr

MODEL = 'tinyllama'
# Sample inputs for the function as a list of strings; 
# if provided, appear below the chatbot and can be clicked to populate the chatbot input.
EXAMPLES= ['Why is the sky blue?', 'Tell me a joke', 'Generate a Python script to play snake'];

def gr_chat (message, history):
    """chat function for gradio. 
    From gradio documentation, parameters are:
    message: a str representing the user’s input.
    history: a list of list representing the conversations up until that point. 
      Each inner list consists of two str representing a pair: [user input, bot response]. 
    """
    # Initialize an empty list to store the conversation history
    messages = []

    # Iterate over the conversation history
    for msg in history:
      # Unpack the input and output from each message in the history
      input, output = msg

      # Append the user's input to the messages list
      messages.append({'role': 'user', 'content': input})

      # Append the assistant's output to the messages list
      messages.append({'role': 'assistant', 'content': output})

    # Append the current user message to the messages list
    messages.append({'role': 'user', 'content': message})

    # Print the list of messages for debugging purposes
    print(f"messages:{messages}")
    # Chat with a model using a specific model and prompt

    # Use the chat function of the Ollama library to get a response from the model
    # The 'stream' parameter set to True means the response will be streamed back as it's being generated
    response = ollama.chat(model=MODEL, messages=messages, stream=True) 

    # Initialize a variable to store the partial response
    partial_message = ""
    # Iterate over the chunks in the response stream
    for chunk in response:
      # Only the last chunk contains a True 'done' key 
      if chunk['done'] == True: break

      # Append the content of the current chunk to the partial message
      partial_message += chunk['message']['content']

      # Yield the partial message back to gradio so it can print the chunk
      yield partial_message

def main():
    gr.ChatInterface(
        fn=gr_chat,
        title="Chat with a Language Model",
        description="Enter your message  and the model will respond.",
        examples=EXAMPLES,
        cache_examples=(EXAMPLES!=None)
    ).launch()

if __name__ == "__main__":
    main()
