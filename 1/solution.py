"""
Day 1 challenge
"""


def solution(arg):
    n = 0
    for idx, i in enumerate(arg):
        if i == arg[(idx + 1) % len(arg)]:
            n += int(i)

    return n

if __name__ == '__main__':
    print(solution(
        "3893445835429722678558456317563893861752455542588369533636585887178232467588"
        "8271931735959186485388524639743932644285388567392593993227418446139572296746"
        "1956696692165644347631772996876418394589976529448132799895615495657146787248"
        "7576314549468261122281384513266834769436913544431258253346374641589492728885"
        "2226521461582612252961448356825561339224364381882112884586922177371458344685"
        "3482994599336631437546576746893977393997827296838854679154752636634816367216"
        "2245585168892858977723516752284597322176349412485116173844733679871253985762"
        "6438521517483965932752745824812958649918869859884279661559443923522483146291"
        "3897235846795961427955351124786386966352682332646757146237166339618895169628"
        "6916979923587358992127741723727623235238531991996999181976664226274715591531"
        "5664953452128496835895822254655558473121991222687739231751831281245562499164"
        "5887878536132271351315317515785559728948243944973246975474854443755325141247"
        "6225415932478849961897299721228198262823515159848941742786272262236888514421"
        "2791473293834659293588967614491359178294733218342671227593712473381557877749"
        "5262661679126588992295965388728873523329196814664853375495819982178949991476"
        "3279869931218136266492627818972334549751282191883558361871277375851259751294"
        "6119217569276943949777646339329385731322213898616171952917421563624947695218"
        "2959947675319842228328773588819758432771969775844246288631196172384932695921"
        "3928195182293316227334998926839139915138472514686689887874559367524254175582"
        "1353185459123618771393675384346839333332641462898422389219892751123236813562"
        "5697957694864448998695153868994988478717319445752347415622938946572547381765"
        "1516136514446513436419126533875125645855223921197481833434658264655912731133"
        "3564641932516356374232222272731926288251659938275116259568567547768499198584"
        "1437587494357288915428186274959589643858188942455998891465838729341466236136"
        "4793844213298677236787998677166743945812899526292132465751582925131262933636"
        "2285931348613634938491681687652616476523428915764452924623411714774872232537"
        "95935253493869317616741963486473"
    ))
