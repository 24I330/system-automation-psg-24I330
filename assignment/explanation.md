# Design Explanation

## Safety
Hard limits are 92 Nm torque, 88 C temperature, and 9.5 mm/s vibration. These deterministic checks run before ML.

## Predictive model
The supplied generator creates 120 labelled historical readings. A Random Forest uses normalized torque, temperature and vibration and returns a wear probability.

## Maintenance logs
Twelve notes are included, with relevant and irrelevant entries. Keyword evidence is scored independently, with simple nearby negation handling.

## Signal combination
High model probability plus maintenance evidence schedules maintenance. Moderate model evidence, a watch-range sensor, or log evidence alone produces MONITOR.

## Spoof defense
The implementation looks for a very low torque value accompanied by high temperature and vibration, and for an implausibly large torque jump. This can detect simple torque-masking attacks but is not cryptographic sensor authentication and can miss coordinated multi-sensor attacks.

## Priority
EMERGENCY_STOP > SCHEDULE_MAINTENANCE > MONITOR > SAFE.
