from toga.style.pack import Pack
from toga.colors import BLACK, YELLOW


class SelectionStyle():
    
    
    select_miner = Pack(
        padding_top = 15,
        padding_left = 20,
        width = 250,
        font_size = 11,
        color = YELLOW,
        background_color = BLACK
    )

    select_pool = Pack(
        padding_top = 15,
        padding_left = 25,
        width = 250,
        font_size = 11
    )

    select_server = Pack(
        padding_top = 15,
        padding_left = 60,
        width = 200,
        font_size = 11
    )