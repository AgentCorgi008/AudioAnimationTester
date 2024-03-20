screen anims(anim):

    modal True

    text "[anim.name]" size 40 color "#ffffff" offset(10, 10)

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
            action Call('anim_once', AnimationPlayer.get().anim_once)
