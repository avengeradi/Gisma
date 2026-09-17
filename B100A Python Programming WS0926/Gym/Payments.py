# payments file

class payment:

    # record transactions and payment status
    def __init__(self, payment_id: str, member_id: str, amount: float, status: str = 'pending'):
        self.payment_id = str(payment_id).strip()
        self.member_id = str(member_id).strip()
        self.amount = float(amount)
        self.status = str(status).strip()

    # update transaction status to paid
    def mark_completed(self) -> None:
        self.status = 'paid'

    # update transaction status to failed
    def mark_failed(self) -> None:
        self.status = 'failed'

    # update billing amount
    def update_amount(self, new_amount: float) -> None:
        if new_amount < 0:
            raise ValueError('amount cannot be nagative')
        self.amount = round(float(new_amount), 2)

    # check if the payment is completed
    def is_paid(self) -> bool:
        return self.status.lower() == 'paid'

    # add it to dictionary
    def to_dict(self) -> dict:
        return {
            'payment_id': self.payment_id,
            'member_id': self.member_id,
            'amount': self.amount,
            'status': self.status,
        }
