# Log File Analyzer: Read a .log file and count:
# Errors, Warnings, and Info messages
# (Real-world: Helps in monitoring applications)

# file_path = 'logging.log'

import logging

logging.basicConfig(
    filename="app.log",        # Log file
    filemode="a",              # Append mode
    level=logging.DEBUG,       # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().lower()
                if "error" in line:
                    error_count += 1
                elif "warning" in line:
                    warning_count += 1
                elif "info" in line:
                    info_count += 1
                
        print("📊 Log Analysis Results")
        print(f"Errors:   {error_count}")
        print(f"Warnings: {warning_count}")
        print(f"Info:     {info_count}")
    except FileNotFoundError:
        logging.error("File not found. Please check the file path.")
    except Exception as e:
        logging.warning(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    analyze_log(file_path)