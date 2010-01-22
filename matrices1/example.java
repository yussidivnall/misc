public class example{

	public static void main(String args[]){
		double a[][]={{3,7},{4,-1},{-5,2}};
		double b[][]={{-5,-3},{10,6}};
		double c[][]={{-2,3},{-4,5}};
		Matrix A = new Matrix(a);
		Matrix B = new Matrix(b);
		Matrix C = new Matrix(c);


		C.multiply(C.invert()).print();
		//double ic[][]={{2.5,-1.5},{2,-1}};
		//Matrix IC = new Matrix(ic);
		//Matrix CI = C.invert();

		//CI.print();
		//C.multiply(IC).print();
		/*A.print();
		System.out.println();
		B.print();
		System.out.println();
		C.print();

		Matrix AC = A.multiply(C);
		System.out.println();
		AC.print();
	
		Matrix CA = C.multiply(A);
		*/
	/*	double v1[][]={{2,7},{3,8},{4,9}};
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
	*/	
	}

}
