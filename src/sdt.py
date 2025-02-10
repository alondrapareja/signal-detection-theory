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
    #Calculating z-scores of hit and false alarm rates using percent point function (inverse of the cumulative distribution function)
        z_H = stats.norm.ppf(H) if H>0 and H<1 else 0
        z_FA = stats.norm.ppf(FA) if FA>0 and FA<1 else 0
        return z_H - z_FA

    #Calculating the criterion (C)
    def criterion(self):
        H = self.hits_rate()
        FA = self.falseAlarms_rate()
        z_H = stats.norm.ppf(H) if H>0 and H<1 else 0
        z_FA = stats.norm.ppf(FA) if FA>0 and FA<1 else 0
        return-0.5 * (z_H + z_FA)

#Testing
sd = SignalDetection(hits=25, misses=10,falseAlarms=3, correctRejections=9)
print("Hit Rate: ", sd.hits_rate())
print("False Alarms Rate: ", sd.falseAlarms_rate())
print("d_prime: ", sd.d_prime())
print("Criterion (C): ", sd.criterion())
    
        

