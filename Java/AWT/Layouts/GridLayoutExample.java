import java.awt.*;

public class GridLayoutExample {
	public static void main(String[] args) {
		Frame frame = new Frame("GridLayoutExample.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		frame.setLayout(new GridLayout(3/*Rows*/, 2/*Columns*/)); // 0 is allowed but not both(IllegalArgumentException)
		frame.setSize(420, 420);
		frame.add(new Button("One"));
		frame.add(new Button("Two"));
		frame.add(new Button("Three"));
		frame.add(new Button("Four"));
		frame.add(new Button("Five"));
		frame.add(new Button("Six"));

		frame.setVisible(true);
	}
}