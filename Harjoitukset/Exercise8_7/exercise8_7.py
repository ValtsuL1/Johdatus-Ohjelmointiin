from imageai.Detection import ObjectDetection

recognizer = ObjectDetection()

path_model = "/Models/yolo-tiny.h5"
path_input = "/Input/images.jfif"
path_output = "/Output/newimage.jpg"

recognizer.setModelTypeAsTinyYOLOv3()

recognizer.setModelPath(path_model)
recognizer.loadModel()

recognition = recognizer.detectObjectsFromImage(
    input_image=path_input,
    output_image_path=path_output
    )

print(recognition)
