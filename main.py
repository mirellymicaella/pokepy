# -*- coding: utf-8 -*-
import pygame
from random import randint
pygame.init()
pygame.display.set_caption('MiGame')

def criarPokemons():
    #criação dos pokemon
    pikachu = Pokemon("PIKACHU","ELETRIC",(255,255,0),25,(thunderShock,discharge,thunderWave,quickAttach))
    charmander = Pokemon("CHARMANDER","FIRE",(255,140,0),4,(thunderShock,discharge))
    bulbasaur = Pokemon("BULBASAUR","GRASS",(34,139,34),1,(thunderWave,quickAttach))
    squirtle = Pokemon("SQUIRTLE","WATER",(0,255,255),7,(thunderShock,discharge,thunderWave,quickAttach))
    rhydon = Pokemon("RHYDON","GROUND",(240,255,255),112,(thunderShock,discharge,thunderWave,quickAttach))
    gengar =Pokemon("GENGAR","GHOST",(75,0,130),9,(thunderShock,discharge,thunderWave,quickAttach))
    dragonite = Pokemon("DRAGONITE","FLYING",(244,164,96),94,(thunderShock,discharge,thunderWave,quickAttach))
    mewtwo =Pokemon("MEWTWO","PSYCHIC",(230,230,250),150,(discharge,thunderWave,quickAttach))
    #vetor de pokemons
    pokemons = (pikachu,charmander,bulbasaur,squirtle,rhydon,gengar,dragonite,mewtwo)

    return pokemons
def imagensRun():
    #imagens de run
    run1 = pygame.image.load('run1.jpeg')
    run1 = pygame.transform.scale(run1,(800,600))
    run2 = pygame.image.load('run2.jpg')
    run2 = pygame.transform.scale(run2,(800,600))
    run3 = pygame.image.load('run3.jpeg')
    run3= pygame.transform.scale(run3,(800,600))
    run4 = pygame.image.load('run4.jpeg')
    run4= pygame.transform.scale(run4,(800,600))
    run5 = pygame.image.load('run5.png')
    run5= pygame.transform.scale(run5,(800,600))
    run6 = pygame.image.load('run6.gif')
    run6= pygame.transform.scale(run6,(800,600))
    run7 = pygame.image.load('run7.jpeg')
    run7= pygame.transform.scale(run7,(800,600))
    run8 = pygame.image.load('run8.jpeg')
    run8= pygame.transform.scale(run8,(800,600))
    run9 = pygame.image.load('run9.jpg')
    run9= pygame.transform.scale(run9,(800,600))
    run10 = pygame.image.load('run10.jpg')
    run10= pygame.transform.scale(run10,(800,600))
    run11 = pygame.image.load('run11.jpg')
    run11= pygame.transform.scale(run11,(800,600))
    run12= pygame.image.load('run11.jpg')
    run12= pygame.transform.scale(run11,(800,600))
    run13 = pygame.image.load('run12.jpg')
    run13= pygame.transform.scale(run12,(800,600))
    run14 = pygame.image.load('run13.jpg')
    run14= pygame.transform.scale(run13,(800,600))
    run15 = pygame.image.load('run14.jpg')
    run15= pygame.transform.scale(run14,(800,600))
    run16 = pygame.image.load('run15.jpg')
    run16= pygame.transform.scale(run15,(800,600))
    run17 = pygame.image.load('run16.jpg')
    run17= pygame.transform.scale(run16,(800,600))
    #criar vetor de imagens run
    runs = (run1,run2,run3,run4,run5,run6,run7,run8,run9,run10,run11,run12,run13,run14,run15,run16,run17)

    return runs
#definição das cores
preto = (0,0,0)
cinza = (79,79,79)
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
branco = (255,255,255)
#definição da fonte
pygame.font.init()
font = pygame.font.Font("fonte.ttf", 30)
font0 = pygame.font.Font("fonte.ttf",20)
fontG = pygame.font.Font("fonte.ttf",70)
#definição da primeira janela mesmo
inicio_fundo = pygame.image.load('SpritesInterface/fundo_inicio.png')
inicio_fundo = pygame.transform.scale(inicio_fundo,(800,600))
titulo= pygame.image.load('SpritesInterface/titulo.png')
titulo= pygame.transform.scale(titulo,(600,250))
drag = pygame.image.load('SpritesInterface/drag.png')
drag = pygame.transform.scale(drag,(300,300))
fire =pygame.image.load('SpritesInterface/fire.png')
fire = pygame.transform.scale(fire,(800,100))
fire1 =pygame.image.load('SpritesInterface/fire1.png')
fire1 = pygame.transform.scale(fire1,(800,100))
fire2 =pygame.image.load('SpritesInterface/fire2.png')
fire2 = pygame.transform.scale(fire2,(800,100))
fire3 =pygame.image.load('SpritesInterface/fire3.png')
fire3 = pygame.transform.scale(fire3,(800,100))
fire4 =pygame.image.load('SpritesInterface/fire3.png')
fire4 = pygame.transform.scale(fire4,(800,100))
fires = (fire,fire1, fire2, fire3,fire4)
#definição da primeira janela
win = pygame.display.set_mode((800,600))
#definicao da janela de jogo
fundo = pygame.image.load('SpritesInterface/FundoPokemon.png')
fundo = pygame.transform.scale(fundo,(800,400))
barra = pygame.image.load('SpritesInterface/pp_bar.png')
barra = pygame.transform.scale(barra,(800,200))
texto = pygame.image.load('SpritesInterface/text_bar.png')
texto = pygame.transform.scale(texto,(800,200))
opcoes = pygame.image.load('SpritesInterface/fgt_options.png')
opcoes = pygame.transform.scale(opcoes,(300,200))
barra1 = pygame.image.load('SpritesInterface/bar1.png')
barra1 = pygame.transform.scale(barra1,(300,100))
barra2 = pygame.image.load('SpritesInterface/bar2.png')
barra2 = pygame.transform.scale(barra2,(300,100))
tela_bag = pygame.image.load('SpritesInterface/tela_bag.png')
tela_bag = pygame.transform.scale(tela_bag,(800,600))
icon_bag = pygame.image.load('SpritesInterface/bag.png')
icon_bag = pygame.transform.scale(icon_bag,(250,250))
#definição de coordenadas auxiliares
global x1 
x1 = 200
global y1
y1 = 100
global x2
x2 = 400
global y2 
y2 = 435
#criar o objeto movimento
class Movimento:
    def __init__(self,nome,pp,tipo):
        self.__nome = nome
        self.__pp = pp
        self.__tipo = tipo
        self.__ppRestante = pp

    def getNome(self):
        return self.__nome

    def getNomeRender(self):
        return font0.render(self.__nome,1,cinza)
    
    def getTipoRender(self):
        return font.render(self.__tipo,1,cinza)

    def getPPRender(self):
        return font.render(str(self.__pp),1,preto)
    
    def setPPRestante(self):
        self.__ppRestante -= 1
    
    def getPPRestanteRender(self):
        return font.render(str(self.__ppRestante),1,preto)
#criar o objeto pokemon
class Pokemon:
    def __init__(self,nome,tipo,cor,imagem, movimentos):
        self.__nome = nome
        self.__tipo = tipo
        self.__cor = cor
        self.__imagemF = "SpritesPokemon/Frente/"+ str(imagem) + ".png"
        self.__imagemC = "SpritesPokemon/Costas/"+ str(imagem) + ".png"
        self.__movimentos = movimentos
        self.__hp = 100
        self.__nivel = 1
        self.__corHp = verde

    def getNomeRender(self):
        pok = font.render(self.__nome,1,self.__cor)
        return pok

    def getNomeRenderPreto(self):
        pok = font0.render(self.__nome,1,preto)
        return pok
        
    def getNome(self):
        return self.__nome
    
    def getTipo(self):
        return self.__tipo

    def setPos(self,pos):
        self.__pos =pos
        
    def getPos(self):
        return self.__pos
        
    def getImagemFrenteLoad(self):
        img =  pygame.image.load(self.__imagemF)
        img = pygame.transform.scale(img,(200,200))
        return img

    def getImagemCostasLoad(self):
        img =  pygame.image.load(self.__imagemC)
        img = pygame.transform.scale(img,(200,200))
        return img 

    def getMovimentos(self):
        return self.__movimentos

    def getNivel(self):
        return self.__nivel
    
    def getHp(self):
        return self.__hp

    def setHpPerdido(self,hp):
        self.__hp -= hp

    def getCorHp(self):
        if self.__hp < 55:
            return amarelo
        if self.__hp < 30:
            return vermelho
        return verde

def moverSetaMenu(posSeta):
    #mover a seta
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        posSeta-= 50
    if comandos[pygame.K_DOWN]:
        posSeta+= 50

    #limitar a seta
    if(posSeta<y1+40):
        posSeta = y2+y1-40
        
    if(posSeta > y2+y1-40):
        posSeta = y1 + 40

    return posSeta
def moverSetaOpcoes(setaX,setaY):
    #mover a seta
    pygame.draw.polygon(win,cinza,[(setaX,setaY-15),(setaX+20,setaY),(setaX,setaY+15)])
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        setaY-=70
    if comandos[pygame.K_DOWN]:
        setaY+=70
    if comandos[pygame.K_RIGHT]:
        setaX += 140
    if(comandos[pygame.K_LEFT]):
        setaX -= 140

    #limitar a seta
    if(setaX > 655):
        setaX = 515
    if(setaX <515):
        setaX = 655
    if(setaY > 540):
        setaY = 470
    if(setaY <470):
        setaY = 540
    
    return setaX,setaY
def moverSetaMovimentos(setaX,setaY):
    #mover a seta
    pygame.draw.polygon(win,cinza,[(setaX,setaY-10),(setaX+5,setaY),(setaX,setaY+10)])
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        setaY-=70
    if comandos[pygame.K_DOWN]:
        setaY+=70
    if comandos[pygame.K_RIGHT]:
        setaX += 260
    if(comandos[pygame.K_LEFT]):
        setaX -= 260

    #limitar a seta
    if(setaX > 290):
        setaX = 30
    if(setaX <30):
        setaX = 290
    if(setaY > 535):
        setaY = 465
    if(setaY <465):
        setaY = 535
    
    return setaX,setaY
def printarNomesPokemonsMenu():
    y = y1 + 25
    for x in pokemons:
        win.blit(x.getNomeRender(),(x1+55,y))
        x.setPos(y)
        y += 50
def selecionarPokemonMenu(pokemons,posSeta):
    player = 0 
    for x in pokemons:
        finalLetra = x.getPos() + 30
        if(x.getPos() < posSeta < finalLetra):           
                player = x
    return player      
def desenharMenu(posSeta):
    pygame.draw.rect(win,(255,255,255),[x1,y1,x2,y2])
    pygame.draw.rect(win,(0,0,0),[x1+10,y1+10,x2-20,y2-20])
    pygame.draw.polygon(win,vermelho,[(x1+20,posSeta-15),(x1+50,posSeta),(x1+20,posSeta+15)])
    printarNomesPokemonsMenu()
def desenharTelaJogo(i,player1, player2):
    #definir jogador da vez
    if i == 0:
        jogadorVez = player1
        jogadorOutro = player2
    if i == 1:
        jogadorVez = player2
        jogadorOutro = player1

    win.blit(fundo,(0,0))
    win.blit(jogadorVez.getImagemCostasLoad(),(100,230))
    win.blit(jogadorOutro.getImagemFrenteLoad(),(500,50))
    win.blit(texto,(0,400))

    msg = font.render("What should ",1,branco)
    msg2 =font.render(jogadorVez.getNome()+" do?",1,branco)
    win.blit(msg,(50,450))
    win.blit(msg2,(50,480))

    win.blit(barra1,(450,280))
    x = int(round(jogadorVez.getHp()*1.35))
    win.blit(jogadorVez.getNomeRenderPreto(),(500,300))
    pygame.draw.line(win,jogadorVez.getCorHp(),(590,333),(590+x,333),8)

    win.blit(barra2,(90,80))
    x = int(round(jogadorOutro.getHp()*1.35))
    win.blit(jogadorOutro.getNomeRenderPreto(),(120,90))
    pygame.draw.line(win,jogadorOutro.getCorHp(),(205,135),(205+x,135),8)

    win.blit(opcoes,(500,400))

    return jogadorVez,jogadorOutro
def janelaAberta(tempo):
    janela_aberta= True
    pygame.time.delay(tempo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           janela_aberta = False
    return janela_aberta
def printarMovimentos(pokemon):
    movimentos = pokemon.getMovimentos()
    y = 450
    for i in range (0,5):       
        if(i==0 or i == 1):
            if(len(movimentos) < i+1):
                win.blit(font.render0("--",1,cinza),(100,y+ (i*70)))
            else:
                win.blit(movimentos[i].getNomeRender(),(40,y+ (i*70) ))
        elif(i==2 or i == 3):
            if(len(movimentos) < i+1):
                win.blit(font0.render("--",1,cinza),(350,y + ((i-2)*70)))
            else:
                win.blit(movimentos[i].getNomeRender(),(300,y+ ((i-2)*70) ))
def selecionarMovimento(pokemon,setaX,setaY):
    
    movimentos = pokemon.getMovimentos()
    if(setaX == 30):
        if(setaY == 465):
            return movimentos[0]
        if(setaY == 535):
            if(len(movimentos) >= 2):
                return movimentos[1]
    if(setaX == 290):
        if(setaY == 465):
            if(len(movimentos) >= 3):
                return movimentos[2]
        if(setaY == 535):
            if(len(movimentos) >= 4):
                return movimentos[3]

    return 0
def opcaoFight(jogadorVez,jogadorOutro):
    movimentos = jogadorVez.getMovimentos()
    janela_aberta = True
    setaX = 30
    setaY = 465
    janela_aberta_opcoes = True
    while janela_aberta_opcoes:
        janela_aberta_opcoes = janelaAberta(150)
        if(janela_aberta_opcoes==False):
            janela_aberta = False
            break

        win.blit(barra,(0,400))
        printarMovimentos(jogadorVez)
        setaX,setaY = moverSetaMovimentos(setaX,setaY)

        if(setaX == 30):
            if(setaY == 465):
                movimento = movimentos[0]
            if(setaY == 535):
                if(len(movimentos) >= 2):
                    movimento = movimentos[1]

        if(setaX == 290):
            if(setaY == 465):
                if(len(movimentos) >= 3):
                    movimento = movimentos[2]
        if(setaY == 535):
            if(len(movimentos) >= 4):
                movimento = movimentos[3]
        
        win.blit(movimento.getPPRender(),(730,450))
        win.blit(movimento.getPPRestanteRender(),(660,450))
        win.blit(movimento.getTipoRender(),(630,520))

        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            #movimento = selecionarMovimento(jogadorVez, setaX,setaY)
            if(movimento != 0):
                jogadorVez,jogadorOutro = fazerAtaque(jogadorVez,jogadorOutro,movimento)
                janela_aberta_opcoes = False             
                movimento.setPPRestante()

                if jogadorVez.getHp()<=0:
                    desenharTelaMorte(jogadorVez,jogadorVez,jogadorOutro)
                    janela_aberta = False
                if jogadorOutro.getHp()<=0:
                    desenharTelaMorte(jogadorOutro,jogadorVez,jogadorOutro)
                    janela_aberta = False
            pygame.time.delay(1000)
        pygame.display.update()
    return janela_aberta
def opcaoFightAleatorio(jogadorVez,jogadorOutro):
    janela_aberta = True
    janela_aberta_opcoes = True
    while janela_aberta_opcoes:
        janela_aberta_opcoes = janelaAberta(150)
        if(janela_aberta_opcoes==False):
            janela_aberta = False
            break

        movimentos = jogadorVez.getMovimentos()
        n = randint(0,len(movimentos)-1)

        jogadorVez,jogadorOutro = fazerAtaque(jogadorVez,jogadorOutro,movimentos[n])
        janela_aberta_opcoes = False             
            
        if jogadorVez.getHp()<=0:
            desenharTelaMorte(jogadorVez,jogadorVez,jogadorOutro)
            janela_aberta = False
        if jogadorOutro.getHp()<=0:
            desenharTelaMorte(jogadorOutro,jogadorVez,jogadorOutro)
            janela_aberta = False
        pygame.time.delay(1000)

    pygame.display.update()
    return janela_aberta
def opcaoRun(pokemon):
    n = randint(0,16)
    win.blit(runs[n],(0,0))
    pygame.mixer.music.load('run.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(200)
    pygame.mixer.music.set_volume(1)
    pygame.display.update()
    pygame.time.delay(2200)

    for i in range(0,8):
        win.blit(fundo,(0,0))
        win.blit(pokemon.getImagemFrenteLoad(),(500,50))
        if i%2:
            win.blit(fontG.render("?",1,preto),(400,50))
            win.blit(fontG.render("?",1,preto),(620,100))
        else:
            win.blit(fontG.render("?",1,preto),(550,10))

        pygame.time.delay(200)
        pygame.display.update()
    
    pygame.time.delay(500)
def desenharTelaBag(jogadorVez):
    janela_aberta = True
    janela_aberta_bag = True
    while janela_aberta_bag:
        janela_aberta_bag = janelaAberta(100)
        if(janela_aberta_bag==False):
            janela_aberta = False
            break   
        
        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            break
        win.blit(tela_bag,(0,0))
        win.blit(icon_bag,(10,100))
        pygame.display.update()
    return janela_aberta
def fazerAtaque(jogadorVez,jogadorOutro,movimento):
    pygame.time.delay(200)
    for i in range (0,8):
        pygame.time.delay(80)
        win.blit(fundo,(0,0))
        win.blit(jogadorVez.getImagemCostasLoad(),(100,230))

        if i%2:
            win.blit(jogadorOutro.getImagemFrenteLoad(),(500,50))
        

        win.blit(texto,(0,400))

        win.blit(barra1,(450,280))
        x = int(round(jogadorVez.getHp()*1.35))
        win.blit(jogadorVez.getNomeRenderPreto(),(500,300))
        pygame.draw.line(win,jogadorVez.getCorHp(),(590,333),(590+x,333),8)

        
        win.blit(texto,(0,400))
        msg =font.render(jogadorVez.getNome()+" used",1,branco)
        msg2 = font.render(movimento.getNome() + " !",1,branco)
        win.blit(msg,(50,450))
        win.blit(msg2,(50,480))

        if i==0:
            dano = calcularDano(jogadorVez,jogadorOutro) *8
            jogadorOutro.setHpPerdido(dano)
        pygame.display.update()
    
    pygame.time.delay(100)
    return jogadorVez,jogadorOutro    
def calcularDano(ataque, defesa):
    a = ataque.getTipo()
    d = defesa.getTipo()

    dano = 1
    if a == "ELETRIC" :
        if d == "WATER" or d == "FLYING":
            return 2
    if a == "FIRE" :
        if d == "FIRE" or d == "GRASS":
            return 2
    if a == "GRASS" :
        if d == "WATER" or d == "GROUND":
            return 2
    if a == "WATER":
        if d == "FIRE" or d == "GROUND":
            return 2
    if a == "GROUND":
        if d ==  "ELETRIC" or d == "FIRE":
            return 2
    if a == "GHOST" or d == "PSYCHIC":
        if d == "GHOST":
            return 2
    if a == "FLYING":
        if d == "GRASS":
            return 2
    return 1
def desenharTelaMorte(perdedor,jogadorVez,jogadorOutro):
    win.blit(fundo,(0,0))

    for i in range (0,2):
        if perdedor == jogadorOutro:
            win.blit(barra1,(450,280))
            x = int(round(jogadorVez.getHp()*1.35))
            win.blit(jogadorVez.getImagemCostasLoad(),(100,230))
            win.blit(jogadorVez.getNomeRenderPreto(),(500,300))
            pygame.draw.line(win,jogadorVez.getCorHp(),(590,333),(590+x,333),8)

        if perdedor == jogadorVez:
            print(2)
            win.blit(jogadorOutro.getImagemFrenteLoad(),(500,50))
            win.blit(barra2,(90,80))
            x = int(round(jogadorOutro.getHp()*1.35))
            win.blit(jogadorOutro.getNomeRenderPreto(),(120,90))
            pygame.draw.line(win,jogadorOutro.getCorHp(),(205,135),(205+x,135),8)

        win.blit(texto,(0,400))

        msg =font.render("Wild " +perdedor.getNome(),1,branco)
        msg2 = font.render("fainted!",1,branco)
        win.blit(msg,(50,450))
        win.blit(msg2,(50,480))

        pygame.display.update()
        pygame.time.delay(1000)
def jogoModoPVE():
    player1,janela_aberta = escolherPokemonMenuPVE()
    if not janela_aberta:
        return 0
    player2,janela_aberta =escolherPokemonMenuAleatorio(player1)
    if not janela_aberta:
        return 0
    pygame.time.delay(300)

    #abertura da janela de jogo
    while janela_aberta:  
        i = 0 
        setaX = 515
        setaY = 470
        while i<2:
            janela_aberta = janelaAberta(300)
            if janela_aberta == False:
                break

            jogadorVez,jogadorOutro = desenharTelaJogo(i,player1,player2)
            if i == 0:
                setaX,setaY = moverSetaOpcoes(setaX,setaY)
                #selecionar a posição 
                if(pygame.key.get_pressed()[pygame.K_RETURN]):
                    if(setaY ==470):
                        if(setaX == 515):
                            #fight
                            janela_aberta = opcaoFight(jogadorVez,jogadorOutro)                    
                            if janela_aberta==False:
                                break
                                
                        if(setaX == 655):
                            #bag
                            janela_aberta = desenharTelaBag(jogadorVez)
                            if janela_aberta == False:
                                break

                    if(setaY == 540):
                        if(setaX == 515):
                            #pokemon
                            win.blit(barra,(0,400))
                        if(setaX == 655):
                            #run
                            opcaoRun(jogadorOutro)
                            janela_aberta = False
                            break
                else:
                    i -= 1

            if i == 1:
                janela_aberta=opcaoFightAleatorio(jogadorVez,jogadorOutro)
                if janela_aberta==False:
                    break

            i += 1           
            pygame.display.update()
                    
        if not janela_aberta:
            break
        pygame.display.update()
    return 0
def jogoModoPVP():
    player1,player2,janela_aberta = escolherPokemonMenuPVP()
    #abertura da janela de jogo
    while janela_aberta:  
        i = 0 
        setaX = 515
        setaY = 470
        while i<2:
            janela_aberta = janelaAberta(300)
            if janela_aberta == False:
                break

            jogadorVez,jogadorOutro = desenharTelaJogo(i,player1,player2)

            setaX,setaY = moverSetaOpcoes(setaX,setaY)

            #selecionar a posição 
            if(pygame.key.get_pressed()[pygame.K_RETURN]):
                if(setaY ==470):
                    if(setaX == 515):
                        #fight
                        janela_aberta = opcaoFight(jogadorVez,jogadorOutro)                    
                        if janela_aberta==False:
                            break
                            
                    if(setaX == 655):
                        #bag
                        janela_aberta = desenharTelaBag(jogadorVez)
                        if janela_aberta == False:
                            break

                if(setaY == 540):
                    if(setaX == 515):
                        #pokemon
                        win.blit(barra,(0,400))
                    if(setaX == 655):
                        #run
                        opcaoRun(jogadorOutro)
                        janela_aberta = False
                        break
            else:
                i -= 1

            i += 1 
            print(i)            
            pygame.display.update()
        if not janela_aberta:
            break
        pygame.display.update()
def escolherPokemonMenuPVE():
    win.fill(preto)
    mostar_player = False
    posSeta = y1 + 45
    player = 0
    janela_aberta = True
    while janela_aberta:
        janela_aberta = janelaAberta(150)
        if not janela_aberta:
            break
        #titulo
        text = font.render("CHOOSE YOUR POKÉMON",1,(255,255,255))
        win.blit(text,(x1-200,10))

        desenharMenu(posSeta)
        posSeta = moverSetaMenu(posSeta)
                
        #selecionar um pokemon
        if(pygame.key.get_pressed()[pygame.K_RETURN]):            
            player =selecionarPokemonMenu(pokemons,posSeta)
            mostar_player = True
            
        if mostar_player:
            win.blit(player.getImagemFrenteLoad(),(10,100))
            break
            
        pygame.display.update()
    
    pygame.display.update()
    pygame.time.delay(500)
    return player,janela_aberta
def escolherPokemonMenuAleatorio(player1):
    n = randint(0,7)
    p = pokemons[n]
    
    while p== player1:
        n = randint(0,7)
        p = pokemons[n]

    win.fill(preto)
    posSeta = p.getPos()+23
    janela_aberta = True
    while janela_aberta:
        janela_aberta = janelaAberta(150)
        if not janela_aberta:
            break

        #titulo
        text = font.render("CHOOSE YOUR POKÉMON",1,(255,255,255))
        win.blit(text,(x1-200,10))

        desenharMenu(posSeta)
        posSeta = moverSetaMenu(posSeta)
                    
        #mostar a imagem do pokemon
        win.blit(player1.getImagemFrenteLoad(),(10,100))
        win.blit(p.getImagemFrenteLoad(),(500,400))
        pygame.time.delay(150)

        pygame.display.update()
        break
    
    pygame.time.delay(300)
    return p,janela_aberta
def escolherPokemonMenuPVP():
    i=0
    mostar_player1 = False
    mostra_player2 = False
    janela_aberta_pai = True
    janela_aberta = True
    posSeta = y1 + 45
    win.fill(preto)
    while janela_aberta:
        janela_aberta_pai = janelaAberta(150)
        if not janela_aberta_pai:
            break
        #titulo
        text = font.render("CHOOSE YOUR POKÉMON",1,(255,255,255))
        win.blit(text,(x1-200,10))

        desenharMenu(posSeta)
        posSeta = moverSetaMenu(posSeta)
        
        #selecionar um pokemon
        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            if i==0:
                player1 = selecionarPokemonMenu(pokemons,posSeta) 
                mostar_player1 = True
                i =1
            else:
                player2 = selecionarPokemonMenu(pokemons,posSeta)
                mostra_player2 = True
                janela_aberta = False

        #mostar a imagem do pokemon
        if mostar_player1 :
            win.blit(player1.getImagemFrenteLoad(),(10,100))
        if( mostra_player2):
            win.blit(player2.getImagemFrenteLoad(),(500,400))
            pygame.time.delay(150)

        pygame.display.update()
    return player1,player2,janela_aberta_pai
#criação movimentos
thunderShock = Movimento("THUNDER SHOCK",30,"ELECTR")
discharge = Movimento("DISCHARGE",15,"ELECTR")
quickAttach = Movimento("QUICK ATTACH",30,"NORMAL")
thunderWave=Movimento("THUNDER WAVE",20, "ELECTR")
#criacao pokemons
pokemons = criarPokemons()
#criacao imagens run
runs = imagensRun()
i=0
posSetaI = 270
janela_aberta = True
while janela_aberta:
    janela_aberta = janelaAberta(150)
    if not janela_aberta:
        break

    win.blit(inicio_fundo,(0,0))
    win.blit(titulo,(10,10))
    win.blit(drag,(470,200))
    win.blit(fires[i],(0,400))
    i+=1
    if(i==5):
        i=0
    
    pve = font.render("1 Player",1,branco)
    pvp = font.render("2 Players",1,branco)

    win.blit(pve, (200,250))
    win.blit(pvp, (200,300))

    pygame.draw.polygon(win,vermelho,[(175,posSetaI-15),(190,posSetaI),(175,posSetaI+15)])

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        posSetaI-= 50
    if comandos[pygame.K_DOWN]:
        posSetaI+= 50

    #limitar a seta
    if(posSetaI< 270):
        posSetaI = 320
        
    if(posSetaI > 320):
        posSetaI = 270

    if(pygame.key.get_pressed()[pygame.K_RETURN]):
        if posSetaI == 270:
            a = jogoModoPVE()
            janela_aberta = False
        else:
            jogoModoPVP()
            janela_aberta = False


    pygame.display.update()
    