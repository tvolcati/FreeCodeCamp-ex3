import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    print("iniciando")
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    print("Scatter plot criado")
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_pd = pd.Series([i for i in range(1880, 2051)])
    y_pd = res.slope * x_pd + res.intercept
    plt.plot(x_pd, y_pd, 'r', label='Previsão 1880-2050')
    print("Linha de regressão feita")

    # Generate second regression line
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    res_recent = linregress(x_recent, y_recent)
    x_pd_recent = pd.Series([i for i in range(2000, 2051)])
    y_pd_recent = res_recent.slope * x_pd_recent + res_recent.intercept
    plt.plot(x_pd_recent, y_pd_recent, 'g', label='Previsão 2000-2050')
    print("Segunda linha de regressão feita.")

    # Set labels and title
    plt.xlabel('Ano')
    plt.ylabel('Nível Mar (polegadas)')
    plt.title('Aumento do Nível do Mar')
    plt.legend()
    plt.xlim(1850, 2075)
    print("Rótulos/título definidos.")
    plt.savefig('sea_level_plot.png')
    print("Gráfico salvo 'sea_level_plot.png'.")
    
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
    print("Processo concluído. Veja 'sea_level_plot.png'.")