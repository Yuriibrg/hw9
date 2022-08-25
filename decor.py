def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as err:
            return str(err)
        except KeyError as err:
            return str(err)
        except IndexError as err:
            return print("Bad command format. Required arguments: add [name] [number]")
        except Exception:
            raise SystemExit("Good bye")

    return wrapper