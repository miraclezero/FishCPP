# FishCPP

FishCPP is a Raspberry Pi-based system designed to conduct Conditioned Place Preference (CPP) experiments with zebrafish. The system automates camera recording, manages uniform arena illumination using NeoPixel LEDs, and uses RFID scans to initiate sessions and track device configurations.

## System Features

- **Arena Illumination**: Drives a 128-pixel WS2812B NeoPixel LED array to provide constant, uniform white light.
- **Physical Visual Cues**: Visual conditioning cues consist of physical, 3D-printed floor inserts placed within the arena: a black dots pattern and a grid pattern.
- **RFID-Initiated Sessions**: RFID scans are used to initiate the recording trials, advance experimental stages, and track system device IDs.
- **Automated Video Recording**: Controls the Raspberry Pi Camera Module to record trials (30 frames per second, 20-minute sessions) in raw `.h264` format.
- **Disk Space Verification**: Checks available disk space before starting a trial to ensure there is at least 2.5 GB of free storage.
- **Video Conversion Utility**: Includes a bash script ([convert_video.sh](file:///home/hao/Dropbox/git/FishCPP/convert_video.sh)) to convert raw `.h264` recordings to `.mp4` format using `ffmpeg`.

## Hardware Components

- Raspberry Pi (running Raspberry Pi OS)
- Raspberry Pi Camera Module
- WS2812B NeoPixel LED array (128 pixels, connected to GPIO pin 18)
- RFID Reader (operating in keyboard emulation mode)
- 3D-printed arena partition inserts (black dots versus grid pattern)

## Installation and Setup

1. Clone this repository to the Raspberry Pi:
   ```bash
   git clone https://github.com/miraclezero/FishCPP.git
   ```
2. Install the necessary Python packages:
   ```bash
   pip3 install rpi_ws281x adafruit-circuitpython-neopixel board requests
   ```
3. Enable the camera module using the Raspberry Pi configuration tool:
   ```bash
   sudo raspi-config
   ```
4. Verify that the configuration file `peerpub_config.json` exists in the `/home/pi/` directory. This file tracks the system device ID, current session ID, and experiment step.
5. Grant execute permissions to the video conversion utility:
   ```bash
   chmod +x convert_video.sh
   ```

## Experimental Workflow

1. **Initialization**: Start the main control program ([main.py](file:///home/hao/Dropbox/git/FishCPP/main.py)):
   ```bash
   python3 main.py
   ```
   The program checks for sufficient disk space (at least 2.5 GB free) and verifies that the directory is writable.
2. **Session Initiation**: Scan the appropriate RFID tag to register the subject configuration and initiate the recording script.
3. **Recording and Illumination**: The NeoPixel LED array lights up to provide constant white illumination. The system starts the camera to record a 20-minute trial, saving the video file to `/home/pi/video/`.
4. **Session Termination**: Scan the termination RFID tag to turn off the LEDs and conclude the session. The session counter in `peerpub_config.json` will automatically increment.
5. **Video Conversion**: Convert the raw video output to `.mp4` for analysis:
   ```bash
   ./convert_video.sh <filename_without_extension>
   ```
