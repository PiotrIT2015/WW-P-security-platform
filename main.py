import tkinter as tk

from gui.desktop import Desktop

from core.database import initialize_database

from core.logger import get_logger

from core.constants import (
    APP_NAME,
    DEFAULT_WINDOW_WIDTH,
    DEFAULT_WINDOW_HEIGHT
)

logger = get_logger("main")


def main():

    logger.info("Starting WW-P Security Platform")

    initialize_database()

    root = tk.Tk()

    root.title(APP_NAME)

    root.geometry(

        f"{DEFAULT_WINDOW_WIDTH}x{DEFAULT_WINDOW_HEIGHT}"

    )

    Desktop(root)

    root.mainloop()


if __name__ == "__main__":

    main()