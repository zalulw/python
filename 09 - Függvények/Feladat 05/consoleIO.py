def getStringfromConsole() -> str:
    text: str = None
    isAlpha: bool = False

    while text is None:
        input_str = input().replace(",", "")
        isAlpha = input_str.isalpha()

        if isAlpha:
            text = input_str

    return text