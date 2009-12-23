public class plugin1 extends ValiPlugin{
	public plugin1(){
		System.out.println("init plugin1");
	}
	public String ReturnString(){
		//This is an example for a function that overrides one in ValiPlugin.java
		String ret="ReturnString() was overriden in plugin1";
		return ret;
	}
	//Ben: this is a closer example of how to implement the plugins,  you declare generic methods that all the plugins will have in ValiPlugins.java, and the you override them specifically for the different plugins (don't forget "extends ValiPlugins
	
	// For example:
	// public void setPluginDataobject(SomeDataObject)
	// public JPanel getPluginMenu()	
}
