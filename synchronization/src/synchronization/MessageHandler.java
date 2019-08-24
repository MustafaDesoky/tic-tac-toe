package synchronization;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author ahmedalisalim
 */
public class MessageHandler {

    public synchronized void showWithSync(String message) {
        System.out.println("Showing....." + message);
        
        System.out.println(" " + message + " Showed");
    }

    public void showWithoutSync(String message) {
        System.out.println("Showing....." + message);
        
        System.out.println(message + " Showed");
    }
}
