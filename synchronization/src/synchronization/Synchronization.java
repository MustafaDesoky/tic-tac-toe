/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package synchronization;

/**
 *
 * @author ahmedalisalim
 */
public class Synchronization {

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        MessageHandler messageHandler = new MessageHandler();
        ThreadHandler thread1
                = new ThreadHandler(" Ahmed ", messageHandler);
        ThreadHandler thread2
                = new ThreadHandler(" Salim ", messageHandler);

        
        thread1.start();
        
        thread2.start();

//        // wait for threads to end 
//        try {
//            thread1.join();
//            thread2.join();
//        } catch (Exception e) {
//            System.out.println("Interrupted");
//        }
    }
}
