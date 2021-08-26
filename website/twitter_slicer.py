class SliceMode:
    def __init__(self, text_list, with_counter):
        self.text_list = text_list
        self.with_counter = with_counter
        self.tweets = []


    def limit(self):
        """Slice text to fit tweet character limit"""

        # By limit with counter
        if self.with_counter:
            count = 0
            for text in self.text_list:
                while text:  # While text is not empty
                    count += 1
                    self.tweets.append(f"{text[:272]} ({count}/")  # Append the first 272 chars and add current count
                    text = text[272:]  # Replace var text with the remaining text
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Limit without counter
        else:
            for text in self.text_list:
                while text:  # While text is not empty
                    self.tweets.append(text[:280])  # Append the first 280 chars
                    text = text[280:]  # Replace var text with the remaining text

        return self.tweets


    def space(self):
        """Slice text in whitespace before tweet limit"""

        # By Space with counter
        if self.with_counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:  # While text is longer than limit
                    for index in range(271, -1, -1):  # Start at index 271, loop backwards, and find nearest whitespace
                        if text[index].isspace():
                            count += 1
                            self.tweets.append(f"{text[:index]} ({count}/")  # Append text from start to index and add current count
                            text = text[index+1:]  # Replace var text with remaining text after whitespace
                            break
                    else:  # Slice by limit if no whitespace is found
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:  # Append remaining text
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Space without counter
        else:
            for text in self.text_list:
                while len(text) > 280:  # While text is longer than limit
                    for index in range(279, -1, -1):  # Start at index 279, loop backwards, and find nearest whitespace
                        if text[index].isspace():
                            self.tweets.append(text[:index])  # Append text from start to index
                            text = text[index+1:]  # Replace var text with remaining text after whitespace
                            break
                    else:  # Slice by limit if no whitespace is found
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:  # Append remaining text
                    self.tweets.append(text)

        return self.tweets


    def punct(self):
        """Slice text in punctuation marks before tweet limit"""
        punct_marks = ".?!"

        # By Punctuation with counter
        if self.with_counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:  # While text is longer than limit
                    for index in range(271, -1, -1):  # Start at index 271, loop backwards, and find nearest punct mark
                        if text[index] in punct_marks:
                            count += 1
                            self.tweets.append(f"{text[:index+1]} ({count}/")  # Append text from start to index and add current count
                            text = text[index+2:]  # Replace var text with remaining text after punct mark
                            break
                    else:  # Slice by limit if no punct mark is found
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:  # Append remaining text
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Punctuation without counter
        else:
            for text in self.text_list:
                while len(text) > 280:  # While text is longer than limit
                    for index in range(279, -1, -1):  # Start at index 279, loop backwards, and find nearest punct mark
                        if text[index] in punct_marks:
                            self.tweets.append(text[:index+1])  # Append text from start to index
                            text = text[index+2:]  # Replace var text with remaining text after punct mark
                            break
                    else:  # Slice by limit if no punct mark is found
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:  # Append remaining text
                    self.tweets.append(text)

        return self.tweets


    @staticmethod
    def indicated(text, sep):
        """Slice text in indicated separators"""
        if sep == "":
            return [text]
        else:
            text_list = []
            while text:  # While text is not empty
                for index in range(len(text)):  # Search for indicated separator throughout text
                    if text[index:index+len(sep)] == sep:
                        text_list.append(text[:index])  # Append from start to index
                        text = text[index+len(sep):]  # Replace var text with the remaining text
                        break
                else:  # Append whole text if no separators found
                    text_list.append(text)
                    text = None  # Break out of while loop
            text_list = list(filter(None, text_list))  # Remove empty strings
            return text_list