screen anims(anim):

    modal True

    text "[anim.name]" size 40 color "#ffffff" offset(10, 10)

    if config.developer:
        button:
            xysize(1920, 1080)
            sensitive not AnimationPlayer.loop
            action [Show("repeat_anims_text"), Call('anim_once', AnimationPlayer.get().anim_once)]

    vbox:
        align (1.0, 0.15)

        spacing 50

        imagebutton:
            auto 'gui/recycle_%s.png'
            selected AnimationPlayer.loop
            action [Function(AnimationPlayer.switch_loop_state), If(not AnimationPlayer.loop,
            Call("anim_loop", AnimationPlayer.get().anim_loop),
            Call('anim_once', AnimationPlayer.get().anim_once))]

        imagebutton:
            auto 'gui/prev_%s.png'
            action [If(AnimationPlayer.loop, Call("anim_prev", True), Call('anim_prev', False))]

        imagebutton:
            auto 'gui/next_%s.png'
            action [If(AnimationPlayer.loop, Call("anim_next", True), Call('anim_next', False))]

        imagebutton:
            auto 'gui/repeat_%s.png'
            sensitive not AnimationPlayer.loop
            action [Show("repeat_anims_text"), Call('anim_once', AnimationPlayer.get().anim_once)]


screen repeat_anims_text():
    zorder 3
    hbox:
        xoffset 20 yalign 0.975
        text "Repeat" size 42 color "#ffffff"
        add 'gui/camera_record.png' yalign 0.5 yoffset 3 xoffset 3
    timer 0.25 action Hide("repeat_anims_text")
