// <applet 
//     code = "GraphicsMethods.class" 
//     width = "420" 
//     height = "420"
//     alt = "Applet Here" 
//     name = "GraphicsMethods" 
//     align = "center"
// >
// </applet> 

import java.applet.Applet;
import java.awt.*;

public class GraphicsMethods extends Applet{
    public void paint(Graphics g) {

// int getWidth();
        int w = getWidth();
// int getHeight();
        int h = getHeight();
// Dimension getSize();
        Dimension d = getSize();
        double wD = d.getWidth();
        double hD = d.getHeight();

        if(w == wD && h == hD) {
// void drawString("Message", x, y);
            g.drawString("(" + w + ", " + h + ")", 10, 10);
        }

        Font f = new Font("Arial", Font.PLAIN, 28);
// void setFont(Font f);
        g.setFont(f);

// void setBackground(Color c);
        setBackground(Color.WHITE);

        // Color c = new Color(78, 32, 91);
// void setForeground(Color c);
        setForeground(new Color(78, 32, 91)); // Anonymous Object

// void drawLine(int x1, int y1, int x2, int y2);
        g.drawLine(10, 50, 100, 50);

// void drawRect(int x, int y, int width, int height);
        g.drawRect(10, 100, 100, 70);

// void fillRect(int x, int y, int width, int height);
        g.fillRect(150, 100, 100, 70);

// void draw3DRect(int x, int y, int width, int height, boolean raised);
        g.draw3DRect(10, 200, 100, 70, true);

// void fill3DRect(int x, int y, int width, int height, boolean raised);
        g.fill3DRect(150, 200, 100, 70, true);

// void drawRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight);
        g.drawRoundRect(10, 300, 100, 70, 25, 25);

// void fillRoundRect(int x, int y, int width, int height, int arcWidth, int arcHeight);
        g.fillRoundRect(150, 300, 100, 70, 25, 25);

// void drawOval(int x, int y, int xDia, int yDia);
        g.drawOval(10, 400, 100, 70);

// void fillOval(int x, int y, int xDia, int yDia);
        g.fillOval(150, 400, 100, 70);

// void drawArc(int x, int y, int width, int height, int startAngle, int arcAngle);
        g.drawArc(150, 50, 100, 100, 45, 90);

        int x1[] = {10, 30, 60, 90, 100, 150};
        int y1[] = {500, 520, 500, 530, 500, 520};
// void drawPolyLine(int[] x, int[] y, int numSides);
        g.drawPolyline(x1, y1, 5);

        int x2[] = {150, 170, 200, 230, 240, 290};
        int y2[] = {500, 520, 500, 530, 520, 520};
// void drawPolygon(int[] x, int[] y, int numSides);
        g.drawPolygon(x2, y2, 5);
    }  
}
