import psutil
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def monitor_cpu_usage(threshold=80):
    # Start monitoring CPU usage continuously.

    logging.info("Monitoring CPU usage... Press Ctrl+C to stop.")
    
    try:
        while True:
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            logging.info(f"Current CPU Usage: {cpu_usage}%")
            
            # Check if CPU usage exceeds the threshold i.e. 80%
            if cpu_usage > threshold:
                logging.warning(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    # Set CPU threshold and start monitoring
    monitor_cpu_usage(threshold=80)
