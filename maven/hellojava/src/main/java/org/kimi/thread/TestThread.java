package org.kimi.thread;

/**
 * Created by kimi on 8/20/17.
 */
public class TestThread extends Thread {
    private int count;
    private String name;

    public TestThread(int count, String name) {
        this.count = count;
        this.name = name;
    }

    @Override
    public void run() {
        while (count > 0) {
            System.out.println(name + " get " + count--);
        }
    }

    public static void main(String[] args) {
        TestThread thread1 = new TestThread(10, "Tom");
        TestThread thread2 = new TestThread(10, "Jack");

        thread1.start();
        thread2.start();
    }
}
