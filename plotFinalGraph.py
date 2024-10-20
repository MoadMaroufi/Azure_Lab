import pandas as pd
import matplotlib.pyplot as plt


def calulcatePlot(csv_file, label, color):
    df = pd.read_csv(csv_file)
    df['Successful Requests/s'] = df['Requests/s'] - df['Failures/s']

    #  interval=index of the DataFrame to avoid unix timestamp problems
    plt.plot(df.index, df['Successful Requests/s'], label=label, color=color)


plt.figure(figsize=(12, 6))


calulcatePlot('func.csv', 'Func Successful Requests/s', 'blue')
calulcatePlot('local.csv', 'Local Successful Requests/s', 'green')
calulcatePlot('vmss.csv', 'VMSS Successful Requests/s', 'red')
calulcatePlot('webApp.csv', 'WebApp Successful Requests/s', 'purple')


plt.title('Successful Requests per Second Over Intervals')
plt.xlabel('Interval')
plt.ylabel('Requests per Second')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
