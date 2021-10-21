import java.awt.*;

public class FirstCanvas {
	Frame f1;
	Label l1;
	Panel p1;

	FirstCanvas() {
		f1 = new Frame("FirstCanvas.java");
		f1.setSize(420, 420);
		f1.setLayout(new GridLayout(3, 1));
		l1 = new Label();
		p1 = new Panel();
		f1.add(l1);
		f1.add(p1);

		l1.setText("Canvas");
		Canvas c = new Canvas();
		c.setSize(69, 69);
		c.setBackground(Color.GRAY);
		// f1.add(c);
		p1.add(c);
		
		f1.setVisible(true);
	}

	public static void main(String[] args) {
		FirstCanvas canvas = new FirstCanvas();
	}
}		