from werkzeug.exceptions import BadRequest, NotFound, InternalServerError


# --- Custom Exceptions ---

class InvalidProductDataError(BadRequest):
    description = "Invalid product data provided."


class ProductNotFoundError(NotFound):
    description = "Product not found."


class ProductAlreadyExistError(BadRequest):
    description = "Product already exists."


class DatabaseError(InternalServerError):
    description = "Database operation failed."


# --- Centralized Error Handling ---

def register_error_handlers(app):
    from flask import jsonify
    from werkzeug.exceptions import HTTPException
    import traceback

    @app.errorhandler(HTTPException)
    def handle_http(e):
        return jsonify({
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }), e.code

    @app.errorhandler(Exception)
    def handle_generic(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e),
            "status_code": 500,
            "trace": traceback.format_exc()
        }), 500
