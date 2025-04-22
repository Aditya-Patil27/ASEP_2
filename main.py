#!/usr/bin/env python3

import sys
import logging
from utils.config import Config
from utils.data_logger import DataLogger
from vision.gesture_recognition import GestureRecognizer
from navigation.path_planning import PathPlanner
from terrain.terrain_classifier import TerrainClassifier
from ui.dashboard import Dashboard

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def main():
    logger = setup_logging()
    logger.info("Starting Autonomous Gesture-Controlled Car")
    
    try:
        # Initialize components
        config = Config()
        data_logger = DataLogger()
        gesture_recognizer = GestureRecognizer()
        path_planner = PathPlanner()
        terrain_classifier = TerrainClassifier()
        dashboard = Dashboard()
        
        # Main control loop
        while True:
            # Process gesture input
            gesture = gesture_recognizer.detect_gesture()
            
            # Plan path based on gesture and environment
            path = path_planner.plan_path(gesture)
            
            # Classify terrain and adjust speed
            terrain_type = terrain_classifier.classify_terrain()
            
            # Update dashboard
            dashboard.update_status(gesture, path, terrain_type)
            
            # Log data
            data_logger.log_state(gesture, path, terrain_type)
            
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully")
    except Exception as e:
        logger.error(f"Error in main loop: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 