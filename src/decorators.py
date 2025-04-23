import datetime
import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функции и ее результата.

    Логи могут записываться в файл (если указан `filename`) или в консоль.
    Если функция завершилась ошибкой, логируются параметры и сообщение об ошибке.

    :param filename: Имя файла для записи логов. Если None, логи выводятся в консоль.
    :return: Декорированная функция
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = ""
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                log_message = f"{timestamp} - {func_name} - Args: {args}, Kwargs: {kwargs} - " f"Result: {result}\n"
            except Exception as e:
                log_message = f"{timestamp} - {func_name} - Args: {args}, Kwargs: {kwargs} - " f"Error: {str(e)}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message.strip())
                raise  # Пробрасываем ошибку дальше

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message.strip())

            return result

        return wrapper

    return decorator
