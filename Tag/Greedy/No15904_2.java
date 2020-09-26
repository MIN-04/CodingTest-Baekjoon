package tag.greedy;

import java.util.Scanner;

public class No15904_2 {
	
	/**
	 	[Greedy] Bronze01 - 15904. UCPC는 무엇의 약자일까?
	 	
	 	다른 방법
	 	
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//입력받은 문자
		String str = sc.nextLine();
		//UCPC 배열
		char[] arr = {'U','C','P','C'};
		//arr의 인덱스
		int index = 0;
		
		for(int i=0;i<str.length(); i++) {
			if(str.charAt(i) == arr[index]) index++;
			if(index == 4) break;
		}
		
		if(index == 4) {
			System.out.print("I love UCPC");
		}else {
			System.out.print("I hate UCPC");
		}
		
		
	}
}
