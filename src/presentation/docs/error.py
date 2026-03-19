ERROR_RESPONSES = {
    400: {
        "content": {
            "application/json": {
                "example": {"error": "Bad Request", "message": "str"}
            }
        },
    },
    401: {
        "content": {
            "application/json": {
                "example": {"error": "Unauthorized", "message": "str"}
            }
        },
    },
    403: {
        "content": {
            "application/json": {
                "example": {"error": "Forbidden", "message": "str"}
            }
        },
    },
    404: {
        "content": {
            "application/json": {
                "example": {"error": "Not Found", "message": "str"}
            }
        },
    },
    422: {
        "content": {
            "application/json": {
                "example": {"error": "Unprocessable Content", "message": "str"}
            }
        },
    },
    500: {
        "content": {
            "application/json": {
                "example": {"error": "Internal Server Error", "message": "str"}
            }
        },
    },
}
