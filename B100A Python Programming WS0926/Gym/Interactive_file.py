# interactive file

from Gym_manager_file import GymManager
from Gym_members import member as Member
from Trainers import trainer
from Workout_plans import workoutplan
from Payments import payment

def member_sub_menu(manager: GymManager):
    while True:
        print('\n--- Member Management ---')
        print('1. Register member')
        print('2. View all members')
        print('3. Search member')
        print('4. Update member Contact')
        print('5. Return to main menu')
        choice = input('Select an option (1-5): ').strip()

        if choice == '1':
            mid = input('Enter member id: ').strip()
            if mid in manager.members:
                print('Member id already exists')
                continue
            name = input('Enter name: ').strip()
            email = input('Enter email: ').strip()
            phone = input('Enter phone: ').strip()
            manager.members[mid] = Member(mid, name, email, phone)
            manager.save_all_data()
            print(f"Member: '{name}'registered")

        elif choice == '2':
            if not manager.members:
                print('No member found')
            for m in manager.members.values():
                print(f"ID: {m.member_id} | Name: {m.name} | Email: {m.email} | Phone: {m.phone} | Trainer: {m.assigned_trainer}")

        elif choice == '3':
            query = input('Enter member ID or Name to search: ')
            results = manager.search_member(query)
            if not results:
                print('No matching member found')
            for m in results:
                print(f"Found: ID: {m.member_id} | Name: {m.name} | Trainer: {m.assigned_trainer}")

        elif choice == '4':
            mid = input('Enter Member ID: ').strip()
            member = manager.members.get(mid)
            if not member:
                print('Member not found')
                continue
            new_email = input('Enter new email (leave blank to skip): ').strip()
            new_phone = input('Enter new phone (leave blank to skip): ').strip()
            if new_email:
                if not member.update_email(new_email):
                    print('Invalid email format')
            if new_phone:
                member.update_phone(new_phone)
            manager.save_all_data()
            print('Member details updated')

        elif choice == '5':
            break
        else:
            print('Choose 1-5 !!!')


def trainer_sub_menu(manager: GymManager):
    while True:
        print('\n--- Trainer Management ---')
        print('1. Add Trainer')
        print('2. View Trainer')
        print('3. Assign Trainer to Member')
        print('4. Return to Main Menu')
        choice = input('Select an option (1-4): ').strip()

        if choice == '1':
            tid = input('Enter Trainer ID: ').strip()
            if tid in manager.trainers:
                print('Trainer ID exists')
                continue
            name = input('Enter Name: ').strip()
            manager.trainers[tid] = trainer(tid, name)
            manager.save_all_data()
            print(f"Trainer '{name}' added")

        elif choice == '2':
            if not manager.trainers:
                print('No trainers found')
            for t in manager.trainers.values():
                print(f"ID: {t.trainer_id} | Name: {t.name} | Total Clients: {t.get_client_count()}")

        elif choice == '3':
            mid = input('Enter Member ID: ').strip()
            tid = input('Enter Trainer ID: ').strip()
            if manager.assign_trainer_to_member(mid, tid):
                print('Trainer assigned successfully')
            else:
                print('Assignment failed (invalid Member ID or Trainer ID)')

        elif choice == '4':
            break
        else:
            print('Choose 1-4 !!!')


def workout_sub_menu(manager: GymManager):
    while True:
        print('\n--- Workout Plans ---')
        print('1. Create Plan')
        print('2. Add Exercise to Plan')
        print('3. View Plans')
        print('4. Return to Main Menu')
        choice = input('Select an option (1-4): ').strip()

        if choice == '1':
            pid = input('Enter plan ID: ').strip()
            if pid in manager.plans:
                print('Plan ID already exists')
                continue
            pname = input('Enter plan name: ').strip()
            diff = input('Difficulty (Beginner/Intermediate/Advanced): ').strip()
            manager.plans[pid] = workoutplan(pid, pname, diff or 'Beginner')
            manager.save_all_data()
            print('Workout plan created')

        elif choice == '2':
            pid = input('Enter Plan ID: ').strip()
            plan = manager.plans.get(pid)
            if not plan:
                print('Plan not found')
                continue
            ex = input('Enter Exercise Name: ').strip()
            plan.add_exercise(ex)
            manager.save_all_data()
            print(f"Added '{ex}' to plan")

        elif choice == '3':
            if not manager.plans:
                print('No workout plans recorded')
            for p in manager.plans.values():
                print(f"ID: {p.plan_id} | Name: {p.plan_name} | Difficulty: {p.difficulty} | Exercises: {', '.join(p.exercises) or 'None'}")

        elif choice == '4':
            break
        else:
            print('Choose 1-4 !!!')


def payment_sub_menu(manager: GymManager):
    while True:
        print('\n--- Payment & Billing ---')
        print('1. Make/Record Payment')
        print('2. View All Payments')
        print('3. Check Payment Status')
        print('4. Return to Main Menu')
        choice = input('Select an option (1-4): ').strip()

        if choice == '1':
            pay_id = input('Enter Payment ID: ').strip()
            if pay_id in manager.payments:
                print('Payment ID already exists')
                continue
            mid = input('Enter Member ID: ').strip()
            if mid not in manager.members:
                print('Member does not exist')
                continue
            try:
                amt = float(input('Enter Amount: ').strip())
                status = input('Status (Paid/Pending/Failed) [Default: Paid]: ').strip().capitalize()
                manager.payments[pay_id] = payment(pay_id, mid, amt, status or 'Paid')
                manager.save_all_data()
                print('Payment recorded')
            except ValueError:
                print('Amount must be numeric')

        elif choice == '2':
            if not manager.payments:
                print('No payments recorded')
            for p in manager.payments.values():
                print(f"ID: {p.payment_id} | Member: {p.member_id} | Amount: ${p.amount:.2f} | Status: {p.status}")

        elif choice == '3':
            pay_id = input('Enter Payment ID: ').strip()
            p = manager.payments.get(pay_id)
            if p:
                print(f"Payment {p.payment_id} for Member {p.member_id}: ${p.amount:.2f} [{p.status}]")
            else:
                print('Payment record not found')

        elif choice == '4':
            break
        else:
            print('Choose 1-4')


def main():
    manager = GymManager(data_dir='data')

    while True:
        print('\n=================================')
        print('   GYM MANAGEMENT SYSTEM (CLI)   ')
        print('1. Member Management')
        print('2. Trainer Management')
        print('3. Workout Plans')
        print('4. Payment Management')
        print('5. Exit')

        choice = input('Select a section (1-5): ').strip()

        try:
            if choice == '1':
                member_sub_menu(manager)
            elif choice == '2':
                trainer_sub_menu(manager)
            elif choice == '3':
                workout_sub_menu(manager)
            elif choice == '4':
                payment_sub_menu(manager)
            elif choice == '5':
                manager.save_all_data()
                print('System state saved. Exiting.')
                break
            else:
                print('Please select a number from 1 to 5')
        except Exception as e:
            print(f"Unexpected Exception: {e}")


if __name__ == '__main__':
    main()

