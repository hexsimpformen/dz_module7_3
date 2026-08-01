import tkinter as tk

UKR_LOWER = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UKR_UPPER = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

def shift_char(char, shift):
    if char in UKR_LOWER:
        idx = UKR_LOWER.index(char)
        return UKR_LOWER[(idx + shift) % len(UKR_LOWER)]
    elif char in UKR_UPPER:
        idx = UKR_UPPER.index(char)
        return UKR_UPPER[(idx + shift) % len(UKR_UPPER)]
    elif 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return char

def process_text(mode):
    text = entry_text.get("1.0", tk.END).rstrip('\n')
    
    try:
        shift = int(entry_shift.get())
    except ValueError:
        entry_result.delete("1.0", tk.END)
        entry_result.insert("1.0", "Помилка: Введіть числове зміщення!")
        return

    if mode == "decrypt":
        shift = -shift

    result = "".join(shift_char(char, shift) for char in text)

    entry_result.delete("1.0", tk.END)
    entry_result.insert("1.0", result)

def paste_text():
    try:
        clipboard = root.clipboard_get()
        entry_text.insert(tk.INSERT, clipboard)
    except tk.TclError:
        pass

def copy_result():
    text = entry_result.get("1.0", tk.END).rstrip('\n')
    root.clipboard_clear()
    root.clipboard_append(text)

root = tk.Tk()
root.title("Шифратор/Дешифратор Цезаря")
root.geometry("420x460")

tk.Label(root, text="Введіть текст:").pack(pady=(10, 2))
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

btn_paste = tk.Button(root, text="Вставити текст", command=paste_text)
btn_paste.pack(pady=2)

tk.Label(root, text="Введіть зміщення (ключ):").pack(pady=(10, 2))
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()
entry_shift.insert(0, "3")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(
    frame_buttons, 
    text="Зашифрувати", 
    command=lambda: process_text("encrypt")
)
btn_encrypt.pack(side=tk.LEFT, padx=5)

btn_decrypt = tk.Button(
    frame_buttons, 
    text="Розшифрувати", 
    command=lambda: process_text("decrypt")
)
btn_decrypt.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Результат:").pack(pady=(10, 2))
entry_result = tk.Text(root, height=5, width=40)
entry_result.pack()

btn_copy = tk.Button(root, text="Копіювати результат", command=copy_result)
btn_copy.pack(pady=5)

root.mainloop()