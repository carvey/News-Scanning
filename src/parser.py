

def valid_anchor(anchor):
    """
    Checks whether or not an anchor href is a valid rss link or not
    :param anchor: a beautiful soup anchor (a) Tag
    :return: bool
    """
    invalid_strings = ['.html', 'javascript', 'yahoo.com', 'money.cnn.com/services/rss/']
    href = anchor.get('href')
    if href:
        if 'rss' in href:
            for string in invalid_strings:
                if string in href:
                    return False

            return True
