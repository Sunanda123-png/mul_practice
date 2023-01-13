def mul_serializer(mul) -> dict:
    return {
        "id": str(mul["_id"]),
        "name": mul["name"],
        "email": str(mul["email"]),
        "password": str(mul["password"])
    }


def mulnut_serializer(mulnut) -> list:
    return [mul_serializer(mul) for mul in mulnut]
