def check_thresholds(avg_bottom, threshold_top, threshold_bottom):
    """Check if line is within top and bottom thresholds."""
    return threshold_top <= avg_bottom <= threshold_bottom
