# -*- coding: utf-8 -*-

TODO
----
This project is still in the early stages of planning, there is a lot of work
that still needs to be done.

Here is a short list of things that I think need to be done before a public
release of code:

   - find and fix remaining bugs (obviously!)
   - Documentation:
      - (DONE) create README.rst
      - (DONE) create TODO.rst
      - check parameters before making calls to AQS Data Mart API
        (aqscheckparams())
      - (DONE) add the ability to pull multiple years of data with a single 
        function call (aqsmultiyearparams())
      - (Done) add functions for new AQS Data Mart APIs (annualperformanceeval,
        annualperformanceevaltransaction, "quartersummary",
        "ozoneseasons" (wink wink nod nod)
      - (DONE) finish copying/converting function roxygen2 cooments from 
        RAQSAPI to pyaqsapi docstrings for sphinx API docs
         - document AQSAPI_V2 class object
      - long version of documentation manual (are vignettes a thing in the
        python world?)
      - grammar, spell checking
      - polish refine documentaion (editor needed)
   - peer review (Internal EPA) of entire project
   - unit test
      - (DONE pytest)
      - (planning) continuous development (Github actions, CircleCI, Jenkins,
        TravisCI, et al)
   - get management approval for release
   - (DONE) convert README.md and TODO.md back to README.rst and TODO.rst
   
   Other considerations:
   
   - consider packaging options (pip/setuptools, Anaconda/conda, chocolately, 
     poetry, et al)
      - what platform should the package be hosted on, (defanately github, 
        other options will depend on how the project is packaged)
   - (DONE, decided to go with pandas) Should xarray be dropped in favor of
     just pandas
   - archival options (EPA bitbucket server, zenodo)