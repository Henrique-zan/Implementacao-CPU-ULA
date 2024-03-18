import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

dicionario = {
    0x00: 0,
    0x01: 1,
    0x10: 2,
    0x20: 3,
    0x30: 4,
    0x31: 5,
    0x40: 6,
    0x41: 7,
    0x50: 8,
    0x60: 9,
    0x61: 10,
    0x70: 11,
}

memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
#memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

registradores = ["AX","BX","CX","DX"]

def registrador(registrador):
    if registrador == 2:
        return registrador_ax
    if registrador == 3:
        return registrador_bx
    if registrador == 4:
        return registrador_cx
    if registrador == 5:
        return registrador_dx
def add(idRegistrador,valor, mov):
    global registrador_cp
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx
    if mov == False:
        if idRegistrador == 2:
            registrador_ax += valor
        elif idRegistrador == 3:
            registrador_bx += valor
        elif idRegistrador == 4:
            registrador_cx += valor
        elif idRegistrador == 5:
            registrador_dx += valor
    if mov == True:
        if idRegistrador == 2:
            registrador_ax = valor
        elif idRegistrador == 3:
            registrador_bx = valor
        elif idRegistrador == 4:
            registrador_cx = valor
        elif idRegistrador == 5:
            registrador_dx = valor

def executar(id):
    global flag_zero
    global registrador_cp
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx

    if id == 0:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        valor=memoria.getValorMemoria(registrador_cp + 2)
        add(idRegistrador,valor,False)
        print("lerOperadoresExecutarInstrucao: somando", valor, "em", registradores[idRegistrador-2])
    elif id == 1:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        idRegistrador2=memoria.getValorMemoria(registrador_cp+2)
        Registrador2 = registrador(idRegistrador2)
        add(idRegistrador,Registrador2,False)
        print("lerOperadoresExecutarInstrucao: somando", registradores[idRegistrador2-2], "em", registradores[idRegistrador-2])
    elif id == 2:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        add(idRegistrador,1,False)
        print("lerOperadoresExecutarInstrucao: incrementando 1 em", registradores[idRegistrador-2])
    elif id == 3:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        add(idRegistrador,-1,False)
        print("lerOperadoresExecutarInstrucao: decrementando 1 em", registradores[idRegistrador-2])
    elif id == 4:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        valor=memoria.getValorMemoria(registrador_cp+2)
        add(idRegistrador,-valor,False)
        print("lerOperadoresExecutarInstrucao: subtraindo", valor, "em", registradores[idRegistrador-2])
    elif id == 5:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        idRegistrador2=memoria.getValorMemoria(registrador_cp+2)
        Registrador2 = registrador(idRegistrador2)
        add(idRegistrador,-Registrador2,False)
        print("lerOperadoresExecutarInstrucao: subtraindo", registradores[idRegistrador2-2], "em", registradores[idRegistrador-2])
    elif id == 6:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        valor=memoria.getValorMemoria(registrador_cp+2)
        add(idRegistrador,valor,True)
        print("lerOperadoresExecutarInstrucao: atribuindo", valor, "em", registradores[idRegistrador-2])
    elif id == 7:
        idRegistrador =memoria.getValorMemoria(registrador_cp+1)
        idRegistrador2=memoria.getValorMemoria(registrador_cp+2)
        Registrador2 = registrador(idRegistrador2)
        add(idRegistrador,Registrador2,True)
        print("lerOperadoresExecutarInstrucao: somando", registradores[idRegistrador2-2], "em", registradores[idRegistrador-2])
    elif id == 8:
        byte=memoria.getValorMemoria(registrador_cp+1)
        print('calcularProximaInstrucao: mudando CP para ', byte)
        registrador_cp = byte
    elif id == 9:
        idRegistrador=memoria.getValorMemoria(registrador_cp+1)
        valor=memoria.getValorMemoria(registrador_cp+2)
        Registrador= registrador(idRegistrador)
        print("lerOperadoresExecutarInstrucao: comparando", valor, "com", registradores[idRegistrador-2])
        if Registrador == valor:
            flag_zero = True

    elif id == 10:
        idRegistrador=memoria.getValorMemoria(registrador_cp+1)
        idRegistrador2=memoria.getValorMemoria(registrador_cp+2)
        Registrador= registrador(idRegistrador)
        Registrador2= registrador(idRegistrador2)
        print("lerOperadoresExecutarInstrucao: comparando", registradores[idRegistrador2-2], "com", registradores[idRegistrador-2])
        if Registrador == Registrador2:
            flag_zero = True
    elif id == 11:
        if flag_zero == True:
            byte=memoria.getValorMemoria(registrador_cp+1)
            print('calcularProximaInstrucao: mudando CP para ', byte)
            registrador_cp = byte 

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)
    print(instrucao)
    return dicionario[instrucao]

def lerOperadoresExecutarInstrucao(idInstrucao):
    executar(idInstrucao)
         
def calcularProximaInstrucao(idInstrucao):
    global registrador_cp
    match idInstrucao:
        case 0: 
            print('buscarEDecodificarInstrucao: instrução ADD Registrador, Byte')
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp) 
        case 1: 
            print('buscarEDecodificarInstrucao: instrução ADD Registrador,Registrador')
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 2: 
            print('buscarEDecodificarInstrucao: instrução INC Registrador')
            registrador_cp+= 2
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 3:
            print('buscarEDecodificarInstrucao: instrução DEC Registrador') 
            registrador_cp+= 2
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 4:
            print('buscarEDecodificarInstrucao: instrução SUB Registrador, Byte') 
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 5:
            print('buscarEDecodificarInstrucao: instrução SUB Registrador,Registrador') 
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 6:
            print('buscarEDecodificarInstrucao: instrução MOV Registrador, Byte') 
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 7:
            print('buscarEDecodificarInstrucao: instrução MOV Registrador,Registrador') 
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 8:
            print('buscarEDecodificarInstrucao: instrução JMP Byte') 
            registrador_cp+= 0
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 9:
            print('buscarEDecodificarInstrucao: instrução CMP Registrador, Byte') 
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 10:
            print('buscarEDecodificarInstrucao: instrução CMP Registrador,Registrador')
            registrador_cp+= 3
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        case 11:
            print('buscarEDecodificarInstrucao: instrução JZ Byte') 
            registrador_cp+= 0
            print('calcularProximaInstrucao: mudando CP para ', registrador_cp)
        
def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)