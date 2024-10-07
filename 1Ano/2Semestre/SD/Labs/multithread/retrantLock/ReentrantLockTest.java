import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ReentrantLockTest extends Thread {
    
    private final Lock lock = new ReentrantLock();
    private int seats = 100;

    public void run(){
        while(seats != 0){
            lock.lock();
            try{
                while(seats <= 100 && seats > 0){
                    try{
                        Thread.sleep(50);
                    }catch(InterruptedException e){
                        e.printStackTrace();
                    }
                    seats--;
                    System.out.println(Thread.currentThread().getName() + " booked a seat, the seats left= " + seats);
                }
            }finally{
                lock.unlock();
            }
        }
    }
public static void main(String[] args) throws InterruptedException {
        ReentrantLockTest test = new ReentrantLockTest(); // Create an instance of ReentrantLockTest
        Thread t1 = new Thread(test, "Station 1"); // Pass the ReentrantLockTest instance to the Thread constructor
        Thread t2 = new Thread(test, "Station 2"); // Pass the same ReentrantLockTest instance to another thread

        t1.start();
        t2.start();

        t1.join(); // Isto faz com que o programa principal espere até que ambas as threads tenham terminado a execução antes de continuar
        t2.join();
    }
}


