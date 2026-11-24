consonants = set("bcdfghjklmnpqrstvwxz")

def format_s_to_r(text):
    return text.replace("X", "Ks").replace("x", "ks")

def swedish_to_rovar(text):
    result = []
    string = format_s_to_r(text)
    for x in string:
        if x.lower() in consonants:
            result.append(x + "o" + x.lower())
        else:
            result.append(x)
    return "".join(result)

def rovar_to_swedish(text):
    result = []
    i = 0
    while i < len(text):
        result.append(text[i]) 
        if text[i].lower() in consonants:
            i += 3
        else:
            i += 1
    return "".join(result)
