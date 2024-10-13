import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('/workspace/baseline/data/train_data.csv')

# 여러 단어를 다른 단어로 바꾸기 위한 딕셔너리
replace_dict = {
    '다음': '다음 예시 중',
    '무엇입니까 ?': '어떤 것 입니까 ?',
    '시나리오': '선택지',
    '의미': '뜻' ,
    '우아한' : '아름다운',
    '가장' : '제일',
    '새로운' : '새로운 것',
    '잘못되지'  : '잘못되지 않게',
    '때' : '시점',
    '것은' : '것은 다음과 같습니다',
}

# 여러 단어를 한 번에 바꾸기
df = df.replace(replace_dict, regex=True)

# 변경된 내용을 새로운 CSV 파일로 저장
df.to_csv('train_data_modified.csv', index=False)