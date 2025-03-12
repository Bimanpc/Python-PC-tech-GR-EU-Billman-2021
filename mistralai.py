class MistralChatAgent:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey"]
        self.farewells = ["bye", "goodbye", "see you"]

    def generate_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()

        # Check for greetings
        if user_input in self.greetings:
            return "Hello! How can I assist you today?"

        # Check for farewells
        elif user_input in self.farewells:
            return "Goodbye! Have a great day!"

        # Default response
        else:
            return "I'm here to help! What would you like to know?"

    def chat(self):
        print("Mistral Chat Agent: Hi there! Let's chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in self.farewells:
                print("Mistral Chat Agent:", self.generate_response(user_input))
                break
            response = self.generate_response(user_input)
            print("Mistral Chat Agent:", response)

if __name__ == "__main__":
    agent = MistralChatAgent()
    agent.chat()
