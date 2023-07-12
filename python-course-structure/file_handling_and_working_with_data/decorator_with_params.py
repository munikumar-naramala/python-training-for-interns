def car_decorator(color, model):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Color: {color}")
            print(f"Model: {model}")
            func(*args, **kwargs)
            print("Decorating complete!")

        return wrapper

    return decorator


@car_decorator(color="red", model="Sedan")
def drive_car(speed):
    print(f"Driving at {speed} mph")


drive_car(60)
