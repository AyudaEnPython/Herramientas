

def imc(w, h):
    return round(float(w)/(float(h)**2), 2)


def solver(imc):
    return {
        imc < 18.5: "Underweight",
        18.5 <= imc < 25: "Normal",
        25 <= imc < 30: "Overweight",
        30 < imc: "Obesity",
    }[True]
