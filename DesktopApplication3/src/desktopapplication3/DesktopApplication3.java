/*
 * DesktopApplication3.java
 */

package desktopapplication3;

import org.jdesktop.application.Application;
import org.jdesktop.application.SingleFrameApplication;

/**
 * The main class of the application.
 */
public class DesktopApplication3 extends SingleFrameApplication {

    /**
     * At startup create and show the main frame of the application.
     */
    @Override protected void startup() {
        show(new DesktopApplication3View(this));
    }

    /**
     * This method is to initialize the specified window by injecting resources.
     * Windows shown in our application come fully initialized from the GUI
     * builder, so this additional configuration is not needed.
     */
    @Override protected void configureWindow(java.awt.Window root) {
    }

    /**
     * A convenient static getter for the application instance.
     * @return the instance of DesktopApplication3
     */
    public static DesktopApplication3 getApplication() {
        return Application.getInstance(DesktopApplication3.class);
    }

    public static int validateFile(Object f){
        //BEN!!!!
        //Here you pass the file to the validation code, and return
        // return 0 on success or any other value on error (Error number)
        int ret=-1;
        if(Math.random() > 0.5f){
            ret=0;
        }
        return ret;
    }
    /**
     * Main method launching the application.
     */
    public static void main(String[] args) {
        launch(DesktopApplication3.class, args);
    }
}
