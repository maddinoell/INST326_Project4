class Note():
    def __init__(self, note_dict, created_at=None):
        self.title = note_dict["title"]
        self.text = note_dict["text"]
        self.author = note_dict["author"]
        self.links = note_dict["links"]
        self.tags = note_dict["tags"]
        if "code_text" in note_dict:
            self.code_text = note_dict["code_text"]
        if created_at:
            self.created_at = created_at
        else:
            self.created_at = datetime.datetime.now()
        self.last_edited = None


