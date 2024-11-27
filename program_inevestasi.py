import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class InvestmentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Penghitung Investasi')

        self.label_principal = QLabel('Modal Awal (Rp):')
        self.input_principal = QLineEdit()

        self.label_rate = QLabel('Bunga Tahunan (%):')
        self.input_rate = QLineEdit()

        self.label_time = QLabel('Durasi (Tahun):')
        self.input_time = QLineEdit()

        self.calculate_button = QPushButton('Hitung')
        self.calculate_button.clicked.connect(self.calculate_investment)

        self.result_label = QLabel('Hasil akhir.')

        layout = QVBoxLayout()
        layout.addWidget(self.label_principal)
        layout.addWidget(self.input_principal)
        layout.addWidget(self.label_rate)
        layout.addWidget(self.input_rate)
        layout.addWidget(self.label_time)
        layout.addWidget(self.input_time)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_investment(self):
        try:

            principal = float(self.input_principal.text())
            rate = float(self.input_rate.text()) / 100
            time = int(self.input_time.text())

            final_amount = principal * ((1 + rate) ** time)

            self.result_label.setText(f'Nilai akhir investasi: Rp {final_amount:,.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Mohon masukkan angka yang valid!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = InvestmentCalculator()
    calculator.show()
    sys.exit(app.exec_())