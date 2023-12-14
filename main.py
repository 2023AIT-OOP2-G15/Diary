from diaries.DiarySample import DiarySample
from diaries.KitazawaDiary import KitazawaDiary
from diaries.OyaDiary import OyaDiary
from diaries.LobsterDiary import LobsterDiary

# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [DiarySample(),
           KitazawaDiary(),
           OyaDiary(),
           LobsterDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
