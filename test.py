from project_class import Transaction
class TestTransaction:
    def test_details1(self):
        t = Transaction(1,'Emma','4234324443', 35.00)
        assert (1, 'Emma', '4234324443', 35.00) == (t.transaction_number, t.name, t.phone_number, t.cost)

    def test_details2(self):
        t2 = Transaction(2,'Kaylin','4343268843', 40.00)
        assert (2, 'Kaylin', '4343268843', 40.00) == (t2.transaction_number, t2.name, t2.phone_number, t2.cost)

    def test_details3(self):
        t3 = Transaction(3,'Kate','1422434390', 75.00)
        assert(3,'Kate','1422434390', 75.00) == (t3.transaction_number,t3.name,t3.phone_number,t3.cost)