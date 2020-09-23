package tag.greedy;

import java.util.Scanner;

public class No9625 {
	
	/**
	 	[Greedy] Bronze03 - 5585. °Å½º¸§µ·
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//ÁöºÒÇØ¾ßÇÏ´Â µ·
		int price = sc.nextInt();
		//°Å½º¸§µ· ¹è¿­
		int[] money = {500,100,50,10,5,1};
		//°Å½½·¯Áà¾ßÇÒ µ·
		int change = 1000 - price;
		//°Å½º¸§µ· °¹¼ö
		int cnt = 0;
		
		for(int i=0; i<6; i++) {
			cnt += (change / money[i]);
			change %= money[i];
			if(change == 0) break;
		}
		
		System.out.print(cnt);
	}
}
