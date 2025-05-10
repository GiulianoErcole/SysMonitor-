# 🖥️ SysMonitor

A lightweight, terminal-based system resource monitor that provides real-time visibility into CPU usage, memory consumption, and process activity.

## ✨ Features

- **Real-time CPU monitoring** - Track overall CPU utilization
- **Memory usage tracking** - Monitor system RAM consumption
- **Process monitoring** - View top CPU-consuming processes
- **Visual alerts** - Processes using excessive CPU are highlighted in red
- **Minimal resource footprint** - Designed to be lightweight and efficient
- **Simple user interface** - Clean terminal display using curses

## 📋 Requirements

- Python 3.6 or higher
- `psutil` library
- `curses` library (included in standard Python)

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sysmonitor.git
   cd sysmonitor
   ```

2. Install the required Python package:
   ```bash
   pip install psutil
   ```

## 💻 Usage

Run the monitor with:
```bash
python sysmonitor.py
```

### Controls
- **q** - Quit the application
- The display automatically refreshes every second

## 🔍 How It Works

The monitor continually polls system metrics using Python's `psutil` library and displays them in real-time using the `curses` library for terminal rendering. The application:

1. Collects CPU usage data every second
2. Gathers memory usage statistics
3. Compiles information about running processes
4. Sorts and displays processes by CPU usage
5. Highlights processes that use more than 80% CPU

## 🔧 Technical Details

- CPU usage is sampled with a 1-second interval
- Process information includes:
  - Process ID (PID)
  - Process name
  - CPU percentage usage
- Color highlighting uses curses color pairs
- The application handles process access exceptions gracefully

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
