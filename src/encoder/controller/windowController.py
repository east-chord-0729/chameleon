import tkinter as tk


def init(title, transparency):
    root = tk.Tk()

    root.title(title)
    root.geometry(
        f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.wm_attributes("-transparent", True)
    root.wm_attributes("-topmost", True)
    root.attributes("-alpha", transparency)
    return root


def init_label(root):
    label = tk.Label(root)
    label.pack(expand=True, fill=tk.BOTH)
    return label


def init_canvas(root):
    canvas = tk.Canvas(
        root,
        width=root.winfo_screenwidth(),
        height=root.winfo_screenheight(),
        bg="white")
    canvas.pack()
    return canvas


def get_size(root):
    return (root.winfo_screenwidth(), root.winfo_screenheight())


def set_transparency(root, transparency):
    root.attributes("-alpha", transparency)
