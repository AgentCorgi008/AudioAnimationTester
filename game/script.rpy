label anim_init:
    $ AnimationPlayer.counter = 0
    return

label start:
    stop music fadeout 1
    call anim_init from _call_anim_init
    call anim_loop(AnimationPlayer.get().anim_loop) from _call_anim_loop
    return

label anim_prev(loop):
    $ AnimationPlayer.prev()
    call choose_type_anim(loop) from _call_choose_type_anim

label anim_next(loop):
    $ AnimationPlayer.next()
    call choose_type_anim(loop) from _call_choose_type_anim_1

label choose_type_anim(loop):
    $ file = AnimationPlayer.get()
    if loop:
        call anim_loop(file.anim_loop) from _call_anim_loop_1
    else:
        call anim_once(file.anim_once) from _call_anim_once

label anim_once(anim_once):
    scene expression anim_once
    jump anims

label anim_loop(anim_loop):
    scene expression anim_loop
    jump anims

label anims:
    call screen anims(AnimationPlayer.get())
    $ renpy.pause(hard=True)
