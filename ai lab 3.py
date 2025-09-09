class SmartHeater:
    def __init__(self, preferred_temperature):
        self.preferred_temperature = preferred_temperature
        self.previous_action = None
    
    def sense_temperature(self, current_temperature):
        self.current_temperature = current_temperature
    
    def choose_action(self):
        action = None
        
        if self.current_temperature < self.preferred_temperature:
            action = "Turn Heater ON"
        else:
            action = "Turn Heater OFF"

        if action == self.previous_action:
            action = "No Change (Keep same state)"
        else:
            self.previous_action = action
        
        return action

    def apply_action(self):
        decision = self.choose_action()
        print(f"{self.current_temperature}  =>  {decision}")
house_rooms = {
    "Lounge": 24,
    "Guest Room": 20,
    "Kitchen": 25,
    "Bedroom": 17,
    "Bathroom": 23,
}

heater_system = SmartHeater(22)
for room, temp in house_rooms.items():
    print(f"{room} :\t", end="")
    heater_system.sense_temperature(temp)
    heater_system.apply_action()
