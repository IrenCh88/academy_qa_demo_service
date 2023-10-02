import random
import uuid

valid_username = "admin"
valid_password = "admin"

name_c = str(uuid.uuid4())
name_stat_c = "кошка"
id_c = str(random.randint(330, 1000))
id_stat_c = 702 # использовать существующую категорию

id_p = str(random.randint(100, 300))
id_stat_p = 304
name_p = str(uuid.uuid4())
photo_url_p = str("photo_url")
status_p = random.choice(["available", "pending", "sold"])

