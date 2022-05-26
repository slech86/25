class Singleton(object):
    id_product = None
    id_purchase = None
    id_order = None
    id_vacancies = None
    id_resume = []
    logins_and_mails = {}
    position_object = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
