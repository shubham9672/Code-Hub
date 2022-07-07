import java.awt.*;

public class FlowLayoutExample {
	public static void main(String[] args) {
		Frame frame = new Frame("FlowLayoutExample.java");
		Image icon = Toolkit.getDefaultToolkit().getImage("../icon.png");
		frame.setIconImage(icon);
		frame.setLayout(new FlowLayout(FlowLayout.LEFT, 10, 5)); // Default in Container class // hGap == vGap == 5
		frame.setSize(420, 420);
		frame.add(new Button("One"));
		frame.add(new Button("Two"));
		frame.add(new Button("Three"));
		frame.add(new Button("Four"));
		frame.add(new Button("Five"));
		frame.add(new Button("Six"));
		frame.add(new Button("Seven"));

		frame.setVisible(true);
	}
}