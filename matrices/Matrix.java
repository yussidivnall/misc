public class Matrix{
	double matrix[][];
	int rows;int cols;

	Matrix(int num_cols,int num_rows){
		cols=num_cols;rows=num_rows;
		matrix=new double[num_cols][num_rows];
	}
	Matrix(double m[][]){
		matrix=m;
	}

	public double get_entry(int c,int r){
		return matrix[c-1][r-1];
	}
	public void set_entry(int c,int r,double v){
		matrix[c-1][r-1]=v;
	}
	public double[][] get_matrix(){
		return matrix;
	}
	public int get_width(){
		return matrix[0].length+1;
	}
	public int get_height(){
		return matrix.length+1;
	}
	public Matrix get_identity(){
		int width=matrix.length;
		int height=matrix[0].length;
		if(width!=height){
			System.out.println("Not a square matrix, can't get identify");
			System.exit(1);
		}
		double ident[][]=new double[width][height];
		for(int i=0;i<width;i++){
			for (int j=0;j<height;j++){
				ident[i][j]=0;	
			}
			ident[i][i]=1;
		}
		return new Matrix(ident);
	}
	public Matrix join_identity(){
	//Returns the matrix with the Identity joined
	//used for Jordan-Gauss mathod of finding inverse
		Matrix ident = get_identity();
		Matrix ret = new Matrix(matrix.length,matrix[0].length*2);
		
		for (int c=1;c<ret.get_matrix()[0].length+1;c++){
			for(int r=1;r<ret.get_matrix().length+1;r++){
				if (c < matrix[0].length+1){ // for matrix part
					ret.set_entry(r,c,get_entry(r,c));	
				}else{ // for identity part
					ret.set_entry(r,c,ident.get_entry(r,c-matrix[0].length));
				}
			}
		}
		
		return ret;
	}
	public int test_jg(Matrix j){
	//Tests to see if matrix was inverted (if identity is at the left)
		Matrix ident = get_identity();
		for (int r = 1;r<ident.get_height();r++){
			for(int c=1;c<ident.get_width();c++){
				if(j.get_entry(c,r)!=ident.get_entry(c,r)){
					return 1;
				}
			}
		}
		return 0;
	}
	public Matrix inverse_jg(){
	//Inverse using Jordan Gauss Method
		Matrix ret = join_identity();
		
		return null;
	}

	//scalar multiplication
	public Matrix multiply(double n){
		double[][] ret = matrix;
		for(int c=0;c<ret.length;c++){
			for(int r=0;r<ret[c].length;r++){
				ret[c][r]=ret[c][r]*n;
			}
		}
		return new Matrix(ret);
	}
	//matrix multiplication
	public Matrix multiply(Matrix B){
		Matrix A = this;
		double[][] A_arr = A.get_matrix();
		int A_rows = A.get_matrix().length;
		int A_columns = A.get_matrix()[0].length;
		int B_rows = B.get_matrix().length;
		int B_columns = B.get_matrix()[0].length;		
		if(A_columns != B_rows){
			System.out.println("Incompatible matrices: A is of "+A_columns+" columns and B has "+B_rows+" rows");
			System.exit(1);
		}
		Matrix ret = new Matrix(new double[A_rows][B_columns]);
		//Iterate over columns in B
		for (int b_c=1;b_c<B_columns+1;b_c++){
			//Iterate Over A
			for (int r=1;r<A_rows+1;r++){
				double v=0;
				for (int c=1;c<A_columns+1;c++){
					v+=A.get_entry(r,c)*B.get_entry(c,b_c);
				}
				ret.set_entry(r,b_c,v);
			}
		}
		return ret;
	}

}
