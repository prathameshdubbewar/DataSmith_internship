import numpy as np

def read_csv(file_path):
    data = np.genfromtxt(file_path, delimiter=',')
    return data

def cal_avg_score(scores):
    return np.mean(scores)

csv_file_path = 'file.csv'  

data = read_csv(csv_file_path)

if 'score' in data.dtype:  
    scores = data['score']
    average_score = cal_avg_score(scores)
    print(f"Avg Score: {average_score}")
