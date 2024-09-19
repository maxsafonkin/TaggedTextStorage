class StorageError(Exception):
    pass


class NotFoundError(StorageError):
    pass


class InternalError(StorageError):
    pass
