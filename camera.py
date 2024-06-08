import cv2
import datetime

def CaptureImage():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("python picture capture")

    now = datetime.datetime.now()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("python picture capture", frame)

        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Escape hit, closing...")
            break

        elif k%256 == 32:
            img_name = "Xray_image_{}.png".format(now)
            cv2.imwrite(img_name, frame)
            print("photo taken ", img_name)

    cam.release()
    cv2.destroyAllWindows()


CaptureImage()

