import random

# --- Setup Mock Validators ---

# PoW: Miner with 'power'
pow_validators = [
    {"name": "MinerA", "power": random.randint(1, 100)},
    {"name": "MinerB", "power": random.randint(1, 100)},
    {"name": "MinerC", "power": random.randint(1, 100)}
]

# PoS: Staker with 'stake'
pos_validators = [
    {"name": "StakerA", "stake": random.randint(1, 100)},
    {"name": "StakerB", "stake": random.randint(1, 100)},
    {"name": "StakerC", "stake": random.randint(1, 100)}
]

# DPoS: Voters voting for delegates
delegates = ["DelegateA", "DelegateB", "DelegateC"]
votes = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

# --- PoW Selection ---
def simulate_pow(validators):
    winner = max(validators, key=lambda x: x["power"])
    print("=== PoW (Proof of Work) ===")
    for v in validators:
        print(f"{v['name']} Power: {v['power']}")
    print(f"Selected: {winner['name']} (Highest power wins)")
    print()

# --- PoS Selection ---
def simulate_pos(validators):
    winner = max(validators, key=lambda x: x["stake"])
    print("=== PoS (Proof of Stake) ===")
    for v in validators:
        print(f"{v['name']} Stake: {v['stake']}")
    print(f"Selected: {winner['name']} (Highest stake wins)")
    print()

# --- DPoS Selection ---
def simulate_dpos(vote_dict):
    vote_count = {}
    for voter, delegate in vote_dict.items():
        vote_count[delegate] = vote_count.get(delegate, 0) + 1

    max_votes = max(vote_count.values())
    top_delegates = [d for d, count in vote_count.items() if count == max_votes]
    winner = random.choice(top_delegates)  # Tie-breaker if needed

    print("=== DPoS (Delegated Proof of Stake) ===")
    for voter, delegate in vote_dict.items():
        print(f"{voter} voted for {delegate}")
    print(f"Vote Count: {vote_count}")
    print(f"Selected: {winner} (Most votes wins; random among top if tie)")
    print()

# --- Run All Simulations ---
simulate_pow(pow_validators)
simulate_pos(pos_validators)
simulate_dpos(votes)
