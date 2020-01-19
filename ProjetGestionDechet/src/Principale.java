import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class Principale extends JFrame {

	private JPanel contentPane;
	private Font ecritureFontUpload = new Font("Segoe UI Emoji", Font.PLAIN, 20);
	private Font ecritureFontPanel = new Font("Segoe UI Emoji", Font.PLAIN, 15);

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Principale frame = new Principale();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Principale() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1043, 753);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(0, 191, 255));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblImage = new JLabel("\r\n\r\n");
		lblImage.setOpaque(true);
		lblImage.setBackground(new Color (204, 255, 204));
		lblImage.setBounds(33, 49, 648, 552);
		contentPane.add(lblImage);
		
		JButton btnUpload = new JButton("Upload");
		btnUpload.setFont(ecritureFontUpload);
		btnUpload.setBounds(194, 632, 261, 55);
		contentPane.add(btnUpload);
		
		JLabel lblItemsPresent = new JLabel("Item present in image : ");
		lblItemsPresent.setFont(ecritureFontPanel);
		lblItemsPresent.setBounds(708, 49, 176, 60);
		contentPane.add(lblItemsPresent);
		
		JPanel pnlItemPresent = new JPanel();
		pnlItemPresent.setBounds(691, 52, 315, 288);
		contentPane.add(pnlItemPresent);
		
		JLabel lblBin = new JLabel("Bin :");
		lblBin.setFont(ecritureFontPanel);
		lblBin.setBounds(708, 372, 64, 25);
		contentPane.add(lblBin);
		
		JPanel pnlBin = new JPanel();
		pnlBin.setBounds(691, 365, 315, 74);
		contentPane.add(pnlBin);
		
		JLabel lblNote = new JLabel("Note :");
		lblNote.setFont(ecritureFontPanel);
		lblNote.setBounds(708, 482, 49, 14);
		contentPane.add(lblNote);
		
		JPanel pnlNote = new JPanel();
		pnlNote.setBounds(691, 466, 315, 135);
		contentPane.add(pnlNote);
	}
}
