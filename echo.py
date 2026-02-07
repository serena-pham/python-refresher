# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    lines = []
    current = text[-repetitions:]
    
    for _ in range(repetitions):
        lines.append(current)
        current = current[1:]

    lines.append(".")
    return "\n".join(lines)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))