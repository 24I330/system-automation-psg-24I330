from wear_model import train_model

def demo_readings():
    return [
      {'arm_id':'DEMO-SAFE','torque_nm':42.0,'temperature_c':44.0,'vibration_mm_s':2.0},
      {'arm_id':'DEMO-MONITOR','torque_nm':70.0,'temperature_c':60.0,'vibration_mm_s':3.8},
      {'arm_id':'ARM-05','torque_nm':80.0,'temperature_c':75.0,'vibration_mm_s':6.0},
      {'arm_id':'DEMO-STOP','torque_nm':96.0,'temperature_c':50.0,'vibration_mm_s':2.0},
      {'arm_id':'DEMO-SPOOF','torque_nm':8.0,'temperature_c':76.0,'vibration_mm_s':7.0}]

def main():
    model,accuracy,matrix=train_model(); print('=== Robotic Arm Joint Health Monitor ==='); print(f'Validation accuracy: {accuracy:.3f}'); print(f'Confusion matrix: {matrix}')
    for r in demo_readings():
        from decision import joint_result
        result,details=joint_result(r,model); print(f"{r['arm_id']}: {result}"); print(f'  details: {details}')
if __name__=='__main__': main()
