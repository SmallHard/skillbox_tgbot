user_request_history = []


# Функция для добавления запроса в историю
def add_to_history(user_id, request):
    # Добавляем запрос в историю
    user_request_history.append((user_id, request))
    # Ограничиваем размер истории десятью последними запросами
    if len(user_request_history) > 10:
        user_request_history.pop(0)


# Функция для обработки команды /history
def handle_history_command(user_id):
    # Получаем последние десять запросов пользователя
    user_history = [req for uid, req in user_request_history if uid == user_id][-10:]
    # Формируем ответ
    if user_history:
        response = "История ваших последних десяти запросов:\n"
        for request in user_history:
            response += f"- {request}\n"
    else:
        response = "История ваших запросов пуста."
    return response
