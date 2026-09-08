def simple_chatbot(user_query):
    user_query = user_query.strip().lower()

    if user_query == "what is microsoft's total revenue in 2025?":
        return "Microsoft's total revenue in 2025 was $281,724 million."
    elif user_query == "how did tesla's net income change in 2025?":
        return "Tesla's net income decreased by approximately 46.1% in 2025."
    elif user_query == "what was apple's operating cash flow in 2025?":
        return "Apple's 2025 operating cash flow was $111,482 million."
    else:
        return "Sorry, I didn't understand that. Please ask one of the predefined financial questions."

user_query = input("Ask a financial question: ")
print(simple_chatbot(user_query))