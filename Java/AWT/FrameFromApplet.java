// <applet 
//     code = "FrameFromApplet.class" 
//     width = "420" 
//     height = "69"
//     alt = "Applet Here" 
//     name = "FrameFromApplet" 
//     align = "center"
// >
// </applet> 

import java.applet.Applet;
import java.awt.*;

class MyFrame extends Frame {
	MyFrame(String title) {
		// super(title); // Only needed if want to set properties like this (title in this case)
		setTitle(title);

		// Label l = new Label("Frame");
		// l.setAlignment(Label.CENTER);
		// add(l);

		// setVisible(true); // NOT NEEDED
	}
	public void paint(Graphics g) {
		g.drawString("Frame", 69, 69);
	}
}

public class FrameFromApplet extends Applet{
	Frame f;
	public void init() {
		f = new MyFrame("FrameFromApplet.java");
		f.setSize(420, 420);
		// f.setVisible(true); // NOT NEEDED
	}
	public void start() {
		f.setVisible(true);	
	}
	public void stop() {
		f.setVisible(false);
	}
	public void paint(Graphics g) {
		g.drawString("from Applet", 9, 20);
	}
}