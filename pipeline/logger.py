from datetime import datetime

VALID_LEVELS = {"INFO", "WARNING", "ERROR", "CRITICAL"}

def write_log(level, message):

    if level not in VALID_LEVELS:
        level = "INFO"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")
