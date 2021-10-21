import java.awt.*;
import javax.swing.*;

public class SwingExample {
	public static void main(String[] args) {
		JFrame jFrame = new JFrame("SwingExample.java");
		jFrame.setSize(420, 420);
		JPanel jPanel = new JPanel();
		jFrame.add(jPanel);
		jPanel.add(new JTextField(25));
		jPanel.add(new JButton("Buttom"));
		JList jList = new JList();
		// jList.add("item 1"); // This doesn't work
		// jList.add("item 2"); // This doesn't work
		// jList.add("item 3"); // This doesn't work
		// jList.add("item 4"); // This doesn't work
		// jList.add("item 5"); // This doesn't work
		jPanel.add(jList);
		jFrame.setVisible(true);
	}
}