
def div(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("b is equal 0! Fix it!")
        return

    return result

def ping_db(name_of_db):
    result = len(name_of_db) >= 5
    if result:
        return result
    else:
        raise ConnectionError("Error db connection")


def connect_to_db(name_of_db):
    try:
        connect = ping_db(name_of_db)
        if len(name_of_db) == 6:
            raise ValueError("Wrong link")
    except ZeroDivisionError:
        print("No db connection")
    except (ConnectionError, ValueError) as e:
        print(f"{e} Can`t connect to network db, use local one")
        connect = "local"
    else:
        pass # if not exception
    finally:
        pass # always!
    return connect


class TooLargeError(Exception):
    def __init__(self, value) -> None:
        message = f"Value {value} is too large and hard to calculate"
        super().__init__(message)

def factorial(n:int):
    if n > 100:
        raise TooLargeError(n)

def read_readme():
    with open("README.md", encoding="utf8") as file:
        content = file.read()
    # file = None
    # try:
    #     file = open("README.md", encoding="utf8")
    #     content = file.read()
    # except Exception as e:
    #     print("Виникла помилка:", {e})
    #     return
    # finally:
    #     if file is not None:
    #         file.close()
    print(content)


# print(div(1, 1))
# print(connect_to_db("abcd"))
# print(factorial(100))
# print(factorial(10100))

read_readme()