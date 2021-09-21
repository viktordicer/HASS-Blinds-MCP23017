import time 

class Blind:
    """[asdasdasda]
    """
    def __init__(self, full_u, full_d, tilt, device, bit):
        self.uptime = full_u
        self.downtime = full_d
        self.tilt = tilt
        self.device = device
        self.bit = bit
        self.movement = 'stop'
        self.position = 0
        self.tilt_position = 0
        self.last_run = 0
        self.duration = 0

    def set_position(self, new_position):
        """sad dsd aside"""
        old_position = self.position
        self.position = new_position
        self.set_direction(self.position, old_position)

        if self.movement == 'up':
            self.tilt_position = 100
        elif self.movement == "down":
            self.tilt_position = 0
        self.duration = self.uptime * (abs(self.position - old_position)/100.0)
        self.last_run = time.time()


    def set_tilt(self, new_tilt):
        old_tilt = self.tilt_position
        self.tilt_position = new_tilt
        self.set_direction(self.tilt_position, old_tilt)
        self.duration = self.tilt * (abs(self.tilt_position - old_tilt)/100.0)
        self.last_run = time.time()

    def set_direction(self,new_position, old_position):
        if new_position > old_position:
            self.movement = 'up'
        elif new_position < old_position:
            self.movement = 'down'

    def stop(self):
        if self.duration > self.tilt:
            time_diff = time.time() - self.last_run
            if time_diff < self.duration:
                self.position = int(self.position *(time_diff/self.duration))
        self.movement = 'stop'
        self.last_run = 0
        self.duration = 0


#Set bit function	
def set_bit(value, bit):
	# return value | (1<<bit)
	return value | bit

#Clear bit function
def clear_bit(value, bit):
	# return value & ~ (1<<bit)
	return value & ~ bit

#find all index where bit is 1
def find_index(string):
    string = string[::-1]
    return [i for i, ltr in enumerate(string) if ltr == '1']

#Decode command
def decode_command(command):
    comm, level, blinds = command.split('-')
    return comm, int(level), blinds