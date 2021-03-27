class BusinessException(Exception):
    """
    自定义异常基类
    """
    def __init__(self, message):
        """
        构造函数
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        """
        异常描述
        """
        return self.message
