import sys
score = float(input("Input A Score: "))
if score < 0.0 or score > 10.0:
    print("Score Is Outside The Expected Range")
    sys.exit()
if score >= 9.0:
    print("A")
elif score >= 8.0:
    print("B")
elif score >= 7.0:
    print("C")
elif score >= 6.0:
    print("D")
else:
    print("F")
