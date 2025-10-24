import logging 

# Logging basic configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("You tried to divide by zero?...")
        result = None

    except Exception as e:
        logging.error(f"Unespected error: {e}")
        result = None

    else:
        logging.info(f"division succesfull: {result}")
    finally:
        logging.info("Execution finished")
    return result

# --- Test ---
if __name__ == "__main__":
    assert divide(10, 2) == 5
    assert divide(10, 0) is None
    print("errors.py Works properly")
