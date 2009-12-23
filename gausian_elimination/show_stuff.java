public class show_stuff{
       public static void show_matrix(double m[][],double v[]){
                for(int i=0;i<m.length;i++){
                        System.out.println("| "+m[i][0]+" , "+m[i][1]+" , "+m[i][2]+" |\t\t|"+v[i]+"|");
                }
       }

	public static void show_formulas(double xs[],double ys[]){
                for (int i=0; i< xs.length;i++){
                        System.out.println(ys[i]+" = a*"+xs[i]+"^2 + b*"+xs[i]+" + c");
                }
                System.out.println("meaning...");
                for (int i=0; i< xs.length;i++){
                        System.out.println(ys[i]+" = a*"+xs[i]*xs[i]+" + b*"+xs[i]+" + c");
                }
	}
	public static void show_formulas(double m[][],double v[]){
                for(int i=0;i<m.length;i++){
                        System.out.println(v[i]+" = a*"+m[i][0]+" + b*"+m[i][1]+" + c*"+m[i][2]);
                }

	}

}
