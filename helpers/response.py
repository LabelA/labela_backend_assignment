class CustomResponseBuilder:
    def getSuccessResponse(data, message):
        return {"status": "success", "message": message, "data": data}

    def getErrorResponse(error, message):
        return {"status": "error", "message": message, "data": error}

    def serializerError(error, message):
        return {"status": "error", "message": message, "data": error}


    def getValidationErrorResponse(error):
        return {"status": "error", "message": "validation error", "error": error}