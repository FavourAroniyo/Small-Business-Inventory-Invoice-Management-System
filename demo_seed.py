from pathlib import Path
from database.db import Database
from database.repositories import ProductRepository,CustomerRepository
BASE=Path(__file__).resolve().parent;db=Database(BASE/"inventory.db");db.initialize();p=ProductRepository(db);c=CustomerRepository(db)
if not p.find_by_sku("BEV-0012"):p.add("BEV-0012","Malt Drink 33cl","Beverages","8500","10000",20,5)
if not p.find_by_sku("RIC-0050"):p.add("RIC-0050","Rice 50kg","Food","65000","72000",10,3)
if not c.all():c.add("Demo Customer","08031234567","customer@example.com","Abuja")
d=BASE/"sample_docs";d.mkdir(exist_ok=True)
(d/"supplier_standard.txt").write_text("SUPPLIER DELIVERY NOTE\nBEV-0012 Malt drink 33cl 10 8,500.00 85,000.00\nRIC-0050 Rice 50kg 2 65,000.00 130,000.00\n",encoding="utf-8")
print("Demo data created.")
