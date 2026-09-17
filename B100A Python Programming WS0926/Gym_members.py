# Members file

class member:
    #represents a gym client profile and membership details

    def __init__(self, member_id: str, name: str, email: str, phone: str, assigned_trainer: str = 'none'):
        self.member_id = str(member_id).strip()
        self.name = str(name).strip()
        self.email = str(email).strip()
        self.phone = str(phone).strip()
        self.assigned_trainer = str(assigned_trainer).strip()
    
    # update email
    def update_email(self, new_email: str) -> bool:
        
        if '@' in new_email and '.' in new_email:
            self.email = new_email.strip()
            return True
        return False

    # update phone number
    def update_phone(self, new_phone: str) -> None:
        
        self.phone = new_phone.strip()

    # link a trainer ID to this memeber
    def assign_trainer(self, trainer_id: str) -> None:
        self.assigned_trainer = trainer_id.strip()

    # add it into dictionary
    def to_dict(self) -> dict:
        return {
            'member_id': self.member_id, 
            'name': self.name,
            'email': self.email, 
            'phone': self.phone,
            'assigned_trainer' : self.assigned_trainer,
            }

