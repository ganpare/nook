# /Users/sango/Documents/nook2/nook/config/prompt_editor.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # messageboxを明示的にインポート
from prompt_styles import PROMPT_STYLES, save_prompt_styles

class PromptEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("プロンプトスタイルエディタ")
        
        # スタイル選択
        self.style_label = ttk.Label(root, text="スタイル:")
        self.style_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.style_var = tk.StringVar()
        self.style_combobox = ttk.Combobox(root, textvariable=self.style_var)
        self.style_combobox['values'] = list(PROMPT_STYLES.keys())
        self.style_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.style_combobox.bind('<<ComboboxSelected>>', self.load_style)
        
        # 翻訳ペルソナ
        self.persona_label = ttk.Label(root, text="翻訳ペルソナ:")
        self.persona_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.persona_text = tk.Text(root, height=3, width=40)
        self.persona_text.grid(row=1, column=1, padx=5, pady=5)
        
        # 翻訳スタイル
        self.style_label = ttk.Label(root, text="翻訳スタイル:")
        self.style_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.style_text = tk.Text(root, height=5, width=40)
        self.style_text.grid(row=2, column=1, padx=5, pady=5)
        
        # 保存ボタン
        self.save_button = ttk.Button(root, text="保存", command=self.save_style)
        self.save_button.grid(row=3, column=1, padx=5, pady=5)
        
        # 初期スタイルを読み込む
        self.style_combobox.current(0)
        self.load_style()
    
    def load_style(self, event=None):
        style_name = self.style_var.get()
        style = PROMPT_STYLES[style_name]
        
        self.persona_text.delete(1.0, tk.END)
        self.persona_text.insert(tk.END, style.translation_persona)
        
        self.style_text.delete(1.0, tk.END)
        self.style_text.insert(tk.END, style.translation_style)
    
    def save_style(self):
        style_name = self.style_var.get()
        style = PROMPT_STYLES[style_name]
        
        style.translation_persona = self.persona_text.get(1.0, tk.END).strip()
        style.translation_style = self.style_text.get(1.0, tk.END).strip()
        
        save_prompt_styles(PROMPT_STYLES)
        messagebox.showinfo("保存完了", "プロンプトスタイルを保存しました")

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptEditor(root)
    root.mainloop()