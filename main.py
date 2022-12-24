import monitorcontrol

monitors = monitorcontrol.get_monitors()

for monitor in monitors:
    with monitor:
        print(monitor.set_contrast(100))