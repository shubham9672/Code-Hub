import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}
// Choice == Dropdown
public class MyChoice {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyChoice.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		Choice c1 = new Choice(); // Constructor 1
		c1.add("item 1"); // Method 1
		c1.add("item 2"); // Method 1
		c1.add("item 3"); // Method 1
		c1.add("item 4"); // Method 1
		c1.add("item 5"); // Method 1
		System.out.println("c1.getItem(int index) = " + c1.getItem(0)); // Method 2
		System.out.println("c1.getItemCount() = " + c1.getItemCount()); // Method 3
		c1.select(1); // Method 11
		c1.select("item 4"); // Method 12
		System.out.println("c1.getSelectedIndex() = " + c1.getSelectedIndex()); // Method 4
		System.out.println("c1.getSelectedItem() = " + c1.getSelectedItem()); // Method 5
		System.out.println("c1.getSelectedObjects() = " + c1.getSelectedObjects()); // Method 6
		c1.insert("item 6", 5); // Method 7
		c1.remove(4); // Method 8
		c1.remove("item 3"); // Method 9
		c1.removeAll(); // Method 10
		panel.add(c1);

		frame.setVisible(true);
	}
}

// ItemEvent