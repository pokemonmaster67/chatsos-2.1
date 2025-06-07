# Chatsos 2.1

This repository contains the training scripts for the **Chatsos** language model.

Chatsos is a GPT‑style model with roughly one billion parameters. Training can be
performed using reinforcement learning (RL) so the model can gradually improve
its responses. Once training is finished, the model can be uploaded to
Hugging Face under the repository `underwater45/Chatsos-2.1-base`.

## Getting started

1. Install the dependencies:

   ```bash
   pip install transformers datasets trl huggingface_hub accelerate
   ```

2. Run the training script:

   ```bash
   python train.py
   ```

   The script builds the Chatsos model, performs a small RL training loop and
   saves the resulting weights locally in the `chatsos/` directory. The final
   model and tokenizer are also uploaded to your Hugging Face account.

3. (Optional) Log in to Hugging Face beforehand with:

   ```bash
   huggingface-cli login
   ```

The training configuration in `train.py` is only a minimal example and should
be adapted to your available compute and dataset.
