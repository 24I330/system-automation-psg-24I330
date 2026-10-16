from config import HARD_LIMITS, WATCH_LIMITS
def inspect_reading(reading):
    required=['torque_nm','temperature_c','vibration_mm_s']
    if any(reading.get(k) is None for k in required): return [], ['missing critical sensor']
    emergencies=[]; warnings=[]
    for k,limit in HARD_LIMITS.items():
        if reading[k]>=limit: emergencies.append(f'{k} reached hard limit ({reading[k]})')
    for k,limit in WATCH_LIMITS.items():
        if limit<=reading[k]<HARD_LIMITS[k]: warnings.append(f'{k} entered watch range ({reading[k]})')
    return emergencies,warnings
