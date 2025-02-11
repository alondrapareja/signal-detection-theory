import numpy as np
import scipy.stats as stats #Statistical package from open-source python library

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    #Calculates the hit rate
    def hits_rate(self):
        return self.hits/(self.hits+self.misses)

    #Calulcates the false alarm rates
    def falseAlarms_rate(self):
        return self.falseAlarms/(self.falseAlarms+self.correctRejections)

    #Calculates d_prime 
    def d_prime(self):
        H = self.hits_rate()
        FA = self.falseAlarms_rate()

        # Uses clip function to limit extreme values and prevent z-score calculation issues
        # Found clip function by searching up technqiues to limit extreme values

        H = np.clip(H,1e-10,1-1e-10) #Avoids the value 0 or 1
        FA = np.clip(FA,1e-10,1-1e-10) #Avoids the value 0 or 1

        #Calculates z-scores of hit and false alarm rates using percent point function (inverse of the cumulative distribution function)
        z_H = stats.norm.ppf(H)
        z_FA = stats.norm.ppf(FA) 
        return z_H - z_FA

    #Calculates the criterion (C)
    def criterion(self):
        H = self.hits_rate()
        FA = self.falseAlarms_rate()
       
       #Clips values
        H = np.clip(H,1e-10,1-1e-10) #Avoids the value 0 or 1
        FA = np.clip(FA,1e-10,1-1e-10) #Avoids the value 0 or 1

        z_H = stats.norm.ppf(H)
        z_FA = stats.norm.ppf(FA)
        return-0.5 * (z_H + z_FA)

#Testing scenarios
sd = SignalDetection(hits=0, misses=10,falseAlarms=15, correctRejections=5)
print("Hit Rate: ", sd.hits_rate())
print("False Alarms Rate: ", sd.falseAlarms_rate())
print("d_prime: ", sd.d_prime())
print("Criterion (C): ", sd.criterion())