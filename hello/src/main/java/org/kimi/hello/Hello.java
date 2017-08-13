package org.kimi.hello;

/**
 * Created by kimi on 11/19/16.
 */
public class Hello {

    public String sayHello() {
        return "Hello world!";
    }

    public static void main(String[] arg) {
        System.out.print(new Hello().sayHello());
    }
}
