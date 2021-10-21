import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyList {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyList.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		List l1 = new List(); // Constructor 1
		l1.add("Item 1"); // Method 1
		l1.add("Item 2"); // Method 1
		l1.add("Item 3"); // Method 1
		l1.add("Item 4"); // Method 1
		l1.add("Item 5"); // Method 1
		l1.add("Item 6", 7/*index*/); // Method 2
		l1.remove(5/*index*/); // Method 4
		l1.remove("Item 3"); // Method 5
		System.out.println("l1.getItemCount() = " + l1.getItemCount()); // Method 3
		l1.deselect(0); // Method 6
		System.out.println("\nl1.getItem(int index) = " + l1.getItem(0)); // Method 7
		System.out.println("\nString array of l1.items =");
		String items[] = l1.getItems(); // Method 8
		for (int i = 0; i < l1.getItemCount(); i++) { // Method 3
			System.out.println(items[i]);
		}
		System.out.println("\nl1.getSelectedIndex(int index) = " + l1.getSelectedIndex()); // Method 10 // Only for singleSelect
		int l1Selected[] = l1.getSelectedIndexes(); // Method 11 // For both singleSelect and multiSelect
		System.out.println("l1.getSelectedIndexes = " + l1Selected.length);
		// for (int i = 0; i < l1Selected.length; i++) {
		// 	System.out.println("l1.getSelectedIndexes = " + l1Selected[i]);
		// 	if (l1Selected.length == -1) {
		// 		break;
		// 	}
		// }
		System.out.println("l1.getSelectedItem = " + l1.getSelectedItem()); // Method 12
		String selectedItems[] = l1.getSelectedItems(); // Method 13
		System.out.println("l1.getSelectedItems = " + selectedItems.length);
		System.out.println("l1.isMultipleMode() = " + l1.isMultipleMode()); // Method 14
		l1.select(0); // Method 19
		System.out.println("l1.isIndexSelected(int index) = " + l1.isIndexSelected(0)); // Method 15
		panel.add(l1);

		int rows = 6;
		List l2 = new List(rows); // Constructor 2 // specifies number of items on display
		l2.add("Item 1"); // Method 1
		l2.add("Item 2"); // Method 1
		l2.add("Item 3"); // Method 1
		l2.add("Item 4"); // Method 1
		l2.add("Item 5"); // Method 1
		l2.add("Item 6"); // Method 1
		l2.add("Item 7"); // Method 1 // no error
		if(l2.getRows() == rows) { // Method 9
			System.out.println("\nNumber of visible l2.rows = " + l2.getRows()); // Method 9
		}
		l2.makeVisible(6); // Method 16
		l2.replaceItem("New Item 7", 6); // Method 18
		l2.remove(5); // Method 21
		l2.remove("Item 4"); // Method 22
		panel.add(l2);

		List l3 = new List(5, true); // Constructor 3 // specifies number of items on display and sets Multiple Select
		l3.add("Item 1"); // Method 1
		l3.add("Item 2"); // Method 1
		l3.add("Item 3"); // Method 1
		l3.add("Item 4"); // Method 1
		l3.add("Item 5"); // Method 1
		int l3Selected[] = l3.getSelectedIndexes(); // Method 11 // For both singleSelect and multiSelect
		System.out.println("\nl3.getSelectedIndexes = " + l3Selected.length);
		l3.setMultipleMode(false); // Method 20
		System.out.println("l3.isMultipleMode() = " + l3.isMultipleMode()); // Method 14
		l3.removeAll(); // Method 17
		panel.add(l3);

		frame.setVisible(true);
	}
}

// ActionEvent and ItemEvent