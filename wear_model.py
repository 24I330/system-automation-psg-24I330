import csv
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from config import HARD_LIMITS
DATA=Path(__file__).parent/'data'/'historical_readings.csv'
def load_data():
    X=[]; y=[]
    with DATA.open(newline='',encoding='utf-8') as f:
        for r in csv.DictReader(f):
            X.append([float(r['torque_nm'])/HARD_LIMITS['torque_nm'],float(r['temperature_c'])/HARD_LIMITS['temperature_c'],float(r['vibration_mm_s'])/HARD_LIMITS['vibration_mm_s']]); y.append(int(r['wear_label']))
    return X,y
def train_model():
    X,y=load_data(); xt,xv,yt,yv=train_test_split(X,y,test_size=.25,random_state=17,stratify=y)
    model=RandomForestClassifier(n_estimators=80,max_depth=5,min_samples_leaf=3,random_state=17); model.fit(xt,yt)
    p=model.predict(xv); return model,accuracy_score(yv,p),confusion_matrix(yv,p).tolist()
