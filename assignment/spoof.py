from config import SPOOF_RULES
def detect_spoof(reading, previous=None):
    reasons=[]
    if reading['torque_nm']<=SPOOF_RULES['low_torque_nm'] and reading['temperature_c']>=SPOOF_RULES['high_temperature_c'] and reading['vibration_mm_s']>=SPOOF_RULES['high_vibration_mm_s']:
        reasons.append('torque is unusually low while temperature and vibration are high')
    if previous is not None:
        jump=abs(reading['torque_nm']-previous['torque_nm'])
        if jump>=SPOOF_RULES['max_torque_jump_nm']: reasons.append(f'implausible torque jump of {jump:.1f} Nm')
    return reasons
