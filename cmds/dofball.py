import random
from discord import Message

RESTRICTED = False

def exec(message: Message):
    return random.choice([
        '<:dofsmie:932325302108053525>', '<:dofblush:976395181370773524>', '<:doftective:1014554401244979382>', '<:dofbrian:1029096151447769110>', '<:dofnini:1063135414220755055>', '<:dofblankee:1073411433058017320>', '<:dofgun:976395197552402624>', '<:dofnini2:1077297351309402224>', '<:dofsquish:1071218984189427793>', '<:dofblushtective:1075623363554320425>', '<:dofW:1029455513592799252>', '<:dofdge:1070402662572503132>', '<:dofakl:1074456163854340106>', '<:dofbidness:1010539048508604467>', '<:dofchef:1080862301357363260>', '<:dofcube:1074441514782036048>', '<:dofcunt:1077295056257548399>', '<:dofjail:1075724591957291009>', '<:dofjudge:1029455285582037074>', '<:dofninis:1070849584466759680>', '<:dofsafe:1016711815343902780>', '<:doftldr:1077304477171843073>', '<:dofissue:1074670935682076784>', '<:dofqueen:1029455481225347133>', '<:dofsus:1021159535815172136>', '<:doftrans:1077290208686526635>', '<:dofwithit:1070852051245998090>', '<:smiedof:1027689740486574150>'
    ])
