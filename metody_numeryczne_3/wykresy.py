import matplotlib.pyplot as plt

def wykres(a, b, arguments, values, file_arguments, arguments2, values2, calculated_file):
    plt.plot(arguments, values, color='blue', label='Funkcja pierwotna')
    plt.plot(arguments2, values2, color='orange', label='Funkcja interpolacyjna')
    plt.scatter(file_arguments, calculated_file, c='green', label='Podane wezły')
    plt.legend()
    plt.title("Wykresy funkcji interpolowanej i interpolacyjnej")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid(True)
    plt.xlim(a, b)
    plt.show()