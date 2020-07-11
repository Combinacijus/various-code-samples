# For key places find "NOTE:" comments (without quotes)

import cv2
import requests  # NOTE: Only used for forceful reconnection
import time  # NOTE: Only used for throttling down printing when connection is lost


class IPVideoCapture:
    def __init__(self, cam_address, cam_force_address=None, blocking=False):
        """
        :param cam_address: ip address of the camera feed
        :param cam_force_address: ip address to disconnect other clients (forcefully take over)
        :param blocking: if true read() and reconnect_camera() methods blocks until ip camera is reconnected
        """

        self.cam_address = cam_address
        self.cam_force_address = cam_force_address
        self.blocking = blocking
        self.capture = None

        self.RECONNECTION_PERIOD = 0.5  # NOTE: Can be changed. Used to throttle down printing

        self.reconnect_camera()

    def reconnect_camera(self):
        while True:
            try:
                if self.cam_force_address is not None:
                    requests.get(self.cam_force_address)

                self.capture = cv2.VideoCapture(self.cam_address)

                if not self.capture.isOpened():
                    raise Exception("Could not connect to a camera: {0}".format(self.cam_address))

                print("Connected to a camera: {}".format(self.cam_address))

                break
            except Exception as e:
                print(e)

                if self.blocking is False:
                    break

                time.sleep(self.RECONNECTION_PERIOD)

    def read(self):
        """
        Reads frame and if frame is not received tries to reconnect the camera

        :return: ret - bool witch specifies if frame was read successfully
                 frame - opencv image from the camera
        """

        ret, frame = self.capture.read()

        if ret is False:
            self.reconnect_camera()

        return ret, frame


if __name__ == "__main__":
    CAM_ADDRESS = "http://192.168.8.102:4747/video"  # NOTE: Change
    CAM_FORCE_ADDRESS = "http://192.168.8.102:4747/override"  # NOTE: Change or omit
    cap = IPVideoCapture(CAM_ADDRESS, CAM_FORCE_ADDRESS, blocking=True)
    # cap = IPVideoCapture(CAM_ADDRESS)  # Minimal init example

    while True:
        ret, frame = cap.read()

        if ret is True:
            cv2.imshow(CAM_ADDRESS, frame)

        if cv2.waitKey(1) == ord("q"):
            break
