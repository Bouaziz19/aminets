# choisir la situation qu'il faut travailler
situation=4
# nombre camion choisi (situation 3)
nc = 1
# 1-2-4
if situation==1 :
    # nombre de ville a visiter
    nv = 5
    # la demande pour chaque ville
    dv = [78,81,115,40,98]
    # la distance parcourue pour chaque ville
    distance = [
        [0,66,15,26,27,9],
        [66,0,64,58,47,75],
        [15,64,0,12,36,21],
        [26,58,12,0,40,33],
        [27,47,36,40,0,33],
        [9,75,21,33,33,0],
    ]
    # la capacité de camion (situation 1)
    cc = [412]
elif situation ==2:
    # nombre de ville a visiter
    nv = 7
    # la demande pour chaque ville
    dv = [78, 81, 115, 40, 98, 68, 77]
    # la distance parcourue pour chaque ville
    distance = [
        [0 ,66 ,43 ,27 ,27,49 ,49 ,14],
        [66 ,0 , 34,47 ,64, 17, 75,53],
        [43 ,34 , 0,17 ,31 ,22 ,74 ,29],
        [27 ,47,17 ,0 , 17,32, 66 ,14],
        [27 ,64,31,17 ,0 ,49 ,74 ,21],
        [49 ,17 , 22,32 ,49, 0 ,63 ,36],
        [49 ,75 ,74 ,66 ,74 ,63,0,54],
        [14 ,53,29,14,21,36 ,54 ,0]
    ]
    # la capacité de camion (situation 3)
    cc = [557]
elif situation==3:
    # nombre de ville a visiter
    nv = 10
    # la demande pour chaque ville
    dv = [78, 81, 115, 40, 98, 68, 77, 25, 33, 87]
    # la distance parcourue pour chaque ville
    distance =[
     [0, 67, 15, 26, 28, 9, 11, 49, 66, 31, 15],
     [67, 0, 64, 58, 48, 75, 59, 17, 14, 45, 56],
     [15, 64, 0, 12, 36, 21, 22, 47, 67, 39, 22],
     [26, 58, 12, 0, 40, 33, 30, 42, 63, 42, 28],
     [28, 48, 36, 40, 0, 33, 17, 32, 42, 3, 14],
     [9, 75, 21, 33, 33, 0, 17, 57, 74, 36, 22],
     [11, 59, 22, 30, 17, 17, 0, 41, 57, 20, 5],
     [49, 17, 47, 42, 32, 57, 41, 0, 20, 30, 36],
     [66, 14, 67, 63, 42, 74, 57, 20, 0, 40, 52],
     [31, 45, 39, 42, 3, 36, 20, 30, 40, 0, 17],
     [15, 56, 22, 28, 14, 22, 5, 36, 52, 17, 0]]

    # la capacité de camion (situation 2)
    cc=[702]
elif situation==4 :
    # nombre camion choisi (situation 3)
    nc = 3
    # la capacité de camion (situation 3)
    cc = [20000, 200000, 20000]
   # nombre de ville a visiter
    nv = 7
    # la demande pour chaque ville
    dv = [78, 81, 115, 40, 98, 68, 77]
    # la distance parcourue pour chaque ville
    distance = [
        [0, 66, 43, 27, 27, 49, 49, 14],
        [66, 0, 34, 47, 64, 17, 75, 53],
        [43, 34, 0, 17, 31, 22, 74, 29],
        [27, 47, 17, 0, 17, 32, 66, 14],
        [27, 64, 31, 17, 0, 49, 74, 21],
        [49, 17, 22, 32, 49, 0, 63, 36],
        [49, 75, 74, 66, 74, 63, 0, 54],
        [14, 53, 29, 14, 21, 36, 54, 0]
    ]
    # 1-2-3


else:
    pass


