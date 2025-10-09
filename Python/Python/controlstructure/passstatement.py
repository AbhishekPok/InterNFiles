def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 405:
            return "Not allowed"
        case _ : #default case
            return "Something's wrong with the internet"
message = int(input("Enter a status code: "))
report = http_error(message)
print(f"{report}")