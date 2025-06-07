"""Training script for the Chatsos model.

The model is stored and pushed under the name `underwater45/Chatsos-2.1-base`.
"""

import os
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    GPT2Config,
)
from trl import PPOTrainer, PPOConfig
from huggingface_hub import HfApi


def build_model() -> AutoModelForCausalLM:
    """Create the Chatsos language model configuration."""
    config = GPT2Config(
        vocab_size=50257,
        n_positions=2048,
        n_embd=2048,
        n_layer=24,
        n_head=16,
        n_inner=8192,
        activation_function="gelu_new",
    )
    return AutoModelForCausalLM.from_config(config)


def build_tokenizer():
    """Load tokenizer and ensure a padding token exists."""
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({"pad_token": "[PAD]"})
    return tokenizer


def reward_fn(prompts, responses):
    """Very simple reward: encourage longer responses."""
    rewards = []
    for resp in responses:
        rewards.append(len(resp) / 20.0)
    return rewards


def main():
    tokenizer = build_tokenizer()
    model = build_model()
    model.resize_token_embeddings(len(tokenizer))

    # Example dataset; replace with your own
    dataset = load_dataset("imdb", split="train[:1%]")

    ppo_config = PPOConfig(batch_size=1, ppo_epochs=1)
    trainer = PPOTrainer(model=model, tokenizer=tokenizer, config=ppo_config)

    for sample in dataset["text"][:10]:
        prompt = sample
        response = trainer.generate(prompt, max_new_tokens=32)
        reward = reward_fn([prompt], [response])
        trainer.step([prompt], [response], reward)

    save_dir = "chatsos"
    os.makedirs(save_dir, exist_ok=True)
    trainer.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)

    # Push to the Hugging Face Hub
    api = HfApi()
    api.create_repo(repo_id="underwater45/Chatsos-2.1-base", exist_ok=True)
    api.upload_folder(folder_path=save_dir, repo_id="underwater45/Chatsos-2.1-base", path_in_repo=".")


if __name__ == "__main__":
    main()
