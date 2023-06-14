import datetime
import json
import os

NOTES_FILE = "notes.json"


def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    save_notes()
    print("Заметка успешно сохранена.")


def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note["title"] = title
            note["message"] = message
            note["timestamp"] = timestamp
            save_notes()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")


def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")


def list_notes():
    filter_date = input("Введите дату для фильтрации (гггг-мм-дд): ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(filter_date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['message']}")
            print(f"Дата/Время: {note['timestamp']}")
            print("-" * 30)
    else:
        print("Заметки с указанной датой не найдены.")


def save_notes():
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []


def main():
    global notes
    notes = load_notes()
    while True:
        command = input("Введите команду (add, edit, delete, list, exit): ")
        if command == "add":
            add_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "list":
            list_notes()
        elif command == "exit":
            break
        else:
            print("Неверная команда. Пожалуйста, повторите.")


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


if __name__ == "__main__":
    main()
