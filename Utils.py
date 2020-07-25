class Support:

    def __init__(self) -> None:
        self.word_to_replace = {"  ": " ",
                                " ,": ","}
        self.str_format = "{0}: {1}"

    def replace_all(self, str_to_replace: str) -> str:
        for k, v in self.word_to_replace.items():
            str_to_replace = str_to_replace.replace(k, v)
        return str_to_replace

    def make_message_from_list(self, top_text: str, messages: list, bottom_text: str = None) -> str:
        text = top_text + \
               "\n" + \
               "\n".join([self.str_format.format(i[0], i[1]) for i in messages])

        if bottom_text:
            text = text + \
                   "\n" * 2 + \
                   bottom_text
        return text

    def make_message_from_dict(self, top_text: str, messages: dict, bottom_text: str = None) -> str:
        text = top_text + \
               "\n" + \
               "\n".join([self.str_format.format(k, v) for k, v in messages.items()])

        if bottom_text:
            text = text + \
                   "\n" * 2 + \
                   bottom_text
        return text
