def mask_account_card(info):
    # Разделяем строку на тип и номер
    parts = info.split()
    card_type = ' '.join(parts[:-1])
    number = parts[-1]

    if 'Счет' in card_type:
        # Маскировка для счета
        masked_number = '**' + number[-4:]
        return f"{card_type} {masked_number}"
    else:
        # Маскировка для карт
        masked_number = number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
        return f"{card_type} {masked_number}"

def get_date(date_str):
    from datetime import datetime
    # Преобразуем строку в объект datetime
    dt = datetime.fromisoformat(date_str)
    # Возвращаем в нужном формате
    return dt.strftime("%d.%m.%Y")