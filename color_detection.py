import cv2
import numpy as np

camera=cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

class color_detection:
    def detection_for_rectangles(self):
        self.u=False
        self.l = False
        self.d=False
        self.r = False

        while True:
            ret,frame=camera.read()
            frame=cv2.flip(frame,1)

            #-------------------------- Up Rectangle -------------------------------------:
            x_up, y_up, w_up, h_up = (240, 10, 150, 150)
            rect_up=frame[y_up:y_up+h_up,x_up:x_up+w_up]
            hsv_frame_up = cv2.cvtColor(rect_up, cv2.COLOR_BGR2HSV)
            blue_up = cv2.inRange(hsv_frame_up, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_up, kernal)
            res_blue = cv2.bitwise_and(rect_up, rect_up,
                                       mask=blue_mask)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_up = cv2.rectangle(blue_up, (x, y),
                                            (x + w, y + h),
                                            (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Up Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0),2)
                    self.u = True
                else:
                    self.u = False

            #----------------------------- Left Rectangle -----------------------------------------:
            x_left, y_left, w_left, h_left = (10, 170, 150, 150)
            rect_left = frame[y_left:y_left + h_left, x_left:x_left + w_left]
            hsv_frame_left = cv2.cvtColor(rect_left, cv2.COLOR_BGR2HSV)
            blue_left = cv2.inRange(hsv_frame_left, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_left, kernal)
            res_blue =  cv2.bitwise_and(rect_left,rect_left,blue_left)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_left = cv2.rectangle(blue_left, (x, y),
                                            (x + w, y + h),
                                            (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Left Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0),2)
                    self.l = True
                else:
                    self.l = False

            #----------------------------- Down Rectangle --------------------------------------:
            x_down, y_down, w_down, h_down = (240, 310, 150, 150)
            rect_down = frame[y_down:y_down + h_down, x_down:x_down + w_down]
            hsv_frame_down=cv2.cvtColor(rect_down,cv2.COLOR_BGR2HSV)
            blue_down=cv2.inRange(hsv_frame_down, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_down, kernal)
            res_blue =  cv2.bitwise_and(rect_down,rect_down,blue_down)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_down = cv2.rectangle(blue_down, (x, y),
                                            (x + w, y + h),
                                            (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Down Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0),2)
                    self.d = True
                else:
                    self.d = False

            # ----------------------------- Right Rectangle --------------------------------------:
            x_right, y_right, w_right, h_right = (480, 170, 150, 150)
            rect_right = frame[y_right:y_right + h_right, x_right:x_right + w_right]
            hsv_frame_right = cv2.cvtColor(rect_right, cv2.COLOR_BGR2HSV)
            blue_right = cv2.inRange(hsv_frame_right, (100, 150, 0), (140, 255, 255))
            kernal = np.ones((5, 5), "uint8")
            blue_mask = cv2.dilate(blue_right, kernal)
            res_blue =  cv2.bitwise_and(rect_right,rect_right,blue_right)
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    blue_right = cv2.rectangle(blue_right, (x, y),
                                              (x + w, y + h),
                                              (0, 0, 255), 2)
                    cv2.putText(frame, "Blue Right Colour", (200, 250),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0), 2)
                    self.r = True
                else:
                    self.r = False

            cv2.rectangle(frame, (x_right, y_right), (x_right + w_right, y_right + h_right), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_down, y_down), (x_down + w_down, y_down + h_down), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_left, y_left), (x_left + w_left, y_left + h_left), (0, 255, 0), 3)
            cv2.rectangle(frame, (x_up, y_up), (x_up + w_up, y_up + h_up), (0, 255, 0), 3)
            cv2.imshow("Frame", frame)
            cv2.imshow("Blue Up Frame", blue_up)
            cv2.imshow("Blue Left Frame", blue_left)
            cv2.imshow("Blue Down Frame",blue_down)
            cv2.imshow("Blue Right Frame", blue_right)
            print("Durum Up = ", self.u,"\n")
            print("Durum Left",self.l,"\n")
            print("Durum Down", self.d,"\n")
            print("Durum Right",self.r,"\n")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

detect=color_detection()
detect.detection_for_rectangles()