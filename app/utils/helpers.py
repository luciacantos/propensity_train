def clasificar_cliente(probabilidad):
    if probabilidad < 0.20:
        return "Muy baja"
    elif 0.20 <= probabilidad < 0.40:
        return "Baja"
    elif 0.40 <= probabilidad < 0.60:
        return "Media"
    elif 0.60 <= probabilidad < 0.80:
        return "Alta"
    else:
        return "Muy alta"
