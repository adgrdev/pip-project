import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [2345, 125, 1124]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie1.png')
    plt.close()