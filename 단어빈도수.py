import pandas as pd
from collections import Counter
import re

# CSV 파일 읽기
df = pd.read_csv('/workspace/baseline/data/train_data.csv')

# 모든 텍스트 데이터를 하나의 문자열로 결합
text_data = ' '.join(df.astype(str).values.flatten())

# 문자열을 단어 단위로 분할 (정규 표현식을 사용하여 단어만 추출)
words = re.findall(r'\b\w+\b', text_data)

# 각 단어의 빈도 수 계산
word_counts = Counter(words)

# 가장 많이 쓰인 단어 상위 20개 출력
for word, count in word_counts.most_common(20):
    print(f'{word}: {count}')