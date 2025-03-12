import tkinter as tk
from tkinter import messagebox

class NeuralNetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Neural Network")

        self.nn = SimpleNeuralNetwork(input_size=2, hidden_size=3, output_size=1)

        self.create_widgets()

    def create_widgets(self):
        self.label_x1 = tk.Label(self.root, text="Input X1:")
        self.label_x1.pack()
        self.entry_x1 = tk.Entry(self.root)
        self.entry_x1.pack()

        self.label_x2 = tk.Label(self.root, text="Input X2:")
        self.label_x2.pack()
        self.entry_x2 = tk.Entry(self.root)
        self.entry_x2.pack()

        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict)
        self.predict_button.pack()

        self.result_label = tk.Label(self.root, text="Prediction: ")
        self.result_label.pack()

    def predict(self):
        try:
            x1 = float(self.entry_x1.get())
            x2 = float(self.entry_x2.get())
            input_data = np.array([[x1, x2]])
            prediction = self.nn.forward(input_data)
            self.result_label.config(text=f"Prediction: {prediction[0][0]}")
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers for X1 and X2")

if __name__ == "__main__":
    root = tk.Tk()
    app = NeuralNetApp(root)
    root.mainloop()
