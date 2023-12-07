import cv2
from matplotlib import pyplot as plt
import numpy as np

# Đường dẫn đến file ảnh
green_light = r'lights/green.jpg'
red_light = r'lights/red.jpg'
yellow_light = r'lights/yellow.jpg'

# Tham số cho ROI
x, y, w, h = (1700, 40, 100, 250)

def show_roi_hsv_binarymask(roi, hsv, bin_mask, color):
    # Plot the roi and binary mask
    fig, axes = plt.subplots(1, 4, figsize=(15, 5))
    # frame roi bgr (windows default)
    axes[0].imshow(roi)
    axes[0].set_title('ROI ORG BGR')
    # frame roi rgb (windows default)
    axes[1].imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    axes[1].set_title('ROI ORG RGB')
    # roi hsv
    axes[2].imshow(hsv)
    axes[2].set_title('ROI HSV')
    # binary mask
    axes[3].imshow(bin_mask, cmap='gray')
    axes[3].set_title(f'{color} binary mask')
    # Hiển thị ảnh
    plt.show()

# Đọc ảnh từ đường dẫn
image = cv2.imread(red_light)

# Kiểm tra xem ảnh có đọc thành công không
if image is not None:
    # Hiển thị ảnh
    roi = image[y:y+h, x:x+w]

    # Convert ROI to HSV color space
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Edit red range here
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])

    # Edit yellow range here
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    # Create binary masks for detecting red and yellow in the ROI
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

    # Check which color is present based on the masks
    if cv2.countNonZero(red_mask) > 0:
        show_roi_hsv_binarymask(roi, hsv, red_mask, 'red')

    elif cv2.countNonZero(yellow_mask) > 0:
        show_roi_hsv_binarymask(roi, hsv, yellow_mask, 'yellow')

    # cv2.imshow('Image', roi)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('error')
