#!/usr/bin/python3
""" Define a function called text_indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        Text: input text

    Raises:
          TypeError: if text not srting
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    char_ = ['.', '?', ':']

    new_text = []
    line = ''

    for c in text:
        line = line + c
        if c in char_:
            new_text.append(line.strip())
            new_text.append('')
            line = ''

    if line:
        new_text.append(line.strip())

    for line in new_text:
        print(line)
