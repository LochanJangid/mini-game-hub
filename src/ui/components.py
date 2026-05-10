def title(text: str, tagline: str) -> None:
    line = "-"*(len(tagline)+14)
    print(line)
    print(f"| {text:^{len(tagline)+10}} |")
    print(f"| {tagline:^{len(tagline)+11}} |")
    print(line)

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
