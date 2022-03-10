class Singleton(object):
    id_product = None
    id_purchase = None
    id_vacancies = None
    id_resume = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

