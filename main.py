import cv2
import numpy as np


def find_color(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([color[0] - 10, 100, 100])
    upper_color = np.array([color[0] + 10, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)


def main():
    color = (0, 255, 0)  # Зеленый цвет
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        find_color(frame, color)

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('r'):
            color = (0, 0, 255)  # Красный
        elif key == ord('g'):
            color = (60, 255, 0)  # Зеленый
        elif key == ord('b'):
            color = (120, 255, 255)  # Синий

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()