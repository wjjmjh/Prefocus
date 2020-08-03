import os


def _wrapping_refreshing(func):
    def wrapped(self):
        got = func(self)
        self.refresh_base()
        return got

    return wrapped


class repoPathManager:
    def __init__(self):
        self.base = ""

    def refresh_base(self):
        self.base = ""

    def _combine_one(self, component):
        self.base = os.path.join(self.base, component)

    def combine(self, *directed_folders):
        for folder in directed_folders:
            self._combine_one(folder)
        got = self.base
        self.refresh_base()
        return got

    def find_root(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("Prefocus") + 1])
        return self

    def find_src(self):
        # warning: this method could be harmful when operating in docker container, find_root is more recommended.
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("src") + 1])
        return self

    @property
    @_wrapping_refreshing
    def to_prefocus(self):
        self.find_root()
        [self._combine_one(i) for i in ["src", "prefocus"]]
        return self.base
