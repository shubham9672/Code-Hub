import java.sql.*;

public class JdbcMySQL {
	public static void main(String[] args) {
		try {
			// int total;
			// Class.forName("com.mysql.jdbc.Driver");
			String dbPath = "jdbc:mysql://localhost/Student";
			Connection connection = DriverManager.getConnection(dbPath, "root", "");
			Statement statement = connection.createStatement();
			String sqlQuery = "SELECT * FROM Student;";
			System.out.println(sqlQuery);
			ResultSet resultSet = statement.executeQuery(sqlQuery);
			// resultSet.last();
			// total = resultSet.getRow();
			// resultSet.beforeFirst();
			// if(total > 0) {
				System.out.print("\nEnrollment\tName");
				while (resultSet.next()) {
					System.out.print("\n" + resultSet.getInt(2) + "\t" + resultSet.getString(8));
				}
				// System.out.println("\n" + total + " rows selected.");
			// }
			// else {
			// 	System.out.println("\nNo Rows Selected");
			// }
			connection.close();
		} catch(Exception e) {
			System.out.println("\nException Occured :(\n" + e.getMessage());
		}
	}
}