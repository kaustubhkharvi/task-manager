# 🎉 Task Manager CLI 🎉

```
╔════════════════════════════════════╗
║      🌟 TASK MANAGER CLI 🌟      ║
╚════════════════════════════════════╝
```

Welcome to the **Task Manager CLI**, a vibrant and user-friendly Command-Line Interface (CLI) task management tool crafted in Python! 🌈 This application lets you effortlessly manage tasks with features like adding, editing, deleting, toggling completion, filtering, and sorting. It’s adorned with stunning ASCII art and ANSI colors to brighten your terminal experience, with all task data saved in a `tasks.json` file. 💾

---

## ✨ Features ✨
- 🚀 Add new tasks with title, description, priority, due date, and category.
- ✏️ Edit existing tasks with ease.
- 🗑️ Delete tasks by ID.
- ✅ Toggle task completion status.
- 🔍 Filter tasks by category.
- 📅 Sort tasks by priority or creation date.
- 👀 Display all tasks in a formatted list.
- 💾 Persistent storage using `tasks.json`.
- 🎨 Attractive interface with ASCII art and colorful output.

---

## 🛠️ Prerequisites
- Python 3.6 or higher. Check your version with:
  ```bash
  python3 --version
  ```

## 📦 Dependencies
This project is lightweight and relies solely on the Python standard library. No external packages are required! The following modules are used:
- `datetime`
- `json`
- `os`
- `typing`
- `dataclasses`
- `uuid`

---

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kaustubhkharvi/task-manager.git
   cd task-manager
   ```
2. Ensure Python 3 is installed on your system.

---

## 🎮 Usage
1. Run the script:
   ```bash
   python3 main.py
   ```
2. Enjoy the colorful menu with ASCII art! Choose from these options:
   - `1. Add Task` 🚀
   - `2. Edit Task` ✏️
   - `3. Delete Task` 🗑️
   - `4. Toggle Completion` ✅
   - `5. Filter Tasks` 🔍
   - `6. Sort Tasks` 📅
   - `7. Display All Tasks` 👀
   - `8. Exit` 🚪
3. Enter the number for your choice and follow the vibrant prompts.
   - Task IDs are displayed with each task for edit, delete, and toggle actions.
   - Press Enter after filtering or sorting to return to the menu.
4. Tasks are saved automatically to `tasks.json`. 💾

---

## 🎨 Example Output
```
╔════════════════════════════════════╗
║      🌟 TASK MANAGER CLI 🌟      ║
╚════════════════════════════════════╝
1. Add Task
2. Edit Task
3. Delete Task
4. Toggle Completion
5. Filter Tasks
6. Sort Tasks
7. Display All Tasks
8. Exit
Enter your choice (1-8): 
┌────────────────────────────────────┐
│ [ ] Task Name | high  | 2025-06-20 | work  | ID: abc123 │
└────────────────────────────────────┘
```

---

## 🤝 Contributing
Love this project? 🌟 Feel free to fork it and submit pull requests! For major changes, please open an issue first to discuss your ideas. 💡

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📝

---

## 🙌 Acknowledgments
- Inspired by the desire for a fun and functional task manager. 🎉
- Utilizes ANSI escape codes for a colorful terminal experience, compatible with most modern terminals. 🌈
- Special thanks to the Python community for the robust standard library! 🙏

---

*Created with ❤️ on June 20, 2025, at 05:10 PM IST*
