import random

# Simple Markov chain model for text prediction
class MarkovChain:
    def __init__(self):
        self.chain = {}
    
    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if current_word not in self.chain:
                self.chain[current_word] = []
            self.chain[current_word].append(next_word)
    
    def predict(self, input_text):
        last_word = input_text.split()[-1]
        if last_word in self.chain:
            return random.choice(self.chain[last_word])
        return "unknown"

# Initialize and train the model
model = MarkovChain()
# Sample training data (replace with a larger corpus for better results)
sample_text = """
The sun is shining brightly today. The moon is full tonight. The stars are beautiful at night.
The sun sets slowly behind the mountain. The moon rises gently in the sky.
"""
model.train(sample_text)

def predict_text(input_text):
    return model.predict(input_text)