## 14/06/2018 and 15/06/2018
### Summary
Back in the previous approach, I detected the contours of receipts and then collected them into groups using K-means model by SKlearn, It works pretty well but the principle of this solution depends on equal contours distribution, which means if the size and density of receipts vary a lot all the center and corner will be distracted by others.
**New approach**
As what I observed, almost all the receipt samples are allocated in grid and the borders of them are all pretty significant, which drives me to detect the border and try to cut them accordingly.
### Preprocess
There are several steps in terms of the preprocess to make it easier to get rid of the noise and detect the borders.
#### Original input
![step0](https://github.com/E1even1ee/djangotest/blob/master/invoice/sample/sample_6.jpg)
#### Blurring
Blurring helps get rid of the messy background
```python
blur = cv2.pyrMeanShiftFiltering(img, 10, 30)
```
![step1](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/step1.jpg)
#### Mask
Then I set the lower and upper threshold to tear off the gray background while trying to save as much as contents in the middle
```python
lower_gray = np.array([120, 120, 120], dtype="uint8")
upper_gray = np.array([250, 250, 250], dtype="uint8")
mask = cv2.inRange(blur, lower_gray, upper_gray)
```
![step2](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/step2.jpg)
#### New mask
As there are still plenty of holes in the receipts, I draw black points based on the masked pixel of last process, which makes the mask much cleaner and easier to detect the lines
```python
new_mask = np.zeros(mask.shape, dtype=np.uint8)  
new_mask[:][:] = 255  
black_points = []  
for row in range(int(0.03*len(mask)), int(0.97*len(mask))):  
    for col in range(int(0.03*len(mask[row])), int(0.97*len(mask[row]))):  
        if mask[row][col] == 0:  
            black_points.append((row, col))  
for point in black_points:  
    cv2.circle(new_mask, (int(point[1]), int(point[0])), 4, (0, 0, 0), -1)
```
![step3](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/step3.jpg)
#### Canny edges
Canny can make the mask even cleaner
```python
edges = cv2.Canny(new_mask, 100, 200, apertureSize=3)
```
![step4](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/step4.jpg)
#### Draw the lines
According to the lines drawing by HoughLine, I adjust the parameters to filter out most bad results without impact on the lines I really want
```python
lines = cv2.HoughLines(edges, 1, np.pi/18, img.shape[1]//12)  
row_line_ceil = []  
col_line_ceil = []  
row_line_floor = []  
col_line_floor = []  
for line in lines:  
    rho = line[0][0]  
    theta = line[0][1]  
    a = np.cos(theta)  
    b = np.sin(theta)  
    x0 = a*rho  
    y0 = b*rho  
    x1 = int(x0 + 1000*(-b))  
    y1 = int(y0 + 1000*a)  
    x2 = int(x0 - 1000*(-b))  
    y2 = int(y0 - 1000*a)  
    if max(abs(x1), abs(x2)) == 1000:  
        row_line_floor.append(min(y1, y2)-2)  
        row_line_ceil.append(max(y1, y2)+2)  
    if max(abs(y1), abs(y2)) == 1000:  
        col_line_floor.append(min(x1, x2))  
        col_line_ceil.append(max(x1, x2))  
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
```
![step5](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/step5.jpg)
### Play with the lines
The original output of the lines are like below
```
(230, 1000, 230, -1000)
(21, 1000, 21, -1000)
(18, 1000, 18, -1000)
(-999, 1022, 1000, 1021)
(-999, 544, 1000, 543)
(227, 1000, 227, -1000)
(476, 1000, 476, -1000)
(-999, 53, 1000, 52)
(478, 1000, 478, -1000)
(-999, 552, 1000, 551)
(686, 1000, 686, -1000)
(270, 1000, 270, -1000)
(-999, 30, 1000, 29)
(683, 1000, 683, -1000)
(459, 1000, 459, -1000)
(455, 1000, 455, -1000)
(-999, 550, 1000, 549)
(482, 1000, 482, -1000)
```
Then I sort and make them into groups
```python
row_line_floor.sort()  
row_line_ceil.sort()  
col_line_floor.sort()  
col_line_ceil.sort()

col_group = []  
col_flag = [False]*len(col_line_ceil)  
for i in range(len(col_line_ceil)):  
    if len(col_group) == 0:  
        col_group.append([col_line_ceil[i]])  
        col_flag[i] = True  
        continue  
    for col in col_group:  
        if abs(col_line_ceil[i] - sum(col)/float(len(col))) <= 0.07*max(height, width):  
            col.append(col_line_ceil[i])  
            col_flag[i] = True  
            break  
    if not col_flag[i]:  
        col_group.append([col_line_ceil[i]])  
  
  
row_group = []  
row_flag = [False]*len(row_line_ceil)  
for i in range(len(row_line_ceil)):  
    if len(row_group) == 0:  
        row_group.append([row_line_ceil[i]])  
        row_flag[i] = True  
        continue  
    for row in row_group:  
        if abs(row_line_ceil[i] - sum(row)/float(len(row))) <= 0.07*max(height, width):  
            row.append(row_line_ceil[i])  
            row_flag[i] = True  
            break  
    if not row_flag[i]:  
        row_group.append([row_line_ceil[i]])
```
And the row and col groups are like:
```
[[18, 21], [227, 230, 270], [455, 459, 476, 478, 482], [683, 686]]
[[32, 55], [546, 552, 554], [1024], [1051]]
```
Then I try to make use of the lines, forming the cropping corner matrix
```python
for i in range(len(row_group)-1):  
    for ii in range(i+1, len(row_group)):  
        for j in range(len(col_group)-1):  
            for jj in range(j+1, len(col_group)):  
                row_min = min(row_group[i])  
                row_max = max(row_group[ii])  
                col_min = min(col_group[j])  
                col_max = max(col_group[jj])  
                if i == 0:  
                    row_min = 0  
                if j == 0:  
                    col_min = 0  
                if jj == len(col_group) - 1:  
                    col_max = width  
                crop_corner.append([row_min, row_max, col_min, col_max])
```
Finally I refine the result to cut the image more reasonably
```python
final_crop_corner = []  
for corner in crop_corner:  
    if 0.25*width < corner[3]-corner[2] < 0.4*width and 0.25*height < corner[1]-corner[0]:  
        final_crop_corner.append(corner)
```
```
[[0, 554, 0, 270]
[0, 554, 227, 482]
[0, 554, 455, 744L]
[0, 1024, 0, 270]
[0, 1024, 227, 482]
[0, 1024, 455, 744L]
[0, 1051, 0, 270]
[0, 1051, 227, 482]
[0, 1051, 455, 744L]
[546, 1024, 0, 270]
[546, 1024, 227, 482]
[546, 1024, 455, 744L]
[546, 1051, 0, 270]
[546, 1051, 227, 482]
[546, 1051, 455, 744L]]
```
### Sample output
![output](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/output_1.jpg)
![output](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/output_2.jpg)
![output](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/output_3.jpg)
![output](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/output_13.jpg)
![output](https://github.com/E1even1ee/djangotest/blob/master/invoice/output/output_14.jpg)
### Conclusion
This approach fits more specifically on most samples I got, and around 90% percent of them can be segmented using it. It also should be working to images in any resolution, with different running time perhaps. Another big concern is the redundancy. As I don't want to refine out any of the useful results, I set a relatively tolerant threshold parameter to keep more results, so there will be around 2-3 times redundancy, depending on the exact case.