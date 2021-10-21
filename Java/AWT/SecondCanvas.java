import java.awt.*;

class MyCanvas extends Canvas {
	MyCanvas() {
		setSize(169, 169);
		setBackground(Color.GRAY);
	}
	public void paint(Graphics g) {
		g.drawString("Hello", 10, 10);
	}
}

public class SecondCanvas {
	Frame f1;
	Label l1;
	Panel p1;

	SecondCanvas() {
		f1 = new Frame("SecondCanvas.java");
		f1.setSize(420, 420);
		f1.setLayout(new GridLayout(3, 1));
		l1 = new Label();
		p1 = new Panel();
		f1.add(l1);
		f1.add(p1);
		f1.setVisible(true);
	}

	public void showCanvas() {
		l1.setText("Canvas");
		Canvas c = new MyCanvas();
		p1.add(c);
		f1.setVisible(true);
	}

	public static void main(String[] args) {
		SecondCanvas canvas = new SecondCanvas();
		canvas.showCanvas();
	}
}		