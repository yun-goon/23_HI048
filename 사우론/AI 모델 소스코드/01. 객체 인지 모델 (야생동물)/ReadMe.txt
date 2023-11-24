# 데이터셋 설정 방법
OriginData 디렉토리에 수정되기 전의 원본 데이터셋 저장
Dataset 디렉토리에는 학습하기 위해 가공된 데이터 저장 및 data.yaml, train.txt, test.txt, valid.txt 파일 작성

# 학습 진행 방법

yolov5 디렉토리로 이동 후 파이썬 패키지 설치
$ /yolov5 > pip install -r requirements.txt

학습 진행
$ /yolov5 > sudo python3 train.py --img 416 --batch 64 --epochs 100 --data ../Dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt

테스트 진행
$ /yolov5 > sudo python3 val.py --weights ./runs/train/exp/weights/best.pt --img 416 --task 'test' --data ../Dataset/data.yaml --save-txt
