def computegrade(score):
    if score < 0.0 or score > 10.0:
        print("Score Is Outside The Expected Range")
        return 
    if score >= 9.0:
        return "A"
    elif score >= 8.0:
        return "B"
    elif score >= 7.0:
        return "C"
    elif score >= 6.0:
        return "D"
    else:
        return "F"
