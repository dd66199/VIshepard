def receive_message(message, fwd):
    words = message['text'].split()
    if 'досье' == words[0].lower():
        return get_info_spectre(fwd)
    elif len(words) > 1 and words[0][0] == '+':
        return rate_message(words, fwd)


def rate_message(words, fwd_user):
    if words[0][1:].isdigit():
        if words[1].lower() == 'герой':
            fwd_user.good = fwd_user.good + int(words[0][1:])
            fwd_user.save()
        elif words[1].lower() == 'отступник':
            fwd_user.evil = fwd_user.evil + int(words[0][1:])
            fwd_user.save()

    return 'received'


def get_info_spectre(fwd_user):
    return f"Имя Спектра: {fwd_user.name}\n Герой: {fwd_user.good}\n Отступник: {fwd_user.evil}"