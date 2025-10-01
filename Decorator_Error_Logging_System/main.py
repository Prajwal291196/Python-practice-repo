import time
import logging
import traceback
from functools import wraps

# ✅ Configure logging once
logging.basicConfig(
    filename="error_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_name = func.__name__
        try:
            # ✅ Log arguments before execution
            logging.info(
                f"Function '{func_name}' called with args={args} kwargs={kwargs}"
            )

            result = func(*args, **kwargs)

            # ✅ Calculate execution time
            execution_time = time.time() - start_time
            logging.info(
                f"Function '{func_name}' executed in {execution_time:.4f} seconds and returned: {result}"
            )

            return result

        except Exception as e:
            error_trace = traceback.format_exc()
            logging.error(
                f"❌ Error in '{func_name}' with args={args}, kwargs={kwargs}: {e}\n{error_trace}"
            )
            print(f"❌ An error occurred in '{func_name}'. Check 'error_log.log' for details.")
            return None

    return wrapper


@log_execution
def divide(a, b):
    """Example function that may raise an error"""
    time.sleep(1)  # simulate work
    return a / b

@log_execution
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Alice"))         # ✅ Should log function name + time
    print(divide(10, 2))          # ✅ Should log normally
    print(divide(10, 0))          # ❌ Will log error + stack trace
    print(divide("10", "2"))      # ❌ Will log error + stack trace