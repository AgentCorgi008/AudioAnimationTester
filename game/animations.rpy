init python:
    class AnimFile:
        def __init__(self, name: str, path: str) -> None:
            self.name: str = name
            self.anim_loop: Movie = Movie(play=path)
            self.anim_once: Movie = Movie(play=path, loop=False)

        def __repr__(self) -> str:
            return f"{self.name}"

    def process_animation_files() -> None:
        lst = list(filter(lambda x: 'images/' in x, renpy.list_files()))
        lst = list(map(lambda x: AnimFile(x[7:], x), lst))
        return lst

    class AnimationPlayer:
        list = process_animation_files()
        counter = 0
        loop = True

        @classmethod
        def switch_loop_state(cls) -> None:
            cls.loop = not cls.loop

        @classmethod
        def get(cls):
            return AnimationPlayer.list[AnimationPlayer.counter]

        @classmethod
        def get_names(cls):
            return list([file.name for file in cls.list])

        @classmethod
        def next(cls) -> None:
            if len(cls.list) == cls.counter + 1:
                cls.counter = 0
                return
            cls.counter += 1

        @classmethod
        def prev(cls) -> None:
            if cls.counter == 0:
                cls.counter = len(cls.list) - 1
                return
            cls.counter -= 1
