from diaries.AbstractDiary import AbstractDiary
class AoshimaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return "今日は楽しかった"
    def get_author(self):
        return "Aoshima"