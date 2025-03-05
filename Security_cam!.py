import cv2
import pygame
import time
import numpy as np

# Initialize pygame for playing sound
pygame.mixer.init()

# Load the sound file
sound = pygame.mixer.Sound("sound.mp3")

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)

# Parameters for motion detection
min_contour_area = 500  # Minimum area to consider as motion
motion_detected = False
last_sound_time = 0
sound_cooldown = 5  # Cooldown time in seconds between sounds

while True:
    # Read the next frame
    ret, frame2 = cap.read()
    if not ret:
        break

    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute the absolute difference between the current frame and the first frame
    frame_delta = cv2.absdiff(frame1, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours of the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check for motion
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            motion_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break

    # If motion is detected and cooldown has passed, play the sound
    if motion_detected and (time.time() - last_sound_time) > sound_cooldown:
        sound.play()
        last_sound_time = time.time()

    # Show the frame
    cv2.imshow("Security Camera", frame2)

    # Update the first frame
    frame1 = gray

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
