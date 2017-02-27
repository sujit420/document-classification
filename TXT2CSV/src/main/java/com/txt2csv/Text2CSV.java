package com.txt2csv;

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import au.com.bytecode.opencsv.CSVWriter;

public class Text2CSV {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String filepath = "/trainingData.txt";
		BufferedReader br = new BufferedReader(new InputStreamReader(
				Text2CSV.class.getResourceAsStream(filepath)));
		String line = "";
		String csv = "/home/sujit_kumar_mishra/workspace/TXT2CSV/output.csv";
		CSVWriter writer = new CSVWriter(new FileWriter(csv));
		List<String[]> data = new ArrayList<String[]>();
		data.add(new String[]{"Category","Document"});
		while((line = br.readLine()) != null)
		{
			int endpoint = line.indexOf(" ");
			data.add(new String[]{line.substring(0, endpoint),line.substring(endpoint)});
		}
		writer.writeAll(data);
		writer.close();
	}
}
