class BuilderJson:
    """
    Базовый класс для билдера. Вы его можете дополнить ещё другими полезными
    методами, сейчас представлен только один.
    Base class for builder. You can add additional useful methods, but for now
    it has only one.
    """
    def __init__(self):
        self.structure = {}

    def add(self, keys, value=None):
        """
        Этот метод помогает обновить/добавить новое значение в объекте на
        указанном вами уровне вложенности.
        Если лестница ключей [key1, key2, key3, key4] существует ключу key4 будет присвоено value - если нет она будет
        создана.
        """
        if not isinstance(keys, list):
            self.structure[keys] = value
        else:
            temp = self.structure
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.structure

    def reset(self):
        self.structure = {}