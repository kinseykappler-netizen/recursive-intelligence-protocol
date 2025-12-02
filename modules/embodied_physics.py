import random

# --- THE ENVIRONMENT ---
class FloorSegment:
    def __init__(self, type_name, friction):
        self.type_name = type_name
        self.friction = friction  # 1.0 is sticky, 0.1 is ice

# --- AGENT A: THE STATISTICAL GUESSER ---
class StatisticalAgent:
    def __init__(self, name):
        self.name = name
        self.training_success_rate = 0.95  # "I usually succeed!"
    
    def move(self, floor):
        print(f"🤖 {self.name} approaches {floor.type_name}...")
        
        # The Industry Flaw: Relying on generic training data
        roll = random.random() 
        adjusted_success_chance = self.training_success_rate * floor.friction
        
        if roll < adjusted_success_chance:
            print(f"   -> Result: SUCCESS. Walked normally.")
            return True
        else:
            print(f"   -> Result: 💥 CRASH! Slipped and fell.")
            return False

# --- AGENT B: THE RCT (KINSEY) AGENT ---
class RCTAgent:
    def __init__(self, name):
        self.name = name
        self.current_speed = "Fast"
    
    # THE RECURSIVE CHECK
    def query_coherence(self, floor):
        # "What is the relationship between my Speed and this Friction?"
        if floor.friction < 0.5 and self.current_speed == "Fast":
            return False # INCOHERENT! Violation of physics.
        return True # COHERENT. Safe to proceed.

    def move(self, floor):
        print(f"🧠 {self.name} approaches {floor.type_name}...")
        
        # Step 1: Recursive Questioning
        is_coherent = self.query_coherence(floor)
        
        # Step 2: Establish Coherence
        if not is_coherent:
            print(f"   -> ⚠️ INCOHERENCE DETECTED (Speed too high for Friction).")
            print(f"   -> Action: Adjusting Relationship... (Slowing Down).")
            self.current_speed = "Slow" # Update state to match reality
            
        # Step 3: Action based on Truth
        print(f"   -> Result: ✅ SUCCESS. Walked carefully.")
        return True

# --- RUN THE SIMULATION ---
if __name__ == "__main__":
    print("--- TEST 1: NORMAL CARPET ---")
    carpet = FloorSegment("Carpet", friction=1.0)
    StatisticalAgent("StatBot").move(carpet)
    RCTAgent("KinseyBot").move(carpet)

    print("\n--- TEST 2: THE ICE PATCH ---")
    ice = FloorSegment("Ice", friction=0.2)
    StatisticalAgent("StatBot").move(ice) 
    RCTAgent("KinseyBot").move(ice)
