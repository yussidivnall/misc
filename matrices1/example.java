public class example{

	public static void main(String args[]){
		//Question 3b
		/*
		double a[][]={{-2,3},{-4,5}};
		Matrix A = new Matrix(a);
		Matrix A_I = A.invert();
		A_I.print();

		double b[][]={{5},{7}};
		Matrix B = new Matrix(b);
		System.out.println("X");
		B.print();
		System.out.println("=");
		A_I.multiply(B).print();
		*/

		//question 3a
		double a[][]={{3,7},{4,-1},{-5,2}};
		double b[][]={{-5,-3},{10,6}};
		double c[][]={{-2,3},{-4,5}};
		Matrix A = new Matrix(a);
		Matrix B = new Matrix(b);
		Matrix C = new Matrix(c);

		//(i) 2A + 3B
		//(iii) AC
		A.multiply(C).print();
		//C^-1
		C.invert().print();
		
		//C.multiply(C.invert()).print();
		
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
