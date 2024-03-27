from flask import Flask, render_template, request
from hill_model.Hill_model import Hill_Model

# Criar a aplicação Flask
app = Flask(__name__)
hillModel = Hill_Model()

velocidades = []

@app.route('/teste', methods=['GET','POST'])
def teste():
    if request.method == 'POST':
        velocidade = float(request.form['speed'])
        # segs = int(request.form['segs'])   
        velocidades.append(velocidade)
        print("velocidade: ", velocidade)
        # print("segs: ", segs)
        
        if velocidade == 0:
            velocidades.clear()
            
        hillModel.Plotar_grafico_Heat_Time(velocidades)
        #df = hillModel.Plotar_grafico_Lce_Lse_força(length=length, segs=segs)
        #primeiras_linhas = df.head().to_dict(orient='records')
        
        return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)