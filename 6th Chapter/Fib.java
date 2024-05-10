import java.math.*;
import java.util.*;


public class Main {
	static ArrayList<BigInteger> f = new ArrayList<BigInteger>();
	static void Fibonacci(BigInteger a,BigInteger b,long count,BigInteger n){
	    f.add(a);
	    if(a.compareTo(n) != 1)
	        Fibonacci(b,a.add(b),++count,n);
	}
	
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		BigInteger x = new BigInteger("1");
		BigInteger y = new BigInteger("2");
		BigInteger l = new BigInteger("10");
		l = l.pow(100);
		Fibonacci(x,y,0,l);
		int count;
		BigInteger a,b;
		while(sc.hasNext()){
			a = sc.nextBigInteger();
			b = sc.nextBigInteger();
			if(a.compareTo(new BigInteger("0")) == 0 && b.compareTo(new BigInteger("0")) == 0)
				break;
			int i = 0;
			while(f.get(i).compareTo(a) == -1) i++;
			count = 0;
			while(f.get(i).compareTo(b) != 1){
				count++;
				i++;
			}
			System.out.println(count);
		}
		sc.close();
	}
}