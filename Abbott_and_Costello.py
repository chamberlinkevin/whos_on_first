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

