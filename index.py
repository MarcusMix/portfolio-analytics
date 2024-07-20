from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def data_csv():
    df = pd.read_excel("projetos.xlsx")
    df = df.to_dict(orient="records")
    return df

@app.route("/")
def index():
    data = data_csv()
    description = "Analista de Dados com mais de 1 ano de experiência profissional em analytics, automações, desenvolvimento de dashboards, resolução de problemas e entendimento do negócio."
    description_low = "Cursando Superior em Análise e Desenvolvimento de Sistemas no SENAC."
    return render_template('index.html' ,description=description, description_low=description_low, data=data)


@app.route("/projects")
def project():
    data = data_csv()
    return render_template('projects.html', data=data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80, debug=True)