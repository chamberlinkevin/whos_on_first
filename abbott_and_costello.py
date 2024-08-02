class WhosOnFirstChatbot:
    """
    Module for the Who's on First? Chatbot. 
    """
    def __init__(self):
        responses = {
            "Who's on first?": "That's right.",
            "What's on second?": "Yes.",
            "I Don't Know's on third?": "Naturally.",
            "Who's on first": "That's right.",
            "What's on second": "Yes.",
            "I Don't Know's on third": "Naturally.",
            "Who's on first base?": "That's right.",
            "What's on second base?": "Yes.",
            "I Don't Know's on third base?": "Naturally.",
            "Who's playing first?": "That's right.",
            "What's playing second?": "Yes.",
            "I Don't Know's playing third?": "Naturally.",
        }
        # Convert all keys in the responses dictionary to lowercase
        self.responses = {k.lower(): v for k, v in responses.items()}
    
    def get_response(self, user_input):
        """
        Method for returning response to user depending on their input
        """
        # Convert user input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        return self.responses.get(user_input_lower, "I don't know about that.")

