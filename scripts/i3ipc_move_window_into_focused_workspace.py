#!/usr/bin/env python3
import i3ipc

i3 = i3ipc.Connection()


def on_workspace_focus(i3, e):
    focused_ws = e.current.name

    for win in i3.get_tree().leaves():
        if win.floating == 'user_off' or win.window_class is None:
            continue

        if "dragon" in win.window_class.lower():
            win.command(f'move container to workspace "{focused_ws}"')

        if "picture-in-picture" in (win.name or "").lower():
            win.command(f'move container to workspace "{focused_ws}"')


i3.on("workspace::focus", on_workspace_focus)
i3.main()
