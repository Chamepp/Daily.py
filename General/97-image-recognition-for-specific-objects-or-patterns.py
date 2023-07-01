import cv2

# Load the pre-trained model for object detection
net = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')

# Load the image for object detection
image = cv2.imread('image.jpg')

# Preprocess the image for input to the neural network
blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)

# Set the input to the neural network
net.setInput(blob)

# Perform object detection
detections = net.forward()

# Loop over the detections and draw bounding boxes around the detected objects
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    # Filter out weak detections with a confidence threshold
    if confidence > 0.5:
        class_id = int(detections[0, 0, i, 1])

        # Get the label for the class
        label = classes[class_id]

        # Get the bounding box coordinates
        box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
        (start_x, start_y, end_x, end_y) = box.astype("int")

        # Draw the bounding box and label on the image
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.putText(image, label, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with detected objects
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
