from app import db
from sqlalchemy.sql import func
from app.models.customers import Customer
class CustomerRepository:
    def create_customer(self, email, phone_number, link_id=None, link_type=None):
        customer = Customer(
            email = email,
            phone_number = phone_number,
            link_id = link_id,
            link_type = link_type,
            created_at = func.now(),
            updated_at = func.now() ,
            deleted_at = None
        )
        db.session.add(customer)
        db.session.commit()
        return customer
    
    def get_customer_by_primary_email_or_phone(self, email, phone_number):
        query_email = Customer.query.filter(Customer.email == email, Customer.link_type == 'primary').order_by(Customer.created_at)
        query_phone = Customer.query.filter(Customer.phone_number == phone_number, Customer.link_type == 'primary').order_by(Customer.created_at)
        return query_email.union(query_phone).all()
    
    def update_customer(self, existing_customer):
        print(existing_customer[0])
        for i in range(1, len(existing_customer)):
            existing_customer[i].link_type = 'secondary'
            existing_customer[i].link_id = existing_customer[0].id
            existing_customer[i].updated_at = func.now()
        db.session.commit()

    @staticmethod
    def get_customer_by_link_id(link_id):
        return Customer.query.filter((Customer.link_id == link_id) | (Customer.id == link_id)).all() 
    
    @staticmethod
    def get_by_email_and_phone_number(email, phone_number):
        return Customer.query.filter((Customer.email == email) & (Customer.phone_number == phone_number)).first()
    
    @staticmethod
    def get_by_email(email):
        return Customer.query.filter(Customer.email == email).first()
        
    @staticmethod
    def get_by_phone_number(phone_number):
        return Customer.query.filter(Customer.phone_number == phone_number).first()