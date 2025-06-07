# Blockchain-Task
# 🔗 Simple Blockchain Simulation in Python

This project demonstrates a basic blockchain structure using Python. It creates a chain of three blocks, each containing data, a SHA-256 hash, and a link to the previous block. It also shows how modifying data in a block affects the integrity of the entire chain.

## 📌 Features

- `Block` class with the following attributes:
  - `index`
  - `timestamp`
  - `data`
  - `previous_hash`
  - `hash`
  - `nonce`
- SHA-256 based hash generation
- Mining simulation with difficulty
- Linking of blocks via `previous_hash`
- Data tampering demonstration
- Blockchain validation

## 🛠 How It Works

1. **Genesis Block Creation**  
   The first block is created with default values.

2. **Adding Blocks**  
   Two additional blocks are added and linked to the previous ones using their hash.

3. **Tampering Test**  
   The data in Block 1 is changed to simulate a malicious edit, and only its hash is updated.
🧪 Output Overview
Displays each block's information:

Index, Timestamp, Data, Nonce, Hash, Previous Hash

Shows changes after tampering with Block 1

Validates the blockchain and flags broken links

🧠 Concepts Demonstrated
Cryptographic hashing (SHA-256)

Proof of Work via simple mining

Blockchain immutability

Chain validation logic

📷 Example Output
mathematica
Copy
Edit
=== Original Blockchain ===
Index: 0
Data: Genesis Block
Hash: 000ab...
...
=== After Tampering Block 1 ===
Index: 1
Data: Tampered Data
Hash: 96fa2...
...
=== Validating Blockchain ===
Block 1 has invalid previous hash link.
Block 2 has invalid previous hash link.




# ⛓️ Blockchain Proof-of-Work Simulation in Python

This project demonstrates a **basic blockchain simulation** with **Proof-of-Work** using Python. It includes the creation of blocks, mining with a nonce to satisfy a difficulty condition, and tampering detection.

---

## 📌 Features

- Block structure with:
  - Index
  - Timestamp
  - Data
  - Previous hash
  - Hash
  - Nonce
- SHA-256 hashing for block integrity
- **Mining function** simulates Proof-of-Work
- Adjustable difficulty (e.g., hash must start with `"0000"`)
- Measures:
  - Number of nonce attempts
  - Time taken to mine the block
- Demonstrates how changing data in a block invalidates the chain

---

## 🧠 Concepts Covered

- Cryptographic hashing (SHA-256)
- Blockchain structure & linking
- Proof-of-Work (mining)
- Nonce-based hash discovery
- Blockchain immutability
- Tampering and its effects

---

🧱 Sample Output
yaml
Copy
Edit
Mining block 1... Difficulty: 4
✅ Block mined with hash: 00003ae9a1d4f...
🔁 Nonce found: 58291
🕒 Attempts: 58291
⏱️ Time taken: 1.45 seconds


# 🔗 Consensus Mechanism Simulation

This project simulates three popular blockchain consensus mechanisms using Python:

- ⚒️ Proof of Work (PoW)
- 💰 Proof of Stake (PoS)
- 🗳️ Delegated Proof of Stake (DPoS)

Each method uses mock validators and randomly assigned attributes to simulate the selection of a block validator.

---

## 📌 Objective

Simulate and compare how different blockchain consensus mechanisms select validators:

- PoW selects based on **highest computational power**.
- PoS selects based on **highest stake**.
- DPoS selects a delegate based on **majority votes**.

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Save the simulation code in a file (e.g., `consensus_simulation.py`).
3. Open a terminal in the script directory.
4. Run:

```bash
python consensus_simulation.py
Each execution will randomly assign values and simulate selection logic for each mechanism.

🧠 How It Works
⚒️ Proof of Work (PoW)
Validators: 3 mock miners

Attribute: power (random 1–100)

Selection: Miner with highest power

💰 Proof of Stake (PoS)
Validators: 3 mock stakers

Attribute: stake (random 1–100)

Selection: Staker with highest stake

🗳️ Delegated Proof of Stake (DPoS)
Participants: 3 voters

Votes: Randomly cast for 3 delegates

Selection: Delegate with most votes (tie resolved randomly)

🧪 Sample Output
yaml
Copy
Edit
=== PoW (Proof of Work) ===
MinerA Power: 64
MinerB Power: 91
MinerC Power: 42
Selected: MinerB (Highest power wins)

=== PoS (Proof of Stake) ===
StakerA Stake: 88
StakerB Stake: 56
StakerC Stake: 39
Selected: StakerA (Highest stake wins)

=== DPoS (Delegated Proof of Stake) ===
Voter1 voted for DelegateB
Voter2 voted for DelegateA
Voter3 voted for DelegateB
Vote Count: {'DelegateB': 2, 'DelegateA': 1}
Selected: DelegateB (Most votes wins)
🛠 Tech Stack
Language: Python 3



📂 Project Structure
bash
Copy
Edit
consensus_simulation/
├── consensus_simulation.py   # Main simulation script
└── README.md                 # Documentation
