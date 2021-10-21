import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyTextField {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyTextField.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		TextField t1 = new TextField(); // Constructor 1
		panel.add(t1);
		char c = '*';
		t1.setEchoChar(c); // Method 5
		System.out.println("t1.echoCharIsSet() = " + t1.echoCharIsSet()); // Method 1
		System.out.println("t1.getEchoChar() = " + t1.getEchoChar()); // Method 3
		t1.setColumns(10); // Method 4
		t1.setText("Text Field 1"); // Method 6
		
		TextField t2 = new TextField(20); // Constructor 2
		panel.add(t2);
		System.out.println("t2.getColumns() = " + t2.getColumns()); // Method 2
		
		TextField t3 = new TextField("Text Field 3"); // Constructor 3
		panel.add(t3);

		frame.setVisible(true);
	}
}

// KeyEvent and ActionEvent