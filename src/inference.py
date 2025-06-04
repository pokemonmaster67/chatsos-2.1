import argparse


def main():
    parser = argparse.ArgumentParser(description="Run inference with ChatsOS 2.1 model")
    parser.add_argument('--model', type=str, default='models/checkpoint.pt', help='Path to model checkpoint')
    parser.add_argument('--text', type=str, default='Hello', help='Prompt text')
    args = parser.parse_args()

    print(f"Loading model from {args.model}")
    # Placeholder for model loading
    print(f"Running inference on: {args.text}")
    # Placeholder for inference logic
    print("Response: [sample output]")


if __name__ == '__main__':
    main()
