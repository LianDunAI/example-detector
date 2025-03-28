import random
import cv2


class RandomDetector():
    def __init__(self):
        pass

    def detect(self, cap_image, ref_image=None, image_is_path=False):
        print(cap_image, ref_image)
        if image_is_path:
            img_cap = cv2.imread(cap_image, cv2.IMREAD_GRAYSCALE)
        else:
            # image is file content
            img_cap = cv2.imdecode(cap_image, cv2.IMREAD_GRAYSCALE)

        result = {}
        img_width, img_height = img_cap.shape[:2]

        num_of_boxes = random.randint(0, 5)

        boxes = []
        scores = []
        for _ in range(num_of_boxes):
            left, top = random.randint(0, img_width), random.randint(0, img_height)
            box_width, box_height = random.randint(100, 300), random.randint(100, 300)
            box = (left, top, left+box_width, top+box_height)
            boxes.append(box)
            scores.append(random.randint(40, 99) / 100.0)
        result["boxes"] = boxes
        result["scores"] = scores
        result["labels"] = []
        print(result)
        return result
