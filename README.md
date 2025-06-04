# ChatsOS 2.1

ChatsOS 2.1 is an open-source large language model project. The goal is to provide a roughly 1B parameter transformer that anyone can experiment with. It isn't the smartest model in existence, but it is capable of beating other small language models and serves as a foundation for research and exploration.

## Usage

1. Clone this repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run training with `python src/train.py` to train from scratch or continue training.
4. Run evaluation with `python src/evaluate.py`.
5. Run inference with `python src/inference.py --text "Hello"`.

Checkpoints will be stored in the `models/` directory. Training data can be placed in `data/`.

## Contribution Guidelines

Contributions are welcome! Feel free to open issues or pull requests. When contributing code, please include unit tests where applicable and follow the existing coding style.

Model weights will be distributed separately. Once training checkpoints are stable, we plan to release them via downloadable archives hosted on the project website and on popular model hubs such as Hugging Face.

## License

This project is licensed under the terms of the LICENSE file provided in the repository.
