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

    prev_frame = None

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if prev_frame is not None:
            # use previous frame here
            pass

        """
        detect key feature points using sift
        Requires - opencv-python==3.4.2.16, opencv-contrib-python==3.4.2.16
        """
        # sift = cv2.xfeatures2d.SIFT_create()
        # kp_curr, des_curr = sift.detectAndCompute(frame, None)
        # kp_prev, des_prev = sift.detectAndCompute(prev_frame, None)

        """
        detect key feature points using ORB
        Requires - opencv-python==3.4.2.16, opencv-contrib-python==3.4.2.16
        """
        # Initiate STAR detector
        orb = cv2.ORB_create()

        # find the keypoints and compute the descriptors with ORB for previous frame
        kp_prev, des_prev = orb.detectAndCompute(prev_frame, None)

        # find the keypoints and compute the descriptors with ORB for current frame
        kp_curr, des_curr = orb.detectAndCompute(frame, None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des_prev, des_curr)

        # Sort them in the order of their distance.
        matches = sorted(matches, key=lambda x: x.distance)

        frame_mod = frame.copy()
        frame_mod = cv2.drawMatches(prev_frame, kp_prev, frame, kp_curr, matches[:10], frame_mod, flags=2)

        # save current frame
        prev_frame = frame

        # Showing the frame and waiting
        # for the exit command
        cv2.imshow('Video', frame_mod)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    video_capture.release()
    print("Bye...")

if __name__ == "__main__":
    main()