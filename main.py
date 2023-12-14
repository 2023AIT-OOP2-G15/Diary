from diaries.DiarySample import DiarySample
from diaries.k22035Diary import k22035Diary

# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [DiarySample(), 
           k22035Diary()]
    for d in diaries:
        print("---------------------------------")
        print(d.get_date())
        print(d.get_summary())
        print(d.get_author())
        print()