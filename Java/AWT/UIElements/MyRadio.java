import java.awt.*;

class HomeFrame extends Frame{
	HomeFrame(String title) {
		setTitle(title);
		setSize(420, 420);
	}
}

public class MyRadio {
	public static void main(String[] args) {
		Frame frame = new HomeFrame("MyRadio.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		Panel panel = new Panel();
		frame.add(panel);

		CheckboxGroup cbg = new CheckboxGroup();

		Checkbox checkbox1 = new Checkbox();
		checkbox1.setLabel("Radio Button 1"); // Method 1
		checkbox1.setState(true); // Method 2
		checkbox1.setCheckboxGroup(cbg); // Method 3
		panel.add(checkbox1);

		Checkbox checkbox2 = new Checkbox("Radio Button 2", false, cbg); // Constructor 4
		// checkbox2.setState(true);
		panel.add(checkbox2);

		frame.setVisible(true);

		System.out.println("Label\t\tState\t\tCheckbox Group");
		System.out.println(checkbox1.getLabel() + "\t" + checkbox1.getState() + "\t" + checkbox1.getCheckboxGroup()); // Method 4, 5 and 6
		System.out.println(checkbox2.getLabel() + "\t" + checkbox2.getState() + "\t" + checkbox2.getCheckboxGroup()); // Method 4, 5 and 6

		// Checkbox chbx = getSelectedCheckbox();
		// System.out.println(chbx.getLabel());
	}
}

// ItemEvent