package tag.greedy;

import java.util.Scanner;

public class No15904_2 {
	
	/**
	 	[Greedy] Bronze01 - 15904. UCPC�� ������ �����ϱ�?
	 	
	 	�ٸ� ���
	 	
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//�Է¹��� ����
		String str = sc.nextLine();
		//UCPC �迭
		char[] arr = {'U','C','P','C'};
		//arr�� �ε���
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
