from safety import inspect_reading
from spoof import detect_spoof
from maintenance import score_arm
from config import MODEL
PRIORITY={'SAFE':0,'MONITOR':1,'SCHEDULE_MAINTENANCE':2,'EMERGENCY_STOP':3}
def joint_result(reading,model,previous=None):
    hard,warnings=inspect_reading(reading)
    if hard: return 'EMERGENCY_STOP',{'reason':hard}
    if any(reading.get(k) is None for k in ['torque_nm','temperature_c','vibration_mm_s']): return 'SCHEDULE_MAINTENANCE',{'reason':['missing sensor']}
    spoof=detect_spoof(reading,previous)
    if spoof: return 'EMERGENCY_STOP',{'reason':spoof}
    probability=model.predict_proba([[reading['torque_nm']/92,reading['temperature_c']/88,reading['vibration_mm_s']/9.5]])[0][1]
    log_score,keywords=score_arm(reading['arm_id'])
    if probability>=MODEL['high_probability'] and log_score>0: return 'SCHEDULE_MAINTENANCE',{'wear_probability':round(float(probability),3),'log_keywords':keywords}
    if probability>=MODEL['moderate_probability'] or warnings or log_score>0: return 'MONITOR',{'wear_probability':round(float(probability),3),'log_keywords':keywords,'warnings':warnings}
    return 'SAFE',{'wear_probability':round(float(probability),3)}
def arm_result(readings,model):
    best=('SAFE',{}); previous=None
    for r in readings:
        result,details=joint_result(r,model,previous)
        if PRIORITY[result]>PRIORITY[best[0]]: best=(result,details)
        previous=r
    return best
