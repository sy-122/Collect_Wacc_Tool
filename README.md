# WACC and LTGR Extraction Tool
## Introduction
Analyzing brokers' reports to extract key financial metrics like WACC (Weighted Average Cost of Capital) and LTGR (Long-Term Growth Rate) for specific companies is crucial for making informed investment decisions. However, manually sifting through these reports can be time-consuming if done for a long-term. Our WACC and LTGR Extraction Tool automates this process, enabling you to quickly and accurately gather these metrics from PDF reports.

## How It Works
#### Upload the PDF Report
Easy Upload: Simply upload the PDF report containing the brokers' analyses through our intuitive web interface.
Enter the Company Name
Targeted Extraction: Specify the name of the company you are investigating to filter relevant data from the report.
#### Extract WACC and LTGR
Automated Analysis: The tool scans the entire report, identifies mentions of WACC and LTGR, and extracts these values.
Broker Classification: Reputable banks such as Morgan Stanley and Goldman Sachs are identified by name, while less-known brokers are categorized as 'Others'.
Output
Statistical Summary: The tool calculates and displays the mean and median values of the extracted WACC and LTGR, providing a clear summary for quick analysis.

## Current Limitations
While the WACC and LTGR Extraction Tool greatly streamlines the extraction process, there are a few known limitations that we are actively working to improve:

Duplicate Entries: The tool may extract the same WACC and LTGR values multiple times if mentioned more than once in the report. We are enhancing our algorithms to recognize and filter out duplicate entries.
Date Extraction: Extracting the date of the broker's report has been challenging due to varying formats. Currently, the tool does not capture the report date.
Sentence Structure Variability: The tool may miss some WACC and LTGR values if the sentence structure in the report differs significantly from the patterns recognized by our extraction algorithms.

## Conclusion
Our WACC and LTGR Extraction Tool is designed to simplify the process of gathering key financial metrics from brokers' reports. While there are some limitations, the tool provides a significant efficiency boost, allowing for quicker and more accurate data collection. We are continuously working to improve the tool's accuracy and functionality to better serve your needs.
