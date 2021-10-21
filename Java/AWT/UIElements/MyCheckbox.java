import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyCheckbox {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyCheckbox.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		Checkbox checkbox1 = new Checkbox(); // Constructor 1
		checkbox1.setLabel("Checkbox 1"); // Method 1
		checkbox1.setState(false); // Method 2
		panel.add(checkbox1);

		Checkbox checkbox2 = new Checkbox("Checkbox 2"); // Constructor 2
		checkbox2.setState(true); // Method 2
		panel.add(checkbox2);

		Checkbox checkbox3 = new Checkbox("Checkbox 3", false); // Constructor 3
		panel.add(checkbox3);

		frame.setVisible(true);

		System.out.println("Label\t\tState");
		System.out.println(checkbox1.getLabel() + "\t" + checkbox1.getState()); // Method 4 and 5
		System.out.println(checkbox2.getLabel() + "\t" + checkbox2.getState()); // Method 4 and 5
		System.out.println(checkbox3.getLabel() + "\t" + checkbox3.getState()); // Method 4 and 5
	}
}

// ItemEvent