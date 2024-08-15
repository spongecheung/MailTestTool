import tkinter as tk
from tkinter.ttk import Notebook

from tool.file_manager import FileManager


class MailTestTool(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("邮件测试工具箱")
        self.geometry("500x300")

        self.notebook = Notebook(self)

        # 造附件页面
        file_tab = tk.Frame(self.notebook)
        self.notebook.add(file_tab, text='造附件')
        self.label_file = tk.Label(file_tab, text='附件大小：')
        self.label_file.grid(row=0, column=0, padx=10, pady=10)
        self.entry_size = tk.Entry(file_tab)
        self.entry_size.grid(row=0, column=1, padx=10, pady=10)
        self.label_file_count = tk.Label(file_tab, text='附件数量：')
        self.label_file_count.grid(row=1, column=0, padx=10, pady=10)
        self.entry_count = tk.Entry(file_tab)
        self.entry_count.grid(row=1, column=1, padx=10, pady=10)
        self.button_create_file = tk.Button(file_tab, text='造附件')
        self.button_create_file.grid(row=2, column=1, padx=10, pady=10)

        # SMTP发信页面
        send_tab = tk.Frame(self.notebook)
        self.notebook.add(send_tab, text="SMTP发信")

        self.notebook.pack(fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    mailTestTool = MailTestTool()
    mailTestTool.mainloop()
