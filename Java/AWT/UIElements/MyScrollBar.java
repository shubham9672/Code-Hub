import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyScrollBar {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyChoice.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		Scrollbar s1 = new Scrollbar(); // Constructor 1
		s1.setValues(12, 1, 0, 255); // Method 16
		panel.add(s1);
		Scrollbar s2 = new Scrollbar(Scrollbar.HORIZONTAL); // Constructor 2
		panel.add(s2);
		Scrollbar s3 = new Scrollbar(Scrollbar.HORIZONTAL, 0, 1, 0, 255); // Constructor 3
		s3.setBlockIncrement(3); // Method 9
		System.out.println("s3.getBlockIncrement() = " + s3.getBlockIncrement()); // Method 1
		s3.setMaximum(420); // Method 10
		System.out.println("s3.getMaximum() = " + s3.getMaximum()); // Method 2
		s3.setMinimum(69); // Method 11
		System.out.println("s3.getMinimum() = " + s3.getMinimum()); // Method 3
		s3.setOrientation(Scrollbar.VERTICAL); // Method 12
		System.out.println("s3.getOrientation() = " + s3.getOrientation()); // Method 4
		s3.setUnitIncrement(5); // Method 13
		System.out.println("s3.getUnitIncrement() = " + s3.getUnitIncrement()); // Method 5
		s3.setValue(169); // Method 14
		System.out.println("s3.getValue() = " + s3.getValue()); // Method 6
		s3.setValueIsAdjusting(true); // Method 15
		System.out.println("s3.getValueIsAdjusting() = " + s3.getValueIsAdjusting()); // Method 7
		s3.setVisibleAmount(25); // Method 17
		System.out.println("s3.getVisibleAmount() = " + s3.getVisibleAmount()); // Method 8
		panel.add(s3);

		frame.setVisible(true);
	}
}

// AdjustmentEvent