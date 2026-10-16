from decision import joint_result
from wear_model import train_model
def test_hard_limit_overrides_prediction():
    model,_,_=train_model(); r={'arm_id':'T1','torque_nm':100,'temperature_c':40,'vibration_mm_s':2}; assert joint_result(r,model)[0]=='EMERGENCY_STOP'
def test_spoof_is_detected():
    model,_,_=train_model(); r={'arm_id':'T2','torque_nm':8,'temperature_c':76,'vibration_mm_s':7}; result,details=joint_result(r,model); assert result=='EMERGENCY_STOP' and details['reason']
def test_missing_sensor_requires_maintenance():
    model,_,_=train_model(); r={'arm_id':'T3','torque_nm':None,'temperature_c':45,'vibration_mm_s':2}; assert joint_result(r,model)[0]=='SCHEDULE_MAINTENANCE'
def test_normal_reading_is_safe():
    model,_,_=train_model(); r={'arm_id':'T4','torque_nm':35,'temperature_c':40,'vibration_mm_s':1.5}; assert joint_result(r,model)[0]=='SAFE'
