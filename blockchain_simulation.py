import hashlib
import time

# Block class definition
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain creation
def create_blockchain():
    blockchain = []
    difficulty = 2

    # Genesis block
    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    genesis_block.mine_block(difficulty)
    blockchain.append(genesis_block)

    # Block 1
    block1 = Block(1, time.time(), "Block 1 Data", blockchain[-1].hash)
    block1.mine_block(difficulty)
    blockchain.append(block1)

    # Block 2
    block2 = Block(2, time.time(), "Block 2 Data", blockchain[-1].hash)
    block2.mine_block(difficulty)
    blockchain.append(block2)

    return blockchain

# Display blockchain
def display_blockchain(blockchain):
    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")
        print("-" * 50)

# Challenge: Change data in Block 1 and observe
def tamper_block(blockchain):
    print("\n[!] Tampering with Block 1's data...\n")
    blockchain[1].data = "Tampered Data"
    blockchain[1].hash = blockchain[1].calculate_hash()

# Main flow
blockchain = create_blockchain()
print("=== Original Blockchain ===")
display_blockchain(blockchain)

# Tamper with block
tamper_block(blockchain)

print("\n=== After Tampering Block 1 ===")
display_blockchain(blockchain)

# Validation Check
def validate_chain(blockchain):
    print("\n=== Validating Blockchain ===")
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i - 1]
        if current.hash != current.calculate_hash():
            print(f"Block {i} has invalid hash.")
        if current.previous_hash != previous.hash:
            print(f"Block {i} has invalid previous hash link.")

validate_chain(blockchain)
