from controller import windowController, messageController
from config import config
from PIL import Image, ImageTk, ImageGrab, ImageDraw


SIZE_BLOCK = 78  # size of qrcode. (How to determine autometically ?)


def capture_screen(root):
    width, height = windowController.get_size(root)
    screen_image = ImageGrab.grab()
    screen_image.thumbnail((width, height))
    screen_image = screen_image.crop((0, 65, width, height))
    return screen_image


def calculate_average_color(image):
    image = image.convert('RGB')
    width, _ = image.size
    num_pixels = width

    r_total = 0
    g_total = 0
    b_total = 0
    for x in range(width):
        r, g, b = image.getpixel((x, x))
        r_total += r
        g_total += g
        b_total += b

    newr = r_total // num_pixels
    newg = g_total // num_pixels
    newb = b_total // num_pixels

    return (newr, newg, newb)


def draw_average_color_blocks(screen_image):
    color_grid_image = Image.new('RGB', screen_image.size)
    draw = ImageDraw.Draw(color_grid_image)

    for y in range(0, screen_image.height, SIZE_BLOCK):
        for x in range(0, screen_image.width, SIZE_BLOCK):
            block_area = (x, y, x + SIZE_BLOCK, y + SIZE_BLOCK)
            block = screen_image.crop(block_area)
            avg_color = calculate_average_color(block)
            draw.rectangle(list(block_area), fill=avg_color)

    return color_grid_image


def draw_img(root, label, img):
    tk_image = ImageTk.PhotoImage(img)
    label.config(image=tk_image)
    label.image = tk_image
    root.update()


def update(root, label):
    # 1. turn off the window for caturing the screen
    windowController.set_transparency(root, 0.0)

    # 2. capture the screen
    captured_img = capture_screen(root)

    # 3. generate color grid image using the screen image
    avg_img = draw_average_color_blocks(captured_img)

    # 4. draw color grid image on the windowå
    draw_img(root, label, avg_img)

    # 5. turn on the window
    windowController.set_transparency(root, config.TRANSPARENCY_COLOR)

    root.after(3000, lambda: update(root, label))


def run(info):
    root = windowController.init("Color Window", config.TRANSPARENCY_COLOR)
    label = windowController.init_label(root)
    update(root, label)
    root.mainloop()


if __name__ == "__main__":
    info = (config.HOST_NAME, config.AUDIENCE_NAME, config.HOST_KEY)
    run(info)
