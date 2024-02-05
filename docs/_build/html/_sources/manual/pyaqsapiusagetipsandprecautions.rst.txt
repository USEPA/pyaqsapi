.. index:: Usage tips and precautions

Usage tips and precautions
==========================

This section contains suggestions for completing certain data related tasks.

* Determine if or how much data exists for a time-parameter-geography
  combination:

    * Retrieve data using the annualdata service.
    * If no records are returned, we do not have the data.
    * If records are returned, use the observation count to determine the
      temporal and geographic distribution of the data.

* Monthly averages:

    * AQS does not routinely calculate monthly aggregate statistics.
    * If you need these, you must calculate them yourself.
    * These can be calculated from the sample data or the daily data without
      loss of fidelity.

* Determine a single value for a site with collocated monitors:

    * Many sites will have collocated monitors - monitors collecting the same
      parameter at the same time.
    * The API currently provides only monitor level values. (site-level values
      will be added in the future.)
    * For some criteria pollutants (PM2.5, ozone, lead, and NO2), the
      regulations define procedures for defining a single site-level value.
    * For other pollutants, determining a single site-level value is left to
      the investigator.

* **Please adhere to the following when using the AQS Data Mart API**:

    * *Limit the size of queries*. The AQS Data Mart contains billions of
       values and you may request more than you intend. If you are unsure of
       the amount of data, start small and work your way up. Please limit
       queries to 1,000,000 rows of data each. You can use the
       "observation count" field on the annualdata service to determine how
       much data exists for a time-parameter-geography combination.
    * *Limit the frequency of queries*. The AQS Data Mart can process a limited
       load. Please wait for one request to complete before submitting another
       and do not make more than 10 requests per minute.
    * Be advised that RAQSAPI is capable of retrieving results for multiple
      pollutants, this can result in the amount of data being returned being
      multiplied by the number of pollutants being requested.
    * Be advised that the AQS Data Mart API limits certain data requests to
      one year of data at a time with the exception of the Monitor service.
      In order to retrieve multiple years of data for these functions the
      RAQSAPI library conveniently sends multiple API requests to the Data Mart
      API server, one request for each year, this can result in the amount of
      data being returned being multiplied by the number of years of data being
      requested.

**The AQS Data Mart administrators may disable accounts without notice for
failure to adhere to these terms (Though they will contact the offending
user via the email address provided)**