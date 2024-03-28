import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Hill_Model:
    def __init__(self):
        ...
            
            
    def hill_model(self, L, t):
        a = (380 * 0.098)
        b = 0.325
        PO = a / 0.257
        vm = PO * b / a
        alpha = PO / 0.1
        Lse0 = 0.3
        k = a / 25

        Lse = np.full(len(t), Lse0)
        Lce = np.full(len(t), 1 - Lse0)
    
        H = np.zeros(len(t))
        P = np.zeros(len(t))

        for j in range(len(t) - 1):
            Lse[j] = Lse0 + P[j] / alpha
            Lce[j] = L[j] - Lse[j]
            dt = t[j + 1] - t[j]
            dL = (L[j + 1] - L[j])
            dP = alpha * ((dL / dt) + b * (PO - P[j]) / (a + P[j])) * dt
            P[j + 1] = P[j] + dP
            H[j + 1] = H[j] + (k + a * b * ((PO - P[j]) / (a + P[j]))) * dt

        Lse[-1] = Lse0 + P[-1] / alpha
        Lce[-1] = L[-1] - Lse[-1]
        
        for i in range(len(H)):
            H[i] += (k / 10) * (np.random.randn() - 0.5)
            P[i] += (PO / 100) * (np.random.randn() - 0.5)
            
        print(vm)

        return P, H, Lse, Lce


    def Plotar_grafico_Lce_Lse_força(self, length, segs):
        # ENTRADA COM O LENGHT E PASSOS
        L = [length] * 200 * segs
        t = []

        inc = 0
        for i in range(len(L)):
            t.append(inc)
            inc += 0.005   
            
        # INFERENCIA COM O MODELO    
        P, H, Lse, Lce = self.hill_model(L, t)


        # PLOT DOS RESULTADOS 
        data = {
            'L' : L,
            't' : t,
            'P' : P,
            'H' : H,
            'Lse' : Lse,
        'Lce' : Lce
        }

        df = pd.DataFrame(data)

        print(df)

        # Criar figura e eixos
        fig, ax1 = plt.subplots()

        # Criar um segundo eixo y para Lse/Lce
        ax1.plot(df['t'], df['Lse'], color='m', label='Lse')
        ax1.plot(df['t'], df['Lce'], color='c', label='Lce')
        ax1.set_ylabel('Comprimento (muscle lenght)', color='black')

        # Plotar P no eixo y esquerdo
        ax2 = ax1.twinx()
        ax2.plot(df['t'], df['P'], color='black', label="force")
        ax2.set_ylabel('Força (mN/mm²)', color='black')


        # Adicionar legendas
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')


        # Exibir o gráfico
        plt.title('A')
        plt.xlabel('Tempo (t)')
        plt.grid(True)
        #plt.show()

        plt.savefig('static/images/grafico_Lce_Lse_força.png')

        return df

    def Plotar_grafico_Heat_Time(self, velocidades):
        dfs = []
           
        for i in range(len(velocidades)):
            #z = ((i+1)/2)
            #print(z)
            L = np.full(200 * 2, 2.0)
            
            if len(velocidades) != 0:
                L = np.concatenate((L, np.arange(2.0, 1, -0.005 / velocidades[i])))
                L = np.concatenate((L, np.full(1200 - len(L), 1)))
            else:
                L = np.concatenate((L, np.full(1200 - len(L), 2)))

            t = np.arange(0.0, len(L)*0.005, +0.005)

            # INFERENCIA COM O MODELO    
            P, H, Lse, Lce = self.hill_model(L, t)

            # PLOT DOS RESULTADOS 
            data = {
                'L' : L,
                't' : t,
                'P' : P,
                'H' : H,
                'Lse' : Lse,
                'Lce' : Lce
            }

            df = pd.DataFrame(data)
            print(df)
            dfs.append(df)

        # Criar figura e eixos
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 6))
        fig, ax1 = plt.subplots()
        fig, ax2 = plt.subplots()

        for idx, df in enumerate(dfs):
            ax1.plot(df['t'], df['L'], color='C'+str(idx), label=f'Length {idx+1}')            
            ax2.plot(df['t'], df['H'], color='C'+str(idx), label=f'Heat {idx+1}')


        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Comprimento (mm)')
        ax1.set_title('A')
        #ax1.legend()
        
        ax2.set_xlabel('Tempo (s)')
        ax2.set_ylabel('Heat/Volume (mN/mm²)')
        ax2.set_title('B')
        #ax2.legend()

        ax1.grid(True)
        ax2.grid(True)
        
        #plt.show()
        #plt.tight_layout()
        ax1.figure.savefig('static/images/grafico_tamanho.png')
        ax2.figure.savefig('static/images/grafico_calor.png')

        #return df

        
if __name__ == '__main__':

    hillModel = Hill_Model()
    # hillModel.Plotar_grafico_Lce_Lse_força()
    hillModel.Plotar_grafico_Heat_Time(np.arange(0.1, 4, +0.1))