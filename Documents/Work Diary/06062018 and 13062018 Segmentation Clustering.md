## 06/06/2018 and 13/06/2018
### Summary
I did some research on how to segment multiple receipts on single page and designed the whole OCR process. The results are satisfying mostly but not in some cases.
### Step 1 Set the threshold and preprocess the image
```python
origin_img = cv2.imread("sample/sample_7.jpg")  
img = cv2.resize(origin_img, None, fx=0.5, fy=0.5)  
width = img.shape[0]  
height = img.shape[1]  
  
blur = cv2.pyrMeanShiftFiltering(img, 15, 45)  
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)  
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```
### Step 2 Find contours based on the thresholds
```python
_, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
```
### Step 3 Change the data format to fit the Sklearn.Kmeans
```python
points = contours[0]  
for i in range(1, len(contours)):  
    points = np.concatenate((points, contours[i]), axis=0)  
  
final = points[0]  
for i in range(1, len(points)):  
    if points[i][0][0] != 0 and points[i][0][0] != height-1 and points[i][0][1] != 0 and points[i][0][1] != width-1:  
        final = np.append(final, points[i], axis=0)  
final_float = np.float32(final)
```
### Step 4 K-means clustering
```python
kmeans = KMeans(n_clusters=3, random_state=0).fit(final_float)
```
### Step 5 Find corner points using clustering results
```
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
print(corners)  
  
corner_points = dict()  
for c in corners:  
    corner_points[c] = [(corners[c][0], corners[c][1]), (corners[c][2], corners[c][1]), (corners[c][2], corners[c][3]), (corners[c][0], corners[c][3])]
```
### Step 6 Create masks and modify it based on preset corner
```python
for corner in corner_points.values():  
    mask = np.zeros(img.shape, dtype=np.uint8)  
    roi_corners = np.array([corner], dtype=np.int32)  
    print(roi_corners)  
    channel_count = img.shape[2]  
    ignore_mask_color = (255,)*channel_count  
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)  
    masked_image = cv2.bitwise_and(img, mask)  
    cv2.imshow('Display', masked_image)  
    cv2.waitKey()
```
### Step 7 Show the image 
```python
cv2.drawContours(img, contours, -1, (0, 0, 255), 6)  
for point in corners.values():  
    cv2.circle(img, (int(point[0]), int(point[1])), 10, (255, 255, 0), -1)  
    cv2.circle(img, (int(point[2]), int(point[3])), 10, (255, 255, 0), -1)  
for point in kmeans.cluster_centers_:  
    cv2.circle(img,(int(point[0]), int(point[1])), 10, (0, 255, 0), -1)  
cv2.imshow('Display', img)  
cv2.imwrite("contours.jpg", img)  
cv2.waitKey()
```
**Sample receipt**
![sample](https://github.com/E1even1ee/djangotest/blob/master/invoice/sample/sample_7.jpg)
**Contours division and center allocation**
![contours](https://github.com/E1even1ee/djangotest/blob/master/invoice/contours.jpg)
### Output
![output1](https://github.com/E1even1ee/djangotest/blob/master/invoice/output_1.jpg)
![output2](https://github.com/E1even1ee/djangotest/blob/master/invoice/output_2.jpg)
![output3](https://github.com/E1even1ee/djangotest/blob/master/invoice/output_3.jpg)