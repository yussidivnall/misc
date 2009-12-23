import java.math.*;


public class gaus{
	double[][] matrix;  //x^2,x,0
	double[] vector;
	gaus(){
                double X_values[] = {2,3,4,5};
                double Y_values[] = {5,3,7,2};
               	check_input(X_values,Y_values);
		show_stuff.show_formulas(X_values,Y_values); 
		matrix = new double[X_values.length][3];
		vector = new double[Y_values.length];
		populate_matrix(X_values,Y_values);
		show_stuff.show_matrix(matrix,vector);
		show_stuff.show_formulas(matrix,vector);
		eliminate(matrix,vector);
	}
	public void check_input(double xs[],double ys[]){
		if(xs==null || ys == null)System.exit(1);
                if(xs.length != ys.length)System.exit(2);
	}

	public void populate_matrix(double xs[],double ys[]){
		for(int i =0; i < xs.length;i++){
			matrix[i][0]=xs[i]*xs[i]; // for a
			matrix[i][1]=xs[i]; // for b
			matrix[i][2]=1; // no x for c	
		}
		for(int i=0;i<ys.length;i++){
			vector[i]=ys[i];	
		}
	}
	public void eliminate(double m[][],double v[]){
		//step 1 eliminate X^2s coefficients (as)
		double temp_matrix_a[][]= new double[m.length][3];
		temp_matrix_a[0][0]=m[0][0];	temp_matrix_a[0][1]=m[0][1];	temp_matrix_a[0][2]=m[0][2]; // first row doesn't change
		double temp_vector_a[] = new double[v.length];
		temp_vector_a[0]=v[0];		//as does that
		double pivot_1_1 = m[0][0];
		for(int i = 1;i<v.length;i++){
				double factor = m[i][0]/pivot_1_1;
				double as = m[i][0]-(m[0][0]*factor);//should be 0!
				double bs = m[i][1]-(m[0][1]*factor);
				double cs = m[i][2]-(m[0][2]*factor);
				double ys = v[i]-(v[0]*factor);
				temp_matrix_a[i][0]=as;		temp_matrix_a[i][1]=bs;		temp_matrix_a[i][2]=cs;
				temp_vector_a[i]=ys;
		}
		show_stuff.show_matrix(temp_matrix_a,temp_vector_a);
		//step 2 eliminate x coeficients(bs)
		double temp_matrix_b[][]= new double[m.length][3]; double temp_vector_b[] = new double[v.length];
		temp_matrix_b[0][0]=temp_matrix_a[0][0];temp_matrix_b[0][1]=temp_matrix_a[0][1];temp_matrix_b[0][2]=temp_matrix_a[0][2];
		temp_matrix_b[1][0]=temp_matrix_a[1][0];temp_matrix_b[1][1]=temp_matrix_a[1][1];temp_matrix_b[1][2]=temp_matrix_a[1][2];
		temp_vector_b[0]=temp_vector_a[0];temp_vector_b[1]=temp_vector_a[1]; // first two rows stay the same
		double pivot_2_2 = temp_matrix_a[1][1];
		for(int i = 2;i<v.length;i++){
				double factor = temp_matrix_a[i][1]/pivot_2_2;
				double as = temp_matrix_a[i][0]-(temp_matrix_a[1][0]*factor);//should already be 0, for the sake of clarity only
				double bs = temp_matrix_a[i][1]-(temp_matrix_a[1][1]*factor);
				double cs = temp_matrix_a[i][2]-(temp_matrix_a[1][2]*factor);
				double ys = temp_vector_a[i]-(temp_vector_a[1]*factor);
				temp_matrix_b[i][0]=as;
				temp_matrix_b[i][1]=bs;
				temp_matrix_b[i][2]=cs;
				temp_vector_b[i]=ys;
		}
		System.out.println("Eliminated to:");
		show_stuff.show_matrix(temp_matrix_b,temp_vector_b);
		System.out.println("Which as formula is:");
		show_stuff.show_formulas(temp_matrix_b,temp_vector_b);
	}

	public static void main(String args[]){
		gaus g = new gaus();
	}

}
