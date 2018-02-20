package org.kimi.thread;

/**
 * Created by kimi on 8/20/17.
 */
public class TestRunnable implements Runnable {
    private int ticket = 99;

    public void run() {
        for (int i = 0; i < 100; i++) {
            if (this.ticket > 0) {
                System.out.println(Thread.currentThread().getName()
                        + " buy " + this.ticket--);
            }
        }
    }

    public static void main(String[] args) {
        TestRunnable testRunnable1 = new TestRunnable();

        new Thread(testRunnable1, "T1").start();
        new Thread(testRunnable1, "T2").start();
        new Thread(testRunnable1, "T3").start();
    }
}
