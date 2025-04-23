from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

SAVE_DIR = Path("cropped_results")
SAVE_DIR.mkdir(exist_ok=True)
# Параметры подписи
LABEL_HEIGHT = 30
FONT_MIN_SIZE = 12
FONT_MAX_SIZE = 24
PADDING = 5


def save_cropped_object(image, xyxy, label):
    x1, y1, x2, y2 = map(int, xyxy)
    cropped_img = image.crop((x1, y1, x2, y2))
    img_width, img_height = cropped_img.size

    new_img = Image.new(
        "RGB",
        (img_width, img_height + LABEL_HEIGHT),
        (255, 255, 255)
    )
    new_img.paste(cropped_img, (0, 0))

    font_size = FONT_MIN_SIZE
    font = None

    # Выбираем подходящий по размеру шрифт для подписи изображения
    font_names = ["arial.ttf", "arialbd.ttf", "DejaVuSans.ttf"]
    for font_name in font_names:
        try:
            for size in range(FONT_MIN_SIZE, FONT_MAX_SIZE + 1):
                test_font = ImageFont.truetype(font_name, size)
                text_width = test_font.getlength(label)
                if text_width > (img_width - 2 * PADDING):
                    break
                font = test_font
                font_size = size
            if font: break
        except:
            continue

    if not font:
        font = ImageFont.load_default()
        for size in range(FONT_MIN_SIZE, FONT_MAX_SIZE + 1):
            test_font = ImageFont.load_default(size)
            text_width = test_font.getlength(label)
            if text_width > (img_width - 2 * PADDING):
                break
            font = test_font

    draw = ImageDraw.Draw(new_img)
    text_width = font.getlength(label)
    text_x = (img_width - text_width) // 2
    text_y = img_height + (LABEL_HEIGHT - font.size) // 2

    # Фон подписи
    draw.rectangle(
        [(0, img_height), (img_width, img_height + LABEL_HEIGHT)],
        fill=(50, 50, 50)
    )

    # Текст подписи
    draw.text(
        (text_x, text_y),
        label,
        font=font,
        fill="white"
    )

    filename = f"{label}_{x1}_{y1}.jpg".replace(" ", "_").replace("/", "-")
    save_path = SAVE_DIR / filename
    new_img.save(save_path)

    return str(save_path)
