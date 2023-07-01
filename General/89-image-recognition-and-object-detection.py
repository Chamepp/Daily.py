import cv2

def detect_objects(image_path, cascade_path):
    # Load the image
    image = cv2.imread(image_path)

    # Load the pre-trained object detection model
    cascade = cv2.CascadeClassifier(cascade_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform object detection
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around the detected objects
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to the image and the path to the pre-trained cascade classifier
image_path = 'image.jpg'
cascade_path = 'haarcascade_frontalface_default.xml'

# Call the function to detect and display objects
detect_objects(image_path, cascade_path)
