def main():
    exp = input("Expression: ")
    exp = exp.strip()
    x, y, z = exp.split(" ")
    print(f"{calc(x, y, z):.1f}")

def calc(x, y, z):
    x = float(x)
    z = float(z)
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z

main()
