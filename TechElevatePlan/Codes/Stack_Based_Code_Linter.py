class Linter:
    def init(self):
        # We use a simple list to serve as our stack:
        self.stack = []
    def lint(self, text):
    # We start a loop which reads each character in our text:
        for char in text:
            # If the character is an opening brace:
            if self.is_opening_brace(char):
                # We push it onto the stack:
                self.stack.append(char)
            # If the character is a closing brace:
            elif self.is_closing_brace(char):
                # Pop from stack:
                popped_opening_brace = self.stack.pop() if len(self.stack) > 0 else None
                # If the stack was empty, so what we popped was None,
                # it means that an opening brace is missing:
                if popped_opening_brace is None:
                    return f"{char} doesn't have opening brace"
                # If the popped opening brace doesn't match the
                # current closing brace, we produce an error:
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"{char} has mismatched opening brace"
        # If we get to the end of line, and the stack isn't empty:
        if self.stack:
            # It means we have an opening brace without a
            # corresponding closing brace, so we produce an error:
            return f"{self.stack[-1]} does not have closing brace"
        # Return True if line has no errors:
        return True

    def is_opening_brace(self, char):
        return char in ["(", "[", "{"]

    def is_closing_brace(self, char):
        return char in [")", "]", "}"]

    def is_not_a_match(self, opening_brace, closing_brace):
        return closing_brace != {"(": ")", "[": "]", "{": "}"}[opening_brace]
