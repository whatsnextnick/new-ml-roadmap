import wandb

def run_experiment():
    wandb.init(project="ml-roadmap-foundations", name="first_experiment")
    print("W&B experiment initialized.")
    wandb.finish()

if __name__ == "__main__":
    run_experiment()
