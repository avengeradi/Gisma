# gym manager file

import csv
import os
from Gym_members import member
from Trainers import trainer
from Workout_plans import workoutplan
from Payments import payment

# manage the data
class GymManager:
    def __init__(self, data_dir: str = 'data'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(base_dir, data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        self.members_file = os.path.join(self.data_dir, "members.csv")
        self.trainers_file = os.path.join(self.data_dir, "trainers.csv")
        self.plans_file = os.path.join(self.data_dir, "workout_plans.csv")
        self.payments_file = os.path.join(self.data_dir, "payments.csv")

        self.members = {}
        self.trainers = {}
        self.plans = {}
        self.payments = {}
    
        self.load_all_data()

    def load_all_data(self) -> None:
    # read all data records from CSV storage files."""
        try:
            if os.path.exists(self.members_file):
                with open(self.members_file, mode='r', newline='') as f:
                    for row in csv.DictReader(f):
                        self.members[row['member_id']] = member(
                            row['member_id'], row['name'], row['email'], row['phone'], row['assigned_trainer']
                        )

            if os.path.exists(self.trainers_file):
                with open(self.trainers_file, mode='r', newline='') as f:
                    for row in csv.DictReader(f):
                        t = trainer(row['trainer_id'], row['name'])
                        if row.get('clients'):
                            t.current_clients = row['clients'].split(';')
                        self.trainers[row['trainer_id']] = t

            if os.path.exists(self.plans_file):
                with open(self.plans_file, mode='r', newline='') as f:
                    for row in csv.DictReader(f):
                        wp = workoutplan(row['plan_id'], row['plan_name'], row['difficulty'])
                        if row.get('exercises'):
                            wp.exercises = row['exercises'].split(';')
                        self.plans[row['plan_id']] = wp

            if os.path.exists(self.payments_file):
                with open(self.payments_file, mode='r', newline='') as f:
                    for row in csv.DictReader(f):
                        self.payments[row['payment_id']] = payment(
                            row['payment_id'], row['member_id'], float(row['amount']), row['status']
                        )
        except (IOError, KeyError, ValueError) as err:
            print(f'Failed loading saved data: {err}')

    # save all the data
    def save_all_data(self) -> bool:
        try:
            with open(self.members_file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['member_id', 'name', 'email', 'phone', 'assigned_trainer'])
                writer.writeheader()
                for m in self.members.values():
                    writer.writerow(m.to_dict())

            with open(self.trainers_file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['trainer_id', 'name', 'clients'])
                writer.writeheader()
                for t in self.trainers.values():
                    writer.writerow(t.to_dict())

            with open(self.plans_file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['plan_id', 'plan_name', 'difficulty', 'exercises'])
                writer.writeheader()
                for p in self.plans.values():
                    writer.writerow(p.to_dict())

            with open(self.payments_file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['payment_id', 'member_id', 'amount', 'status'])
                writer.writeheader()
                for pay in self.payments.values():
                    writer.writerow(pay.to_dict())
            return True
        except IOError as err:
            print(f' File write failure: {err}')
            return False

    # assign trainer
    def assign_trainer_to_member(self, member_id: str, trainer_id: str) -> bool:
        member = self.members.get(member_id)
        trainer = self.trainers.get(trainer_id)

        if not member or not trainer:
            return False

        if trainer.assign_client(member_id):
            member.assign_trainer(trainer_id)
            self.save_all_data()
            return True
        return False

    # seach member
    def search_member(self, query: str) -> list:
        q = query.strip().lower()
        return [m for m in self.members.values() if q in m.member_id.lower() or q in m.name.lower()]