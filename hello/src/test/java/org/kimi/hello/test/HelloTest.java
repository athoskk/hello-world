package org.kimi.hello.test;

import org.junit.Test;
import org.kimi.hello.Hello;

import static org.junit.Assert.assertEquals;

/**
 * Created by kimi on 11/19/16.
 */
public class HelloTest {
    @ Test
    public void tesSayHello() {
        Hello hello = new Hello();
        String res = hello.sayHello();
        assertEquals("Hello world!", res);
    }
}
