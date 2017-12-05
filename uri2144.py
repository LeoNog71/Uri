#voidCarro
import statistics


l = []

while True:

        try:
             w1,w2,r = input().split(" ")
             w1 = int(w1)
             w2 = int(w2)
             r = int(r)
             if w1 == 0 and w1 ==0 and r == 0 and w1 == w2 and w2 ==r:

                       
                teste = statistics.mean(l)
                
                if teste > 40:
                        print("")
                        print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")
                        l = []

             else:                      

                m = (w1+w2)*(1+r/30)
                m = m/2
                
                if m >= 1 and m < 13:
                        print("Nao vai da nao")
                elif m >= 13 and m < 14:
                        print("E 13")
                elif m >=14 and m< 40:
                        print("Bora, hora do show! BIIR!")
                elif m >= 40 and m <= 60:
                        print("Ta saindo da jaula o monstro!")
                elif m >60 :
                        print("AQUI E BODYBUILDER!!")
                l.append(m)
        except EOFError:
                quit()
