public class example{

	public static void main(String args[]){
		double v1[][]={{2,7},{3,8},{4,9}};
		Matrix m1 = new Matrix(v1);
		m1.print();
		System.out.println("---------------");
		Matrix row = m1.get_row(1);
		row.print();
		System.out.println("==============");
		Matrix c=m1.subtract_row(row,3);
		c.print();
		System.out.println("Transpose");
		Matrix transpose=c.transpose();
		transpose.print();
		System.out.println("Multiply to get symetric matrix");
		transpose.multiply(c).print();
		System.out.println("C * transpose:");
		c.multiply(transpose).print();
		
	}

}
