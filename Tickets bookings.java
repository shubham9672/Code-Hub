/*Sample Input:

5

3

2

  

Sample Output:

John: tickets booked: 3

Mike: tickets booked: 2

*/  




class AvailableTicket extends Thread{

  // Write your code here

    int available;

    int wantedMike;

    int wantedJohn;

    public AvailableTicket(int avail, int reqJohn, int reqMike) {

        available = avail;

        wantedMike = reqMike;

        wantedJohn = reqJohn;

    }

    public void run() {

        synchronized (this) {

            int wanted;

            String threadName = Thread.currentThread().getName();

            if(threadName=="John") {

                wanted = wantedJohn;

            }

            else {

                wanted = wantedMike;

            }

            if(available >= wanted) {

                System.out.print(Thread.currentThread().getName());

                System.out.println(": tickets booked: " + wanted);

                available = available - wanted;

            }

            else {

                System.out.println(Thread.currentThread().getName() + ": not booked");

            }

        }

    }




}
