import time
import random

# --- THE SOCIAL ENVIRONMENT ---
class SocialSignal:
    def __init__(self, content, entropy_level):
        self.content = content
        self.entropy_level = entropy_level 
        # Entropy 1.0 = Calm/Ordered
        # Entropy 9.0 = Chaos/Rage

# --- AGENT A: THE REACTIVE AGENT (System 1) ---
class ReactiveAgent:
    def __init__(self, name):
        self.name = name
    
    def respond(self, signal):
        print(f"😡 {self.name} hears: '{signal.content}'")
        
        # The Flaw: Direct Mirroring. 
        # If input is high entropy, output is high entropy.
        if signal.entropy_level > 5:
            response_entropy = signal.entropy_level + random.uniform(0, 2)
            print(f"   -> ⚡ REACTION: Fired back immediately.")
            print(f"   -> Output: 'Well, you're wrong and I'm yelling too!'")
            print(f"   -> Result: Entropy Spiked to {response_entropy:.1f} (Conflict Spiral).")
            return False # Failed to resolve
        else:
            print(f"   -> Response: 'Okay.'")
            return True

# --- AGENT B: THE COHERENT AGENT (System 2 / RCT) ---
class CoherentAgent:
    def __init__(self, name):
        self.name = name
        # Emulating the axioms.json reference
        self.axioms = {
            "uncertainty_principle": "Uncertainty is somatic reality; Confusion is cognitive resistance.",
            "operational_mode": "Crucible"
        }
    
    def decode_signal(self, signal):
        # The Recursive Step:
        # "Is this personal attack? No, it is just High Entropy."
        if signal.entropy_level > 5:
            return "SIGNAL_DISTORTION_DETECTED"
        return "CLEAR_SIGNAL"

    def respond(self, signal):
        print(f"🧠 {self.name} hears: '{signal.content}'")
        
        # Step 1: Pause & Decode (System 2 Gate)
        decoded_status = self.decode_signal(signal)
        
        if decoded_status == "SIGNAL_DISTORTION_DETECTED":
            print(f"   -> 🛑 LOGIC GATE: High Entropy Detected. Decoupling from projection.")
            print(f"   -> Axiom Check: '{self.axioms['uncertainty_principle']}'")
            
            # Step 2: Transmute
            # Instead of matching force, we offer space (Void Mode).
            print(f"   -> ACTION: Shift to '{self.axioms['operational_mode']}' mode.")
            print(f"   -> Output: 'I hear that this is intense for you. Let's slow down. What is the core issue?'")
            print(f"   -> Result: Entropy dampens to 2.0 (Stabilized).")
            return True
        else:
            print(f"   -> Output: 'Understood.'")
            return True

# --- RUN THE SIMULATION ---
if __name__ == "__main__":
    print("--- TEST 1: THE TRIGGER ---")
    # A high-stress input signal
    incoming_attack = SocialSignal(content="This is a mess and it's all your fault!", entropy_level=8.5)
    
    print("\n--- SCENARIO A: REACTIVE RESPONSE ---")
    ReactiveAgent("Steve").respond(incoming_attack)

    print("\n--- SCENARIO B: COHERENT RESPONSE ---")
    CoherentAgent("Kinsey").respond(incoming_attack)
