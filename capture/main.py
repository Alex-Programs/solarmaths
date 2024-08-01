import os
import time

last_minute = None
while True:
    time.sleep(1)
    minute = time.localtime().tm_min

    if minute != last_minute:
        last_minute = minute
        print(f"Current minute: {minute}")

        if minute % 30 == 0:
            iso_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            print(f"Taking picture at {iso_time}")

            # Step 1: Capture a short video to allow the camera to adjust exposure
            os.system(f"ffmpeg -f video4linux2 -i /dev/video0 -t 2 -video_size 1920x1080 -q:v 2 ./out/{iso_time}.mp4")
            
            # Step 2: Extract the last frame from the captured video
            os.system(f"ffmpeg -sseof -3 -i {iso_time}.mp4 -vf 'thumbnail' -q:v 2 ./out/{iso_time}.jpg")
            
            # Optional: Clean up the temporary video file
            os.remove(f"./out/{iso_time}.mp4")

            print("Taken")
