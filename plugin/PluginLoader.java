import java.net.*;
///home/volcan/Desktop/development/ExamplesForBen/plugin
public class PluginLoader {
	PluginLoader(){
		String pathToClass="file:///home/volcan/Desktop/development/ExamplesForBen/plugin/plugins/";
		try{
			ClassLoader loader = new URLClassLoader(new URL[]{new URL(pathToClass)});
			Class c = loader.loadClass("plugin1"); // class name in plugins
			Object o = c.newInstance();
			ValiPlugin p = (ValiPlugin)o;
			String rec = p.ReturnString();
			System.out.println("Recivied this: "+rec);
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	public static void main(String args[]){
		PluginLoader me = new PluginLoader();
	}
}


//Reference : http://onjava.com/pub/a/onjava/2005/01/26/classloading.html
// Ben, go to the library and get yourself O'Reilly's "Java in a nutshell"
// If you want some java lessons i'm happy to spend a few days teaching you.
// When you actually get to use this you'd want to either call the class loader in a different thread '
// or put each of the "plugins" in a seperate thread
