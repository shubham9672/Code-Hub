import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyTextArea {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyTextArea.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		TextArea t1 = new TextArea(); // Constructor 1
		panel.add(t1);
		t1.setColumns(60); // Method 8
		System.out.println("t1.getColumns() = " + t1.getColumns()); // Method 2
		t1.setRows(10); // Method 9
		System.out.println("t1.getRows() = " + t1.getRows()); // Method 4
		Dimension d = t1.getMinimumSize(); // Method 3
		System.out.println("d.width = " + d.width + "\td.height = " + d.height);

		TextArea t2 = new TextArea(10/*Rows*/, 60/*Columns*/); // Constructor 2 // Default (10, 60)
		panel.add(t2);
		
		TextArea t3 = new TextArea("Text Area 3"); // Constructor 3
		t3.append("\tAppend Hello World"); // Method 1
		t3.insert("\tInsert", 18); // Method 6
		t3.replaceRange("Heyoo", 26, 31); // Method 7
		panel.add(t3);
		
		TextArea t4 = new TextArea("Text Area 4", 10, 60); // Constructor 4
		panel.add(t4);
		
		TextArea t5 = new TextArea("Text Area 5", 10, 60, 4); // Constructor 5
		System.out.println(t5.getScrollbarVisibility()); // Method 5
		panel.add(t5);

		frame.setVisible(true);
	}
}

// KeyEvent and TextEvent