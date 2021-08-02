package com.github.cristobalm.jena_query_timeout;

import org.apache.commons.cli.*;
import org.apache.jena.query.*;
import org.apache.jena.rdfconnection.RDFConnection;
import org.apache.jena.rdfconnection.RDFConnectionFactory;
import org.apache.jena.tdb.TDBFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class QueryWithTimeout {
  public static void main(String[] args) throws IOException {
    Logger logger = LoggerFactory.getLogger(QueryWithTimeout.class);

    Options options = new Options();

    Option datasetOption = new Option("d", "dataset", true, "Dataset folder path");
    datasetOption.setRequired(true);
    options.addOption(datasetOption);

    Option queryOption = new Option("q", "query-file", true, "Query file path");
    queryOption.setRequired(true);
    options.addOption(queryOption);

    Option timeoutMsOption = new Option("t", "timeout-ms", true, "Timeout ms");
    timeoutMsOption.setRequired(true);
    options.addOption(timeoutMsOption);

    CommandLineParser parser = new DefaultParser();
    HelpFormatter formatter = new HelpFormatter();
    CommandLine cmd = null;

    try {
      cmd = parser.parse(options, args);
    } catch (ParseException e) {
      logger.error("Error parsing arguments", e);
      formatter.printHelp("utility-name", options);
      System.exit(1);
    }

    String datasetPath = cmd.getOptionValue("dataset");
    String queryPath = cmd.getOptionValue("query-file");
    long timeoutMs = Long.parseLong(cmd.getOptionValue("timeout-ms"));

    ARQ.init();

    Dataset dataset = TDBFactory.createDataset(datasetPath);
    RDFConnection rdfConnection = RDFConnectionFactory.connect(dataset);

    String queryStr = Files.readString(Path.of(queryPath));


    boolean canceled = false;
    long count = 0;

    try{
        QueryExecution queryExecution = rdfConnection.query(queryStr);
        System.out.println("started query execution");
        queryExecution.setTimeout(timeoutMs);
        System.out.println("timeout set to " + timeoutMs);

        ResultSet resultSet = queryExecution.execSelect();
        System.out.println("called execSelect");
        while(resultSet.hasNext()){
           resultSet.next();
           count++;
        }
    }
    catch (QueryCancelledException e){
      logger.info("query was cancelled");
      canceled = true;
    }

    if(!canceled){
      System.out.println("count = " + count);
    }

    rdfConnection.close();
  }
}
