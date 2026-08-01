import tkinter as tk

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

    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'а' <= char <= 'я':
            result += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        elif 'А' <= char <= 'Я':
            result += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        else:
            result += char

    entry_result.delete("1.0", tk.END)
    entry_result.insert("1.0", result)

root = tk.Tk()
root.title("Шифратор/Дешифратор Цезаря")
root.geometry("400x420")

tk.Label(root, text="Введіть текст:").pack(pady=(10, 2))
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

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

root.mainloop()