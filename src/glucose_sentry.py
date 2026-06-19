import json
from dataclasses import dataclass
from typing import List

@dataclass
class SensorData:
    """Sensor data with glucose level and calibration info"""
    glucose_level: float
    calibration_factor: float

def detect_glucose_level(sensor_data: List[SensorData]) -> float:
    """Detect glucose level from sensor data"""
    if not sensor_data:
        raise ValueError("No sensor data provided")
    # Calculate average glucose level
    total_glucose = sum(data.glucose_level for data in sensor_data)
    average_glucose = total_glucose / len(sensor_data)
    # Apply calibration factor
    calibrated_glucose = average_glucose * sensor_data[0].calibration_factor
    return calibrated_glucose

def normalize_glucose_level(glucose_level: float) -> float:
    """Normalize glucose level to a standard range"""
    # Normalize to a range of 0-100
    normalized_glucose = (glucose_level - 80) / 40 * 100
    return normalized_glucose

def display_glucose_level(glucose_level: float) -> str:
    """Display glucose level in a user-friendly format"""
    return f"Glucose level: {glucose_level:.2f} mg/dL"
