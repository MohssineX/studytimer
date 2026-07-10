# ⏳ studytimer

A lightweight terminal study timer with a built-in audible alarm.

## Features

* Countdown timer for study sessions
* Displays remaining time in `HH:MM:SS` format
* Colorized terminal interface
* Audible alarm when the timer reaches zero
* Supports study sessions up to 24 hours
* Built-in input validation and error handling
* Works on Linux and Windows

## Requirements

* Python 3.x
* miniaudio

## Installation

```bash
git clone https://github.com/MohssineX/studytimer.git
cd studytimer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install miniaudio
```

## Usage

Run the program:

```bash
python studytimer.py
```

If your system uses `python3`:

```bash
python3 studytimer.py
```

## How It Works

1. Start the program
2. Enter a study duration in minutes
3. The countdown begins immediately
4. The remaining time is displayed in real time
5. When the timer reaches zero, an alarm starts playing
6. Press `Ctrl+C` to stop the alarm and exit

## Error Codes

| Code   | Description                                                                       |
| ------ | ----------------------------------------------------------------------------------|
| err101 | Invalid timer (The time must be between 1 minute and 1440 minutes(24 hours) only) |
| err102 | Invalid input (integer numbers only)                                              |

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Mohssine :**
[ https://github.com/MohssineX](https://github.com/MohssineX)

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.
