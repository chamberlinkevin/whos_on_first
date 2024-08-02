class WhosOnFirstChatbot:
    def __init__(self):
        self.responses = {
            "Who's on first?": "That's right.",
            "What's on second?": "Yes.",
            "I Don't Know's on third?": "Naturally.",
            "Who's on first": "That's right.",
            "What's on second": "Yes.",
            "I Don't Know's on third": "Naturally.",
            "Who's on first?": "That's right.",
            "What's on second?": "Yes.",
            "I Don't Know's on third?": "Naturally.",
            "Who's on first base?": "That's right.",
            "What's on second base?": "Yes.",
            "I Don't Know's on third base?": "Naturally.",
            "Who's playing first?": "That's right.",
            "What's playing second?": "Yes.",
            "I Don't Know's playing third?": "Naturally.",
        }
    
    def get_response(self, user_input):
        return self.responses.get(user_input, "I don't know about that.")

# Example usage:
bot = WhosOnFirstChatbot()

user_inputs = [
    "Who's on first?",
    "What's on second?",
    "I Don't Know's on third?",
    "Who's on first base?",
    "What's on second base?",
    "I Don't Know's on third base?",
    "Who's playing first?",
    "What's playing second?",
    "I Don't Know's playing third?",
    "Why?",
]

for user_input in user_inputs:
    print(f"User: {user_input}")
    print(f"Bot: {bot.get_response(user_input)}\n")
