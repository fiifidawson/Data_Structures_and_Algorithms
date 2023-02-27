class Linter {
    constructor() {
      // We use a simple array to serve as our stack:
      this.stack = [];
    }
  
    lint(text) {
      // We start a loop which reads each character in our text:
      for (let i = 0; i < text.length; i++) {
        const char = text.charAt(i);
  
        // If the character is an opening brace:
        if (this.is_opening_brace(char)) {
          // We push it onto the stack:
          this.stack.push(char);
        }
  
        // If the character is a closing brace:
        else if (this.is_closing_brace(char)) {
          // Pop from stack:
          const popped_opening_brace = this.stack.pop();
  
          // If the stack was empty, so what we popped was undefined,
          // it means that an opening brace is missing:
          if (!popped_opening_brace) {
            return `${char} doesn't have opening brace`;
          }
  
          // If the popped opening brace doesn't match the
          // current closing brace, we produce an error:
          if (this.is_not_a_match(popped_opening_brace, char)) {
            return `${char} has mismatched opening brace`;
          }
        }
      }
  
      // If we get to the end of line, and the stack isn't empty:
      if (this.stack.length > 0) {
        // It means we have an opening brace without a
        // corresponding closing brace, so we produce an error:
        return `${this.stack[this.stack.length - 1]} does not have closing brace`;
      }
  
      // Return true if line has no errors:
      return true;
    }
  
    is_opening_brace(char) {
      return ["(", "[", "{"].includes(char);
    }
  
    is_closing_brace(char) {
      return [")", "]", "}"].includes(char);
    }
  
    is_not_a_match(opening_brace, closing_brace) {
      return closing_brace !== {"(": ")", "[": "]", "{": "}"}[opening_brace];
    }
  }
  