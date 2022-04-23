from tkinter import Tk, Frame, ttk

root = Tk()
frame_tree = Frame(root)
treeview = ttk.Treeview(frame_tree)
treeview.insert('', '10', 'material', text='C:')
treeview.insert('material', '0', 'coil', text='Катушка')
treeview.insert('coil', '0', 'shell', text='Оболочка')
treeview.insert('coil', '1', 'conductor', text='Проводник')
treeview.insert('conductor', '0', 'cable', text='Кабель')
treeview.insert('material', '1', 'size_pipeline', text='Типоразмер трубопровода')
treeview.insert('size_pipeline', '0', 'aluminum_alloy', text='Алюминиевые сплавы')
treeview.item('material', open=True)
frame_tree.pack(padx=10, pady=10, side='left')
treeview.pack()
root.mainloop()
