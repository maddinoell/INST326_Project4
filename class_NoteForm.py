import tkinter as tk


class NoteForm(tk.Toplevel):
    def __init__(self, master, notebook, note):  # initialize the new object
        super().__init__(master)  # initialize it as a toplevel window
        self.notebook = notebook
        self.current_note = note

        # title
        title_label = tk.Label(self, bg='white', text='Note Title:')
        self.note_title = tk.Entry(self, width=80)

        title_label.grid(row=0, column=0, padx=2, pady=2, sticky='E')
        self.note_title.grid(row=0, column=1, padx=10, pady=2, sticky='W')

        # text
        text_label = tk.Label(self, bg='white', text='Note Text:')
        self.note_text = tk.Text(self, height=5, width=60)

        text_label.grid(row=1, column=0, padx=2, pady=2, sticky='E')
        self.note_text.grid(row=1, column=1, padx=10, pady=2, sticky='W')


        # code text
        self.code_text = tk.StringVar()

        code_label = tk.Label(self, bg='white', text='Code Text:')
        self.code_entry = tk.Entry(self, textvariable=self.code_text, width=80)
        self.code_text_editable = False

        code_label.grid(row=2, column=0, padx=2, pady=2, sticky='E')
        self.code_entry.grid(row=2, column=1, padx=10, pady=10, sticky='W')

        # edit code button
        edit_code_button = tk.Button(self, text='Edit Code', command=self.edit_code)
        edit_code_button.grid(row=3, column=0, padx=10, pady=10, sticky='W')

        # save edit button
        save_edit_button = tk.Button(self, text='Save Edit', command=self.save_edit)
        save_edit_button.grid(row=3, column=1, padx=10, pady=10, sticky='W')

        # author
        author_label = tk.Label(self, bg='white', text='author:')
        self.note_author = tk.Entry(self, width=80)

        author_label.grid(row=4, column=0, padx=2, pady=2, sticky='E')
        self.note_author.grid(row=4, column=1, padx=10, pady=10, sticky='W')

        # links
        links_label = tk.Label(self, bg='white', text='Note Links:')
        self.note_links = tk.Entry(self, width=80)

        links_label.grid(row=5, column=0, padx=2, pady=2, sticky='E')
        self.note_links.grid(row=5, column=1, padx=10, pady=10, sticky='W')

        # tags
        tags_label = tk.Label(self, bg='white', text='Note Tags:')
        self.note_tags = tk.Entry(self, width=80)

        tags_label.grid(row=6, column=0, padx=2, pady=2, sticky='E')
        self.note_tags.grid(row=6, column=1, padx=10, pady=2, sticky='W')

        # submit button
        submit_button = tk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky='W')

        # created_at label
        created_at_label = tk.Label(self, bg='white', text='Created At:')
        self.created_at_display = tk.Label(self, bg='white')

        created_at_label.grid(row=8, column=0, padx=2, pady=2, sticky='E')
        self.created_at_display.grid(row=8, column=1, padx=10, pady=2, sticky='W')

        # last_edited label
        last_edited_label = tk.Label(self, bg='white', text='Last Edited:')
        self.last_edited_display = tk.Label(self, bg='white')

        last_edited_label.grid(row=9, column=0, padx=2, pady=2, sticky='E')
        self.last_edited_display.grid(row=9, column=1, padx=10, pady=2, sticky='W')

        #search notes
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=0, column=4, padx=0, pady=0)

        search_button = tk.Button(self, text='Search', command=self.search_notes, bg='lightgray', fg='black', padx=5, pady=2)
        search_button.grid(row=0, column=5, padx=5, pady=0)


        self.search_results_text = tk.Text(self, height=5, width=20, wrap='word')
        self.search_results_text.grid(row=1, column=2, columnspan=6, padx=0, pady=0, sticky='w')  

        
        # scrollbar
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.search_results_text.yview)
        scrollbar.grid(row=1, column=6, sticky='ns')  
        self.search_results_text.config(yscrollcommand=scrollbar.set)

        





        # if viewing an existing note, remove submit button, disable inputs, and displays created_at and last_edited
        if note is None:
            self.last_edited_display.config(text='')  
        else:
            self.note_title.insert(0, note.title)
            self.note_text.insert("1.0", note.text)
            self.code_entry.insert(0, note.code_text)
            self.note_author.insert(0, note.author)
            self.note_links.insert(0, note.links)
            self.note_tags.insert(0, note.tags)
            self.created_at_display.config(text=note.created_at.strftime("%m/%d/%y %H:%M"))
            if note.last_edited:
                self.last_edited_display.config(text=note.last_edited.strftime("%m/%d/%y %H:%M"))
            else:
                self.last_edited_display.config(text='')

    def edit_code(self):
        if not self.code_text_editable:
            self.code_entry.config(state=tk.NORMAL)
            self.code_text_editable = True
        else:
            self.code_entry.config(state=tk.DISABLED)
            self.code_text_editable = False

    def save_edit(self):
        if self.current_note:
            self.current_note.code_text = self.code_entry.get()
            self.current_note.last_edited = datetime.datetime.now()
            self.last_edited_display.config(text=self.current_note.last_edited.strftime("%m/%d/%y %H:%M"))
            self.code_entry.config(state=tk.DISABLED)
            self.code_text_editable = False

    def submit(self):
        new_note_dict = {'title': self.note_title.get(),
                         'text': self.note_text.get("1.0", "end-1c"),
                         'code_text': self.code_entry.get(),
                         'author': self.note_author.get(),
                         'links': self.note_links.get(),
                         'tags': self.note_tags.get()}
        if self.current_note:
            new_note = Note(new_note_dict, self.current_note.created_at)
        else:
            new_note = Note(new_note_dict)

        index = self.notebook.index(self.current_note) if self.current_note else None
        if index is not None:
            self.notebook[index] = new_note
        else:
            self.notebook.append(new_note)

        self.destroy()
        self.master.refresh_notes_list()
        return None

    def search_notes(self):
        search = self.search_entry.get().lower()
        results = []

        for note in self.notebook:
            if search in note.title.lower() or search in note.text.lower():
                results.append(note)

        self.display_search_results(results)

    def display_search_results(self, results):
        self.search_results_text.delete(1.0, tk.END)  

        if not results:
            self.search_results_text.insert(tk.END, "No matching notes found.")
        else:
            for note in results:
                self.search_results_text.insert(tk.END, f"Title: {note.title}\n")
                self.search_results_text.insert(tk.END, f"Text: {note.text}\n\n")


        

    


