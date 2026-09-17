# Trainers file
class trainer:
    # represents a trainer and assigned clients
    def __init__(self, trainer_id: str, name: str):
        self.trainer_id = str(trainer_id).strip()
        self.name = str(name).strip()
        self.current_clients = []

    # assign a client if they are not already assigned
    def assign_client(self, member_id: str) -> bool:
        
        mid = str(member_id).strip()
        if mid not in self.current_clients:
            self.current_clients.append(mid)
            return True
        return False

    # remove a client from the trainer's plan
    def remove_client(self, member_id: str) -> bool:
        mid = str(member_id).strip()
        if mid in self.current_clients:
            self.current_clients.remove(mid)
            return True
        return False

    # returns the total assigned clients
    def get_client_count(self) -> int:
        return len(self.current_clients)
    
    # which trainer is assigned to this member
    def has_client(self, member_id: str) -> bool:
        return str(member_id).strip() in self.current_clients

    # add it into dictionary
    def to_dict(self) -> dict:
        return {
            'trainer_id': self.trainer_id,
            'name': self.name,
            'clients': ';'.join(self.current_clients),
        }