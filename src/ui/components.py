def border(cmd: str, inner_width:int):
    """border(cmd: top/empty/bottom), inner_width: width of thing that you want to store in it."""
    cmds = {
    "top": "┏" + "━" * inner_width + "┓",
    "empty": "┃" + " " * inner_width + "┃",
    "bottom": "┗" + "━" * inner_width + "┛"
    }
    if cmd not in cmds:
        raise ValueError("Give right cmd: top / empty / bottom.")
    return cmds[cmd]

def box(text: str):
    """Prints a string inside a clean, rounded terminal box."""
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    
    # Box drawing characters
    top_border = "╭" + "─" * (width + 2) + "╮"
    bottom_border = "╰" + "─" * (width + 2) + "╯"
    
    print(top_border)
    for line in lines:
        # ljust ensures the right border aligns perfectly
        print(f"│ {line.ljust(width)} │")
    print(bottom_border)