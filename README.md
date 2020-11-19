# Image Min Max Normalization

## Repository 설명
`gt_depth`에 있는 이미지들을 모두 불러온 다음,  
각각 이미지 마다 max value 값을 계산하고 평균을 낸다.  

그 max value를 이용하여 0~255 범위로 되어 있는 `pred_depth`폴더 안에 이미지들을  
0 ~ max value까지 normalized 된 이미지로 바꿔주고,  
바뀐 이미지를 `output`폴더에 저장한다.  

## 사용 방법  

Ubuntu 18.04를 기준으로 터미널 창에 다음과 같이 입력한다.  
- `git clone https://github.com/Taeyoung96/Image_Min_Max_Normalization.git`  
- `cd Image_Min_Max_Normalization`  
- `python main.py` **`main.py`안에 있는 절대 경로를 자신의 경로에 맞춰서 실행해주자!**




