# 🧾 Day 24 - Notes App v2 (File Handling with seek() and tell())

Hey there! 👋  
Welcome to **Day 24** of my **#30DaysOfPythonChallenge**. Today I upgraded the Notes App to demonstrate powerful file manipulation techniques using cursor controls in Python.

---

## 📌 What’s This About?
Today’s focus:  
- Advanced **File Handling**
- Using `seek()` to move the file cursor  
- Using `tell()` to get current cursor position  
- Cleaner code with **modular functions** and better **error handling**

---

## 💭 Why Is This Useful?
Understanding how file cursors work is essential when working with large files, logs, or byte-level editing. This version of the app gives you deeper control and insight into file internals.

---

## ✨ What’s New in v2

- 🧭 Move cursor to a specific byte using `seek()`
- 📍 Show cursor position with `tell()`
- 🧠 Modularized functions for better readability
- ⚠️ Stronger error handling with detailed feedback

---

## ✅ Features

- 📝 Add a new note
- 📖 View all notes
- ✏️ Update or delete a note by index
- 📍 Show file cursor position (`tell()`)
- 🔁 Read file from a specific byte (`seek()`)

---

## 🛠️ Tech Stack

Built with:
- 🐍 **Python 3**
- `with open()` context manager
- File cursor methods: `seek()`, `tell()`
- Defensive coding with `try-except` blocks

---

## 🚀 Run It Like This

Open your terminal and run:
```bash
python Day-24Code.py
