/*
 * SelectFileDialog.java
 *
 * Created on 22 February 2010, 23:20
 */

package desktopapplication3;

/**
 *
 * @author  volcan
 */
public class SelectFileDialog extends javax.swing.JDialog {
    
    /** Creates new form SelectFileDialog */
    public SelectFileDialog(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
    }
    
    //Ben: Sets the callback to go to
    // This is so we can update the parent's SelectedFilesList
    public void setCallback(DesktopApplication3View p){
        myCallback = p;
    }
    
    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        SelectFileChooser = new javax.swing.JFileChooser();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        setName("Form"); // NOI18N

        SelectFileChooser.setMultiSelectionEnabled(true);
        SelectFileChooser.setName("SelectFileChooser"); // NOI18N
        SelectFileChooser.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                SelectFileChooserActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(SelectFileChooser, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(SelectFileChooser, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    //Ben: Action Preformed so we check what action that was
    private void SelectFileChooserActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_SelectFileChooserActionPerformed
        System.out.println("Filechooser action:" + evt.getActionCommand());
        if(evt.getActionCommand().equals("ApproveSelection")){ // OK Clicked
            myCallback.updateList(SelectFileChooser.getSelectedFiles());
            this.setVisible(false);
        }
    }//GEN-LAST:event_SelectFileChooserActionPerformed
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                SelectFileDialog dialog = new SelectFileDialog(new javax.swing.JFrame(), true);
                dialog.addWindowListener(new java.awt.event.WindowAdapter() {
                    public void windowClosing(java.awt.event.WindowEvent e) {
                        System.exit(0);
                    }
                });
                dialog.setVisible(true);
            }
        });
    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JFileChooser SelectFileChooser;
    // End of variables declaration//GEN-END:variables
    private DesktopApplication3View myCallback;
}
