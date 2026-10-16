import csv, random
from pathlib import Path
random.seed(91)
OUT=Path(__file__).parent/'data'/'historical_readings.csv'
rows=[]
for i in range(120):
    arm=f'ARM-{random.randint(1,10):02d}'; joint=random.choice(['shoulder','elbow','wrist'])
    torque=random.uniform(20,82); temperature=random.uniform(35,72); vibration=random.uniform(1.2,6.8)
    score=(torque/92)*.35+(temperature/88)*.30+(vibration/9.5)*.35
    label=1 if score>=.53 else 0
    if random.random()<.06: label=1-label
    rows.append([arm,joint,round(torque,2),round(temperature,2),round(vibration,2),label])
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['arm_id','joint','torque_nm','temperature_c','vibration_mm_s','wear_label']); w.writerows(rows)
print(f'Generated {len(rows)} labelled readings at {OUT}')
