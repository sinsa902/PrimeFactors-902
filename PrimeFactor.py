from abc import ABCMeta, abstractmethod


class I_PrimeFactor(metaclass=ABCMeta):
    @abstractmethod
    def run(self, param):
        pass


class PrimeFactor(I_PrimeFactor):
    def __init__(self):
        self.rst = []

    def run(self, param):
        self.rst = []
        if param ==1:
            self.rst = []
            return self.rst
        self._calc(param)
        return self.rst

    def _calc(self, param):
        if param <= 1:
            return
        for num in range(2,param+1):
            if param%num ==0:
                self.rst.append(num)
                self._calc(param//num)
                return
        self.rst.append(param)



