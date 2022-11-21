def new_position(width=0, length=0, actions="", position={'x':0, 'y':0, 'o':'N'}, info=True):

    if info == True:
        grade = "".join(input()).split()
        actions = str(input())
        width = int(grade[0])
        length = int(grade[1])

    #Dicionarios que contém os valores de cada ação para cada orientação(N,S,L,O) que o aspirador irá assumir
    N = {'F':1, 'T':-1, 'E':'O', 'D':'L'}
    S = {'F':-1, 'T':1, 'E':'L', 'D':'O'}
    L = {'F':1, 'T':-1, 'E':'N', 'D':'S'}
    O = {'F':-1, 'T':1, 'E':'S', 'D':'N'}
    w = width
    l = length
    
    #Loop que intera cada ação da lista de instruções(carecteres) que nosso aspirador irá realizar
    for action in actions:

        x = 0
        y = 0  

        #Atribui valores para x e y para a ação 'F' do aspirador baseado na sua orientação atual
        if action == 'F':
            
            if position['o'] == 'N':
                y = N['F']

            elif position['o'] == 'S':
                y = S['F']
            
            elif position['o'] == 'L':
                x = L['F']
            
            elif position['o'] == 'O':
                x = O['F']

        #Atribui valores para x e y para a ação 'T' do aspirador baseado na sua orientação atual
        elif action == 'T':

            if position['o'] == 'N':
                y = N['T']

            elif position['o'] == 'S':
                y = S['T'] 

            elif position['o'] == 'L':
                x = L['T'] 
            
            elif position['o'] == 'O':
                x = O['T']
        
        #Troca a orientação do aspirador baseado na sua ação correspondente e na orientação atual.
        elif action == 'D' or 'E':

            if position['o'] == 'N':
                position['o'] = N[action]

            elif position['o'] == 'S':
                position['o'] = S[action]
            
            elif position['o'] == 'L':
                position['o'] = L[action]
            
            elif position['o'] == 'O':
                position['o'] = O[action]

        #Condicionais que impedem o arpirador de atravessar paredes.
        condition_x = position['x'] + x < l and position['x'] + x >= 0
        condition_y = position['y'] + y < w and position['y'] + y >= 0

        #Atualiza a posição do aspirador caso as condicionais forem satisfeitas.
        if condition_x:
            position['x'] += x

        if condition_y:
            position['y'] += y

    orientation = position['o']
    x_axis = position['x']
    y_axis = position['y']

    position_final = f'{orientation} {x_axis} {y_axis}'


    return print(position_final)


new_position()


