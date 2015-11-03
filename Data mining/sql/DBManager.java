package sql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBManager {
	private Connection connect = null;
	private DBQuery dbquery;
	
	public DBManager() {
		connectDB();
		dbquery = new DBQuery(connect);
	}
	
	public DBQuery getQuery() {
		return dbquery;
	}
	
	private void connectDB() {
		try {
			Class.forName("mysqldriver.com.mysql.jdbc.Driver");
			connect = DriverManager.getConnection("jdbc:mysql://localhost/scrapydb?" 
					+ "user=root&password=0000");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			System.err.print("SQL Connection Error: " + e);
		}
	}
	
	public void close() {
	    try {
	    	dbquery.closeQuery();
			connect.close();
			System.out.print("Successfully closed connections.");
		} catch (SQLException e) {
			System.err.print("Error closing connections: " + e);
		}
	}
}
