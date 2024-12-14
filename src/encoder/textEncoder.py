from controller import windowController, messageController
from config import config


def get_start_position_of_text(root):
    width, height = windowController.get_size(root)
    move_x = 3
    move_y = 1

    x = 0 - (width // 4)
    y = 0 + (height // 8) * 3

    gap = height // 4

    line = [(0, 0)] * 1200
    for i in range(1200):
        line[i] = (x, y)
        x += move_x
        y -= move_y

    return line, gap


def update(root, canvas, info, line, gap, num):
    message, mac = messageController.generate(info)
    message = "[Do Not Copy] " + message + "\n" + mac

    canvas.delete("tag")

    for i in range(5):
        for j in range(6):
            x, y = line[j * 200 + num]
            canvas.create_text(
                x, y + gap * i,
                text=message,
                angle=config.TEXT_ANGLE,
                font=(config.TEXT_FONT, config.TEXT_SZ, config.TEXT_STYLE),
                fill=config.TEXT_COLOR,
                justify="center",
                tags="tag"
            )

    num += 1
    if num == 200:
        num = 0

    root.after(config.UPDATE_TIME_TEXT, lambda: update(
        root, canvas, info, line, gap, num))


def run(info):
    root = windowController.init("Text Window", config.TRANSPARENCY_TEXT)
    root.configure(bg='white')
    canvas = windowController.init_canvas(root)

    line, gap = get_start_position_of_text(root)

    update(root, canvas, info, line, gap, 0)

    root.mainloop()


if __name__ == "__main__":
    info = (config.HOST_NAME, config.AUDIENCE_NAME, config.HOST_KEY)
    run(info)
