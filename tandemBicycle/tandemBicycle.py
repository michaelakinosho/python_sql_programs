# Credit: source of solution is AlgoExpert provided solution
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True)
    
    if not fastest:
        blueShirtSpeeds.sort()
    
    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
    
    return totalSpeed