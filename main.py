import cv2
import numpy as np
import os


# 폴더 안에 파일 읽어오기
gt_depth_path = '/home/taeyoungkim/Desktop/MinMaxNormalization/gt_depth'
file_list = os.listdir(gt_depth_path)

pred_depth_path = '/home/taeyoungkim/Desktop/MinMaxNormalization/pred_depth'
# 폴더 내 파일을 오름차순으로 정렬 - 반드시 파일 이름이 숫자여야 함!!
# 순서가 매우 중요하기 때문이다.
file_list_pred = os.listdir(pred_depth_path)
file_list_pred.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

max_avg = 0

# real depth data에서 각 이미지 마다 최대값을 구한 후, 모든 이미지의 최대값을 평균을 낸다.
print('Calculating average max Value...')

# 폴더 안에 파일 하나씩 읽기
for gt_path in file_list:
    depth_img = cv2.imread('gt_depth/'+gt_path)
    target_max = depth_img[...,0].max() # all channel have same value
    max_avg += target_max   # 모두 max value를 더한다.

# 평균 내고 반올림 한 수를 구한다.
max_avg = round(max_avg / len(file_list))

print('Finished calculating!')
print('max_avg : ',max_avg)

# 방금 구한 max value를 이용하여 predict_depth값을 normalized 작업을 거친다.
# output을 폴더 하나를 생성하여 그 안에 모두 저장한다.

output_path = './output'
if not os.path.isdir(output_path):
    os.mkdir(output_path)
    print('Create New Output Folder!')

print("Start Normalizing source images...")
i = 0 # output의 이름을 순서대로 만들기 위해서
# 폴더 안에 파일 하나씩 읽기
for pred_path in file_list_pred:
    depth_pred_img = cv2.imread('pred_depth/'+pred_path)
    height, width, _ = depth_pred_img.shape
    # normalized 작업을 진행한다.
    normal_pred = np.zeros((height, width))
    normal_pred = cv2.normalize(depth_pred_img, normal_pred, 0, max_avg, cv2.NORM_MINMAX)

    cv2.imwrite(output_path+'/%d_depth_norm.jpg' %i,normal_pred)
    i += 1

print('Finished!')