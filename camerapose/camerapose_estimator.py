import time
import cv2

def main():
    video_capture = cv2.VideoCapture(0)
    time.sleep(2.0)  # to give time to the camera to warm up

    if not video_capture.isOpened():
        print("Error: The camera resource is busy or unavailable")
    else:
        print("The video source has been opened correctly...")

    # Create the main window and move it
    cv2.namedWindow('Video')
    cv2.moveWindow('Video', 20, 20)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Initiate STAR detector
        orb = cv2.ORB_create()

        # find the keypoints with ORB
        kp = orb.detect(frame, None)

        # compute the descriptors with ORB
        kp, des = orb.compute(frame, kp)

        # draw only keypoints location,not size and orientation
        for marker in kp:
            img2 = cv2.drawMarker(frame, tuple(int(i) for i in marker.pt), color=(0, 255, 0))

        # Showing the frame and waiting
        # for the exit command
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    video_capture.release()
    print("Bye...")

if __name__ == "__main__":
    main()