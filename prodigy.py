import random

class MarkovChain:
    def __init__(self):
        self.memory = {}

    def _learn_key(self, key, value):
        if key not in self.memory:
            self.memory[key] = {}

        self.memory[key][value] = self.memory[key].get(value, 0) + 1

    def learn(self, text):
        for i in range(1, len(text)):
            self._learn_key(text[i-1], text[i])

    def _next(self, current_state):
        possible_next = self.memory[current_state]
        total_count = sum(possible_next.values())
        probs = {k: v/total_count for k, v in possible_next.items()}
        return random.choices(list(probs.keys()), list(probs.values()))[0]

    def generate_text(self, start_char, length):
        result = start_char
        for _ in range(length - 1):
            result += self._next(result[-1])
        return result

# Example usage
mc = MarkovChain()
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
mc.learn(text)

print(mc.generate_text('L', 100))