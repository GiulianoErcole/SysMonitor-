import psutil
import curses
import time

# Function to get system information: CPU, memory, and processes
def get_system_info():
    # Get current CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get memory usage percentage
    memory = psutil.virtual_memory()
    
    # Get the top processes by CPU usage, filtering out processes with invalid CPU usage
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            cpu_percent = p.info['cpu_percent']
            if cpu_percent is not None:  # Only include processes with valid cpu_percent
                processes.append((p.info['pid'], p.info['name'], cpu_percent))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that have ended or we don't have permission to access
            continue

    processes.sort(key=lambda x: x[2], reverse=True)  # Sort processes by CPU usage in descending order
    
    return cpu_usage, memory.percent, processes

# Function to display the information using curses
def display_info(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(1000)  # Update every second

    # Initialize color pair for highlighting alert processes
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Red color for alert

    while True:
        # Get system information
        cpu_usage, memory_usage, processes = get_system_info()

        # Clear the screen to update information
        stdscr.clear()

        # Display general system stats
        stdscr.addstr(0, 0, f"CPU Usage: {cpu_usage}%")
        stdscr.addstr(1, 0, f"Memory Usage: {memory_usage}%")

        # Display top 5 processes by CPU usage
        stdscr.addstr(3, 0, "Top Processes by CPU Usage:")
        for i, (pid, name, cpu) in enumerate(processes[:5]):
            stdscr.addstr(4 + i, 2, f"{name} (PID: {pid}) - {cpu}% CPU")
        
        # Highlight suspicious processes (e.g., if CPU usage is > 80%)
        for i, (pid, name, cpu) in enumerate(processes[:5]):
            if cpu > 80:  # Alert threshold for suspicious process (using 80% CPU as an example)
                stdscr.addstr(4 + i, 2, f"{name} (PID: {pid}) - {cpu}% CPU", curses.color_pair(1))

        # Handle user input: press 'q' to quit
        key = stdscr.getch()
        if key == ord('q'):  # Exit on 'q'
            break

        # Refresh the screen to display updated information
        stdscr.refresh()

# Main function to start the display using curses wrapper
def main():
    # Call the curses.wrapper to handle curses initialization and cleanup
    curses.wrapper(display_info)

# Run the main function
if __name__ == "__main__":
    main()

