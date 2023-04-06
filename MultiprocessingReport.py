from arcpy import env, management as mg
import multiprocessing

env.overwriteOutput = True
env.workspace = "C:/Reports"  # PDF output folder
REPORT = "C:/Reports/Report.rptx"  # report input file
THREADS = multiprocessing.cpu_count()  # You can change this to however many CPUs you want to use
MAX = 40000  # This is the number of reports you want to run


def create_pdf(i):
    mg.ExportReportToPDF(REPORT, i + ".pdf", "ID = " + i, 96, "FASTEST", "NO_EMBED_FONTS", "COMPRESS_GRAPHICS")


if __name__ == '__main__':
    range_list = list(range(1, MAX))
    string_list = [str(x) for x in range_list]  # convert the range list to str for the arcpy function
    pool = multiprocessing.Pool(THREADS)
    pool.map(create_pdf, string_list)
    pool.close()
    pool.join()

