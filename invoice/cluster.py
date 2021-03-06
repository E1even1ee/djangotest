import cv2
import numpy as np
from sklearn.cluster import KMeans

np.set_printoptions(threshold=np.nan)

origin_img = cv2.imread("sample/sample_5.jpg")
img = cv2.resize(origin_img, None, fx=0.5, fy=0.5)
width = img.shape[0]
height = img.shape[1]

blur = cv2.pyrMeanShiftFiltering(img, 15, 45)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

points = contours[0]
for i in range(1, len(contours)):
    points = np.concatenate((points, contours[i]), axis=0)

final = points[0]
for i in range(1, len(points)):
    if points[i][0][0] != 0 and points[i][0][0] != height-1 and points[i][0][1] != 0 and points[i][0][1] != width-1:
        final = np.append(final, points[i], axis=0)
print(final)
final_float = np.float32(final)

kmeans = KMeans(n_clusters=6, random_state=0).fit(final_float)

corners = dict()

for i in range(len(kmeans.labels_)):
    if kmeans.labels_[i] not in corners:
        corners[kmeans.labels_[i]] = [final[i][0], final[i][1], final[i][0], final[i][1]]
    else:
        if final[i][0] < corners[kmeans.labels_[i]][0]:
            corners[kmeans.labels_[i]][0] = final[i][0]
        if final[i][1] < corners[kmeans.labels_[i]][1]:
            corners[kmeans.labels_[i]][1] = final[i][1]
        if final[i][0] > corners[kmeans.labels_[i]][2]:
            corners[kmeans.labels_[i]][2] = final[i][0]
        if final[i][1] > corners[kmeans.labels_[i]][3]:
            corners[kmeans.labels_[i]][3] = final[i][1]

corner_points = dict()
for c in corners:
    corner_points[c] = [(corners[c][0], corners[c][1]), (corners[c][2], corners[c][1]),
                        (corners[c][2], corners[c][3]), (corners[c][0], corners[c][3])]

corner_count = 1
for corner in corner_points.values():
    mask = np.zeros(img.shape, dtype=np.uint8)
    roi_corners = np.array([corner], dtype=np.int32)
    print(roi_corners)
    channel_count = img.shape[2]
    ignore_mask_color = (255,)*channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    # cv2.imwrite("output_" + str(corner_count) + ".jpg", masked_image)
    # corner_count += 1
    cv2.imshow('Display', masked_image)
    cv2.waitKey()

cv2.drawContours(img, contours, -1, (0, 0, 255), 6)
for point in corners.values():
    cv2.circle(img, (int(point[0]), int(point[1])), 10, (255, 255, 0), -1)
    cv2.circle(img, (int(point[2]), int(point[3])), 10, (255, 255, 0), -1)
for point in kmeans.cluster_centers_:
    cv2.circle(img, (int(point[0]), int(point[1])), 10, (0, 255, 0), -1)
cv2.imshow('Display', img)
cv2.waitKey()
