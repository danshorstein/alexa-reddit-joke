def cleanup(msg):

    msg2 = msg.lower().replace('shit', 'sh-it') \
        .replace('fuck', 'fu-ck') \
        .replace('asshole', 'ass hole') \
        .replace('..', '.. ') \
        .replace('http://', '') \
        .replace('https://', '') \
        .replace('goddamn', 'god damn') \
        .replace('bitch', 'bit-ch') \
        .replace('nigger', 'gnigger')

    return msg2