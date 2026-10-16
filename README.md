# Robotic Arm Joint Health Monitoring System

Independent implementation using a deterministic safety gate, Random Forest wear classifier, independent maintenance-note evidence, and cross-sensor spoof checks.

## Run

pip install -r requirements.txt
python generate_dataset.py
python main.py
python -m pytest -q

Safety limits are evaluated before predictive inference. The system demonstrates SAFE, MONITOR, SCHEDULE_MAINTENANCE, and EMERGENCY_STOP outcomes.
