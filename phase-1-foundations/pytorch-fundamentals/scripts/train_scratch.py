import torch
import torch.nn as nn
import torch.optim as optim

def main():
    print("PyTorch Scratch Training Script")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

if __name__ == "__main__":
    main()
