def getcolor(color): return "\033[38;5;%dm" % color
def getstyle(style): return "\033[%dm" % style
def setcolor(color): print(getcolor(color), end="")
def setstyle(style): print(getstyle(style), end="")
def resetcolor(): print("\033[0m", end="")

def format_string(*args, sep=" ", end="\033[0m"):
    text = str(sep).join([str(arg) for arg in args]) + str(end)
    formatted = ""
    i = 0
    while i < len(text):
        if text[i:i + 2] == "&&":
            formatted += "&"
            i += 1
        elif text[i] == "&" and set(text[i + 1:i + 3]).issubset("0123456789abcdef") and len(text[i + 1:i + 3]) == 2:
            formatted += f"\033[38;5;{str(int(text[i + 1:i + 3], 16))}m"
            i += 2
        elif len(text) - i > 1 and text[i] == "&" and text[i + 1] in "0123456789abcdef":
            formatted += f"\033[38;5;{str(int(text[i + 1], 16))}m"
            i += 1
        elif text[i:i + 2] == "&#" and set(text[i + 2:i + 4]).issubset("0123456789abcdef") and len(
                text[i + 2:i + 4]) == 2:
            formatted += f"\033[48;5;{str(int(text[i + 2:i + 4], 16))}m"
            i += 3
        elif len(text) - i > 2 and text[i:i + 2] == "&#" and text[i + 2] in "0123456789abcdef":
            formatted += f"\033[48;5;{str(int(text[i + 2], 16))}m"
            i += 2
        elif len(text) - i > 1 and text[i] == "&" and text[i + 1] in "rliusU":
            formatted += f"\033["
            if text[i + 1] == "r": formatted += "0"
            if text[i + 1] == "l": formatted += "1"
            if text[i + 1] == "i": formatted += "3"
            if text[i + 1] == "u": formatted += "4"
            if text[i + 1] == "s": formatted += "9"
            if text[i + 1] == "U": formatted += "21"
            formatted += "m"
            i += 1
        else:
            formatted += text[i]
        i += 1
    return formatted


def print_formatted(*args, sep=" ", end="\n"):
    print(format_string(*args, sep, end), end="\033[0m")


def get_guide():
    for x in range(16):
        for y in range(16):
            code = hex(x * 16 + y)[2:].rjust(2, "0")
            print(format_string(f"&{code}{('&&' + str(code)).rjust(5)}"), end=" ")
        print()
    for x in range(16):
        for y in range(16):
            code = hex(x * 16 + y)[2:].rjust(2, "0")
            print(format_string(f"&#{code}{('&&#' + str(code)).rjust(6)} "), end=" ")
        print()
    print(format_string("&i&&i&r &l&&l&r &u&&u&r &s&&s&r &U&&U"))


if __name__ == '__main__':
    get_guide()
