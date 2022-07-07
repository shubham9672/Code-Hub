import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyButton {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyButton.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		Button button1 = new Button(); // Constructor 1
		button1.setLabel("Button 1"); // Method 1
		panel.add(button1);

		Button button2 = new Button("Button 2"); // Constructor 2
		panel.add(button2);

		frame.setVisible(true);

		System.out.println("Label Text");
		System.out.println(button1.getLabel()); // Method 2
		System.out.println(button2.getLabel()); // Method 2
	}
}

// ActionEvent and MouseEvent