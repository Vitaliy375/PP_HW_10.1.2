import sys
from functools import wraps


def log(filename: str | None = None):
    """Декоратор для логирования начала/окончания функции и ошибок."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(f"{func.__name__} called\n")
                    try:
                        result = func(*args, **kwargs)
                        f.write(f"{func.__name__} ok\n")
                        f.flush()
                        return result
                    except Exception as e:
                        f.write(
                            f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                        )
                        f.flush()
                        raise
            else:
                # Консоль
                print(f"{func.__name__} called", file=sys.stderr)
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok", file=sys.stderr)
                    return result
                except Exception as e:
                    print(
                        f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}",
                        file=sys.stderr,
                    )
                    raise

        return wrapper

    return decorator
