package tag.greedy;

import java.util.Scanner;

public class No1439 {
	
	/**
	 	[Greedy] Silver05 - 1439. 뒤집기
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//문자열 입력
		String str = sc.next();
		String[] strArr = str.split("");
		//0,1 덩어리 개수
		int zero = 0, one = 0;
		String standard = strArr[0];
		if(standard.equals("0")) {
			zero++;
		}else {
			one++;
		}
		
		//덩어리 개수 세기
		for(int i=1; i<strArr.length; i++) {
			if(!strArr[i].equals(standard)) {
				standard = strArr[i];
				if(standard.equals("0")) {
					zero++;
				}else {
					one++;
				}
			}
		}
		
		System.out.print(Math.min(zero, one));
		
	}
}
