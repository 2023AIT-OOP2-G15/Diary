from diaries.DiarySample import DiarySample
from diaries.k22035Diary import k22035Diary
from diaries.yutoDiary import yutoDiary
from diaries.KitazawaDiary import KitazawaDiary
from diaries.OyaDiary import OyaDiary
from diaries.LobsterDiary import LobsterDiary

# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [
      DiarySample(), 
      yutoDiary(),
      KitazawaDiary(),
      OyaDiary(),
      LobsterDiary(),
      k22035Diary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()