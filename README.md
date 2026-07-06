class TextEditor:
    def __init__(self, initial_text=""):
        # Represents the current state of the document
        self.document = initial_text
        # Stack to hold past states for undoing
        self.undo_stack = []
        # Stack to hold undone states for redoing
        self.redo_stack = []

    def make_change(self, new_text):
        """Applies a new change to the document."""
        # Save current state to undo stack before changing
        self.undo_stack.append(self.document)
        self.document = new_text
        # A new action clears the redo history
        self.redo_stack.clear()
        print(f"📝 Changed text to: \"{self.document}\"")

    def undo(self):
        """Reverts the most recent change."""
        if not self.undo_stack:
            print("⚠️ Nothing to undo!")
            return
        
        # Move current state to redo stack
        self.redo_stack.append(self.document)
        # Pop the last state from undo stack and make it current
        self.document = self.undo_stack.pop()
        self.display_state()

    def redo(self):
        """Reapplies the most recently undone action."""
        if not self.redo_stack:
            print("⚠️ Nothing to redo!")
            return
        
        # Move current state to undo stack
        self.undo_stack.append(self.document)
        # Pop the last state from redo stack and make it current
        self.document = self.redo_stack.pop()
        self.display_state()

    def display_state(self):
        """Shows the current state of the document."""
        print(f"📄 Current Document State: \"{self.document}\"")


# --- Demonstration Workflow ---
editor = TextEditor("Hello")

editor.make_change("Hello World")
editor.make_change("Hello World!")

editor.undo()  # Reverts to "Hello World"
editor.undo()  # Reverts to "Hello"
editor.redo()  # Reapplies "Hello World"

editor.make_change("Hello World? (New Change)") 
editor.redo()  # Will trigger "Nothing to redo" because redo stack cleared
