import google.generativeai as genai
API_KEY="AIzaSyDZDqHb-NhymSj0dUEWhO5iwOCwQB9b-4g"
genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-2.5-pro")
chat=model.start_chat()



while True:
    user_input=input("You: ")
    response=chat.send_message(user_input)
    print("Aditya's ai:",response.text)
