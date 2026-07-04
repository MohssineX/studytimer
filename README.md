# ⏳ studytimer

A lightweight terminal study timer with an audible alarm.

## Features

* Countdown timer for study sessions
* Displays remaining time in `HH:MM:SS` format
* Color-coded terminal output
* Audible alarm when the timer reaches zero
* Simple and interactive terminal interface
* Supports Linux and Windows

## Requirements

* Python 3.x
* playsound3

## Installation

```bash
git clone https://github.com/MohssineX/studytimer.git
cd studytimer
```

Install the required dependency:

```bash
pip install -r requirements.txt
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

1. Enter the desired study time in minutes
2. The countdown begins immediately
3. The remaining time is displayed in real time
4. When the timer reaches zero, an alarm sound starts playing
5. Press `Ctrl + C` to stop the alarm and exit

## Error Handling

| Error | Description                          |
| ----- | ------------------------------------ |
| err   | Invalid input (integer numbers only) |

## Note

`playsound3` needs a system audio backend to work. Most desktop Linux distros already have one, but if you get:

---

## License

This project is licensed under the **MIT License**

---

## Author

**Mohssine :**
[ https://github.com/MohssineX](https://github.com/MohssineX)

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.
