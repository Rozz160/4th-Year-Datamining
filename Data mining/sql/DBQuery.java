package sql;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import type.GPU;

public class DBQuery {
	private Connection connect;
	private Statement statement = null;
	private ResultSet resultSet = null;
	
	public DBQuery(Connection connect) {
		this.connect = connect;
	}
	
	public List<GPU> queryStatement() {
		List<GPU> list = new ArrayList<GPU>();
		try {
			statement = connect.createStatement();
			resultSet = statement.executeQuery("SELECT * FROM items");
			
			while(resultSet.next()) {
				GPU gpu = new GPU();
				gpu.setRating(resultSet.getInt("Rating"));
				gpu.setNumberRated(resultSet.getInt("NumberRated"));
				gpu.setPrice(resultSet.getFloat("Price"));
				gpu.setName(resultSet.getString("Name"));
				gpu.setNameBrand(resultSet.getString("NameBrand"));
				gpu.setNameGPU(resultSet.getString("NameGPU"));
				gpu.setCoreClock(resultSet.getString("CoreClock"));
				gpu.setCudaCores(resultSet.getString("CudaCores"));
				gpu.setEffectiveMem(resultSet.getString("EffectiveMemory"));
				gpu.setMemSize(resultSet.getString("MemorySize"));
				list.add(gpu);
			}
		} catch (SQLException e) {
			System.err.print("Error querying statement: " + e);
		}
		return list;	
	}
	
	public void printQuery(List<GPU> gpuList) {
		for(GPU gpu: gpuList) {
			System.out.println(gpu.getPrice());
		}
	}
	
	public void closeQuery() throws SQLException {
		statement.close();
		resultSet.close();
	}
}
