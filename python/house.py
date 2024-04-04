name = str(input("what's your name? "))


match name:
    case "adam" | "ramyar" | "rasty":
        print("dadash")

    case "narmen":
        print("alton")
    case _:
        print("who?")


# if name == "adam" or name == "rasty" or name == "ramyar":
#   print("bnaslawa")
# elif name == "sma":
#   print("domawa")
# else:
#   print("who? ")
