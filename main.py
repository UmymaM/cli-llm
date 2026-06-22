from llm_client import call_llm

while True:
    user_input=input("You:")
    if user_input.lower() in ["exit","quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response=call_llm(user_input)
    print(f"Assistant: {response}")
    