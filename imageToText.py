from pytesseract import pytesseract     # find text in image
from PIL import Image   # manage image
import dearpygui.dearpygui as dpg   # graphics
import os           # execute os program
import pyperclip    # manage clipboard


def button_click(sender, app_data, user_data):
    if user_data == "Screenshot":
        exit_status = os.system("xfce4-screenshooter -r --save ./tmp.png")
        if exit_status == 0:
            print("Image saved successfully!")
            pyperclip.copy(pytesseract.image_to_string(Image.open('./tmp.png'), lang="ita+eng"))    # find text in image and copy in on clipboard
            print("Now text is on your clipboard!")
            os.system("rm ./tmp.png")   # delete screencapture
        else:
            print("Image NOT saved!")


def guiCreate():
    dpg.create_context()

    # add a font registry
    with dpg.font_registry():
        new_font = dpg.add_font("./Reace_Story.ttf", 52)

    with dpg.window(label="Text Extractor", no_collapse=True, no_close=True, no_move=True, no_title_bar=True, width=320, height=150):
        # set Button
        button1 = dpg.add_button(tag="Button1", label="Take screenshot", callback=button_click, user_data="Screenshot", width=300, height=130)
        # set font
        dpg.bind_font(new_font)

    dpg.create_viewport(title="TextExtractor", width=320, height=150, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    guiCreate()
