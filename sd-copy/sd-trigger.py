#!/usr/bin/python3

import sys
import datetime
import glob
import shutil
import os
import time
import ffmpeg


FOLDER_NAME = "/media/pi/*/timelapse"
DESTINATION = "/home/pi/timelapse/copy"
VIDEO_OUTPUT = "/home/pi/timelapse/stiched"


def main():

    print("\nWaiting for drive mount\n")
    time.sleep(5)
    print(FOLDER_NAME)

    ###########################################

    for name in glob.glob(f"{FOLDER_NAME}"):
        print(f"Found '{FOLDER_NAME}' folder: {name}")

        os.makedirs(DESTINATION, exist_ok=True)

        for idx, image in enumerate(glob.glob(f"{name}/*.jpg")):
            print(f"\t{image}")
            shutil.copy(image, f"{DESTINATION}/image_{idx:04}.jpg")
    ###########################################

    os.makedirs(VIDEO_OUTPUT, exist_ok=True)

    (
        ffmpeg.input(f"{DESTINATION}/image_%04d.jpg", framerate=25)
        .output(f"{VIDEO_OUTPUT}/timelapse.mp4")
        .run()
    )

    ###########################################

    print("\nWaiting 10secs and will remove copied images\n")
    time.sleep(10)

    for name in glob.glob(f"{DESTINATION}"):

        for image in glob.glob(f"{DESTINATION}/*.jpg"):
            os.remove(image)
            print(f"Deleted: {image}")

        os.rmdir(DESTINATION)
        print(f"Deleted: {DESTINATION}")

    print("\nClosing in 10 seconds\n")
    time.sleep(10)


###########################################


if __name__ == "__main__":
    print("MAIN")
    # FOLDER_NAME = "../timelapse"
    # DESTINATION = "./copy"
    # VIDEO_OUTPUT = "./stiched"
    main()
