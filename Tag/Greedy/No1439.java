package tag.greedy;

import java.util.Scanner;

public class No1439 {
	
	/**
	 	[Greedy] Silver05 - 1439. ������
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//���ڿ� �Է�
		String str = sc.next();
		String[] strArr = str.split("");
		//0,1 ��� ����
		int zero = 0, one = 0;
		String standard = strArr[0];
		if(standard.equals("0")) {
			zero++;
		}else {
			one++;
		}
		
		//��� ���� ����
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
