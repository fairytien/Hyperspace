def rgb(r, g, b):
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return(hex)
    else:
        return("Invalid argument")
