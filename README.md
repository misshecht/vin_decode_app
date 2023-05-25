Author: Rhiannon Hecht
Date: 05/24/2023
For: Koffie Financial Take Home Coding Challenge

This is a simple FastAPI backend that will decode VINs, powered by the vPIC API and backed by an sqlite cache. 

I'm going to be completely honest here, as this tactic seemed to be received well by Sarah as we discussed in our initial interview. My background is not likely to be common to other applicants. First of all, I am a female engineer. Second my undergrad degree is in Philosophy and master's is in Computer Science. While I do have some background in web programming, it's minimal, but I think the following quick summary the period of my career in which I learned way more than I ever thought I could in 8 years time will reveal a lot to you about my character, my skillset, my outstanding work ethic, and my mastery of problem solving:

I have nearly a decade of experience writing in Python, however all of it is self-taught and gained specifically to tackle a myriad of challenges I met along the way ofbringing a custom i/o semiconductor controller manufacturing company kicking and screaming from the last century into this one. The reason they allowed it to happen? The improvements I made to all production processes saved the company 386 man hours and $486,000 in that first year, while also doubling production output without increasing headcount.

When I arrived to the company, everything was done on paper written in pen, and white out was the acceptable way to make corrections. Despite this being my first experience in a Windows domain, I adapted from my Mac and Linux background and while I learned assembly in a single day, and then, super curious because I had not had hardware experience before, in my spare time I went from station to station and figured out what everything was for, what each process meant to the finished product. I spotted so many inefficiences along the way but I did not complain or point fingers, I just took note and eventually worked all these things into a Production Improvement Project. 

The first thing I figured out was a way to digitize our paper travelers into a digital ones, using inexpensive tablets I was allowed to procure. I managed to sign them into the Domain, despite not being fully legit copies of Windows on the tablets, so that they could communicate with our NAS and our SYSPRO database, because I noticed we were collecting all the serials of the boards we were assembling together, but we were hand writing them onto paper travelers. So I triggered kit content pick lists to be created by a job creation trigger point in our ERP system, which then automatically generated the labels I had previously had to type by hand every time. I also provided resources from the traveler so that operators were guided along through assembly, as well as automating calibration or the analog signals, and fullly testing the assembled units to within 2 millivolts of our specs. I did all of this not to eliminate anyone's jobs, but to try to reduce human error and just make everyone's jobs easier. 

I did all of this using mainly Python, but also NiceLabel, and SYSPRO, and even assembly when required to program PIC chips (you would be surpised how much ancient hardware is still in use in the semiconductor industry) So my skillset ranges widely and I have been able to make just about anything work. I am a fast learner, I love to learn, I love to work with other engineers, I am very excited about this role.

This is all to say that I have never had to build an API as this coding challenge has required. I am certain that your other candidates will have done this many times before. So I do apologize if these contents are not what you expect but they do accomplish what is requested in the README.md that is found at the link from Sarah in the hiring process steps. 

I have enjoyed this challenge. And I believe very strongly in your company's mission. And I hope that my unusual background will be a plus and not a minus in considering me for this position.

About the endpoints:

The `/lookup/{vin}` endpoint retrieves data from the cache table if the VIN exists, otherwise it fetches the data from the VPIC API and caches it in the database.

The `/export` endpoint exports all records from the cache table and outputs a parquet file stored as export_file.parquet

The `/delete/{vin}` endpoint deletes a specific record from the cache table based on the provided VIN.
