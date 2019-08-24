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
public class ThreadHandler extends Thread {

    MessageHandler messageHandler;
    private String message;
    private Thread thread;

    // Recieves a message object and a string 
    // message to be sent 
    ThreadHandler(String m, MessageHandler obj) {
        message = m;
        messageHandler = obj;
    }

    // synchronized method
    public void run() {
        // one thread can handlle a message at a time. 
        messageHandler.showWithSync(message);
    }

//    // unsynchronized method
//    public void run() {
//        // multiable threads can handlle a message at a time. 
//        messageHandler.showWithoutSync(message);
//    }

//    // synchronized opject
//    public void run() {
//        // one thread can access massageHndler object at a time
//        synchronized (messageHandler) {
//        // synchronizing the messageHandler object 
//        messageHandler.showWithoutSync(message);
//
//        }
//    }

}
