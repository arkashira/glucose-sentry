import pytest
from glucose_sentry import detect_glucose_level, normalize_glucose_level, display_glucose_level
from glucose_sentry import SensorData

def test_detect_glucose_level():
    sensor_data = [
        SensorData(glucose_level=100, calibration_factor=1.0),
        SensorData(glucose_level=120, calibration_factor=1.0),
        SensorData(glucose_level=110, calibration_factor=1.0),
    ]
    glucose_level = detect_glucose_level(sensor_data)
    assert glucose_level == 110.0

def test_detect_glucose_level_empty_data():
    with pytest.raises(ValueError):
        detect_glucose_level([])

def test_normalize_glucose_level():
    glucose_level = 120.0
    normalized_glucose = normalize_glucose_level(glucose_level)
    assert normalized_glucose == 100.0

def test_display_glucose_level():
    glucose_level = 110.0
    display_text = display_glucose_level(glucose_level)
    assert display_text == "Glucose level: 110.00 mg/dL"

def test_glucose_level_detection_accuracy():
    sensor_data = [
        SensorData(glucose_level=100, calibration_factor=1.0),
        SensorData(glucose_level=120, calibration_factor=1.0),
        SensorData(glucose_level=110, calibration_factor=1.0),
    ]
    glucose_level = detect_glucose_level(sensor_data)
    assert abs(glucose_level - 110.0) <= 10.0
