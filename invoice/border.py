import cv2
import numpy as np

np.set_printoptions(threshold='nan')

origin_img = cv2.imread("sample/sample_6.jpg")
img = cv2.resize(origin_img, None, fx=0.6, fy=0.6)
img_for_crop = cv2.resize(origin_img, None, fx=0.6, fy=0.6)
height = img.shape[0]
width = img.shape[1]
blur = cv2.pyrMeanShiftFiltering(img, 10, 30)
cv2.imwrite("output/step1.jpg", blur)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

lower_gray = np.array([120, 120, 120], dtype="uint8")
upper_gray = np.array([250, 250, 250], dtype="uint8")

mask = cv2.inRange(blur, lower_gray, upper_gray)
cv2.imwrite("output/step2.jpg", mask)
new_mask = np.zeros(mask.shape, dtype=np.uint8)
new_mask[:][:] = 255


black_points = []
for row in range(int(0.03*len(mask)), int(0.97*len(mask))):
    for col in range(int(0.03*len(mask[row])), int(0.97*len(mask[row]))):
        if mask[row][col] == 0:
            black_points.append((row, col))
for point in black_points:
    cv2.circle(new_mask, (int(point[1]), int(point[0])), 4, (0, 0, 0), -1)

cv2.imwrite("output/step3.jpg", new_mask)

edges = cv2.Canny(new_mask, 100, 200, apertureSize=3)

cv2.imwrite("output/step4.jpg", edges)

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
    print(x1, y1, x2, y2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite("output/step5.jpg", img)

row_line_floor.sort()
row_line_ceil.sort()
col_line_floor.sort()
col_line_ceil.sort()
# row_line_check = []
# for i in range(len(row_line_floor)):
#     temp = []
#     for j in range(len(new_mask[0])):
#         temp.append(bool(new_mask[row_line_floor[i]][j]) ^ bool(new_mask[row_line_ceil[i]][j]))
#         # temp.append((bool(new_mask[row_line_floor[i]][j]) ^ bool(new_mask[row_line_ceil[i]][j])) or not (bool(new_mask[row_line_floor[i]][j]) | bool(new_mask[row_line_ceil[i]][j])))
#     row_line_check.append(temp)
#
# for i in range(len(row_line_check)):
#     for j in range(len(row_line_check[i])):
#         if row_line_check[i][j]:
#             if 3 < j < len(row_line_check[i]) - 5:
#                 if row_line_check[i][j-4:j+5].count(False) >= 6:
#                     row_line_check[i][j] = False

# print(col_line_ceil)
# print(row_line_floor)
# print(row_line_ceil)
# row_line_check_index = []
# for row in row_line_check:
#     row_line_check_index.append([row.index(True), len(row) - 1 - row[::-1].index(True)])
# print(row_line_check_index)

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


# col_group.append([int(width)])
row_group.append([int(height)])
print(col_group)
print(row_group)
crop_corner = []
# crop_flag = []
# for i in range(len(row_line_check_index)):
#     if row_line_check_index[i][1] - row_line_check_index[i][0] > 0.8*width:
#         continue
#     for j in range(i, len(row_line_check_index)):
#         if row_line_check_index[j][1] - row_line_check_index[j][0] > 0.8*width:
#             continue
#         if abs(row_line_check_index[i][0] - row_line_check_index[j][0]) <= 10 \
#                 and abs(row_line_check_index[i][1] - row_line_check_index[j][1]) <= 10\
#                 and row_line_ceil[j] - row_line_ceil[i] > 100:
#             crop_corner.append([row_line_floor[i], row_line_ceil[j], row_line_check_index[i][0], row_line_check_index[i][1]])
# print(crop_corner)
print(height, width)
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
                # if ii == len(row_group) - 1:
                #     row_max = height
                if j == 0:
                    col_min = 0
                if jj == len(col_group) - 1:
                    col_max = width
                crop_corner.append([row_min, row_max, col_min, col_max])
print(crop_corner)

corner_count = 1
final_crop_corner = []
for corner in crop_corner:
    if 0.25*width < corner[3]-corner[2] < 0.4*width and 0.25*height < corner[1]-corner[0]:
        final_crop_corner.append(corner)
print(final_crop_corner)

for corner in final_crop_corner:
    crop = img_for_crop[corner[0]:corner[1], corner[2]:corner[3]]
    cv2.imwrite("output/output_" + str(corner_count) + ".jpg", crop)
    corner_count += 1
    # cv2.imshow('Display', crop)
    # cv2.waitKey()

cv2.imshow('Display', img)
cv2.waitKey()