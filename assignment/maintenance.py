import re
from pathlib import Path
POSITIVE={'overheat','overheating','bearing','friction','rough','noise','drift','lubrication','vibration'}
NEGATION={'no','not','without','never'}
def read_notes():
    path=Path(__file__).parent/'data'/'maintenance_log.txt'; out=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            date,arm,note=[x.strip() for x in line.split('|',2)]; out.append({'date':date,'arm':arm,'note':note})
    return out
def score_arm(arm_id):
    score=0; matched=[]
    for e in read_notes():
        if e['arm']!=arm_id: continue
        words=re.findall(r'[a-z]+',e['note'].lower())
        for i,w in enumerate(words):
            if w in POSITIVE and not any(x in NEGATION for x in words[max(0,i-2):i]): score+=1; matched.append(w)
    return score,sorted(set(matched))
