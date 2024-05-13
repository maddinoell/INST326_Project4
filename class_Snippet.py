import tkinter as tk


class Snippet(tk.Toplevel):
    def __init__(self, master, snippet):
        super().__init__(master)
        self.snippet = snippet

        # code text field
        code_label = tk.Label(self, bg='light gray', text='Code Text:')
        self.code_text = tk.Text(self, height=5, width=60)

        code_label.grid(row=1, column=0, padx=2, pady=2, sticky='E')
        self.code_text.grid(row=1, column=1, padx=10, pady=2, sticky='W')

        # if viewing an existing snippet, keeps the existed text there
        if self.snippet:
            self.code_text.insert("1.0", self.snippet.code_text)

        # submit button
        save_edit_button = tk.Button(self, text='Save Edit', command=self.save_edit)
        save_edit_button.grid(row=2, column=1, padx=10, pady=10, sticky='W')

    def save_edit(self):
        if self.snippet:
            self.snippet.code_text = self.code_text.get("1.0", "end-1c")
        else:
            self.master.code_text.set(self.code_text.get("1.0", "end-1c"))
        self.destroy()


