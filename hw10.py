import pickle
import os

def save_scores(filename, scores):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            scores = pickle.load(file)
            return scores
    else:
        return None

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

# 사용자로부터 학생들의 수 입력 받기
num_students = int(input("학생 수를 입력하세요: "))

# 학생들의 점수 입력 받기
scores = []
for i in range(num_students):
    score = float(input(f"학생 {i+1}의 점수를 입력하세요: "))
    scores.append(score)

# 점수들의 평균 계산
average = calculate_average(scores)
print("평균 점수:", average)

# 파일 경로
file_path = "scores.pkl"

# 점수들을 파일에 저장
save_scores(file_path, scores)
print("점수가 파일에 저장되었습니다.")

# 파일에서 점수들을 로드하여 출력
loaded_scores = load_scores(file_path)
if loaded_scores is not None:
    print("파일 내의 점수들:")
    for score in loaded_scores:
        print(score)
else:
    print("파일이 존재하지 않습니다.")
