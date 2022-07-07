import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyLabel {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyLabel.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		Label label1 = new Label(); // Constructor 1
		label1.setText("Label 1"); // Method 1
		// label1.setAlignment(Label.LEFT); // Method 2
		panel.add(label1);

		Label label2 = new Label("Label 2"); // Constructor 2
		label2.setAlignment(Label.CENTER); // Method 2
		panel.add(label2);

		Label label3 = new Label("Label 3", Label.RIGHT); // Constructor 3
		panel.add(label3);

		frame.setVisible(true);

		System.out.println("Text\t\tAlignment");
		System.out.println(label1.getText() + "\t\t" + label1.getAlignment()); // Method 3 and 4
		System.out.println(label2.getText() + "\t\t" + label2.getAlignment()); // Method 3 and 4
		System.out.println(label3.getText() + "\t\t" + label3.getAlignment()); // Method 3 and 4
	}
}

// No Events