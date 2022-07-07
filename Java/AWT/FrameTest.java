import java.awt.*;

public class FrameTest extends Frame{
	FrameTest(String title) {
		super(); // Calling the super class constructor (Frame)
		this.setTitle(title);
		this.setSize(420, 420);
		this.setVisible(true);
	}
	public static void main(String[] args) {
		FrameTest f = new FrameTest("FrameTest.java");
	}
}