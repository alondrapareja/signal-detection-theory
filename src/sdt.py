<<<<<<< Updated upstream
import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections

    # Calculate Hit Rate 
    def hit_rate(self):
        return self.hits / (self.hits + self.misses)

    # Calculate False Alarm rate
    def false_alarm_rate(self):
        return self.false_alarms / (self.false_alarms + self.correct_rejections)

    # Calculates d-prime 
    def d_prime(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        # ppf
        z_H = stats.norm.ppf(H) if H > 0 and H < 1 else 0
        z_FA = stats.norm.ppf(FA) if FA > 0 and FA < 1 else 0
        return z_H - z_FA 

    # Criterion (C)
    def criterion(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        z_H = stats.norm.ppf(H) if H > 0 and H < 1 else 0
        z_FA = stats.norm.ppf(FA) if FA > 0 and FA < 1 else 0
        return -0.5 * (z_H + z_FA)
=======
import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections

    # Calculate Hit Rate 
    def hit_rate(self):
        return self.hits / (self.hits + self.misses)

    # Calculate False Alarm rate
    def false_alarm_rate(self):
        return self.false_alarms / (self.false_alarms + self.correct_rejections)

    # Calculates d-prime 
    def d_prime(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        # ppf
        z_H = stats.norm.ppf(H) if H > 0 and H < 1 else 0
        z_FA = stats.norm.ppf(FA) if FA > 0 and FA < 1 else 0
        return z_H - z_FA 

    # Criterion (C)
    def criterion(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        z_H = stats.norm.ppf(H) if H > 0 and H < 1 else 0
        z_FA = stats.norm.ppf(FA) if FA > 0 and FA < 1 else 0
        return -0.5 * (z_H + z_FA)
>>>>>>> Stashed changes
