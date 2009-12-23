public class example{

	public static void print_matrix(Matrix m){
		double arr[][]=m.get_matrix();
		for(int c=0;c<arr.length;c++){
			System.out.print("|");
			for(int r=0;r<arr[c].length;r++){
				System.out.print(arr[c][r]+" ");
			}
			System.out.println("|");
		}
	}

	public static void main(String args[]){
		double v1[][]={{1,2,3},{4,5,6},{7,8,9}};
		Matrix m1= new Matrix(v1);
		print_matrix(m1);
		Matrix id=m1.get_identity();
		System.out.println("identity");
		print_matrix(id);
		Matrix jg = m1.join_identity();
		System.out.println("joined");
		print_matrix(jg);
	}
}
