import subprocess

def detect_hidden_camera():
    # Scan for WiFi networks
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    networks = networks.decode('utf-8')
    networks = networks.replace('\r', '')

    keywords = ['camera', 'spy', 'surveillance']
    hidden_cameras = []

    for line in networks.split('\n'):
        if any(keyword in line.lower() for keyword in keywords):
            hidden_cameras.append(line.strip())

    return hidden_cameras

# Call the function to detect hidden cameras
hidden_cameras = detect_hidden_camera()

# Print the list of hidden cameras (if any)
if hidden_cameras:
    print("Hidden cameras detected:")
    for camera in hidden_cameras:
        print(camera)
else:
    print("No hidden cameras detected.")
