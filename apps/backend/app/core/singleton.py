class SingletonMetaclass:
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonMetaclass, cls).__new__(cls)
    return cls.instance