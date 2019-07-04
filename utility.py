
def checkStr(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            continue
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
            continue
        elif ord(char) >= ord('0') and ord(char) <= ord('9'):
            continue
        elif char in ["!", "#", "$", "%", "&", "(", ")", "+", "-", ":",
                      ";", "<", "=", ".", ">", "?", "@", "[", "]", "^",
                      "_", "{", "}", "|", "~", ","] or ord(char) == 32:
            continue
        else:
            return "The channel name contains illegal character."
    if len(str) == 0:
        return "Please input the channel name."
    if len(str) > 64:
        return "The length of the channel name must be less than 64."
    return ""