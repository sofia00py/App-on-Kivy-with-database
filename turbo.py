def compression(string):
    dict = {}
    entry = ''
    index = 1
    for i in range(len(string)):
        entry += string[i]
        if entry not in dict:
            lst = [index]
            encoder = [dict[entry[0:len(entry) - 1]][0] if entry[0:len(entry) - 1] in dict else 0, entry[-1]]
            lst.append(encoder)
            dict[entry] = lst
            index += 1
            entry = ''
    ans = ''
    for x in dict:
        ans += f'<{dict[x][1][0]},{dict[x][1][1]}>'

    return ans


def parse(string):
    dict = {}
    index = 1
    incorrect = False
    for i in range(len(string)):
        if string[i] == '<':
            encoderIndex = ''
            encoderTail = ''
            comma = False
            i += 1
            while string[i] != '>':
                if string[i] == ',':
                    comma = True
                    i += 1
                    continue
                if comma:
                    encoderTail += string[i]
                    i += 1
                    continue
                encoderIndex += string[i]
                i += 1

            lst = [[int(encoderIndex), encoderTail], '']
            dict[index] = lst
            index += 1

    return dict


def decompression(string):
    error = False
    ans, entry = '', ''
    try:
        parse(string)
    except BaseException:
        error = True
        return error, ans, {}

    dict = parse(string)
    for x in dict:
        value = dict[x]
        entry += dict[value[0][0]][1] if value[0][0] != 0 else ''
        entry += value[0][1]

        value[1] = entry
        ans += entry
        entry = ''

    return ans
