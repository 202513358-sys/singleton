class Counter:
    _instance = None

    def __new__(cls):
        raise TypeError("Use Counter.get_instance() instead.")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.count = 0

        return cls._instance
