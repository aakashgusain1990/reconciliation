from app.dto.customer_dtos import CustomerDto
from app.repositories.customer_repositories import CustomerRepository

class IdentifyService:
    customer_repository: CustomerRepository = CustomerRepository()

    @classmethod
    def add_customer(cls, customer: CustomerDto):
        same_user_exists = cls.check_if_exists(customer.email, customer.phone_number)
        if same_user_exists is not None:
            if same_user_exists.link_type == "secondary":
                return cls.get_customer_detais(same_user_exists.link_id)
            else:
                return cls.get_customer_detais(same_user_exists.id)
        else:
            existing_customer = cls.customer_repository.get_customer_by_primary_email_or_phone(customer.email, customer.phone_number)
            if not existing_customer:
                customer = cls.customer_repository.create_customer(customer.email,customer.phone_number,None,"primary")
            else:
                if len(existing_customer) == 1:
                    customer = cls.customer_repository.create_customer(customer.email,customer.phone_number,existing_customer[0].id,"secondary")
                elif len(existing_customer) == 2:
                    cls.customer_repository.update_customer(existing_customer)
                return cls.get_customer_detais(existing_customer[0].id)
        return cls.get_customer_detais(customer.id)
    
    @classmethod
    def get_customer_detais(cls, id):
        customer_details = cls.customer_repository.get_customer_by_link_id(id)
        primary_contact_id = id
        emails = set()
        phone_numbers = set()
        secondary_contact_ids = set()
        for customer in customer_details:
            emails.add(customer.email)
            phone_numbers.add(customer.phone_number)
            if customer.link_id is not None:
                secondary_contact_ids.add(customer.id)
        
        emails = list(emails)
        phone_numbers = list(phone_numbers)
        secondary_contact_ids = list(secondary_contact_ids)
        resp = {
                "contact":{
                    "primaryContactId": primary_contact_id,
                    "emails": emails,
                    "phoneNumbers": phone_numbers,
                    "secondaryContactIds": secondary_contact_ids
                }
            }
        return resp
    
    @classmethod
    def check_if_exists(cls, email, phone_number):
        if phone_number is not None and email is not None:
            customer=cls.customer_repository.get_by_email_and_phone_number(email, phone_number)
        elif phone_number is None:
            customer=cls.customer_repository.get_by_email(email)
        elif email is None:
            customer=cls.customer_repository.get_by_phone_number(phone_number)
        return customer