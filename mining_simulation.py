import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        print(f"\nMining block {self.index}... Difficulty: {difficulty}")
        start_time = time.time()

        attempts = 0
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()
        print(f"✅ Block mined with hash: {self.hash}")
        print(f"🔁 Nonce found: {self.nonce}")
        print(f"🕒 Attempts: {attempts}")
        print(f"⏱️ Time taken: {round(end_time - start_time, 4)} seconds")

# Simulate mining
difficulty = 4  # e.g., hash must start with "0000"

# Create and mine the block
block = Block(1, time.time(), "Mining Block Data", "0")
block.mine_block(difficulty)
