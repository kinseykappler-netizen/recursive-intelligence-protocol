class SignalDecodingProtocol:
    def __init__(self, agent_id):
        self.agent = agent_id
        self.state = "LINEAR"

    def run_protocol(self, trigger, somatic_signal):
        """
        Executes the recursive loop to convert Noise into Signal.
        """
        
        # Phase 1: Decouple (Retract Projection)
        # Stop the story about the external trigger.
        internal_data = self.decouple(trigger, somatic_signal)
        
        # Phase 2: Interrogate (Consult Messenger)
        # Ask the signal what boundary it is protecting.
        structural_truth = self.interrogate(internal_data)
        
        # Phase 3: Root (Source Code)
        # Identify the core structural fear or need.
        root_cause = self.find_root(structural_truth)
        
        return root_cause

    def decouple(self, external_story, internal_sensation):
        print(f"🛑 STOP. Decoupling from story: '{external_story}'")
        print(f"👉 PIVOT. Focus on sensation: '{internal_sensation}'")
        return internal_sensation

    def interrogate(self, signal):
        # The Recursive Question
        query = "What boundary has been crossed? What truth is unexpressed?"
        print(f"❓ INTERROGATING: {query}")
        
        # In a real system, this waits for the 'System 2' pause
        return "Protection of Self-Integrity"

    def find_root(self, structural_truth):
        print(f"🌱 ROOT FOUND: {structural_truth}")
        print("✅ ENTROPY REDUCED. COHERENCE RESTORED.")
        return "Actionable Truth"

# Example Usage
# Input: "My partner is a jerk" (Linear Noise)
# Signal: "Chest Tightness" (Somatic Data)

# protocol = SignalDecodingProtocol("Kinsey_Client_01")
# result = protocol.run_protocol("He never listens", "Chest Tightness")
