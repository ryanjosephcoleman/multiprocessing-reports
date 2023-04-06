# multiprocessing-reports
use multiprocessing to build arcpy reports quickly

multiprocessing is included in the default ArcGIS Pro python environment but there are few places where you can use it. Building reports is one useful example. After you export your ArcGIS Pro report to a .rptx file you can use this short handy script to build thousands of reports. I built 40k in about 2.5 hours! The more CPU cores you have the faster it gets. I can then fold this into my mantainance scripts and update the reports as often as I need to. It's helpful if you have a sequential ID field already set up, by default this looks for ID and names the pdf files by this ID.
