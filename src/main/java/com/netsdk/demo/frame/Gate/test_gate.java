package com.netsdk.demo.frame.Gate;

public class test_gate {
    public static void main(String[] args) {
        long x = 2147483640;
        int y = 15;
        long sum = x + y;
        System.out.println(sum); // -2147483641
    }

}
