from diaries.DiarySample import DiarySample
from diaries.AoshimaDiary import AoshimaDiary

# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [
      DiarySample(), 
      AoshimaDiary(),
      yutoDiary(),
      KitazawaDiary(),
      OyaDiary(),
      LobsterDiary(),
      k22035Diary(),
      NishidaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()