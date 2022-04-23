from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import simpledialog
from tkinter import ttk
import os
import shutil
import subprocess
from datetime import datetime
import string
from ctypes import windll
from getpass import getuser as WinGetUsername
import threading


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ':\\')
        bitmask >>= 1

    return drives


win = Tk()
win.title('Porter')
win.iconphoto(True, PhotoImage(file='img/app_icon.png'))


class FileFrame(Frame):
    def __init__(self, window=None, master=None, width=80, height=50):
        super().__init__(master, height=height, width=width)
        self.notepad_exist = False
        self.window = window
        if os.path.isfile('C:\\Program Files\\Notepad++\\notepad++.exe'):
            self.notepad_exist = True
        self.drives = get_drives()

        self.user = WinGetUsername()
        ttk.Style().theme_use('vista')
        self._w = ttk.Frame(master)
        '''ttk.Label(self._w, text='Имя').grid(row=0, column=1)
        ttk.Label(self._w, text='Дата создания').grid(row=0, column=2)
        ttk.Label(self._w, text='Тип').grid(row=0, column=3)'''
        self.cmd_img = PhotoImage(file='img/cmd_img.png')
        self.dir_img = PhotoImage(file='img/dir.png')
        self.newdir_img = PhotoImage(file='img/new_dir.png')
        self.desktop_img = PhotoImage(file='img/desktop.png')
        self.documents_img = PhotoImage(file='img/documents.png')
        self.images_img = PhotoImage(file='img/images.png')
        self.videos_img = PhotoImage(file='img/videos.png')
        self.drive_img = PhotoImage(file='img/drives.png')
        self.drives_img = PhotoImage(file='img/drives2.png')
        self.user_img = PhotoImage(file='img/user.png')
        self.music_img = PhotoImage(file='img/music.png')
        self.unselect_img = PhotoImage(file='img/un-select.png')
        self.download_img = PhotoImage(file='img/download.png')
        self.simplefilelist = ttk.Treeview(self._w, height=25)
        self.simplefilelist.grid(sticky='E', column=1)
        self.full_libs()
        self.simplefilelist.bind('<Button-1>', self.click2)

        self.img_lib = os.getcwd() + '\\img\\'
        self.filelistframe = ttk.Frame(self._w)
        self.filelistframe.grid(sticky='E')
        self.filelistframe2 = ttk.Frame(self.filelistframe)
        self.filelistframe2.grid(sticky='E')
        self.tk = master.tk
        self.listbox = ttk.Treeview(self.filelistframe2, columns=("1n", "2n", '3n'), height=10)
        self.listbox.heading("#0", text="             Имя", anchor=W)
        self.listbox.heading("1n", text="Дата создания", anchor=W)
        self.listbox.heading("2n", text="Тип", anchor=W)
        self.listbox.heading("3n", text="Размер", anchor=W)
        self.listbox.grid(sticky='E')
        scrolly = ttk.Scrollbar(self.filelistframe2)
        self.listbox.config(yscrollcommand=scrolly.set)
        scrolly.grid(sticky='E')
        scrolly.config(command=self.listbox.yview)
        hbar = ttk.Scrollbar(self.filelistframe, orient=HORIZONTAL)
        hbar.grid(sticky='E')
        hbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=hbar.set)
        button_frm = ttk.Frame(self._w)
        button_frm.grid(sticky='E')
        ttk.Button(button_frm, text='Cmd', command=self.cmd_start, image=self.cmd_img).grid(row=0)
        ttk.Button(button_frm, text='Новая папка', command=self.new_dir, image=self.newdir_img).grid(row=1)
        self.width = width
        self.height = height
        self.files = {}
        self.images = []
        self.copy_file = os.getcwd()
        self.copy_or_cut = 0
        self.notepad_plus_plus_img = PhotoImage(file='../test/img\\notepad++.png')

        self.listbox.bind('<Double-Button-1>', self.click)
        self.context_menu = Menu(tearoff=0, bg='#fffff0', font=('arial', 9))

        self.context_menu.add_command(label="Открыть", command=self.OPEN)
        self.context_menu.add_command(label="Вставить", command=self.PASTE)
        self.context_menu.add_command(label="Копировать", command=self.COPY)
        self.context_menu.add_command(label="Вырезать", command=self.CUT)
        self.context_menu.add_command(label="Переименовать", command=self.RENAME)
        self.context_menu.add_command(label="Удалить", command=self.DELETE)
        self.context_menu.add_separator()
        '''self.context_menu.add_command(label="Открыть в блокноте", command=lambda: self.startfile('notepad'))
        if self.notepad_exist:
            self.context_menu.add_command(label="Открыть в Notepad++", command=lambda: self.startfile(
                '"C:\\Program Files\\Notepad++\\notepad++.exe"'), font=('arial', 11), image=self.notepad_plus_plus_img)'''
        self.listbox.bind('<Button-3>', self.context)
        os.chdir('C:\\Users\\' + self.user + '\\')
        self.full_files()

    def full_libs(self):
        # for it in self.listbox.keys():
        # self.simplefilelist.delete(it)
        self.sfl_dict = {}
        self.drives = get_drives()
        self.simplefilelist.heading("#0", text="Библиотеки и диски", anchor=W)
        self.user_column = self.simplefilelist.insert("", 0, None, text='Пользователь', image=self.user_img)
        self.sfl_dict[self.user_column] = 'C:\\Users\\' + self.user
        self.desktop_column = self.simplefilelist.insert("", 1, None, text='Рабочий стол', image=self.desktop_img)
        self.sfl_dict[self.desktop_column] = 'C:\\Users\\' + self.user + '\\Desktop\\'
        self.download_column = self.simplefilelist.insert("", 2, None, text='Загрузки', image=self.download_img)
        self.sfl_dict[self.download_column] = 'C:\\Users\\' + self.user + '\\Downloads\\'
        self.docs_column = self.simplefilelist.insert("", 3, None, text='Документы', image=self.documents_img)
        self.sfl_dict[self.docs_column] = 'C:\\Users\\' + self.user + '\\Documents\\'
        self.images_column = self.simplefilelist.insert("", 4, None, text='Изображения', image=self.images_img)
        self.sfl_dict[self.images_column] = 'C:\\Users\\' + self.user + '\\Pictures\\'
        self.video_column = self.simplefilelist.insert("", 5, None, text='Видео', image=self.videos_img)
        self.sfl_dict[self.video_column] = 'C:\\Users\\' + self.user + '\\Videos\\'
        self.music_column = self.simplefilelist.insert("", 6, None, text='Музыка', image=self.music_img)
        self.sfl_dict[self.music_column] = 'C:\\Users\\' + self.user + '\\Music\\'
        self.drive_column = self.simplefilelist.insert("", 7, None, text='Диски', image=self.drive_img)
        self.sfl_dict[self.drive_column] = '.'
        i = 0
        for logical_drive in self.drives:
            i += 1
            logdrive = self.simplefilelist.insert(self.drive_column, i, None, text=logical_drive, image=self.drives_img)
            self.sfl_dict[logdrive] = logical_drive
        self.simplefilelist.insert("", 8, None, text='                   ')

    def strhex(self, st):
        a = '0123456789ABCDEF'
        return a[st // 256] + a[st % 256 // 16] + a[st % 16]

    def check_size(self, fn):
        bsize = os.path.getsize(fn)
        if bsize > 2 ** 30:
            return str(bsize // 2 ** 30) + 'Гб'
        if bsize > 2 ** 20:
            return str(bsize // 2 ** 20) + 'Мб'
        if bsize > 2 ** 10:
            return str(bsize // 2 ** 10) + 'Кб'
        else:
            return str(bsize) + 'Б'

    def new_dir(self):
        newname = simpledialog.askstring('Введите имя новой папки!', 'Введите имя: ')
        os.makedirs(newname)
        self.full_files()

    def click2(self, event=None):
        el = self.sfl_dict[self.simplefilelist.selection()[0]]
        if el != '..':
            try:
                os.chdir(el)
                self.full_files()
            except Exception as ErrorOpenFolder:
                msgbox.showerror('Ошибка', 'Не удалось открыть папку или диск!')

    def click(self, event=None):
        el = self.files[self.listbox.selection()[0]]
        # if(1):
        try:
            if self.isfile(el):
                os.startfile(el)
            else:
                os.chdir(el + '\\')
                self.full_files()
        except Exception as ErrorOpenFile:
            msgbox.showerror('Ошибка', 'Не удалось открыть файл или директорию!')

    def full_files(self):
        def process():
            for it in self.files.keys():
                self.listbox.delete(it)
            files = ['..'] + list(os.listdir())
            self.images = []
            self.files = {}
            i = 1
            for ob in files:
                if self.isfile(ob):
                    if '.' in ob:
                        res = '.' + ob.split('.')[-1]
                    else:
                        res = 'Файл'
                else:
                    res = 'Папка'
                if self.isfile(ob):
                    try:
                        self.images += [PhotoImage(file=self.img_lib + ob.split('.')[-1] + '.png')]
                        self.files[self.listbox.insert("", i, None, text=ob, values=(
                            str(datetime.fromtimestamp(int(os.path.getctime(ob)))), res, self.check_size(ob)),
                                                       image=self.images[-1])] = ob
                    except Exception as ErrorNoImageForThisTypeFiles:
                        self.images += [PhotoImage(file=self.img_lib + 'who.png')]
                        self.files[self.listbox.insert("", i, None, text=ob, values=(
                            str(datetime.fromtimestamp(int(os.path.getctime(ob)))), res, self.check_size(ob)),
                                                       image=self.images[-1])] = ob
                else:
                    self.files[self.listbox.insert("", i, None, text=ob, values=(
                        str(datetime.fromtimestamp(int(os.path.getctime(ob)))), res, self.check_size(ob)),
                                                   image=self.dir_img)] = ob
                if i % 200 == 199:
                    self.window.update_idletasks()
                    self.window.update()
                i += 1
            self.window.update()
            self.window.update_idletasks()

        process()

    def round_word(self, word, n):
        if len(word) > n - 1:
            return word[:n - 4] + '... '
        else:
            return word + ' ' * (n - len(word))

    def isfile(self, name):
        return os.path.isfile(name)

    def PASTE(self):
        mandms = None

        def process():
            print(mandms)
            if self.copy_or_cut == 0:
                if self.isfile(self.copy_file):
                    shutil.copyfile(self.copy_file, os.getcwd() + '\\' + self.copy_file.split('\\')[-1])
                else:
                    shutil.copytree(self.copy_file, os.getcwd() + '\\' + self.copy_file.split('\\')[-1] + '\\')
            else:
                if self.isfile(self.copy_file):
                    shutil.copyfile(self.copy_file, os.getcwd() + '\\' + self.copy_file.split('\\')[-1])
                    os.remove(self.copy_file)
                else:
                    shutil.copytree(self.copy_file, os.getcwd() + '\\' + self.copy_file.split('\\')[-1] + '\\')
                    shutil.rmtree(self.copy_file)
            self.full_files()

        mandms = threading.Thread(target=process)
        mandms.start()
        self.full_files()

    def COPY(self):
        el = self.files[self.listbox.selection()[0]]
        self.copy_file = os.getcwd() + '\\' + el
        self.copy_or_cut = 0

    def CUT(self):
        el = self.files[self.listbox.selection()[0]]
        self.copy_file = os.getcwd() + '\\' + el
        self.copy_or_cut = 1

    def RENAME(self):
        el = self.files[self.listbox.selection()[0]]
        newname = simpledialog.askstring('Введите новое имя!', 'Старое имя: ' + el)
        os.rename(os.getcwd() + '\\' + el, os.getcwd() + '\\' + newname)
        self.full_files()

    def startfile(self, prgrm):
        el = self.files[self.listbox.selection()[0]]
        try:
            if self.isfile(el):
                os.popen(prgrm + ' ' + el)
        except EXCEPTION as ErrorOpenFile:
            msgbox.showerror('Ошибка', 'Не удалось открыть папку или директорию!')

    def DELETE(self):
        el = self.files[self.listbox.selection()[0]]
        try:
            if self.isfile(el):
                os.remove(el)
                self.full_files()
            else:
                shutil.rmtree(el)
                self.full_files()
        except EXCEPTION as ErrorOpenFile:
            msgbox.showerror('Ошибка', 'Не удалось удалить папку или директорию!')

    def OPEN(self):
        el = self.files[self.listbox.selection()[0]]
        try:
            if self.isfile(el):
                def process():
                    os.startfile(el)

                threading.Thread(target=process).start()
            else:
                os.chdir(el)
                self.full_files()
        except EXCEPTION as ErrorOPenFolder:
            msgbox.showerror('Ошибка', 'Не удалось открыть папку или директорию!')

    def cmd_start(self):
        subprocess.Popen('cmd')

    def context(self, event=None):
        try:
            self.context_menu.post(event.x_root, event.y_root)

        except EXCEPTION:
            pass


filesys = FileFrame(win, win)
filesys.pack(fill=BOTH, expand=1)
win.mainloop()
