import cv2
from ultralytics import YOLO
import pygame

# Initialize pygame for sound playback
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound(r"E:\detect\audio.mp3") #Using a raw string for the path

#Load the trained YOLO model
model = YOLO(r"E:\detect\best.pt")

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set of classes to trigger the alarm (excluding 'person')
trigger_classes = ['LeftRight', 'child', 'drowsy', 'mobile', 'talking']

# Flag to track if the alarm is already playing
alarm_played = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Process results and draw bounding boxes
    annotated_frame = results[0].plot()  # Annotate the frame with detections

    # Check for detections
    detected_classes = results[0].names  # Get class names from results
    
    # Check if 'person' is detected
    person_detected = any(class_name == 'person' for result in results[0].boxes.data for class_name in detected_classes)

    if person_detected:
        # If 'person' is detected, stop the alarm if it was playing
        alarm_played = False  # Reset alarm flag when a person is detected
    else:
        # If no 'person' is detected, check for other trigger classes
        for result in results[0].boxes.data:  # Iterate over detected boxes
            class_id = int(result[5])  # Get class ID of detected object
            class_name = detected_classes[class_id]  # Get class name

            # Check if the detected class is in the trigger list (excluding 'person')
            if class_name in trigger_classes:
                if not alarm_played:
                    alarm_sound.play()  # Play alarm sound
                    alarm_played = True  # Set flag to indicate that the alarm has been played

                break  # Exit loop after playing the alarm once for this frame

    # Reset the alarm flag if no triggering classes are found and person is not found
    if not person_detected and not any(class_name in trigger_classes for result in results[0].boxes.data for class_name in detected_classes):
        alarm_played = False  # Reset flag when no triggering classes are found

    # Display the annotated frame
    cv2.imshow("Live Detection", annotated_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()




