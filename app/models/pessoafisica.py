from app import db

class PessoaFisica(db.model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    taxpayer_id = Column(String(11), nullable=False)  # cpf 
    birthdate = Column(Date, nullable=False)
    statement_descriptor = Column(String(100), nullable=True)
    revenue = Column(Float, nullable=False)  #float ou decimal para melhor precisao
    address_line1 = Column(String(100), nullable=False)
    address_line2 = Column(String(10), nullable=False)
    address_line3 = Column(String(100), nullable=True)
    neighborhood = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(2), nullable=False)  # UF do user
    postal_code = Column(String(10), nullable=False)  # CEP do user!
    country_code = Column(String(2), default='BR', nullable=False)  # Código do país
    mcc = Column(String(10), nullable=False)  # não entendi mt bem oq é mcc, apenas segui a doc

    def __repr__(self):
        return f"<PessoaFisica(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"
