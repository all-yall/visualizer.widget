vars = {
    #This is the number of bars you want shown. there are a lot.
    num:70
    getDisplay:()->
        result=""
        for x in [0.. vars.num]
            result+="""<div class="bar#{x}"></div>"""
        result
}

command: "cat \"/tmp/vis.txt\""

refreshFrequency: 20

render: ()->
    vars.getDisplay()

update: (output,domEl) ->
    out=output.split(", ")
    for x in [0.. vars.num]
        $(domEl).find(".bar#{x}").css("width","#{out[x]}")

style: """
    div{
        border-radius: 2px;
        height: 4px
        margin-top: 5px
        rounded:True
        background-color:rgba(255,255,255,.8)
        width:3px
    }
    text-align: left
    position: fixed
    top: 0px
    left: 0px
    margin: 0px
    padding: 0px
"""

