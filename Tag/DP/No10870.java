package tag.dp;

import java.util.Scanner;

public class No10870 {
	
	/**
	 	[DP] Bronze02 - 10870. �Ǻ���ġ �� 5
	 */
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//�Է¹��� ��
		int n = sc.nextInt();
		//�Ǻ���ġ ��� ���� ������ �迭
		int[] arr = new int[n+1];
		
		//�Ǻ���ġ ���
		for(int i=0; i<=n; i++) {
			if(i == 0) arr[i] = 0;
			else if(i == 1) arr[i] = 1;
			else arr[i] = arr[i-1] + arr[i-2];
		}
		
		System.out.print(arr[n]);
	}
}
