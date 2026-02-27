import numpy as np

def calculate_ear(eye_landmarks):
    """
    Calculates the Eye Aspect Ratio (EAR) from 6 facial landmarks.
    
    Args:
        eye_landmarks (np.array): Array of shape (6, 2) containing (x, y) coordinates.
        
    Returns:
        float: The calculated Eye Aspect Ratio.
    """
    # Vertical distances
    A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
    B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
    
    # Horizontal distance
    C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
    
    # EAR Formula
    ear = (A + B) / (2.0 * C)
    return ear

# MediaPipe Face Mesh 468 landmarks indices for eyes
LEFT_EYE_INDICES = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_INDICES = [362, 385, 387, 263, 373, 380]