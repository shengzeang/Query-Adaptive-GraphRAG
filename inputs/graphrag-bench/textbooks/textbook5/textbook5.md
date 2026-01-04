
# Introduction

In the recent decades, due to the explosion of data accumulated and processed in all spheres of human activity, humanity has faced a new global problem (threat), which was called the “Information gap”. This gap is since now every 2 years mankind doubles the volume of data produced, but processes, analyzes and comprehends only a part of these data. Non-analyzed and unreasonable data can be interpreted as “black information holes”, which bring to humanity many unexpected, poorly explained events. These circumstances make the “Big Data” problem very urgent and necessitate the development of an effective theory and practical methods for storing, processing and analyzing these data.

Big data (BD) is data sets that are so big and complex that traditional data-processing application software are inadequate to deal with them. Big data challenges include capturing data, data storage, data analysis, search, sharing, transfer, visualization, querying, updating, information privacy and data source. There are a number of concepts associated with big data: originally there were three concepts volume, variety, velocity [1]. Other concepts later attributed with big data are veracity (i.e., how much noise is in the data) [2] and value [3].

Lately, the term “big data” tends to refer to the use of predictive analytics, user behavior analytics, or certain other advanced data analytics methods that extract value from data, and seldom to a particular size of data set. “There is little doubt that the quantities of data now available are indeed large, but that’s not the most relevant characteristic of this new data ecosystem” [4]. Analysis of data sets can find new correlations to “spot business trends, prevent diseases, combat crime and so on” [5]. Scientists, business executives, practitioners of medicine, advertising and governments alike regularly meet difficulties with large data sets in areas including Internet search, fintech, urban informatics, and business informatics. Scientists encounter limitations in e-Science work, including meteorology, genomics [6], complex physics simulations, biology and environmental research [7].

Data sets grow rapidly—in part because they are increasingly gathered by cheap and numerous information-sensing Internet of things devices such as mobile devices, aerial (remote sensing), software logs, cameras, microphones, radio-frequency identification (RFID) readers and wireless sensor networks [8, 9].

The world’s technological per-capita capacity to store information has roughly doubled every 40 months since the 1980s [10]; as of 2012, every day 2.5 exabytes $( 2 . 5 \times 1 0 ^ { 1 8 } ,$ ) of data are generated [11]. Based on an IDC report prediction, the global data volume was growing up exponentially from 4.4 zettabytes to 44 zettabytes between 2013 and 2020 [12]. By 2025, IDC predicts there will be 163 zettabytes of data [13]. One question for large enterprises is determining who should own big-data initiatives that affect the entire organization [14].

Relational database management systems and desktop statistics and software packages to visualize data often have difficulty handling big data. The work may require “massively parallel software running on tens, hundreds, or even thousands of servers” [15]. What counts as “big data” varies depending on the capabilities of the users and their tools, and expanding capabilities make big data a moving target. “For some organizations, facing hundreds of gigabytes of data for the first time may trigger a need to reconsider data management options. For others, it may take tens or hundreds of terabytes before data size becomes a significant consideration” [16].

Big data repositories have existed in many forms, often built by corporations with a special need. Commercial vendors historically offered parallel database management systems for big data beginning in the 1990s. For many years, WinterCorp published a largest database report [17].

Teradata Corporation in 1984 marketed the parallel processing DBC 1012 system. Teradata systems were the first to store and analyze 1 terabyte of data in 1992. Hard disk drives were $2 . 5 \ \mathrm { G B }$ in 1991, so the definition of big data continuously evolves according to Kryder’s Law. Teradata installed the first petabyte class RDBMS-based system in 2007. As of 2017, there are a few dozen petabyte class Teradata relational databases installed, the largest of which exceeds 50 PB. Systems up until 2008 were $100 \%$ structured relational data. Since then, Teradata has added unstructured data types including XML, JSON, and Avro.

CERN and other physics experiments have collected big data sets for many decades, usually analyzed via high performance computing (supercomputers) rather than the commodity map-reduce architectures usually meant by the current “big data” movement.

In 2004, Google published a paper on a process called MapReduce that uses a similar architecture. The MapReduce concept provides a parallel processing model, and an associated implementation was released to process huge amounts of data. With MapReduce, queries are split and distributed across parallel nodes and processed in parallel (the Map step). The results are then gathered and delivered (the Reduce step). The framework was very successful [18], so others wanted to replicate the algorithm. Therefore, an implementation of the MapReduce framework was adopted by an Apache open-source project named Hadoop [19]. Apache Spark was developed in 2012 in response to limitations in the MapReduce paradigm, as it adds the ability to set up many operations (not just map followed by reduce).

MIKE2.0 is an open approach to information management that acknowledges the need for revisions due to big data implications identified in an article titled “Big

Data Solution Offering” [20]. The methodology addresses handling big data in terms of useful permutations of data sources, complexity in interrelationships, and difficulty in deleting (or modifying) individual records [21].

Various studies since 2012 showed that a multiple-layer architecture is one option to address the issues that big data presents. A distributed parallel architecture distributes data across multiple servers; these parallel execution environments can dramatically improve data processing speeds. This type of architecture inserts data into a parallel DBMS, which implements the use of MapReduce and Hadoop frameworks. This type of framework looks to make the processing power transparent to the end user by using a front-end application server [22].

Big data analytics for manufacturing applications is marketed as a 5C architecture (connection, conversion, cyber, cognition, and configuration) [23].

Data lake allows an organization to shift its focus from centralized control to a shared model to respond to the changing dynamics of information management. This enables quick segregation of data into the data lake, thereby reducing the overhead time [24, 25].

Big data has increased the demand of information management specialists so much so that Software AG, Oracle Corporation, IBM, Microsoft, SAP, EMC, HP and Dellhave spent more than $\$ 15$ billion on software firms specializing in data management and analytics. In 2010, this industry was worth more than $\$ 100$ billion and was growing at almost $10 \%$ a year: about twice as fast as the software business as a whole [5].

Developed economies increasingly use data-intensive technologies. There are 4.6 billion mobile-phone subscriptions worldwide, and between 1 billion and 2 billion people accessing the Internet [5]. Between 1990 and 2005, more than 1 billion people worldwide entered the middle class, which means more people became more literate, which in turn led to information growth. The world’s effective capacity to exchange information through telecommunication networks was 281 petabytes in 1986, 471 petabytes in 1993, 2.2 exabytes in 2000, 65 exabytes in 2007 [10] and predictions put the amount of Internet traffic at 667 exabytes annually by 2014 [5]. According to one estimate, one-third of the globally stored information is in the form of alphanumeric text and still image data [26], which is the format most useful for most big data applications. This also shows the potential of yet unused data (i.e. in the form of video and audio content).

Consider the main sources of Big Data.

# Networking Ways of Communication Between People on the Planet

As the development of modern means of communication between people, such as Mobile Communications, the Internet, Social Networks and other, volumes of data generated by people increase in an avalanche. According to the analytical studies of the International Labor Organization at the United Nations, these changes have the following features:

– If the number of Internet devices in the world in 1984 was at the level of 1,000, now it has reached 15 billion, about 2.5 per every inhabitant of the Planet; As of 1900, the amount of human knowledge doubled every 100 years. Now, due to global “digitalization”, they are doubled every 2 years. At the same rate, the volume of new data produced by mankind is growing; This means that now for university students, the newest knowledge that they receive during the first year of training already in the third year becomes obsolete; These changes are no longer linear in time. According to the UN, they are exponential, and the new digital world is called exponential.

# Internet of Things (IoT)

Big data and the IoT work in conjunction. Data extracted from IoT devices provides a mapping of device interconnectivity. Such mappings have been used by the media industry, companies and governments to more accurately target their audience and increase media efficiency. IoT is also increasingly adopted as a means of gathering sensory data, and this sensory data has been used in medical [27] and manufacturing [28] contexts.

Kevin Ashton, digital innovation expert who is credited with coining the term [29], defines the Internet of Things in this quote: “If we had computers that knew everything there was to know about things—using data they gathered without any help from us—we would be able to track and count everything, and greatly reduce waste, loss and cost. We would know when things needed replacing, repairing or recalling, and whether they were fresh or past their best.”

# Information Technology

Especially since 2015, big data has come to prominence within Business Operations as a tool to help employees work more efficiently and streamline the collection and distribution of Information Technology (IT). The use of big data to resolve IT and data collection issues within an enterprise is called IT Operations Analytics (ITOA) [30]. By applying big data principles into the concepts of machine intelligence and deep computing, IT departments can predict potential issues and move to provide solutions before the problems even happen [30]. In this time, ITOA businesses were also beginning to play a major role in systems management by offering platforms that brought individual data silos together and generated insights from the whole of the system rather than from isolated pockets of data.

• Walmart handles more than 1 million customer transactions every hour, which are imported into databases estimated to contain more than 2.5 petabytes (2560 terabytes) of data—the equivalent of 167 times the information contained in all the books in the US Library of Congress. Windermere Real Estate uses location information from nearly 100 million drivers to help new home buyers determine their typical drive times to and from work throughout various times of the day [31].   
• FICO Card Detection System protects accounts worldwide [32].

# Science

• The Large Hadron Collider experiments represent about 150 million sensors delivering data 40 million times per second. There are nearly 600 million collisions per second. After filtering and refraining from recording more than $9 9 . 9 9 9 9 5 \%$ [33] of these streams, there are 100 collisions of interest per second [34–36].

As a result, only working with less than $0 . 0 0 1 \%$ of the sensor stream data, the data flow from all four LHC experiments represents 25 petabytes annual rate before replication (as of 2012). This becomes nearly 200 petabytes after replication.

If all sensor data were recorded in LHC, the data flow would be extremely hard to work with. The data flow would exceed 150 million petabytes annual rate, or nearly 500 exabytes per day, before replication. To put the number in perspective, this is equivalent to 500 quintillion $( 5 \times 1 0 ^ { 2 0 } )$ bytes per day, almost 200 times more than all the other sources combined in the world.

• The Square Kilometre Array is a radio telescope built of thousands of antennas. It is expected to be operational by 2024. Collectively, these antennas are expected to gather 14 exabytes and store one petabyte per day [37, 38]. It is considered one of the most ambitious scientific projects ever undertaken [39]. When the Sloan Digital Sky Survey (SDSS) began to collect astronomical data in 2000, it amassed more in its first few weeks than all data collected in the history of astronomy previously. Continuing at a rate of about $2 0 0 \mathrm { G B }$ per night, SDSS has amassed more than 140 terabytes of information [40]. When the Large Synoptic Survey Telescope, successor to SDSS, comes online in 2020, its designers expect it to acquire that amount of data every five days [5]. Decoding the human genome originally took 10 years to process; now it can be achieved in less than a day. The DNA sequencers have divided the sequencing cost by 10,000 in the last ten years, which is 100 times cheaper than the reduction in cost predicted by Moore’s Law [5]. The NASA Center for Climate Simulation (NCCS) stores 32 petabytes of climate observations and simulations on the Discover supercomputing cluster [41, 42]. Google’s DNAStack compiles and organizes DNA samples of genetic data from around the world to identify diseases and other medical defects. These fast and

exact calculations eliminate any ‘friction points,’ or human errors that could be made by one of the numerous science and biology experts working with the DNA. DNAStack, a part of Google Genomics, allows scientists to use the vast sample of resources from Google’s search server to scale social experiments that would usually take years, instantly [43, 44]. 23andme’s DNA database contains genetic information of over 1,000,000 people worldwide [45]. The company explores selling the “anonymous aggregated genetic data” to other researchers and pharmaceutical companies for research purposes if patients give their consent [46–50]. Ahmad Hariri, professor of psychology and neuroscience at Duke University who has been using 23andMe in his research since 2009 states that the most important aspect of the company’s new service is that it makes genetic research accessible and relatively cheap for scientists [51]. A study that identified 15 genome sites linked to depression in 23andMe’s database lead to a surge in demands to access the repository with 23andMe fielding nearly 20 requests to access the depression data in the 2 weeks after publication of the paper [52]. Computational Fluid Dynamics (CFD) and hydrodynamic turbulence research generate massive datasets. The Johns Hopkins Turbulence Databases (JHTDB) contains over 350 terabytes of spatiotemporal fields from Direct Numerical simulations of various turbulent flows. Such data have been difficult to share using traditional methods such as downloading flat simulation output files. The data within JHTDB can be accessed using “virtual sensors” with various access modes ranging from direct web-browser queries, access through Matlab, Python, Fortran and C programs executing on clients’ platforms, to cut out services to download raw data. The data have been used in over 150 scientific publications.

# Technology

• eBay.com uses two data warehouses at 7.5 petabytes and 40 PB as well as a 40 PB Hadoop cluster for search, consumer recommendations, and merchandising [53].   
Amazon.com handles millions of back-end operations every day, as well as queries from more than half a million third-party sellers. The core technology that keeps Amazon running is Linux-based and as of 2005 they had the world’s three largest Linux databases, with capacities of 7.8 TB, 18.5 TB, and 24.7 TB [54].   
• Facebook handles 50 billion photos from its user base [55].   
• Google was handling roughly 100 billion searches per month since August 2012 [56].

In March 2012, The White House announced a national “Big Data Initiative” that consisted of six Federal departments and agencies committing more than $\$ 200$ million to big data research projects [57].

The initiative included a National Science Foundation “Expeditions in Computing” grant of $\$ 10$ million over 5 years to the AMPLab [58] at the University of California, Berkeley [59]. The AMPLab also received funds from DARPA, and over a dozen industrial sponsors and uses big data to attack a wide range of problems from predicting traffic congestion [60] to fighting cancer [61].

The White House Big Data Initiative also included a commitment by the Department of Energy to provide $\$ 25$ million in funding over 5 years to establish the Scalable Data Management, Analysis and Visualization (SDAV) Institute [62], led by the Energy Department’s Lawrence Berkeley National Laboratory. The SDAV Institute aims to bring together the expertise of six national laboratories and seven universities to develop new tools to help scientists manage and visualize data on the Department’s supercomputers.

The U.S. state of Massachusetts announced the Massachusetts Big Data Initiative in May 2012, which provides funding from the state government and private companies to a variety of research institutions [63]. The Massachusetts Institute of Technology hosts the Intel Science and Technology Center for Big Data in the MIT Computer Science and Artificial Intelligence Laboratory, combining government, corporate, and institutional funding and research efforts [64].

The European Commission is funding the 2-year-long Big Data Public Private Forum through their Seventh Framework Program to engage companies, academics and other stakeholders in discussing big data issues. The project aims to define a strategy in terms of research and innovation to guide supporting actions from the European Commission in the successful implementation of the big data economy. Outcomes of this project will be used as input for Horizon 2020, their next framework program [65].

Facing the challenges of BD the problems of development and implementation of adequate methods, techniques and software of BD analysis (BD Mining) are extremely important. It’s worth to notice that conventional methods and techniques of Data Mining are not adequate for this goal.

The mankind have developed some fruitful approaches to deal with high dimension and large volumes of data. One of them widely used is clustering. Clustering enables to divide large data set into several groups of similar objects and replace the whole group by one representative object—center of cluster. Up to date many algorithms of cluster analysis were developed. But problem of clustering in real-time mode arises when new data are entering as stream data and demands new efficient methods and algorithms.

Another approach of reducing volume of data set is hierarchy. Hierarchical organization of data enables to structuring initial data set into several subordinate levels which gives opportunity classify objects by feature set and easily find the searched object or small group of objects by its features.

Last years due to demand of speed processing, prediction and classification of huge volumes of data Deep learning networks were developed with large number of neuron layers. With their appearance the new problem has arisen to develop efficient methods of learning such networks. Some novel approach to solution of fast

Deep learning is the application of so-called Group Method of Data Handling which represents very efficient tools for reducing dimensionality.

The present book deals with some problems of BD analysis, considers and investigates as conventional tools of Data Mining and novel efficient methods and tools as well developed for this goal.

In Chap. 1 methods of cluster analysis are considered. The crisp and fuzzy clustering methods are described and analyzed. New efficient possibilistic methods of clustering including robust clustering methods working under high noise level are considered. Special attention is played for development of new clustering methods which operate under data streams in on-line mode. The examples of application of clustering methods for some practical problems are presented.

Chapter 2 is devoted to analysis, training of Deep learning (DL) networks and their applications to solution some BD tasks. At the beginning structure and conventional training methods of DL are considered, the problem of vanishing gradient while training is considered and several ways of its prevention are considered (so-called methods of regularization).

The main attention in this chapter is played to development and presentation of so-called Hybrid GMDH-neo-fuzzy networks for solution computation intelligence task with BD. This new class of FNN turned to be efficient tools to overcome high dimensionality. In the chapter are presented several types of hybrid GMDH-FNNs and their application to the solution of real problems of prediction, classification and control.

Chapter 3 deals with classification problems. The FNN NefClass is considered as efficient tools of classification under BD conditions. The structure, training algorithms of FNN NefClass are presented and analyzed. The application of FNN NefClass for solution of medical images analysis and recognition in the problems of medical diagnostics are presented.

As it is known the new efficient tools for images processing and recognition are Convolutional neural networks (CNN). CNN are applied to find informative features of image which are fed into multilayered perceptron for further classification.

In the chapter new hybrid CNN-FNN system for image recognition is described where CNN is used for finding features of image while FNN NEFClass is used for further classification. The investigations of the suggested hybrid network and comparison with known CNN systems are performed at the practical problem of recognition of breast cancer at the standard data set BreakHis.

Chapter 4 of the book is devoted to the intellectual analysis of large historical data with the purpose of recognizing the laws of the origin and development of global systemic conflicts and with the purpose of analyzing the causes leading to these conflicts. The generalization and formalization of approaches to the recognition of C-waves of global systemic conflicts through big historical data have been carried out and general concept of description and interpretation of these waves has been proposed. Based on intellectual analysis of big data on the conflicts, taking place since $7 5 0 ~ \mathrm { B } . \mathrm { C }$ . up to now, have been analyzed and their general pattern has been revealed. These have been tried to foresee the next global conflict called the conflict of the 21st century. Its nature and main characteristics have been analyzed.

The hypotheses for a metric relation between the global periodic processes, namely between the sequence of 11-year cycles of solar activity, so called Kondratieff cycles of the development of the global economy, and the process of evolutionary structuration of the family of the C-waves of global systemic conflicts have been formulated.

The problem of prediction of these processes in the 21st century by using a metric approach was considered. The possible scenarios of the development of the conflict of the 21st century have been constructed and analyzed. Ideas aimed to avoiding of undesirable consequences for humanity in the case of full or partial implementation of the predicted scenarios are proposed.

On the whole, this chapter represents the wonderful example of application and development of general ideas and paradigms of Data Mining to detection of hidden laws in evolution of world economy and global conflicts and their systemic analysis.

# References

1. D. Laney, 3D data management: controlling data volume, velocity and variety. META Group Res. Note 6(70) (2001)   
2. P.B. Goes, Design science research in top information systems journals. MIS Q. Manag. Inf. Syst. 38(1) (2014)   
3. B. Marr, Big data: The 5 Vs everyone must know (6 March 2014)   
4. D. Boyd, K. Crawford, Six provocations for big data, in Social Science Research Network: A Decade in Internet Time: Symposium on the Dynamics of the Internet and Society, https://doi. org/10.2139/ssrn.1926431 (21 Sept 2011)   
5. Data, data everywhere. The Economist. Retrieved 9 Dec 2012 (25 Feb 2010)   
6. Community cleverness required. Nature 455(7209), 1 (4 Sept 2008), https://doi.org/10.1038/ 455001a   
7. O.J. Reichman, M.B. Jones, M.P. Schildhauer, Challenges and opportunities of open data in ecology. Science 331(6018), 703–705 (2011), https://doi.org/10.1126/science.1197962   
8. J. Hellerstein, Parallel programming in the age of big data. Gigaom Blog (9 Nov 2008)   
9. T. Segaran, J. Hammerbacher, Beautiful Data: The Stories Behind Elegant Data Solutions (O’Reilly Media, 2009), p. 257. ISBN: 978-0-596-15711-1   
10. M. Hilbert, P. López, The world’s technological capacity to store, communicate, and compute information. Science 332(6025), 60–65 (2011), https://doi.org/10.1126/science.1200970   
11. IBM What is big data?—Bringing big data to the enterprise. www.ibm.com. Retrieved 26 Aug 2013   
12. M. Sh. Hajirahimova, A.S. Aliyeva, About big data measurement methodologies and indicators. Int. J. Mod. Educ. Comput. Sci. 9(10), 1–9. https://doi.org/10.5815/ijmecs.2017. 10.01.   
13. D. Reinsel, J. Gantz, J. Rydning, Data Age 2025: The Evolution of Data to Life-Critical (International Data Corporation, Framingham). Retrieved 2 Nov 2017 (13 April 2017)   
14. Oracle and FSN, Mastering big data: CFO strategies to transform insight into opportunity, December 2012   
15. A. Jacobs, The pathologies of big data. ACMQueue (6 July 2009)   
16. R. Magoulas, B. Lorica, Introduction to big data. Release 2.0 (11) (O’Reilly Media, Sebastopol) (Feb 2009)   
17. Survey: biggest databases approach 30 terabytes. Eweek.com. Retrieved 8 Oct 2017   
18. J. Bertolucci, Hadoop: from experiment to leading big data platform. Information Week. Retrieved on 14 Nov 2013   
19. J. Webster, MapReduce: simplified data processing on large clusters. Search Storage. Retrieved on 25 Mar 2013 (2004)   
20. Big data solution offering. MIKE2.0. Retrieved 8 Dec 2013   
21. Big data definition. MIKE2.0. Retrieved 9 Mar 2013   
22. C. Boja, A. Pocovnicu, L. Bătăgan, Distributed parallel architecture for big data. Informatica Economica 16(2), 116–127 (2012)   
23. IMS_CPS—IMS Center. Imscenter.net. Retrieved 16 June 2016   
24. Solving key business challenges with a big data lake. Hcltech.com. Retrieved 8 Oct 2017 (Aug 2014)   
25. Method for testing the fault tolerance of MapReduce frameworks. Computer Networks (2015)   
26. M. Hilbert, P. López, The world’s technological capacity to store, communicate, and compute information. Science 332(6025), 60–65 (2011), https://doi.org/10.1126/science.1200970   
27. M. Hilbert, What is the content of the world’s technologically mediated information and communication capacity: how much text, image, audio, and video? Inf. Soc. 30(2), 127–143 (2014), https://doi.org/10.1080/01972243.2013.873748   
28. QuiO named innovation champion of the Accenture healthtech innovation challenge. Businesswire.com. Retrieved 8 Oct 2017 (10 Jan 2017)   
29. A software platform for operational technology innovation. Predix.com. Retrieved 8 Oct 2017   
30. That internet of things thing   
31. R. Solnik, The time has come: analytics delivers for IT operations. Data Cent. J. Retrieved 21 June 2016   
32. N. Wingfield, Predicting commutes more accurately for would-be home buyers— NYTimes.com. Bits.blogs.nytimes.com. Retrieved 21 July 2013 (12 March 2013)   
33. FICO® Falcon® Fraud Manager. Fico.com. Retrieved 21 July 2013   
34. D. Alexandru, Prof. cds.cern.ch. CERN. Retrieved 24 March 2015   
35. LHC Brochure, English version. A presentation of the largest and the most powerful particle accelerator in the world, the Large Hadron Collider (LHC), which started up in 2008. Its role, characteristics, technologies, etc. are explained for the general public. CERN-Brochure-2010-006-Eng. LHC Brochure, English version. CERN. Retrieved 20 Jan 2013   
36. LHC Guide, English version. A collection of facts and figures about the Large Hadron Collider (LHC) in the form of questions and answers. CERN-Brochure-2008-001-Eng. LHC Guide, English version. CERN. Retrieved 20 Jan 2013   
37. G. Brumfiel, High-energy physics: Down the petabyte highway. Nature 469, 282–283, https:// doi.org/10.1038/469282a (19 Jan 2011)   
38. IBM Research—Zurich. Zurich.ibm.com. Retrieved 8 Oct 2017   
39. Future telescope array drives development of Exabyte processing. Ars Technica. Retrieved 15 April 2015   
40. Australia’s bid for the square kilometre array—an insider’s perspective. The Conversation. Retrieved 27 Sept 2016 (1 Feb 2012)   
41. P. Delort, OECD ICCP technology foresight forum, 2012. Oecd.org. Retrieved 8 Oct 2017   
42. NASA—NASA Goddard Introduces the NASA Center for Climate Simulation. Nasa.gov. Retrieved 13 April 2016   
43. P. Webster, Supercomputing the climate: NASA’s big data mission. CSC World. Computer Sciences Corporation. Archived from the original on 4 January 2013. Retrieved 18 Jan 2013   
44. These six great neuroscience ideas could make the leap from lab to market. The Globe and Mail. Retrieved 1 Oct 2016 (20 Nov 2014)   
45. DNAstack tackles massive, complex DNA datasets with Google Genomics. Google Cloud Platform. Retrieved 1 Oct 2016   
46. 23andMe—Ancestry. 23andme.com. Retrieved 29 Dec 2016   
47. A. Potenza (13 July 2016), 23andMe wants researchers to use its kits, in a bid to expand its collection of genetic data. The Verge. Retrieved 29 Dec 2016   
48. This startup will sequence your dna, so you can contribute to medical research. Fast Company. Retrieved 29 Dec 2016 (23 Dec 2016)   
49. C. Seife, 23andMe Is terrifying, but not for the reasons the FDA thinks. Scientific American. Retrieved 29 Dec 2016   
50. A. Zaleski, This biotech start-up is betting your genes will yield the next wonder drug. CNBC. Retrieved 29 Dec 2016 (22 June 2016)   
51. A. Regalado, How 23andMe turned your DNA into a $\$ 1$ billion drug discovery machine. MIT Technology Review. Retrieved 29 Dec 2016   
52. 23andMe reports jump in requests for data in wake of Pfizer depression study|FierceBiotech. fiercebiotech.com. Retrieved 29 Dec 2016   
53. L. Tay, Inside eBay’s 90PB data warehouse. ITNews. Retrieved 12 Feb 2016   
54. J. Layton, Amazon technology. Money.howstuffworks.com. Retrieved 5 March 2013   
55. Scaling Facebook to 500 million users and beyond. Facebook.com. Retrieved 21 July 2013   
56. Google still doing at least 1 trillion searches per year. Search Engine Land. Retrieved 15 April 2015 (16 Jan 2015)   
57. Obama administration unveils “big data” initiative: announces $\$ 200$ million in new R&D investments. The White House. Archived from the original (PDF) on 1 Nov 2012   
58. AMPLab at the University of California, Berkeley. Amplab.cs.berkeley.edu. Retrieved 5 March 2013   
59. NSF leads federal efforts in big data. National Science Foundation (NSF). 29 March 2012   
60. T. Hunter, T. Moldovan, M. Zaharia, J. Ma, M. Franklin, P. Abbeel, A. Bayen (October 2011), Scaling the mobile millennium system in the cloud   
61. D. Patterson, Computer scientists may have what it takes to help cure cancer. The New York Times (5 Dec 2011)   
62. Secretary Chu announces new institute to help scientists improve massive data set research on doe supercomputers. energy.gov.   
63. Governor Patrick announces new initiative to strengthen Massachusetts’ position as a world leader in big data. Commonwealth of Massachusetts   
64. Big Data $@$ CSAIL. Bigdata.csail.mit.edu. Retrieved 5 March 2013 (22 Feb 2013)   
65. Big data public private forum. Cordis.europa.eu. Archived from the original on 20 May 2013. Retrieved 5 March 2013 (1 Sept 2012)

# Chapter 1 The Cluster Analysis in Big Data Mining

# 1.1 Introduction

Methods of clustering represent a powerful tools for reducing dimensions of BD warehouses. Clustering enables to split the initial big data set into several groups of similar objects by features of similarity-difference using various distance metrics and replace the whole group by the most representative object locating in the cluster center. In this chapter different clustering methods and techniques are considered and their applications for practical problems solutions are presented

Term cluster analysis (introduced by Tryon, 1939 for the first time) actually includes a set of various algorithms of classification without teacher [1]. The general question asked by researchers in many areas is how to organize observed data in evident structures, i.e. to develop taxonomy.

The clustering is applied in the most various areas. For example, in the field of medicine the clustering of diseases, treatments of diseases or symptoms of diseases leads to widely used taxonomy. In the field of psychiatry the correct diagnostics of clusters of symptoms, such as paranoia, schizophrenia, etc., is decisive for successful therapy. In archeology by means of the cluster analysis researchers try to make taxonomy of stone tools, funeral objects, etc. Broad applications of the cluster analysis in market researches are well known. Generally, every time when it is necessary to classify “mountains” of information to groups, suitable for further processing, the cluster analysis is very useful and effective. In recent years the cluster analysis is widely used in the intellectual analysis of data (Data Mining), as one of the principal methods.

The purpose of this chapter is the consideration of modern methods of the cluster analysis, crisp methods(a method of C-means, Ward’s method, the next neighbor, the most distant neighbor), and fuzzy methods, robust probabilistic and possibilistic clustering methods.

Numerous results of pilot studies of fuzzy methods of a cluster analysis are presented in the Sect. 1.9 among them is a problem of UN countries clustering by indicators of sustainable development.

# 1.2 Cluster Analysis, Problem Definition. Criteria of Quality and Metrics

Let the set of observations $c _ { 1 }$ be given, where $X _ { i } = \{ x _ { i j } \} , j = \overline { { 1 , N } }$ . It is required to divide a set $X$ into not intersected K subsets—clusters $S _ { 1 } , . . . , S _ { K }$ so that to provide extremum of some criterion (functional of quality), that is:

to find such $\boldsymbol { S } = ( S _ { 1 } , . . . , S _ { K } )$ that $f ( S )  m i n ( m a x )$ .

Different types of criteria (functional) of splitting are possible. It’s worth to note that this task is closely connected with definition of some metrics in a feature space.

Consider the most widely used functionals of splitting quality [2]:

1. Coefficient of splitting $\mathrm { \Delta F }$ which is defined as follows:

$$
F = \sum _ { j = 1 } ^ { K } \sum _ { i = 1 } ^ { n } \frac { w _ { i j } ^ { 2 } } { n } ,
$$

where $w _ { i j } \in [ 0 ; 1 ]$ —some degree of membership of the i-th object to the $\mathrm { j }$ -th cluster. Change range is $\begin{array} { r } { F \in \left[ \frac { 1 } { k } ; 1 \right] } \end{array}$ , where n—number of objects, $K$ —number of clusters.

2. Non-fuzziness index:

$$
N F I = \frac { K F - 1 } { k - 1 } , N F I \in [ 0 ; 1 ] ,
$$

where $K$ —number of classes (clusters); $F .$ —splitting coefficient.

3. Entropy of splitting:

$$
H = - \sum _ { j = 1 } ^ { K } \sum _ { i = 1 } ^ { n } \frac { w _ { i j } \ln ( w _ { i j } ) } { n } , H \in ( 0 ; \ln K ) .
$$

4. The normalized entropy of splitting:

$$
H _ { 1 } = \frac { H } { 1 - K / n } , \quad H _ { 1 } \in \bigg ( 0 ; \frac { n \ln K } { n - K } \bigg ) ,
$$

where n is a number of points.

5. The modified entropy:

$$
H _ { 2 } = \frac { H } { \ln K } , \quad H _ { 2 } \in ( 0 ; 1 )
$$

6. Second functional of Rubens:

Table 1.1 Clustering metrics   

<html><body><table><tr><td>No.</td><td>Name of a metrics</td><td>Type of features</td><td>Formula for an assessment of a measure of proximity (metrics)</td></tr><tr><td>1</td><td>Euclidean distance</td><td>The quantitative</td><td>1/2 dik=</td></tr><tr><td>2</td><td>Measure of similarity of Hamming</td><td>Nominal (qualitative)</td><td>=， where nik—number of coinciding features in samples Xi and Xk</td></tr><tr><td>3</td><td>Measure of similarity of Rogers-Tanimoto</td><td>Nominal scales</td><td>-T=n"（n+n"-n") where n'k—number of coinciding unit features at samples Xi and Xk; n',n"—total number of unit features at samplesXi and Xk respectively</td></tr><tr><td>4</td><td>Manhattan metrics</td><td>The quantitative</td><td>=</td></tr><tr><td>5</td><td>Makhalonobis's distance</td><td>The quantitative</td><td>d=(xij-xkj）TW-1(xij-xkj) W—covariance matrix of sample X={X,X2,...Xn}</td></tr><tr><td>6</td><td>Minkovsky's metrics LP</td><td></td><td>D(xk,Cj)=(∑i=1 |xk,i-Cj,|)²,p≥1</td></tr></table></body></html>

$$
\begin{array} { l } { \displaystyle F _ { 2 } = \frac { 1 } { 2 } \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname* { m a x } _ { j } W _ { i j } + \operatorname* { m i n } _ { i } \operatorname* { m a x } _ { j } W _ { i j } \right) , } \\ { \displaystyle F _ { 2 } \in \left( \frac { 1 } { K } , 1 \right) . } \end{array}
$$

7. Third functional of Rubens (second index of Non-fuzziness):

$$
N F 2 I = \frac { K F 2 - 1 } { K - 1 } , N F 2 I \in ( 0 , 1 ) .
$$

As initial information is set in the form of a matrix $X$ , there is a metrics choice problem. Metrics choice—the most important factor influencing results of a cluster analysis. Depending on type of features various measures of distance (metrics) are used.

Let be samples $X _ { i }$ and $X _ { K }$ in $N$ -dimensional feature space.

The main metrics of clustering are given in the Table 1.1.

There is a large number of clustering algorithms which use various metrics and criteria of splitting.

# 1.3 Classification of Algorithms of Cluster Analysis

When performing a clustering it is important to know, how many clusters contains an initial sample It is supposed that the clustering has to reveal natural local grouping of objects. Therefore the number of clusters is the parameter which is often significantly complicates an algorithm if it is supposed to be unknown and significantly influencing quality of result if it is known.

The problem of a choice of clusters number is very nontrivial. It is enough to tell that for obtaining the satisfactory theoretical decision often it is required to make in advance very strong assumptions of properties of some family of distributions. But about what assumptions one can make when, especially at the beginning of research, of data practically it isn’t known? Therefore algorithms of a clustering usually are constructed as some way of search clusters number and determination of its optimum value in the course of search.

The number of methods of splitting a set of objects into clusters is quite great All of them can be subdivided on hierarchical and not hierarchical.

In not hierarchical algorithms their work and conditions of stop need to be regulated in advance often with large number of parameters that is sometimes difficult, especially at the initial stage of investigation. But in such algorithms big flexibility in a variation of a clustering is reached and usually the number of clusters is defined. In not hierarchical algorithms a criterion of clustering is given and it should be optimized in result of splitting initial sample or set into clusters.

On the other hand, when objects are characterized by a large number of features (parameters), a task of grouping features is important. Initial information contains in a square matrix of features interconnections, in particular, in a correlation matrix. Basis of the successful solution of a grouping task is the informal hypothesis of a small number of the hidden factors which define structure of an interconnection between features.

In hierarchical algorithms one actually refuses to define a number of clusters, building a full tree of the enclosed clusters (so-called dendrogram). The number of clusters is defined from the assumptions, in principle, which aren’t relating to work of algorithms, for example on dynamics of change of a threshold of splitting (merge) of clusters. Difficulties of such algorithms are well studied: choice of measures of proximity of clusters, problem of inversions of indexation in the dendrograms, inflexibility of hierarchical classifications which is sometimes undesirable. Nevertheless, representation of a clustering in the form of a dendrogram allows to gain the most complete display of structure of clusters.

Hierarchical algorithms are connected with dendrograms construction and divided on:

1. agglomerative, characterized by consecutive merge of initial elements and the corresponding reduction of number of clusters (creation of clusters from below to top);

2. divisional (divided) in which the number of clusters increases, starting with one cluster therefore the sequence of the splitting groups is constructed (creation of clusters from top to down).

# 1.3.1 Hierarchical Algorithms. Agglomerative Algorithms

On the first step all the set of objects is represented as a set of clusters:

$$
c _ { 1 } = \{ i _ { 1 } \} , c _ { 2 } = \{ i _ { 2 } \} , . . . , c _ { m } = \{ i _ { m } \}
$$

On the following step two closest one to another clusters are chosen (for example, $c _ { p }$ and $c _ { q }$ ) and unite in one joint cluster. The new set consisting already of $\mathrm { m } - 1$ of clusters will be such:

$$
c _ { 1 } = \{ i _ { 1 } \} , c _ { 2 } = \{ i _ { 2 } \} , . . . , c _ { p } = \{ i _ { p } , i _ { q } \} , . . . , c _ { p } = \{ i _ { m } \}
$$

Repeating process, we obtain step by step the consecutive sets consisting of $( m -$ 2), $( m - 3 )$ , $( m - 4 )$ and etc. clusters.

At the end of procedure the cluster consisting of $\mathfrak { m }$ of objects and coinciding with an initial set $I$ will be obtained.

For determination of distance between clusters it is possible to choose different metrics. Depending on it algorithms with various properties exist.

There are some methods of recalculation of distances with use of old values of distances for the united clusters differing in coefficients in a formula:

$$
d _ { r s } = \alpha _ { p } d _ { p s } + \alpha _ { q } d _ { q s } + \beta d _ { p q } + \gamma \vert d _ { p s } - d _ { q s } \vert
$$

If clusters $\boldsymbol { \mathrm { ~ p ~ } }$ and q unite in one cluster of $\mathbf { r }$ and it is required to calculate distance from a new cluster to cluster say, s, application of this or that method depends on a way of determination of distance between clusters, these methods differ with values of coefficients $\alpha _ { p } , \alpha _ { q } , \beta , \gamma$ .

Coefficients of recalculation of distances between clusters $\alpha _ { p } , \alpha _ { q } , \beta , \gamma$ are specified in Table 1.2.

# 1.3.2 Divisional Algorithms

Divisional cluster algorithms, unlike agglomerative, on the first step represent all set of elements I as the only cluster. On each step of algorithm one of the existing clusters is recursively divided into two affiliated. Thus, clusters from top to down are iteratively formed. This approach isn’t so in detail described in literature devoted to the cluster analysis, as agglomerative algorithms. It is applied when it is necessary to divide all set of objects on rather small amount clusters.

Table 1.2 Coefficients of recalculation distances between clusters   

<html><body><table><tr><td>Name of a method</td><td>αp</td><td>aq</td><td>β</td><td>2</td></tr><tr><td>Distance between the closest neighbours—the closest objects of clusters (Nearest neighbour)</td><td>1/2</td><td>1/2</td><td>0</td><td>-1/ 2</td></tr><tr><td>Distance between the farthest neighbours (Furthest neighbour)</td><td>1/2</td><td>1/2</td><td>0</td><td>1/2</td></tr><tr><td>The method of medians—the same centroid method,but the centre of the integrated clusteris calculated asanaverage of all objects (Median clustering)</td><td>1/2</td><td>1/2</td><td>-1/4</td><td>0</td></tr><tr><td>Average distance between clusters (Between一 groups linkage)</td><td>1/2</td><td>1/2</td><td>0</td><td>0</td></tr><tr><td>Average distance between all objects of couple of clusters taking into account distances inside clusters (intra-groups linkage)</td><td>kp kp +kq</td><td>kq kp +kq</td><td>0</td><td>0</td></tr><tr><td>Distance between centres clusters (Centroid clustering),or centroid method.A lack of this methodis thatthe centre of the integrated cluster is calculated as an average of the centres of the united clusters,without their volume by Ward's method.</td><td>kp kp +kq</td><td>kp kp + kq</td><td>−kpkq kp +kq</td><td>0</td></tr><tr><td>As distance between clusters the gain of the sum of squares of distances of objects to the centres of clusters received as a result of their association is calculated</td><td>k, +kp kr +kq +kp</td><td>kr+kp kr + kq + kp</td><td>-kr kr + kq +kp</td><td>0</td></tr></table></body></html>

One of the first the divisional algorithms was offered by Smith Maknaoton in 1965 [2].

All elements are located on the first step in one cluster $C 1 = I$ .

Then the element, at which average value of distance from other elements in this cluster is the greatest is selected. Average value can be calculated, for example, by means of a formula

$$
D _ { C 1 } = \frac { 1 } { N _ { C 1 } } \times \sum _ { i p } \sum _ { i q } d ( i _ { p } , i _ { q } ) , \quad \forall i _ { p } , i _ { q } \in C
$$

$$
\mathrm { W h e r e } N _ { C 1 } = \frac { n _ { C 1 } ( n _ { C 1 } - 1 ) } { 2 } , n _ { C 1 } = | C _ { 1 } |
$$

The chosen element is removed from a cluster of C1 and becomes the first member of the second cluster C2.

On each subsequent step an element in a cluster of C1 for which the difference between average distance to the elements which are in C2, and average distance to the elements remaining in C1 is the greatest is transferred to C2.. Transfer of elements from C1 in C2 proceed until the corresponding differences of averages become negative, i.e. so far there are elements located to elements of a cluster of C2 closer than to cluster elements of C1.

As a result one cluster is divided into two affiliated ones which will be split at the following level of hierarchy. Each subsequent level procedure of division is applied to one of the clusters received at the previous level. The choice of cluster to be split can be carried out differently.

In 1990 Kauffman and Rouzeuv suggested to choose at each level a cluster for splitting with the greatest diameter which is calculated on a formula [2]

$$
D _ { C } = \operatorname* { m a x } { d ( i _ { p } , i _ { q } ) } \forall i _ { p } , i _ { q } \in C
$$

Recursive division of clusters proceeds, so far all clusters or won’t become singleton (i.e. consisting of one object), or so far all members of one cluster won’t have zero difference from each other.

# 1.3.3 Not Hierarchical Algorithms

The great popularity at the solution of clustering problems was acquired by the algorithms based on search of splitting a data set into clusters (groups). In many tasks algorithms of splitting are used owing to the advantages. These algorithms try to group data (in clusters) so that criterion function of splitting algorithm reaches an extremum (minimum). We’ll consider three main algorithms of a clustering based on splitting methods. In these algorithms the following basic concepts are used:

the training set (an input set of data) of $\mathbf { M }$ on which splitting is based; distance metrics:

$$
d _ { A } ^ { 2 } ( m _ { j } , c ^ { ( i ) } ) = \big \vert \big \vert m _ { j } - c ^ { ( i ) } \big \vert \big \vert ^ { 2 } = ( m _ { j } - c ^ { ( i ) } ) ^ { t } A ( m _ { j } - c ^ { ( i ) } )
$$

where the matrix A defines a way of distance calculation. For example, for a singular matrix distance according to Euclid metrics is used;

vector of the centers of clusters $\mathbf { C }$ ; splitting matrix on clusters U; $\bullet$ goal function $J = J ( M , d , C , U )$ ; $\bullet$ set of restrictions.

# Description of $\pmb { K }$ -means Algorithm

Basic definitions and concepts within this algorithm are following:

• the training set $M = \left\{ m _ { j } \right\} _ { j = 1 } ^ { d } d \cdot$ —number of points (vectors) of data; the distance metrics counted by a formula (1.6);   
vector of the centers of clusters $C = \{ c ^ { ( i ) } \} _ { i = 1 } ^ { c }$

where

$$
c ^ { ( i ) } = \frac { \sum _ { j = 1 } ^ { d } u _ { i j } m _ { j } } { \sum _ { j = 1 } ^ { d } u _ { i j } } , \quad 1 \leq i \leq c ;
$$

• splitting matrix $U = \{ u _ { i j } \}$ .where

$$
\begin{array} { r } { u _ { i j } ^ { ( l ) } = \left\{ { 1 , i f d ( m _ { j } , c _ { i } ^ { ( l ) } ) = \operatorname* { m i n } _ { 1 \leq k \leq c } d ( m _ { j } , c _ { k } ^ { ( l ) } ) } \right. } \\ { 0 , o t h e r w i s e } \end{array}
$$

Object function

$$
J ( M , U , C ) = \sum _ { i = 1 } ^ { c } \sum _ { j = 1 } ^ { d } u _ { i j } d _ { A } ^ { 2 } ( m _ { j } , c ^ { ( i ) } )
$$

set of restrictions

$$
\{ u _ { i j } \} \in \{ 0 , 1 \} ; \sum _ { i = 1 } ^ { c } u _ { i j } = 1 ; 0 < \sum _ { j = 1 } ^ { d } u _ { i j } < d
$$

which defines that each vector of data can belong only to one cluster and doesn’t belong to the rest. Each cluster contains not less than one point, but less than a total number of points.

Structurally the algorithm represents the following iterative procedure [1].

Step 1. To initialize initial splitting (for example, in a random way), to choose accuracy value d (it is used in a condition of end of an algorithm), to initialize a number of iteration $1 = 0$ .

Step 2. To define the centers of clusters by the following formula:

$$
c ^ { ( i ) } = \frac { \sum _ { j = 1 } ^ { d } u _ { i j } ^ { ( l - 1 ) } m _ { j } } { \sum _ { j = 1 } ^ { d } u _ { i j } ^ { ( l - 1 ) } } , \quad 1 \leq i \leq c
$$

Step 3. To update a splitting matrix to minimize squares of errors, using a formula

$$
u _ { i j } ^ { ( l - 1 ) } = \left\{ \begin{array} { c } { 1 , i f d ( m _ { j } , c _ { i } ^ { ( l ) } ) = \displaystyle \operatorname* { m i n } _ { 1 \leq k \leq c } d ( m _ { j } , c _ { k } ^ { ( l ) } ) \medskip } \\ { 0 , o t h e r w i s e } \end{array} \right.
$$

Step 4. To check a condition $\big \| U ^ { ( l ) } - U ^ { ( l - 1 ) } \big \| < \delta .$ If the condition is satisfied, finish process if it isn’t true then pa	ss to a step 2 	with number of iteration $l = l + 1$ . The main shortcoming inherent to this algorithm owing to discrete character of elements of a splitting matrix is the big size of splitting space. One way to overcome this shortcoming is the choice of elements of a splitting matrix by numbers from a unit interval. That is, belonging of a data element to a cluster has to be defined by membership function—the element of data can belong to several clusters with various degree of membership. In that case we come to a problem of fuzzy clustering. This approach found the embodiment in algorithm of fuzzy clustering— fuzzy method of K-means (Fuzzy C-Means).

# 1.4 Fuzzy C-Means Method

Consider a neural network with self-organization where training is performed without a teacher. The algorithm of self-organization relates a vector x to the corresponding cluster of data which is presented by its center, using a competitive training.

The basic form of algorithm of self-organization allows to find precisely position of the centers of the relevant groups (clusters) into which the output multidimensional space is split. These centers can be used further in hybrid algorithm of training of FNNs as initial values that considerably accelerates process of training and guarantees convergence to a global minimum [3].

# 1.4.1 Algorithm of Fuzzy C-Means

Let’s assume that in a network exists m fuzzy neurons with the centers in points $c _ { j } , ( j = 1 , 2 , . . . , m )$ . Initial values of these centers can be chosen randomly from areas of admissible values of the corresponding components of vectors $x _ { k } , ( k =$ $1 , 2 , . . . , N )$ used for training. Let function of a fuzzification be set in the form of the generalized Gauss function expressed by a formula (1.8).

The vector entered in a network input $x _ { k }$ will belong to various groups represented by the centers $c _ { j }$ , with degree $w _ { k j }$ , and $0 < w _ { k j } < 1$ , and total degree of membership to all groups, is obviously, equal 1. Therefore

$$
\sum _ { j = 1 } ^ { m } w _ { k j } = 1 ,
$$

for all $w _ { k j } ( k = 1 , 2 , . . . , N )$ .

The function of an error corresponding to such representation can be defined as the sum of individual errors of membership to the centers $c _ { i }$ taking into account fuzziness degree $\beta$ . Therefore, [4]

$$
E = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } { \Big | } { \Big | } c _ { j } - x _ { k } { \Big | } { \Big | } ^ { 2 }
$$

where $\beta$ is a weight coefficient which accepts values from an interval $( 1 , \infty )$ . The training goal of self-organization consists in such selection of the centers $c _ { j }$ , that for the whole set of the training vectors $x _ { k }$ —achievement of a minimum of function (1.14) at simultaneous fulfillment of conditions (1.13) is attained. Thus it is a problem of minimization of nonlinear function (1.14) with $\mathbf { N }$ constraints of type (1.13). The solution of this task can be transferred to minimization of Lagrange function defined by the form [4].

$$
L E = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } \| c _ { j } - x _ { k } \| ^ { 2 } + \sum _ { k = 1 } ^ { N } \lambda _ { k } \left( \sum _ { j = 1 } ^ { m } w _ { k j } - 1 \right)
$$

where $\lambda _ { k } ( k = 1 , 2 , . . . , N )$ are Lagrange’s multipliers. In it is proved that the solution of a task (1.15) can be presented in the form

$$
c _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } x _ { k } } { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } } ,
$$

$$
w _ { k j } = \frac { 1 } { \displaystyle \sum _ { i = 1 } ^ { m } \left( \frac { d _ { k j } ^ { 2 } } { d _ { i j } ^ { 2 } } \right) ^ { \frac { 1 } { \beta - 1 } } } ,
$$

where $d _ { k j }$ —is Euclidean distance between the center $c _ { j }$ and vector $x _ { k } , d _ { k j } = \left\| c _ { j } - x _ { k } \right\|$ . As exact values of the centers $c _ { j }$ at the beginning of process aren’t known, th	e trainin	g algorithm has to be iterative. It can be formulated in the following way:

1. To execute random initialization of coefficients $w _ { k j }$ , choosing their values from an interval [0, 1] so that the condition (1.13) be satisfied.   
2. To define К centers $c _ { j }$ , in accordance with (1.16).   
3. To calculate value of the error function according to expression (1.14). If its value appears below the established threshold or if reduction of this error of previous iteration is negligible, to finish calculations. The last values of the centers represent the required decision. Otherwise, go to step 4   
4. To calculate new values $u _ { k j }$ in a formula (1.17) and to pass to step 2.

Such procedure is called the fuzzy self-organization algorithm C-means.

Repetition of iterative procedure leads to achievement of a minimum of function E which won’t be a global minimum. The quality of the found centers estimated by value of an error function E essentially depends on preliminary selection of values $w _ { k j }$ and centers $c _ { j }$ . As the best will be such placement of the centers at which they settle down in the areas containing the greatest number of the shown vectors $x _ { j }$ . At such selection of the centers they will represent vectors of data $x _ { j }$ with the smallest total error.

Therefore the beginning of iterative procedure of calculation of optimum values of the centers has to be preceded by procedure of their initialization. Algorithms of peak and differential grouping of data belong to the most known algorithms of initialization.

# 1.4.2 Definition of Initial Location of the Centers of Clusters

# Algorithm of Peak Grouping

The algorithm of peak grouping was offered by Jager and Filev [4, 5].

When using N input vectors the special grid which evenly covers space of these vectors is constructed. Nodes of this grid are considered as potential centers $\vartheta$ , for each of which peak function is calculated:

$$
m ( \vartheta ) = \sum _ { k = 1 } ^ { N } \exp \left\{ \frac { - \vert \vert \vartheta - x _ { k } \vert \vert ^ { 2 b } } { 2 \sigma ^ { 2 } } \right\}
$$

where $\sigma$ is some constant which is selected separately for each specific task.

Value $m ( \vartheta )$ is considered as an assessment of height of peak function. It is proportional to quantity of vectors $x _ { j }$ , which get to the vicinity of the potential center $\vartheta$ . Great value $m ( \vartheta )$ testifies to that the center $\vartheta$ locates in the area in which the greatest number of vectors is concentrated $\left\{ x _ { k } \right\}$ .

The coefficient of $\sigma$ influences final proportions between $m ( \vartheta )$ and $\vartheta$ slightly.

After calculation of values $m ( \vartheta )$ for all potential centers the first center is selected $c _ { 1 }$ , which has the greatest value $m ( \vartheta )$ . For a choice of the following centers it is necessary to exclude $c _ { 1 }$ and nodes which are placed in close proximity to $c _ { 1 }$ .

It can be done by redefinition of peak function at the expense of separation of Gauss function from it with the center in a point $c _ { 1 }$ . Having designated this new function through $m _ { n e w } ( \vartheta )$ , we receive:

$$
m _ { n e w } ( \vartheta ) = m ( \vartheta ) - m ( c _ { 1 } ) \exp \left\{ \frac { - \vert \vert \vartheta - c _ { 1 } \vert \vert ^ { 2 b } } { 2 \sigma ^ { 2 } } \right\}
$$

Note that this function has zero in a point $c _ { 1 }$ .

Then the same procedure repeats value with the next center $c _ { 2 }$ , etc.

Process of finding of the following centers $c _ { 2 } , c _ { 3 }$ is realized consistently on the modified values $m _ { n e w } ( \vartheta )$ , which turn out at an exception of the next neighbors of the center which was found at the previous stage. It comes to an end at the moment of localization of all the centers.

The method of peak grouping is effective at not really big dimension of a vector of $X$ . Otherwise number of the potential centers increases as avalanche.

# Algorithm of Differential Grouping

The algorithm of differential grouping is a modification of the previous algorithm, in which vectors $x _ { j }$ are considered as the potential centers $\vartheta$ . Peak function $D ( x _ { i } )$ in this case takes the form [5]:

$$
D ( x _ { i } ) = \sum _ { j = 1 } ^ { N } \exp \Bigg \{ { - \frac { \big \| x _ { i } - x _ { j } \big \| ^ { 2 b } } { \big ( r _ { a } / 2 \big ) ^ { 2 } } } \Bigg \} ,
$$

where value of coefficient $r _ { a }$ defines the sphere of the neighborhood. On value $D ( x _ { i } )$ considerably influence only vectors $x _ { j }$ , which are inside this sphere.

At the big density of points near $x _ { i }$ function value $D ( x _ { i } )$ is large. After calculation of values of peak function for each point $x _ { i }$ , the vector $\mathbf { \boldsymbol { x } }$ is found, for which density measure $D ( x )$ will appear to be the greatest. This point becomes the first center $c _ { 1 }$ .

Choice of the following center $c _ { 2 }$ is performed after an exception of the previous center and all points which lie in its vicinity.

As well as in the previous case peak function is redefined so

$$
D _ { n e w } ( x _ { i } ) = D ( x _ { i } ) - D ( c _ { 1 } ) \exp \Biggl \{ - \frac { \left\| x _ { i } - c _ { 1 } \right\| ^ { 2 b } } { \left( r _ { b } / 2 \right) ^ { 2 } } \Biggr \}
$$

At new definition of function $D$ coefficients $r _ { b }$ designate new values of a constant which sets the sphere of the neighborhood of the following center. Usually a condition $r _ { b } \geq r _ { a }$ is used.

After modification of value of peak function a search of a new point $x$ , for which $D _ { n e w } ( x _ { i } ) \to \operatorname* { m a x }$ is performed It becomes the new center.

Process of finding of the next center is resumed after the exception of all already selected points. Initialization comes to an end at the time of fixing of all centers which are provided by entry conditions.

# 1.5 Gustavson-Kessel’s Fuzzy Cluster Analysis Algorithm

In classical algorithm fuzzy $C =$ means elements of error function E are obtained by means of usual Euclid distance between a vector x and the center of a cluster c with:

$$
d ( x , c ) = \| x - c \| = { \sqrt { ( x - c ) ^ { T } ( x - c ) } }
$$

At such metrics of distance between two vectors the set of the points equidistant from the center represents a sphere with an identical scale on all axes. But if data form groups which form differs from spherical or if scales of separate coordinates of a vector strongly differ, such metrics becomes inadequate. In this case quality of a clustering can be increased considerably at the expense of the improved version of the self-organization algorithm which is called as Gustavson-Kessel’s algorithm [3, 4].

The main changes of basic algorithm fuzzy C-means consist in introduction to a metrics calculation formula of the scaling matrix A. At such scaling the distance between the center $c$ and vectors $\mathbf { \boldsymbol { x } }$ is defined by a formula:

$$
d ( x , c ) = \| x - c \| = { \sqrt { ( x - c ) ^ { T } A ( x - c ) } }
$$

As scaling usually the positive-definite matrix is used, that is a matrix, at which all eigenvalues are real and positive.

Similar to the basic algorithm C-means the training goal of Gustavson-Kessel algorithm lies in such placement of the centers at which the criterion $\mathrm { ~ E ~ }$ is minimized:

$$
E = \sum _ { k } \sum _ { j } w _ { k j } ^ { \beta } d ^ { 2 } ( x _ { k } , c _ { j } )
$$

# 1.5.1 Description of Gustavson-Kessel Algorithm

1. To carry out initial placement of the centers in data space. To create an elementary form of the scaling matrix A.

2. To create a matrix of membership coefficients of all vectors $\mathbf { X }$ to the centers by a formula:

$$
w _ { k j } = \frac { 1 } { \displaystyle \sum _ { i = 1 } ^ { m } \left( \frac { d _ { k j } ^ { 2 } } { d _ { i j } ^ { 2 } } \right) ^ { \frac { 1 } { \beta - 1 } } }
$$

3. To calculate new placement of the centers according to a formula:

$$
c _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } x _ { k } } { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } } ,
$$

4. To generate a covariance matrix for each vector:

$$
S _ { j } = \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } ( x _ { k } - c _ { j } ) ( x _ { k } - c _ { j } ) ^ { T }
$$

5. To calculate a new scaling matrix for each j-th centre by a formula:

$$
A _ { j } = \sqrt [ n ] { \operatorname* { d e t } ( S _ { j } ) } S _ { j } ^ { - 1 } .
$$

6. If the last changes of centers and a covariance matrix are rather small in relation to the previous values (don’t exceed the set values), finish iterative process, otherwise go to step 2.

# 1.6 Adaptive Robust Clustering Algorithms

# 1.6.1 Possibilistic Clustering Algorithm

Major drawbacks associated with a probabilistic approach (Fuzzy C-means algorithm)are connected with constraints (1.13). In the simplest case of two clusters ${ \bf \zeta } _ { m } = 2 )$ is easy to see that the observation $x _ { k }$ , equally owned by both clusters and observation $x _ { p }$ , not belonging to any of them, may have the same levels of membership $w _ { ( k , 1 ) } = w _ { ( k , 2 ) } = w _ { ( p , 1 ) } = w _ { ( p , 2 ) } = 0 . 5$ .

Naturally, this fact decreasing the accuracy of classification, led to a possibilistic approach to the fuzzy classification [5]. In the possibilistic clustering algorithm goal function has the form

$$
E ( w _ { k , j } , c _ { j } ) = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } d ^ { 2 } ( x _ { k } , c _ { j } ) + \sum _ { j = 1 } ^ { m } \mu _ { j } \left( \sum _ { k = 1 } ^ { N } { ( 1 - w _ { k , j } ) ^ { \beta } } \right) ,
$$

where scalar parameter $\mu _ { j } > 0$ determines the distance on which membership level takes the value 0.5, that is if $d ^ { 2 } ( x _ { k } , c _ { j } ) = \mu _ { j }$ , then $w _ { k , j } = 0 . 5$ .

Minimization (1.27) by $w _ { k , j } , c _ { j } , \mu _ { j }$ gives evident solution

$$
w _ { k , j } = \left( 1 + \left( \frac { d ^ { 2 } ( x _ { k } , c _ { j } ) } { \mu _ { j } } \right) ^ { \frac { 1 } { \beta - 1 } } \right) ^ { - 1 } ,
$$

$$
c _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } x _ { k } } { \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } } ,
$$

$$
\mu _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } d ^ { 2 } ( x _ { k } , c _ { j } ) } { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } } ,
$$

It can be seen that the possibilistic and probabilistic algorithms are very similar and pass one into other by replacing the expression (1.27) to the formula (1.15), and vice versa. A common disadvantage of the considered algorithms is their computational complexity and the inability to work in real time. The algorithm (1.15)– (1.17) begins with the initial task (normal random) partitions matrix $W ^ { 0 }$ . On the basis of its values initial set of prototypes $c _ { j } ^ { 0 }$ is calculated which then is used to calculate a new matrix $W ^ { 1 }$ . Then this procedure is continued and sequence of solutions $c _ { j } ^ { 1 } W ^ { 2 } , \ldots , W ^ { t } , c _ { j } ^ { t } W ^ { t + 1 }$ etc. is obtained until the difference $\left\| W ^ { t + 1 } - W ^ { t } \right\|$ is less than a preassigned threshold e.

Therefore, all available data sample is processed repeatedly.

The solution obtained using a probabilistic algorithm, is recommended as the initial conditions for possibilistic algorithm (1.28)–(1.30) [5]. Parameter distance $\mu _ { j }$ is initialized in accordance with (1.30) on the results of the probabilistic algorithm.

# 1.6.2 Recurrent Fuzzy Clustering Algorithms

Analysis of (1.15) shows that, for the calculation of membership levels $w _ { k , j }$ instead of the Lagrangian (1.15) can be used its local modification:

$$
L ( w _ { k , j } , c _ { j } , \lambda _ { k } ) = \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } d ^ { 2 } ( x _ { k } , c _ { j } ) + \lambda _ { k } \left( \sum _ { j = 1 } ^ { m } w _ { k , j } - 1 \right)
$$

Optimization of the expression (1.31) by the procedure of the Arrow-Hurwicz-Uzawa leads to an algorithm

$$
w _ { k , j } = \frac { d ^ { 2 } ( x _ { k } , c _ { k , j } ) ^ { \frac { 1 } { \beta - 1 } } } { \sum _ { l = 1 } ^ { m } \big ( d ^ { 2 } ( x _ { k } , c _ { k , l } ) \big ) ^ { \frac { 1 } { \beta - 1 } } }
$$

$$
\begin{array} { r l } & { c _ { k + 1 , j } = c _ { k , j } - \eta _ { k } \nabla _ { c j } L _ { k } \big ( w _ { k , j } , c _ { k , j } , \lambda _ { k } \big ) } \\ & { \qquad = c _ { k , j } - \eta _ { k } w _ { k , j } ^ { \beta } d \big ( x _ { k + 1 } , c _ { k , j } \big ) \nabla c _ { j } } \end{array}
$$

Procedure (1.32), (1.33) is close to the learning algorithm Chang-Lee], and for $\beta = 2$ coincides with the gradient procedure clustering Park-Degger [6]:

$$
w _ { k , j } = \frac { \left\| x _ { k } - c _ { k , j } \right\| ^ { - 2 } } { \sum _ { l = 1 } ^ { m } \left\| x _ { k } - c _ { k , l } \right\| ^ { - 2 } }
$$

$$
c _ { k + 1 , j } = c _ { k , j } - \eta _ { k } w _ { k , j } ^ { 2 } ( x _ { k + 1 } - c _ { k , j } )
$$

Within the framework of possibilistic approach local criterion takes the form

$$
E _ { k } ( w _ { k , j } , c _ { j } ) = \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } d ^ { 2 } ( x _ { k } , c _ { j } ) + \sum _ { j = 1 } ^ { m } \mu _ { j } ( 1 - w _ { k , j } ) ^ { \beta }
$$

and the result of its optimization has the form

$$
w _ { k , j } = \left( 1 + \left( \frac { d ^ { 2 } ( \boldsymbol { x } _ { k } , c _ { k , j } ) } { \mu _ { j } } \right) ^ { \frac { 1 } { \beta - 1 } } \right) ^ { - 1 }
$$

$$
c _ { k + 1 , j } = c _ { k , j } - \eta _ { k } w _ { k , j } ^ { \beta } d ( x _ { k + 1 } , c _ { k , j } ) \nabla c _ { j }
$$

where the distance parameter $\mu _ { j }$ initialized according to (1.30).

In this case, $\mathbf { N }$ in Eq. (1.30) is a volume of data set used for initialization

In the quadratic case, the algorithm (1.37), (1.38) is converted into a rather simple procedure and optimization result is of the form

$$
w _ { k , j } = \frac { \mu _ { j } } { \mu _ { j } + \left\| x _ { k } - c _ { k , j } \right\| ^ { 2 } }
$$

wherein $\mu _ { j }$ is the distance parameter initialized by the results of the probabilistic clustering (for example, using an algorithm Fuzzy C-means (1.15)–(1.17) according to the equation:

$$
\mu _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { 2 } \left| \left| \boldsymbol { x } _ { k } - \boldsymbol { c } _ { j } \right| \right| ^ { 2 } } { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { 2 } } ,
$$

# 1.6.3 Robust Adaptive Algorithms of Probabilistic Fuzzy Clustering

The considered above clustering methods can effectively solve the problem of classification with a substantial intersection of the clusters, however, it assumes that the data within each cluster are located compactly enough without sharp (abnormal) outliers.

However, it should be noted that the actual data is usually distorted by outliers, the share of which according to some estimates [7], is up to $20 \%$ so that to speak of a compact placement of data is not always correct.

In this regard, recently, much attention was paid to problems of fuzzy cluster analysis of the data, the density distribution of which differs from the normal by presence of “heavy tails” [8, 9].

# Robust Recursive Algorithm for Probabilistic Fuzzy Clustering

After standardization of feature vectors components so that all source vectors would belong to the unit hypercube $[ 0 , 1 ] ^ { n }$ , the objective function is constructed

$$
E ( w _ { k , j } , c _ { j } ) = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } D ( x _ { k } , c _ { j } )
$$

under constraints

$$
\sum _ { j = 1 } ^ { m } w _ { k , j } = 1 , \quad k = 1 , . . . , N ,
$$

$$
0 < \sum _ { k = 1 } ^ { N } w _ { k , j } \leq N , \quad j = 1 , . . . , m .
$$

Here $D ( x _ { k } , c _ { j } )$ is a distance between $x _ { k }$ and $c _ { j }$ in adopted metric. The result of clustering is assumed to be $N \times m$ matrix $W = \{ w _ { k , j } \}$ , called “matrix of fuzzy

decomposition.” Typically, as the distance function $D ( x _ { k } , c _ { j } )$ Minkowski metric $L ^ { p }$ is applied

$$
D ( x _ { k } , c _ { j } ) = \Big ( \sum _ { i = 1 } ^ { n } \big | x _ { k , i } - c _ { j , i } \big | ^ { p } \Big ) ^ { \frac { 1 } { p } } , \quad p \geq 1 ,
$$

where $x _ { k , i } , c _ { j , i }$ are the $i \cdot$ -th components of $( n \times 1 )$ —vectors $x _ { k } , c _ { j }$ correspondingly.

Estimates relating to the quadratic objective functions are optimal when the data belong to the class of distributions with finite variance, the most famous member of which is a Gaussian.

Varying parameter $p$ allows to improve the properties of the robustness of clustering procedures, however, the quality of assessment is determined by the type of data distribution. Thus, the estimates with $\mathsf { p } = 1$ are optimal for the Laplacian data distribution, but their construction involves great computational expense. Quite realistic is the class of approximate normal distributions [9].

Approximately normal distributions are mixture of Gaussian density and distribution of some arbitrary density, which distorts with outliers the normal distribution. The optimal objective function in this case is the quadratic-linear, and tends to linear type as the distance from the minimum grows.

The most prominent representative of the approximate normal distribution density function is

$$
p ( x _ { i } , c _ { i } ) = S e ( c _ { i } , s _ { i } ) = \frac { 1 } { 2 s _ { i } } \sec h ^ { 2 } \frac { x _ { i } - c _ { i } } { s _ { i } } ,
$$

where $c _ { i } , s _ { i }$ are parameters, determining a center and a width of the distribution.

This function resembles a Gaussian in the vicinity of the center, however, has a more heavy tails. With the distribution (1.46) is associated an objective function

$$
f _ { i } ( x _ { i } , c _ { i } ) = \beta _ { i } \ln \cosh \frac { x _ { i } - c _ { i } } { \beta _ { i } } ,
$$

where the parameter $\beta _ { i }$ defines steepness of this function, while in the vicinity of the minimum this function is very close to the quadratic, tending with the growth of $X$ to a linear one.

Also interesting is the fact that the derivative of this function

$$
f _ { i } ^ { \prime } ( x _ { i } ) = \phi ( x _ { i } ) = \operatorname { t a n h } \frac { x _ { i } } { \beta _ { i } } ,
$$

is a standard activation function of artificial neural networks. Using as a metric the following structure

$$
D ^ { R } ( \boldsymbol { x } _ { k } , \boldsymbol { c } _ { j } ) = \sum _ { i = 1 } ^ { n } f _ { i } ( \boldsymbol { x } _ { k , i } , \boldsymbol { c } _ { j , i } ) = \sum _ { i = 1 } ^ { n } \beta _ { i } \ln \cosh \frac { \boldsymbol { x } _ { k , i } - \boldsymbol { c } _ { j , i } } { \beta _ { i } } ,
$$

is possible to introduce the objective function of robust classification [9]

$$
\begin{array} { c } { { E ^ { R } ( w _ { k , j } , c _ { j } ) = \displaystyle \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } D ^ { 2 } ( x _ { k } , c _ { j } ) } } \\ { { = \displaystyle \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } \sum _ { i = 1 } ^ { n } \beta _ { i } \mathrm { l n } \mathrm { c o s h } \frac { x _ { k , i } - c _ { j , i } } { \beta _ { i } } } } \end{array}
$$

and a corresponding Lagrangian

$$
L = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } \sum _ { i = 1 } ^ { n } \beta _ { i } \ln \cosh \frac { x _ { k , i } - c _ { j , i } } { \beta _ { i } } + \sum _ { k = 1 } ^ { N } \lambda _ { k } \left( \sum _ { j = 1 } ^ { m } w _ { k , j } - 1 \right)
$$

where $\lambda _ { k }$ —is indefinite Lagrange multiplier, ensuring fulfillment of constraints (1.43), (1.44). The saddle point of the Lagrangian (1.51) can be found by solving the equations system of Kuhn-Tucker

$$
\left\{ \begin{array} { l l } { \frac { \partial L ( w _ { k , j } , c _ { j } , \lambda _ { k } ) } { \partial w _ { k , j } } = 0 , } \\ { \frac { \partial L ( w _ { k , j } , c _ { j } , \lambda _ { k } ) } { \partial \lambda _ { k } } = 0 , } \\ { \nabla c _ { j } L ( w _ { k , j } , c _ { j } , \lambda _ { k } ) = 0 . } \end{array} \right.
$$

Solutions of the first and second equations lead to well-known results

$$
\left\{ \begin{array} { l l } { w _ { k , j } = \frac { \left( D ^ { R } ( x _ { k } , c _ { j } ) \right) ^ { \frac { 1 } { 1 - \beta } } } { \sum _ { l = 1 } ^ { m } \left( D ^ { R } ( x _ { k } , c _ { l } ) \right) ^ { \frac { 1 } { 1 - \beta } } } } \\ { \lambda _ { k } = - \left( \sum _ { l = 1 } ^ { m } \left( \beta D ^ { R } ( x _ { k } , c _ { l } ) \right) ^ { \frac { 1 } { 1 - \beta } } \right) ^ { 1 - \beta } } \end{array} \right.
$$

But the third equation

$$
\nabla c _ { j } L ( w _ { k , i } , c _ { j } , \lambda _ { k } ) = \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } \nabla c _ { j } D ^ { R } ( x _ { k } , c _ { j } ) = 0 ,
$$

evidently has no analytic solution. The solution of Eq. (1.54) can be obtained with the help of local modification of Lagrangian and recurrent fuzzy clustering algorithm.

Search of the Lagrangian local saddle point

$$
L _ { k } ( w _ { k , j } , c _ { j } , \lambda _ { k } ) = \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } D ^ { R } ( x _ { k } , c _ { j } ) + \lambda _ { k } \left( \sum _ { j = 1 } ^ { m } w _ { k , j } - 1 \right)
$$

using procedures Arrow-Hurwitz-Udzawa leads to an algorithm

$$
\left\{ \begin{array} { c } { w _ { k , j } ^ { p r } = \frac { \left( D ^ { R } ( x _ { k } , c _ { j } ) \right) ^ { \frac { 1 } { 1 - \beta } } } { \sum _ { l = 1 } ^ { m } \left( D ^ { R } ( x _ { k } , c _ { l } ) \right) ^ { \frac { 1 } { 1 - \beta } } } } \\ { c _ { k + 1 , j , i } = c _ { k , j , i } - \eta _ { k } \frac { \partial L ( w _ { k , j , c _ { j } , \lambda _ { k } } ) } { \partial c _ { j , i } } = c _ { k , j , i } + \eta _ { k } w _ { k , j } ^ { \beta } \operatorname { t a n h } { \frac { x _ { k , i } - c _ { k , j , i } } { \beta _ { i } } } } \end{array} \right.
$$

where $\eta _ { k }$ is a parameter of learning rate, $c _ { k , j , i }$ is the i-th component of the $\mathrm { j }$ -th prototype calculated at the $\mathbf { k }$ -th step.

But despite low computational complexity this algorithm (1.56) has the disadvantage inherent to all probabilistic clustering algorithm.

# 1.7 Robust Recursive Algorithm of Possibilistic Fuzzy Clustering for Big Data

When the data sample is big (BD) and data enters into system sequentially (e.g. time series) then we may use recursive algorithms of possibilistic fuzzy clustering. For possibilistic fuzzy clustering algorithms the criterion is the following expression

$$
E ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { i } ) = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } D ^ { 2 } ( x _ { k } , c _ { j } ) + \sum _ { j = 1 } ^ { m } \mu _ { i } \sum _ { k = 1 } ^ { N } ( 1 - w _ { k , j } ) ^ { \beta }
$$

Minimization of (1.57) by parameters $w _ { k , j } , \boldsymbol { c } _ { j }$ and $\mu _ { i }$ leads to equations system

$$
\left\{ \begin{array} { c } { \frac { \partial E ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { j } ) } { \partial w _ { k , j } } = 0 , } \\ { \frac { \partial E ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { j } ) } { \partial \mu _ { j } } = 0 , } \\ { \nabla c _ { j } E ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { j } ) = 0 . } \end{array} \right.
$$

The solution of the first two equations of (1.58) leads to the well-known result

$$
\left\{ \begin{array} { l } { w _ { k , j } ^ { p o s } = \left( 1 + \left( \frac { D ^ { R } ( x _ { k } , c _ { j } ) } { \mu _ { j } } \right) ^ { \frac { 1 } { \beta - 1 } } \right) ^ { - 1 } } \\ { \mu _ { j } = \frac { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } D ^ { R } ( x _ { k } , c _ { j } ) } { \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } } } \end{array} \right.
$$

while the third one

$$
\nabla c _ { j } E ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { j } ) = \sum _ { k = 1 } ^ { N } w _ { k , j } ^ { \beta } \nabla c _ { j } D ^ { R } ( x _ { k } , c _ { j } ) = 0
$$

fully corresponds to (1.54).

Introducing the local modification of (1.57)

$$
\begin{array} { l } { { \displaystyle E _ { k } ^ { R } = \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } D ^ { R } ( x _ { k } , c _ { j } ) + \sum _ { j = 1 } ^ { m } \mu _ { j } ( 1 - w _ { k , j } ) ^ { \beta } } } \\ { { \displaystyle \quad = \sum _ { j = 1 } ^ { m } w _ { k , j } ^ { \beta } \sum _ { i = 1 } ^ { n } \beta _ { i } \ln \cosh \frac { x _ { k , i } - c _ { j , i } } { \beta _ { i } } + \sum _ { j = 1 } ^ { m } \mu _ { j } ( 1 - w _ { k , j } ) ^ { \beta } } } \end{array}
$$

and optimizing it we obtain:

$$
\left\{ \begin{array} { c } { w _ { k , j } ^ { p o s } = \left( 1 + \left( \frac { D ^ { R } ( x _ { k } , c _ { j } ) } { \mu _ { j } } \right) ^ { \frac { 1 } { \beta - 1 } } \right) } \\ { c _ { k + 1 , j , i } = c _ { k , j , i } - \eta _ { k } \frac { \partial E _ { k } ^ { R } ( w _ { k , j } , c _ { j } , \mu _ { j } ) } { \partial c _ { j , i } } = c _ { k , j , i } + \eta _ { k } w _ { k , j } ^ { \beta } \operatorname { t a n h } { \frac { x _ { k } - c _ { k , j , i } } { \beta _ { i } } } } \end{array} \right.
$$

where the distance parameter $\mu _ { k j }$ may be determined according to the second equation of the system (1.59) for $\mathbf { k }$ observations rather than the entire sample volume $N .$

It should be noted that the last equation of system (1.52) and (1.58) are identical and are determined only by choice of metrics. This makes possible to use any suitable metric for a particular case, which will determine only the setup procedure of prototypes if the equation for calculating the weights still remains the same.

Considered robust recursive methods may be used in a batch mode and in the on-line mode as well. In the last case the number of observation $\mathbf { k }$ represents a discrete time.

Experiments with a repository of data, distorted by abnormal outliers (emissions), have shown high efficiency of the proposed algorithms in the processing of the information given in the form of tables “object-property” [7, 8] and in the form of time series [10].

In particular, the problem of data classification of specially artificially generated sample containing three-dimensional cluster of data was considered, whose observations are marked the symbols “o”, “x” and $" \boldsymbol { + } \boldsymbol { \mathbf { \mathit { \Sigma } } }$ [9] (see Fig. 1.1). Points in each cluster are distributed according to the density of Laplace distribution having “heavy tails”

$$
p ( x _ { i } ) = \sigma ( 1 + ( x _ { i } - c ) ^ { 2 } ) ^ { - 1 }
$$

where $\sigma$ and $c$ are width and center correspondingly.

The sample includes 9000 observations (3000 in each cluster) and is divided into training (7200 cases) and testing (1800 cases) subsamples [10, 11].

It should be noted that some observations are very far away from the centers of the clusters (Fig. 1.1a). Prototypes of the clusters are located in the central region of the data as shown in Fig. 1.1b. In order to find the correct prototypes clustering algorithm should be insensitive to outliers.

For all of the algorithms involved in the comparison, the procedure of the experiment was performed as follows. At the beginning of training a sample was clustered by appropriate algorithms and prototypes of clusters have been found.

![](images/648fddda4100354f158747df671ddac26ca1eea23e1db96a5a38baee5dbaad77.jpg)  
Fig. 1.1 Full sample (а) and its central part (b)

Table 1.3 Results of classification. Classification error   

<html><body><table><tr><td>Algorithm</td><td>Training sample</td><td>Testing sample</td></tr><tr><td>Fuzzy C-means</td><td>17.1% (1229 obs.)</td><td>16.6% (299 obs.)</td></tr><tr><td>Robust probabilistic</td><td>15.6% (1127) obs.)</td><td>15.6% (281 obs.)</td></tr><tr><td>Robust possibilistic</td><td>15.2% (1099 obs.)</td><td>14.6% (263 obs.)</td></tr></table></body></html>

Then, training and testing samples were classified according to the results of clustering. Observations belonging to each cluster in the classification process are calculated in accordance with Eqs. (1.17), (1.56) or (1.62) depending on the type of clustering algorithm. The cluster, to which the observation belongs with a maximum membership degree, defines the class of this observation. Classification and training is performed in the on-line mode of receiving observations, where $\beta = 2 , \beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = 1 , \eta ( k ) = 0 . 0 1$ . The results are shown in Table 1.3 [9].

![](images/7a119945f34afc5c4a949012f567aea3bfe4728c407c6962c9259fed6dbf5804.jpg)  
Fig. 1.2 Prototypes of clusters

In the Fig. 1.2 it can be easily seen that the centers of the clusters (prototypes) produced by the algorithm «fuzzy C-means» by Bezdek, are shifted from the visual centers of the clusters, due to the presence of “heavy tails” of the data distribution density, in contrast to the robust methods with objective function (1.56) and (1.62) in which prototypes are found more precisely, which is confirmed by the less classification error (see Table 1.3).

Continuous growth in the successful application of computational intelligence technologies in the areas of data analysis confirms the versatility of this approach. At the same time, real problems that arise in the processing of very large databases (Big Data), complicate the use of existing algorithms and tools and demand to be improved to meet the challenges of data mining in real time using the paradigms of CI and soft computing.

# 1.8 Application of Fuzzy Clustering Methods in the Problems of Automatic Classification

Example 1.1 Classification of the UN countries These UN Millennium Indicators are presented in the Table 1.4.

Table 1.4 UN Millenium Indicators for world countries   

<html><body><table><tr><td></td><td>Population percent below the poverty line</td><td>Percent of children for 5 years with an insufficient</td><td>Literacy</td><td>Gender equality.Percent of women among workers of the non-agricultural sphere</td></tr><tr><td>Afghanistan</td><td>70</td><td>weight 48</td><td>50</td><td>17.8</td></tr><tr><td>Albania</td><td>25.4</td><td>14.3</td><td>99.4</td><td>40.3</td></tr><tr><td>Algeria</td><td>12.2</td><td>6</td><td>89.9</td><td>15.5</td></tr><tr><td>Angola</td><td>70</td><td>30.5</td><td>71.4</td><td>26.4</td></tr><tr><td>Argentina</td><td>15</td><td>5.4</td><td>98.6</td><td>47.6</td></tr><tr><td>Armenia</td><td>53.7</td><td>2.6</td><td>99.8</td><td>47</td></tr><tr><td>Azerbaijan</td><td>49.6</td><td>6.8</td><td>99.9</td><td>48.5</td></tr><tr><td>Bahrain</td><td>15</td><td>8.7</td><td>97</td><td>13.4</td></tr><tr><td>Bangladesh</td><td>49.8</td><td>47.7</td><td>49.7</td><td>24.2</td></tr><tr><td>Belize</td><td>40</td><td>6.2</td><td>84.2</td><td>44.4</td></tr><tr><td>Belarus</td><td>41.9</td><td>2</td><td>99.8</td><td>55.9</td></tr><tr><td>Butane</td><td>70</td><td>18.7</td><td>80</td><td>12</td></tr><tr><td>Benin</td><td>33</td><td>22.9</td><td>55.5</td><td>46</td></tr><tr><td>Bolivia</td><td>62.7</td><td>7.5</td><td>97.3</td><td>36.5</td></tr><tr><td>Bosnia Herzegovina</td><td>19.5</td><td>4.1</td><td>99.6</td><td>35.8</td></tr><tr><td>Botswana</td><td>70</td><td>12.5</td><td>89.1</td><td>47</td></tr><tr><td>Brazil</td><td>17.4</td><td>5.7</td><td>96.3</td><td>46.7</td></tr><tr><td>Bulgaria</td><td>12.8</td><td>2</td><td>99.7</td><td>52.2</td></tr><tr><td>Burundi</td><td>70</td><td>45.1</td><td>72.3</td><td>13.3</td></tr><tr><td>Burkina Faso</td><td>45.3</td><td>34.3</td><td>19.4</td><td>15.2</td></tr><tr><td>Cambodia</td><td>36.1</td><td>45.2</td><td>80.3</td><td>52.6</td></tr><tr><td>Cameroon</td><td>40.2</td><td>21</td><td>81.1</td><td>20.7</td></tr><tr><td>Verde's cap It is central</td><td>40</td><td>13.5</td><td>89.1</td><td>39.1</td></tr><tr><td>the African Republic</td><td>70</td><td>24.3</td><td>58.5</td><td>30.4</td></tr><tr><td>Fumes</td><td>64</td><td>28.1</td><td>37.3</td><td>5.5</td></tr><tr><td>Chile</td><td>17</td><td>0.7</td><td>99</td><td>37.3</td></tr><tr><td>China</td><td>4.6</td><td>10</td><td>98.9</td><td>39.5</td></tr><tr><td>Colombia</td><td>64</td><td>6.7</td><td>97.2</td><td>48.8</td></tr><tr><td>Congo</td><td>50</td><td>13.9</td><td>97.8</td><td>26.1</td></tr><tr><td>Costa Rica</td><td>22</td><td>5.1</td><td>98.4</td><td>39.5</td></tr><tr><td>Cote d'Ivoire</td><td>59</td><td>21.2</td><td>59.8</td><td>20.2</td></tr><tr><td>Croatia</td><td>20</td><td>0.6</td><td>99.6</td><td>46.3</td></tr><tr><td>Cuba</td><td>60</td><td>4.1</td><td>99.8</td><td>37.7</td></tr></table></body></html>

(continued)

Table 1.4 (continued)   

<html><body><table><tr><td></td><td>Population percent below the poverty line</td><td>Percent of children for 5 years with an insufficient weight</td><td>Literacy</td><td>Gender equality.Percent of women among workers of the non-agricultural sphere</td></tr><tr><td>Czech Republic</td><td>10</td><td>1</td><td>99.8</td><td>45.8</td></tr><tr><td>Democratic republic of</td><td>70</td><td>31.1</td><td>68.7</td><td>25.9</td></tr><tr><td>Congo Djibouti</td><td>45.1</td><td>18.2</td><td>73.2</td><td>25</td></tr><tr><td>Dominican Republic</td><td>28.6</td><td>5.3</td><td>94</td><td>34.9</td></tr><tr><td>Ecuador</td><td>35</td><td>11.6</td><td>96.4</td><td>41.1</td></tr><tr><td>Egypt</td><td>16.7</td><td>8.6</td><td>73.2</td><td>21.6</td></tr><tr><td>El Salvador</td><td>48.3</td><td>10.3</td><td>88.9</td><td>31.1</td></tr><tr><td>Equatorial Guinea</td><td>50</td><td>18.6</td><td>92.7</td><td>10.5</td></tr><tr><td>Eritrea</td><td>53</td><td>39.6</td><td>60.9</td><td>35</td></tr><tr><td>Estonia</td><td>8.9</td><td>1</td><td>99.8</td><td>51.5</td></tr><tr><td>Ethiopia</td><td>44.2</td><td>47.2</td><td>57.4</td><td>39.9</td></tr><tr><td>Fiji</td><td>40</td><td>7.9</td><td>99.3</td><td>35.9</td></tr><tr><td>Gabon</td><td>40</td><td>11.9</td><td>59</td><td>37.7</td></tr><tr><td>Gambia</td><td>64</td><td>17</td><td>42.2</td><td>20.9</td></tr><tr><td>Georgia</td><td>11.1</td><td>3.1</td><td>99.8</td><td>45.2</td></tr><tr><td>Ghana</td><td>50</td><td>24.9</td><td>81.8</td><td>56.5</td></tr><tr><td>Guatemala</td><td>56.2</td><td>22.7</td><td>80.1</td><td>38.7</td></tr><tr><td>Guinea</td><td>40</td><td>23.2</td><td>50</td><td>30.3</td></tr><tr><td>Guinea-Bissau</td><td>48.7</td><td>25</td><td>44.1</td><td>10.8</td></tr><tr><td>Guyana</td><td>35</td><td>13.6</td><td>80</td><td>37.4</td></tr><tr><td>Haiti</td><td>45</td><td>17.3</td><td>66.2</td><td>39.5</td></tr><tr><td>Honduras</td><td>53</td><td>16.6</td><td>88.9</td><td>50.5</td></tr><tr><td>Hungary</td><td>17.3</td><td>3</td><td>99.5</td><td>47.1</td></tr><tr><td>India</td><td>28.6</td><td>47</td><td>64.3</td><td>17.5</td></tr><tr><td>Indonesia</td><td>27.1</td><td>26.1</td><td>98</td><td>30.8</td></tr><tr><td>Iran</td><td>30</td><td>10.9</td><td>86.3</td><td>17.2</td></tr><tr><td>Iraq</td><td>35</td><td>15.9</td><td>41</td><td>11.9</td></tr><tr><td>Jamaica</td><td>18.7</td><td>3.6</td><td>94.5</td><td>48</td></tr><tr><td>Jordan</td><td>11.7</td><td>4.4</td><td>99.4</td><td>24.9</td></tr><tr><td>Kazakhstan</td><td>34.6</td><td>4.2</td><td>99.8</td><td>48.7</td></tr><tr><td>Laos</td><td>38.6</td><td>40</td><td>78.5</td><td>42.1</td></tr><tr><td>Kenya</td><td>52</td><td>20.2</td><td>95.8</td><td>38.5</td></tr></table></body></html>

(continued)

Table 1.4 (continued)   

<html><body><table><tr><td></td><td>Population percent below the poverty line</td><td>Percent of children for 5 years with an insufficient weight</td><td>Literacy</td><td>Gender equality. Percent of women among workers of the non-agricultural sphere</td></tr><tr><td>Democratic People's Republic of</td><td>60</td><td>20.8</td><td>99.8</td><td>40.7</td></tr><tr><td>Korea Kuwait</td><td>20</td><td>9.8</td><td>93.1</td><td>24.1</td></tr><tr><td>Kyrgyzstan</td><td>64.1</td><td>11</td><td>99.7</td><td>44.1</td></tr><tr><td>Lebanon</td><td>20</td><td>3</td><td>92.1</td><td>25.9</td></tr><tr><td>Lesotho</td><td>50</td><td>17.9</td><td>87.2</td><td>24.7</td></tr><tr><td>Liberia</td><td>60</td><td>26.4</td><td>70.8</td><td>23.6</td></tr><tr><td>Libya</td><td>30</td><td>4.7</td><td>97</td><td>15</td></tr><tr><td>Madagascar</td><td>71.3</td><td>33.1</td><td>70.1</td><td>24.2</td></tr><tr><td>Malawi</td><td>65.3</td><td>21.9</td><td>63.2</td><td>12.5</td></tr><tr><td>Malaysia</td><td>40</td><td>12.4</td><td>97.2</td><td>38</td></tr><tr><td>Maldives</td><td>70</td><td>30.4</td><td>99.2</td><td>36.1</td></tr><tr><td>Mali</td><td>63.8</td><td>33.2</td><td>24.2</td><td>35.9</td></tr><tr><td>Mauritania</td><td>46.3</td><td>31.8</td><td>49.6</td><td>37</td></tr><tr><td>Mexico</td><td>30</td><td>7.5</td><td>96.6</td><td>37.4</td></tr><tr><td>Mozambique</td><td>69.4</td><td>23.7</td><td>62.8</td><td>11.4</td></tr><tr><td>Mongolia</td><td>36.3</td><td>12.7</td><td>97.7</td><td>49.4</td></tr><tr><td>Morocco</td><td>19</td><td>8.9</td><td>69.5</td><td>26.2</td></tr><tr><td>Nepal</td><td>42</td><td>48.3</td><td>70.1</td><td>11.8</td></tr><tr><td>Nicaragua</td><td>47.9</td><td>9.6</td><td>86.2</td><td>41.1</td></tr><tr><td>Niger</td><td>63</td><td>39.6</td><td>25.6</td><td>8.6</td></tr><tr><td>Nigeria</td><td>34.1</td><td>28.7</td><td>88.6</td><td>34</td></tr><tr><td>Pakistan</td><td>32.6</td><td>38</td><td>53.9</td><td>8.7</td></tr><tr><td>Panama</td><td>37.3</td><td>6.8</td><td>96.1</td><td>44</td></tr><tr><td>Papua New Guinea</td><td>37.5</td><td>7</td><td>68.6</td><td>35.4</td></tr><tr><td>Paraguay</td><td>21.8</td><td>4.6</td><td>96.3</td><td>42</td></tr><tr><td>Peru</td><td>49</td><td>7.1</td><td>96.6</td><td>37.2</td></tr><tr><td>Philippines</td><td>36.8</td><td>30.6</td><td>95.1</td><td>41.1</td></tr><tr><td>Poland</td><td>23.8</td><td>3</td><td>99.8</td><td>47.7</td></tr><tr><td>Moldova</td><td>23.3</td><td>3.2</td><td>98.7</td><td>54.6</td></tr><tr><td>Romania</td><td>21.5</td><td>5.7</td><td>97.8</td><td>45.3</td></tr><tr><td>Russian Federation</td><td>30.9</td><td>3</td><td>99.8</td><td>50.1</td></tr></table></body></html>

(continued)

Table 1.4 (continued)   

<html><body><table><tr><td></td><td>Population percent below the poverty line</td><td>Percent of children for 5 years with an insufficient</td><td>Literacy</td><td>Gender equality.Percent of women among workers of the non-agricultural sphere</td></tr><tr><td>Rwanda</td><td>51.2</td><td>weight 27.2</td><td>76.5</td><td>14.6</td></tr><tr><td>Senegal</td><td>33.4</td><td>22.7</td><td>51.5</td><td>25.7</td></tr><tr><td>Sri Lanka</td><td>25</td><td>29.4</td><td>97</td><td>43.2</td></tr><tr><td>Serbia and</td><td>30</td><td>1.9</td><td>99.8</td><td>44.9</td></tr><tr><td>Montenegro Swaziland</td><td>40</td><td>10.3</td><td>88.1</td><td>31.3</td></tr><tr><td>Thailand</td><td>13.1</td><td>18.6</td><td>98</td><td>46.9</td></tr><tr><td>Trinidad and Tobago</td><td>21</td><td>5</td><td>99.8</td><td>41.3</td></tr><tr><td>Turkey</td><td>25</td><td>8.3</td><td>95.5</td><td>20.6</td></tr><tr><td>Turkmenistan</td><td>30</td><td>12</td><td>99.8</td><td>20</td></tr><tr><td>Tunisia</td><td>7.6</td><td>4</td><td>94.3</td><td>25.3</td></tr><tr><td>Uganda</td><td>44</td><td>22.8</td><td>80.2</td><td>35.6</td></tr><tr><td>Ukraine</td><td>31.7</td><td>3</td><td>99.9</td><td>53.6</td></tr><tr><td>United Arab Emirates</td><td>20</td><td>14.4</td><td>91.4</td><td>14.4</td></tr><tr><td>Tanzania</td><td>35.7</td><td>29.4</td><td>91.6</td><td>28.5</td></tr><tr><td>USA</td><td>5</td><td>1.4</td><td>99.1</td><td>48.8</td></tr><tr><td>Uzbekistan</td><td>27.5</td><td>7.9</td><td>99.7</td><td>41.5</td></tr><tr><td>Vietnam</td><td>50.9</td><td>33.1</td><td>94.1</td><td>51.8</td></tr><tr><td>Yemen</td><td>41.8</td><td>45.6</td><td>67.9</td><td>6.1</td></tr><tr><td>Zambia</td><td>72.9</td><td>28.1</td><td>81.2</td><td>29.4</td></tr><tr><td>Zimbabwe</td><td>34.9</td><td>13</td><td>97.6</td><td>21.8</td></tr></table></body></html>

In this experiment it was required to perform a clustering of the United Nations countries into 4 clusters by the above indicators. As a result of the clustering algorithm of Gustavson–Kessel application the following results were obtained centers of clusters are presented in Table 1.5.

The matrix of belonging coefficients to different clusters (membership functions) are presented in Table 1.6.

As can be seen from the table in the first cluster are countries with relatively high rates of all indicators (compared to other countries in the sample). These are the countries of CIS, Eastern and western Europe, USA, Canada, the Balkans and Latin America countries.

Table 1.5 The centers of the clusters   

<html><body><table><tr><td>28.25</td><td>5.96</td><td>97.86</td><td>43.77</td></tr><tr><td>29.85</td><td>12.51</td><td>82.14</td><td>23.67</td></tr><tr><td>59.72</td><td>26.00</td><td>65.40</td><td>24.48</td></tr><tr><td>40.39</td><td>34.25</td><td>74.51</td><td>31.35</td></tr></table></body></html>

In the second cluster are countries with smaller values of indicators, it’s countries of North Africa and Middle East. In this cluster, is the lowest level of gender equality.

In the third cluster are the poorest countries with the lowest levels of literacy, as well as the low level of gender equality. Mainly it’s African countries.

In the fourth cluster are poor countries with the most unfavorable conditions for the growth of children.

Example 1.2 Classification of the United Nations countries on sustainable development indicators.

Investigations of fuzzy clustering method C-means by indicators of sustainable development for the countries of the United Nations were carried out. For this, the data of the World Data Center in Ukraine (WDC) were used.

As sustainable development indicators the following indices were taken:

Index GINI—GINI Ihd—index of health status Iql—standard of living index Isd—index of sustainable development.

As algorithm of initial centers placement the algorithm of differential grouping was applied. Clustering was carried out for a different number of clusters $\mathrm { K } = 3 , 4$ , 5. Besides the value of optimized criterion the quality of splitting will be evaluated by the indicator of Hi-Beni:

$$
\chi = \frac { d _ { a \nu } } { D _ { a \nu } } ,
$$

where $d _ { a \nu }$ is the average intra-cluster distance, $D _ { a \nu }$ —average inter-cluster distance.   
This indicator should be minimized.

# Experiment 1. $\mathbf { K } = 3$ (Tables 1.7 and 1.8)

Let us analyze the results. The first cluster contains countries with the highest values of all parameters. These are the countries of Western Europe, as well as some other. Namely, Australia, Austria, Belgium, Great Britain, Hungary, Denmark, Iceland, Ireland, Israel, Italy, Cyprus, Latvia, Lithuania, Luxembourg,

Table 1.6 Membership coefficients to different clusters   
(continued)   

<html><body><table><tr><td>Afghanistan</td><td>0.055</td><td>0.162</td><td>0.495</td><td>0.288</td></tr><tr><td>Albania</td><td>0.599</td><td>0.114</td><td>0.073</td><td>0.214</td></tr><tr><td>Algeria</td><td>0.174</td><td>0.733</td><td>0.031</td><td>0.062</td></tr><tr><td>Angola</td><td>0.045</td><td>0.102</td><td>0.789</td><td>0.064</td></tr><tr><td>Argentina</td><td>0.939</td><td>0.024</td><td>0.016</td><td>0.021</td></tr><tr><td>Armenia</td><td>0.731</td><td>0.067</td><td>0.116</td><td>0.087</td></tr><tr><td>Azerbaijan</td><td>0.757</td><td>0.058</td><td>0.103</td><td>0.082</td></tr><tr><td>Bahrain</td><td>0.204</td><td>0.687</td><td>0.030</td><td>0.080</td></tr><tr><td>Bangladesh</td><td>0.031</td><td>0.071</td><td>0.187</td><td>0.712</td></tr><tr><td>Belize</td><td>0.251</td><td>0.252</td><td>0.266</td><td>0.231</td></tr><tr><td>Belarus</td><td>0.761</td><td>0.056</td><td>0.087</td><td>0.096</td></tr><tr><td>Butane</td><td>0.241</td><td>0.156</td><td>0.479</td><td>0.124</td></tr><tr><td>Benin</td><td>0.057</td><td>0.282</td><td>0.371</td><td>0.290</td></tr><tr><td>Bolivia</td><td>0.645</td><td>0.087</td><td>0.191</td><td>0.077</td></tr><tr><td>Bosnia Herzegovina</td><td>0.764</td><td>0.157</td><td>0.029</td><td>0.050</td></tr><tr><td>Botswana</td><td>0.530</td><td>0.130</td><td>0.215</td><td>0.124</td></tr><tr><td>Brazil</td><td>0.920</td><td>0.033</td><td>0.020</td><td>0.027</td></tr><tr><td>Bulgaria</td><td>0.914</td><td>0.033</td><td>0.025</td><td>0.028</td></tr><tr><td>Burundi</td><td>0.178</td><td>0.171</td><td>0.445</td><td>0.206</td></tr><tr><td>Burkina Faso</td><td>0.020</td><td>0.249</td><td>0.495</td><td>0.236</td></tr><tr><td>Cambodia</td><td>0.120</td><td>0.050</td><td>0.163</td><td>0.667</td></tr><tr><td>Cameroon</td><td>0.115</td><td>0.522</td><td>0.095</td><td>0.268</td></tr><tr><td>Verde's cap</td><td>0.428</td><td>0.197</td><td>0.160</td><td>0.215</td></tr><tr><td>It is central the African Republic</td><td>0.048</td><td>0.287</td><td>0.471</td><td>0.194</td></tr><tr><td>Fumes</td><td>0.021</td><td>0.117</td><td>0.681</td><td>0.180</td></tr><tr><td>Chile</td><td>0.758</td><td>0.158</td><td>0.034</td><td>0.049</td></tr><tr><td>China</td><td>0.800</td><td>0.091</td><td>0.040</td><td>0.070</td></tr><tr><td>Colombia</td><td>0.703</td><td>0.075</td><td>0.136</td><td>0.086</td></tr><tr><td>Congo</td><td>0.435</td><td>0.275</td><td>0.157</td><td>0.133</td></tr><tr><td>Costa Rica</td><td>0.930</td><td>0.039</td><td>0.012</td><td>0.019</td></tr><tr><td>Cote d'Ivoire</td><td>0.013</td><td>0.091</td><td>0.819</td><td>0.077</td></tr><tr><td>Croatia</td><td>0.928</td><td>0.032</td><td>0.018</td><td>0.022</td></tr><tr><td>Cuba</td><td>0.631</td><td>0.092</td><td>0.183</td><td>0.093</td></tr><tr><td>Czech Republic</td><td>0.919</td><td>0.040</td><td>0.018</td><td>0.022</td></tr><tr><td>Democratic republic of Congo</td><td>0.038</td><td>0.108</td><td>0.784</td><td>0.069</td></tr><tr><td>Djibouti</td><td>0.036</td><td>0.604</td><td>0.203</td><td>0.158</td></tr><tr><td>Dominican Republic</td><td>0.642</td><td>0.234</td><td>0.049</td><td>0.074</td></tr><tr><td>Ecuador</td><td>0.839</td><td>0.053</td><td>0.038</td><td>0.070</td></tr></table></body></html>

Table 1.6 (continued)   

<html><body><table><tr><td>Egypt</td><td>0.065</td><td>0.791</td><td>0.068</td><td>0.076</td></tr><tr><td>El Salvador</td><td>0.389</td><td>0.243</td><td>0.219</td><td>0.148</td></tr><tr><td>Equatorial Guinea</td><td>0.347</td><td>0.331</td><td>0.140</td><td>0.182</td></tr><tr><td>Eritrea</td><td>0.035</td><td>0.076</td><td>0.246</td><td>0.642</td></tr><tr><td>Estonia</td><td>0.909</td><td>0.037</td><td>0.026</td><td>0.028</td></tr><tr><td>Ethiopia</td><td>0.048</td><td>0.060</td><td>0.174</td><td>0.718</td></tr><tr><td>Fiji</td><td>0.716</td><td>0.130</td><td>0.067</td><td>0.087</td></tr><tr><td>Gabon</td><td>0.038</td><td>0.428</td><td>0.351</td><td>0.183</td></tr><tr><td>Gambia</td><td>0.035</td><td>0.200</td><td>0.509</td><td>0.256</td></tr><tr><td>Georgia</td><td>0.934</td><td>0.032</td><td>0.015</td><td>0.020</td></tr><tr><td>Ghana</td><td>0.180</td><td>0.107</td><td>0.264</td><td>0.448</td></tr><tr><td>Guatemala</td><td>0.100</td><td>0.143</td><td>0.577</td><td>0.181</td></tr><tr><td>Guinea</td><td>0.020</td><td>0.401</td><td>0.397</td><td>0.182</td></tr><tr><td>Guinea-Bissau</td><td>0.021</td><td>0.193</td><td>0.572</td><td>0.214</td></tr><tr><td>Guyana</td><td>0.126</td><td>0.435</td><td>0.206</td><td>0.233</td></tr><tr><td>Haiti</td><td>0.040</td><td>0.353</td><td>0.366</td><td>0.241</td></tr><tr><td>Honduras</td><td>0.368</td><td>0.122</td><td>0.275</td><td>0.235</td></tr><tr><td>Hungary</td><td>0.961</td><td>0.017</td><td>0.010</td><td>0.013</td></tr><tr><td>India</td><td>0.087</td><td>0.070</td><td>0.098</td><td>0.745</td></tr><tr><td>Indonesia</td><td>0.220</td><td>0.099</td><td>0.077</td><td>0.604</td></tr><tr><td>Iran</td><td>0.106</td><td>0.785</td><td>0.035</td><td>0.074</td></tr><tr><td>Iraq</td><td>0.034</td><td>0.306</td><td>0.464</td><td>0.196</td></tr><tr><td>Jamaica</td><td>0.815</td><td>0.077</td><td>0.051</td><td>0.057</td></tr><tr><td>Jordan</td><td>0.322</td><td>0.588</td><td>0.029</td><td>0.061</td></tr><tr><td>Kazakhstan</td><td>0.920</td><td>0.024</td><td>0.025</td><td>0.031</td></tr><tr><td>Laos</td><td>0.057</td><td>0.029</td><td>0.086</td><td>0.828</td></tr><tr><td>Kenya</td><td>0.375</td><td>0.131</td><td>0.318</td><td>0.177</td></tr><tr><td>Democratic People's Republic ofKorea</td><td>0.293</td><td>0.128</td><td>0.451</td><td>0.127</td></tr><tr><td>Kuwait</td><td>0.232</td><td>0.689</td><td>0.023</td><td>0.055</td></tr><tr><td>Kyrgyzstan</td><td>0.609</td><td>0.093</td><td>0.213</td><td>0.085</td></tr><tr><td>Lebanon</td><td>0.240</td><td>0.656</td><td>0.040</td><td>0.063</td></tr><tr><td>Lesotho</td><td>0.276</td><td>0.360</td><td>0.204</td><td>0.160</td></tr><tr><td>Liberia</td><td>0.013</td><td>0.056</td><td>0.893</td><td>0.038</td></tr><tr><td>Libya</td><td>0.302</td><td>0.489</td><td>0.069</td><td>0.141</td></tr><tr><td>Madagascar</td><td>0.051</td><td>0.111</td><td>0.764</td><td>0.074</td></tr><tr><td>Malawi</td><td>0.044</td><td>0.120</td><td>0.715</td><td>0.120</td></tr><tr><td>Malaysia</td><td>0.725</td><td>0.100</td><td>0.069</td><td>0.106</td></tr><tr><td>Maldives</td><td>0.203</td><td>0.133</td><td>0.557</td><td>0.108</td></tr><tr><td>Mali</td><td>0.027</td><td>0.438</td><td>0.231</td><td>0.304</td></tr></table></body></html>

(continued)

Table 1.6 (continued)   

<html><body><table><tr><td>Mauritania</td><td>0.028</td><td>0.206</td><td>0.350</td><td>0.415</td></tr><tr><td>Mexico</td><td>0.900</td><td>0.054</td><td>0.017</td><td>0.029</td></tr><tr><td>Mozambique</td><td>0.050</td><td>0.117</td><td>0.721</td><td>0.112</td></tr><tr><td>Mongolia</td><td>0.648</td><td>0.068</td><td>0.107</td><td>0.177</td></tr><tr><td>Morocco</td><td>0.055</td><td>0.757</td><td>0.101</td><td>0.086</td></tr><tr><td>Nepal</td><td>0.108</td><td>0.079</td><td>0.110</td><td>0.703</td></tr><tr><td>Nicaragua</td><td>0.299</td><td>0.206</td><td>0.290</td><td>0.204</td></tr><tr><td>Niger</td><td>0.020</td><td>0.170</td><td>0.533</td><td>0.276</td></tr><tr><td>Nigeria</td><td>0.096</td><td>0.040</td><td>0.052</td><td>0.813</td></tr><tr><td>Pakistan</td><td>0.065</td><td>0.172</td><td>0.163</td><td>0.600</td></tr><tr><td>Panama</td><td>0.930</td><td>0.023</td><td>0.021</td><td>0.025</td></tr><tr><td>Papua New Guinea</td><td>0.066</td><td>0.411</td><td>0.334</td><td>0.189</td></tr><tr><td>Paraguay</td><td>0.930</td><td>0.036</td><td>0.014</td><td>0.020</td></tr><tr><td>Peru</td><td>0.748</td><td>0.081</td><td>0.100</td><td>0.070</td></tr><tr><td>Philippines</td><td>0.119</td><td>0.045</td><td>0.096</td><td>0.740</td></tr><tr><td>Poland</td><td>0.966</td><td>0.013</td><td>0.009</td><td>0.012</td></tr><tr><td>Moldova</td><td>0.873</td><td>0.038</td><td>0.041</td><td>0.048</td></tr><tr><td>Romania</td><td>0.979</td><td>0.009</td><td>0.005</td><td>0.007</td></tr><tr><td>Russian Federation</td><td>0.924</td><td>0.023</td><td>0.024</td><td>0.029</td></tr><tr><td>Rwanda</td><td>0.138</td><td>0.315</td><td>0.240</td><td>0.308</td></tr><tr><td>Senegal</td><td>0.027</td><td>0.466</td><td>0.322</td><td>0.185</td></tr><tr><td>Sri Lanka</td><td>0.186</td><td>0.058</td><td>0.099</td><td>0.657</td></tr><tr><td>Serbia and Montenegro</td><td>0.921</td><td>0.031</td><td>0.021</td><td>0.027</td></tr><tr><td>Swaziland</td><td>0.293</td><td>0.433</td><td>0.125</td><td>0.150</td></tr><tr><td>Thailand</td><td>0.550</td><td>0.094</td><td>0.106</td><td>0.250</td></tr><tr><td>Trinidad and Tobago</td><td>0.931</td><td>0.035</td><td>0.013</td><td>0.021</td></tr><tr><td>Turkey</td><td>0.133</td><td>0.806</td><td>0.018</td><td>0.043</td></tr><tr><td>Turkmenistan</td><td>0.197</td><td>0.656</td><td>0.037</td><td>0.110</td></tr><tr><td>Tunisia</td><td>0.369</td><td>0.537</td><td>0.035</td><td>0.059</td></tr><tr><td>Uganda</td><td>0.089</td><td>0.145</td><td>0.241</td><td>0.525</td></tr><tr><td>Ukraine</td><td>0.867</td><td>0.036</td><td>0.044</td><td>0.053</td></tr><tr><td>United Arab Emirates</td><td>0.255</td><td>0.584</td><td>0.039</td><td>0.122</td></tr><tr><td>Tanzania</td><td>0.151</td><td>0.072</td><td>0.070</td><td>0.706</td></tr><tr><td>USA</td><td>0.905</td><td>0.043</td><td>0.025</td><td>0.027</td></tr><tr><td>Uzbekistan</td><td>0.889</td><td>0.046</td><td>0.023</td><td>0.042</td></tr><tr><td>Vietnam</td><td>0.190</td><td>0.077</td><td>0.308</td><td>0.426</td></tr><tr><td>Yemen</td><td>0.117</td><td>0.106</td><td>0.118</td><td>0.659</td></tr><tr><td>Zambia</td><td>0.147</td><td>0.125</td><td>0.659</td><td>0.069</td></tr><tr><td>Zimbabwe</td><td>0.249</td><td>0.585</td><td>0.046</td><td>0.120</td></tr></table></body></html>

Table 1.7 Indicators of the sustainable development   

<html><body><table><tr><td></td><td></td><td>0.57383</td><td>0.57353</td></tr><tr><td>0.58387</td><td>0.54820</td><td></td><td></td></tr><tr><td>0.56706</td><td>0.48474</td><td>0.26571</td><td>0.35047</td></tr><tr><td>0.35296</td><td>0.63011</td><td>0.76377</td><td>0.49466</td></tr><tr><td>0.65586</td><td>0.51200</td><td>0.33448</td><td>0.47481</td></tr><tr><td>0.56994</td><td>0.81968</td><td>0.78295</td><td>0.86663</td></tr><tr><td>0.68752 0.60008</td><td>0.72971</td><td>0.80098 0.35928</td><td>0.8154</td></tr><tr><td>0.65282</td><td>0.53918</td><td></td><td>0.40572</td></tr><tr><td>0.614967</td><td>0.21060</td><td>0.20669</td><td>0.17571</td></tr><tr><td>0.498461</td><td>0.748405</td><td>0.817869</td><td>0.676777</td></tr><tr><td>0.172206</td><td>0.178393</td><td>0.334484</td><td>0.208119</td></tr><tr><td>0.548856</td><td>0.433633</td><td>0.492253</td><td>0.298884</td></tr><tr><td>0.13233</td><td>0.534668</td><td>0.492253</td><td>0.354646</td></tr><tr><td>0.216163</td><td>0.418817</td><td>0.464936</td><td>0.347845</td></tr><tr><td>0.361631</td><td>0.518054</td><td>0.626328</td><td>0.60656</td></tr><tr><td>0.380226</td><td>0.583907</td><td>0.699515</td><td>0.518325</td></tr><tr><td>0.376477</td><td>0.23689</td><td>0.157964</td><td>0.204641</td></tr><tr><td>0.62295</td><td>0.201684</td><td>0.143939</td><td>0.2182</td></tr><tr><td>0.243463</td><td>0.77159</td><td>0.72201</td><td>0.84180</td></tr><tr><td>0.437748</td><td>0.64134</td><td>0.546863</td><td>0.731782</td></tr><tr><td>0.157988</td><td>0.463597</td><td>0.384858</td><td>0.332749</td></tr><tr><td>0.271513</td><td>0.502915</td><td>0.546863</td><td>0.618515</td></tr><tr><td>0.601288</td><td>0.557193</td><td>0.600368</td><td>0.724376</td></tr><tr><td>0.962098</td><td>0.61875</td><td>0.676009</td><td>0.603607</td></tr><tr><td>0.744175</td><td>0.678039</td><td>0.600368</td><td>0.681226</td></tr><tr><td>0.761651</td><td>0.717602</td><td>0.722017</td><td>0.702571</td></tr><tr><td>0.303631</td><td>0.747263</td><td>0.743451</td><td>0.816827</td></tr><tr><td>0.294138</td><td>0.463597</td><td>0.464936</td><td>0.412767</td></tr><tr><td>0.631237</td><td>0.512001 0.399777</td><td>0.600368 0.265716</td><td>0.403071 0.419674</td></tr><tr><td>0.331064</td><td>0.457576</td><td>0.437827</td><td>0.504924</td></tr><tr><td>0.553215</td><td>0.680678</td><td>0.699515</td><td>0.689583</td></tr><tr><td>0.676386</td><td>0.101967</td><td>0.143939</td><td>0.201635</td></tr><tr><td>0.72688</td><td>0.752941</td><td>0.699515</td><td>0.85815</td></tr><tr><td>0.619443</td><td>0.754066</td><td>0.817869</td><td>0.794635</td></tr><tr><td>0.324594</td><td>0.141861</td><td>0.265716</td><td>0.235642</td></tr><tr><td>0.441675</td><td>0.516541</td><td></td><td>0.47656</td></tr><tr><td>0.702424</td><td>0.768379</td><td>0.411085 0.800988</td><td>0.806349</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>0.588835</td><td>0.73447</td><td>0.743451</td><td>0.517882</td></tr></table></body></html>

(continued)

Table 1.7 (continued)   

<html><body><table><tr><td>0.219163</td><td>0.316496</td><td>0.437827</td><td>0.325601</td></tr><tr><td>0.167474</td><td>0.376757</td><td>0.359283</td><td>0.269843</td></tr><tr><td>0.64978</td><td>0.67139</td><td>0.763774</td><td>0.663.185</td></tr><tr><td>0.962098</td><td>0.75068</td><td>0.743451</td><td>0.87829</td></tr><tr><td>0.536571</td><td>0.265352</td><td>0.225227</td><td>0.253416</td></tr><tr><td>0.537406</td><td>0.371083</td><td>0.359283</td><td>0.268663</td></tr><tr><td>0.588616</td><td>0.778987</td><td>0.743451</td><td>0.752281</td></tr><tr><td>0.486303</td><td>0.754066</td><td>0.651581</td><td>0.644542</td></tr><tr><td>0.552527</td><td>0.733286</td><td>0.782957</td><td>0.668513</td></tr><tr><td>0.357959</td><td>0.5014</td><td>0.546863</td><td>0.405747</td></tr><tr><td>0.759359</td><td>0.767299</td><td>0.800988</td><td>0.793311</td></tr><tr><td>0.517332</td><td>0.490799</td><td>0.359283</td><td>0.445905</td></tr><tr><td>0.655486</td><td>0.540692</td><td>0.265716</td><td>0.434827</td></tr><tr><td>0.31728</td><td>0.211616</td><td>0.28762</td><td>0.234049</td></tr><tr><td>0.641912</td><td>0.759641</td><td>0.743451</td><td>0.610841</td></tr><tr><td>0.605705</td><td>0.36826</td><td>0.310566</td><td>0.317857</td></tr><tr><td>0.558807</td><td>0.621604</td><td>0.699515</td><td>0.655443</td></tr><tr><td>0.520474</td><td>0.64134</td><td>0.676009</td><td>0.6509</td></tr><tr><td>0.962098</td><td>0.73091</td><td>0.546863</td><td>0.802207</td></tr><tr><td>0.32533</td><td>0.178393</td><td>0.206696</td><td>0.19195</td></tr><tr><td>0.490073</td><td>0.138213</td><td>0.28762</td><td>0.23739</td></tr><tr><td>0.344576</td><td>0.585379</td><td>0.437827</td><td>0.527639</td></tr><tr><td>0.248442</td><td>0.594174</td><td>0.651581</td><td>0.552042</td></tr><tr><td>0.510835</td><td>0.404146</td><td>0.437827</td><td>0.336335</td></tr><tr><td>0.542408</td><td>0.402688</td><td>0.334484</td><td>0.305619</td></tr><tr><td>0.451213</td><td>0.325741</td><td>0.464936</td><td>0.427675</td></tr><tr><td>0.356033</td><td>0.080015</td><td>0.206696</td><td>0.241402</td></tr><tr><td>0.047323</td><td>0.379606</td><td>0.464936</td><td>0.449997</td></tr><tr><td>0.324226</td><td>0.172261</td><td>0.28762</td><td>0.3035</td></tr><tr><td>0.655107</td><td>0.773727</td><td>0.782957</td><td>0.775775</td></tr><tr><td>0.549644</td><td>0.79125</td><td>0.833616</td><td>0.854503</td></tr><tr><td>0.239314</td><td>0.323085</td><td>0.334484</td><td>0.315336</td></tr><tr><td>0.40908</td><td>0.167985</td><td>0.157964</td><td>0.181214</td></tr><tr><td>0.744654</td><td>0.820582</td><td>0.763774</td><td>0.851428</td></tr><tr><td>0.619443</td><td>0.232537</td><td>0.130966</td><td>0.172761</td></tr><tr><td>0.239162</td><td>0.601457</td><td>0.573832</td><td>0.600787</td></tr><tr><td>0.245166</td><td>0.429174</td><td>0.546863</td><td>0.583011</td></tr><tr><td>0.312213</td><td>0.554201</td><td>0.310566</td><td>0.522702</td></tr><tr><td>0.386772</td><td>0.426208</td><td>0.310566</td><td>0.340265</td></tr><tr><td>0.589972</td><td>0.657887</td><td>0.722017</td><td>0.625403</td></tr></table></body></html>

(continued)

Table 1.7 (continued)   

<html><body><table><tr><td></td><td></td><td></td><td></td></tr><tr><td>0.501937</td><td>0.657887</td><td>0.782957</td><td>0.667165</td></tr><tr><td>0.650353</td><td>0.61875</td><td>0.600368</td><td>0.547301</td></tr><tr><td>0.42253</td><td>0.548206</td><td>0.310566</td><td>0.515363</td></tr><tr><td>0.486509</td><td>0.158067</td><td>0.28762</td><td>0.195048</td></tr><tr><td>0.744335</td><td>0.688527</td><td>0.651581</td><td>0.687639</td></tr><tr><td>0.650353</td><td>0.70137</td><td>0.763774</td><td>0.673112</td></tr><tr><td>0.166191</td><td>0.366851</td><td>0.464936</td><td>0.29966</td></tr><tr><td>0.580784</td><td>0.743814</td><td>0.743451</td><td>0.724533</td></tr><tr><td>0.464124</td><td>0.456073</td><td>0.359283</td><td>0.450402</td></tr><tr><td>0.757052</td><td>0.768379</td><td>0.699515</td><td>0.874694</td></tr><tr><td>0.600644</td><td>0.756307</td><td>0.722017</td><td>0.851068</td></tr><tr><td>0.602294</td><td>0.343272</td><td>0.189316</td><td>0.253371</td></tr><tr><td>0.520265</td><td>0.147865</td><td>0.225227</td><td>0.255087</td></tr><tr><td>0.220891</td><td>0.450068</td><td>0.411085</td><td>0.400544</td></tr><tr><td>0.463915</td><td>0.573568</td><td>0.464936</td><td>0.385968</td></tr><tr><td>0.452668</td><td>0.493827</td><td>0.464936</td><td>0.492711</td></tr><tr><td>0.47499</td><td>0.487771</td><td>0.492253</td><td>0.455756</td></tr><tr><td>0.381611</td><td>0.16714</td><td>0.244906</td><td>0.22529</td></tr><tr><td>0.716261</td><td>0.534668</td><td>0.464936</td><td>0.361609</td></tr><tr><td>0.962098</td><td>0.684616</td><td>0.225227</td><td>0.51641</td></tr><tr><td>0.55376</td><td>0.72732</td><td>0.800988</td><td>0.780447</td></tr><tr><td>0.452668</td><td>0.786202</td><td>0.937406</td><td>0.805513</td></tr><tr><td>0.419463</td><td>0.615887</td><td>0.743451</td><td>0.687183</td></tr><tr><td>0.53824</td><td>0.395423</td><td>0.225227</td><td>0.17794</td></tr><tr><td>0.397572</td><td>0.513515</td><td>0.265716</td><td>0.30664</td></tr><tr><td>0.520474</td><td>0.332429</td><td>0.265716</td><td>0.317299</td></tr><tr><td>0.264436</td><td>0.145589</td><td>0.310566</td><td>0.254877</td></tr><tr><td>0.264436</td><td>0.035073</td><td>0.10799</td><td>0.1072</td></tr><tr><td>GINI</td><td>Ihd</td><td>Iql</td><td>Isd</td></tr><tr><td>0.63499</td><td>0.724</td><td>0.73749</td><td>0.73457</td></tr><tr><td>0.44656</td><td>0.236</td><td>0.25218</td><td>0.24782</td></tr><tr><td>0.38459</td><td>0.493</td><td>0.45717</td><td>0.45412</td></tr><tr><td>Criterion</td><td>9.8738</td><td>Hi-Beni</td><td>0.438</td></tr></table></body></html>

Table 1.8 Degrees of membership to clusters   

<html><body><table><tr><td>3</td><td>Albania</td><td>0.40165</td><td>0.10648</td><td>0.49186</td></tr><tr><td></td><td></td><td>0.08839</td><td>0.43869</td><td>0.47292</td></tr><tr><td>3 3</td><td>Algeria Argentina</td><td>0.38845</td><td>0.11707</td><td>0.49448</td></tr><tr><td>3</td><td>Armenia</td><td>0.17773</td><td>0.27465</td><td>0.54762</td></tr><tr><td>1</td><td>Australia</td><td>0.90018</td><td>0.02894</td><td>0.07086</td></tr><tr><td>1</td><td>Austria</td><td>0.95403</td><td>0.01378</td><td>0.03218</td></tr><tr><td>3</td><td>Azerbaijan</td><td>0.13099</td><td>0.24733</td><td>0.62168</td></tr><tr><td>2</td><td>Bangladesh</td><td>0.04774</td><td>0.8121</td><td>0.14015</td></tr><tr><td>1</td><td>Belgium</td><td>0.95258</td><td>0.01291</td><td>0.0345</td></tr><tr><td>2</td><td>Benin</td><td>0.017346</td><td>0.91288</td><td>0.069771</td></tr><tr><td>3</td><td>Bolivia</td><td>0.086566</td><td>0.27213</td><td>0.6413</td></tr><tr><td>3</td><td>Bosnia and Herzegovina</td><td>0.1149</td><td>0.16889</td><td>0.71621</td></tr><tr><td>3</td><td>Botswana</td><td>0.090011</td><td>0.27373</td><td>0.63626</td></tr><tr><td>3</td><td>Brazil</td><td>0.21422</td><td>0.13172</td><td>0.65406</td></tr><tr><td>3</td><td>Bulgaria</td><td>0.29843</td><td>0.10605</td><td>0.59552</td></tr><tr><td>2</td><td>Cambodia</td><td>0.015168</td><td>0.92082</td><td>0.064017</td></tr><tr><td>2</td><td>Cameroon</td><td>0.017754</td><td>0.91106</td><td>0.071185</td></tr><tr><td>1</td><td>Canada</td><td>0.94729</td><td>0.01499</td><td>0.03771</td></tr><tr><td>3</td><td>Chile</td><td>0.34211</td><td>0.1277</td><td>0.53019</td></tr><tr><td>3</td><td>China</td><td>0.04406</td><td>0.22574</td><td>0.7302</td></tr><tr><td>3</td><td>Colombia</td><td>0.17747</td><td>0.15295</td><td>0.66959</td></tr><tr><td>3</td><td>Costa Rica</td><td>0.33409</td><td>0.12403</td><td>0.54188</td></tr><tr><td>1</td><td>Croatia</td><td>0.75759</td><td>0.052825</td><td>0.18958</td></tr><tr><td>1</td><td>Cyprus</td><td>0.68146</td><td>0.11573</td><td>0.2028</td></tr><tr><td>1</td><td>Czech Republic</td><td>0.94321</td><td>0.016686</td><td>0.0401</td></tr><tr><td>1</td><td>Denmark</td><td>0.92516</td><td>0.023355</td><td>0.051486</td></tr><tr><td>3</td><td>Dominican Republic</td><td>0.023839</td><td>0.05861</td><td>0.91755</td></tr><tr><td>3</td><td>Ecuador</td><td>0.08807</td><td>0.10437</td><td>0.80756</td></tr><tr><td>2</td><td>Egypt</td><td>0.10324</td><td>0.48662</td><td>0.41014</td></tr><tr><td>3</td><td>El Salvador</td><td>0.021848</td><td>0.041038</td><td>0.93711</td></tr><tr><td>1</td><td>Estonia</td><td>0.91918</td><td>0.018352</td><td>0.062473</td></tr><tr><td>2</td><td>Ethiopia</td><td>0.063802</td><td>0.77286</td><td>0.16334</td></tr><tr><td>1</td><td>Finland</td><td>0.91557</td><td>0.025895</td><td>0.058533</td></tr><tr><td>1</td><td>France</td><td>0.95921</td><td>0.011702</td><td>0.029093</td></tr><tr><td>2</td><td>Gambia</td><td>0.023284</td><td>0.87702</td><td>0.099697</td></tr><tr><td>3</td><td>Georgia</td><td>0.023663</td><td>0.038418</td><td>0.93792</td></tr><tr><td>1</td><td>Germany</td><td>0.94903</td><td>0.015455</td><td>0.03551</td></tr><tr><td>1</td><td>Greece</td><td>0.74098</td><td>0.062566</td><td>0.19646</td></tr><tr><td>3</td><td>IBaTeMaJIa</td><td>0.067026</td><td>0.40502</td><td>0.52795</td></tr></table></body></html>

(continued)

Table 1.8 (continued)   

<html><body><table><tr><td>3</td><td>Honduras</td><td>0.071116</td><td>0.45306</td><td>0.47582</td></tr><tr><td></td><td></td><td></td><td>0.012626</td><td></td></tr><tr><td>1 1</td><td>Hungary</td><td>0.95232 0.76693</td><td>0.084196</td><td>0.03505 0.14888</td></tr><tr><td>2</td><td>Iceland India</td><td>0.012701</td><td>0.93374</td><td>0.053564</td></tr><tr><td>2</td><td></td><td>0.050291</td><td>0.64789</td><td>0.30182</td></tr><tr><td>1</td><td>Indonesia</td><td>0.97523</td><td>0.006589</td><td>0.018182</td></tr><tr><td>1</td><td>Ireland Israel</td><td>0.75846</td><td>0.049725</td><td>0.19181</td></tr><tr><td>1</td><td></td><td>0.93061</td><td>0.01727</td><td>0.052117</td></tr><tr><td>3</td><td>Italy Jamaica</td><td>0.037423</td><td>0.05336</td><td>0.90922</td></tr><tr><td>1</td><td>Japan</td><td>0.92541</td><td>0.023439</td><td>0.051152</td></tr><tr><td>3</td><td>Yordaniya</td><td>0.070166</td><td>0.17151</td><td>0.75832</td></tr><tr><td>3</td><td>Kazakhstan</td><td>0.16399</td><td>0.33124</td><td>0.50477</td></tr><tr><td>2</td><td>Kenya</td><td>0.020158</td><td>0.8778</td><td>0.10204</td></tr><tr><td>1</td><td>Korea, Republic</td><td>0.91524</td><td>0.02221</td><td>0.062547</td></tr><tr><td>2</td><td>Kyrgyzstan</td><td>0.066312</td><td>0.62744</td><td>0.30625</td></tr><tr><td>1</td><td>Latvia</td><td>0.82602</td><td>0.037702</td><td>0.13627</td></tr><tr><td>1</td><td>Lithuania</td><td>0.76748</td><td>0.046179</td><td>0.18634</td></tr><tr><td>1</td><td>Luxembourg</td><td>0.6903</td><td>0.11288</td><td>0.19682</td></tr><tr><td>2</td><td>Madagascar</td><td>0.021309</td><td>0.89052</td><td>0.088166</td></tr><tr><td>2</td><td>Malawi</td><td>0.014653</td><td>0.92942</td><td>0.055931</td></tr><tr><td>3</td><td>Malaysia</td><td>0.058977</td><td>0.05684</td><td>0.88418</td></tr><tr><td>3</td><td>Mexico</td><td>0.23705</td><td>0.117</td><td>0.64595</td></tr><tr><td>3</td><td>Moldova, Republic</td><td>0.064556</td><td>0.31673</td><td>0.61872</td></tr><tr><td>2</td><td>Mongolia</td><td>0.057925</td><td>0.56437</td><td>0.3777</td></tr><tr><td>3</td><td>Morocco</td><td>0.062452</td><td>0.26329</td><td>0.67426</td></tr><tr><td>2</td><td>Mozambique</td><td>0.029408</td><td>0.86369</td><td>0.1069</td></tr><tr><td>3</td><td>Namibia</td><td>0.1218</td><td>0.28352</td><td>0.59468</td></tr><tr><td>2</td><td>Nepal</td><td>0.025167</td><td>0.84944</td><td>0.12539</td></tr><tr><td>1</td><td>Niderlandi</td><td>0.97497</td><td>0.007208</td><td>0.017824</td></tr><tr><td>1</td><td>Zealand is new</td><td>0.8935</td><td>0.030837</td><td>0.075666</td></tr><tr><td>2</td><td>Nicaragua</td><td>0.051662</td><td>0.54775</td><td>0.40058</td></tr><tr><td>2</td><td>Niger</td><td>0.017697</td><td>0.91677</td><td>0.065531</td></tr><tr><td>1</td><td>Norway</td><td>0.90361</td><td>0.030465</td><td>0.065925</td></tr><tr><td>2</td><td>Pakistan</td><td>0.044592</td><td>0.82182</td><td>0.13359</td></tr><tr><td>3</td><td>Panama</td><td>0.21163</td><td>0.11324</td><td>0.67513</td></tr><tr><td>3</td><td>Paraguay</td><td>0.12109</td><td>0.13045</td><td>0.74846</td></tr><tr><td>3</td><td>Peru</td><td>0.0764</td><td>0.13887</td><td>0.78473</td></tr><tr><td>3</td><td>Philippines</td><td>0.043558</td><td>0.41156</td><td>0.54488</td></tr><tr><td>1</td><td>Poland</td><td>0.8745</td><td>0.028966</td><td>0.096534</td></tr><tr><td>1</td><td>Portugal</td><td>0.83716</td><td>0.037676</td><td>0.12517</td></tr><tr><td>1</td><td>Rumuniya</td><td>0.57831</td><td>0.094633</td><td>0.32706</td></tr></table></body></html>

(continued)

Table 1.8 (continued)   

<html><body><table><tr><td>3</td><td>Russian Federation</td><td>0.076257</td><td>0.13511</td><td>0.78863</td></tr><tr><td>2</td><td>Senegal</td><td>0.013131</td><td>0.93672</td><td>0.050145</td></tr><tr><td>1</td><td>Slovakia</td><td>0.89028</td><td>0.031444</td><td>0.078275</td></tr><tr><td>1</td><td>Slovenia</td><td>0.97281</td><td>0.007269</td><td>0.019919</td></tr><tr><td>3</td><td>South Africa</td><td>0.08185</td><td>0.34815</td><td>0.57</td></tr><tr><td>1</td><td>Spain</td><td>0.98221</td><td>0.004552</td><td>0.013235</td></tr><tr><td>3</td><td>Sri Lanka</td><td>0.043578</td><td>0.13993</td><td>0.8165</td></tr><tr><td>1</td><td>Sweden</td><td>0.89026</td><td>0.034693</td><td>0.075048</td></tr><tr><td>1</td><td>Switzerland</td><td>0.93911</td><td>0.017102</td><td>0.043793</td></tr><tr><td>2</td><td>Tajikistan</td><td>0.045867</td><td>0.78327</td><td>0.17087</td></tr><tr><td>2</td><td>Tanzania,Republic</td><td>0.015506</td><td>0.92838</td><td>0.056119</td></tr><tr><td>3</td><td>Thailand</td><td>0.055589</td><td>0.17785</td><td>0.76656</td></tr><tr><td>3</td><td>TrinidadiTobago</td><td>0.059986</td><td>0.083263</td><td>0.85675</td></tr><tr><td>3</td><td>Tunisia</td><td>0.026507</td><td>0.033837</td><td>0.93966</td></tr><tr><td>3</td><td>Turkey</td><td>0.039097</td><td>0.051998</td><td>0.90891</td></tr><tr><td>2</td><td>Uganda</td><td>0.01028</td><td>0.94557</td><td>0.044149</td></tr><tr><td>3</td><td>Ukraine</td><td>0.23303</td><td>0.27103</td><td>0.49594</td></tr><tr><td>1</td><td>United Arab Emirates</td><td>0.36305</td><td>0.28152</td><td>0.35543</td></tr><tr><td>1</td><td>Great Britain</td><td>0.94643</td><td>0.014397</td><td>0.039177</td></tr><tr><td>1</td><td>USA</td><td>0.79335</td><td>0.060098</td><td>0.14655</td></tr><tr><td>1</td><td>Uruguay</td><td>0.666</td><td>0.069556</td><td>0.26445</td></tr><tr><td>2</td><td>Uzbekistan</td><td>0.043994</td><td>0.77022</td><td>0.18578</td></tr><tr><td>3</td><td>Venezuela,Bolivar Republic</td><td>0.06372</td><td>0.38883</td><td>0.54745</td></tr><tr><td>2</td><td>Vietnam</td><td>0.028441</td><td>0.81113</td><td>0.16043</td></tr><tr><td>2</td><td>Zambia</td><td>0.03963</td><td>0.78231</td><td>0.17806</td></tr><tr><td>2</td><td>Zimbabwe</td><td>0.061394</td><td>0.75431</td><td>0.18429</td></tr><tr><td>Number of a cluster</td><td></td><td>1</td><td>2</td><td>3</td></tr></table></body></html>

Netherlands, New Zealand, Norway, Poland, Portugal. USA, Slovakia, Slovenia, Croatia, Czech Republic, Sweden, Switzerland, Uruguay.

The second cluster contains countries with an average value of the index GINI, and minimum values of all other indicators. These are the countries of Africa and South-East Asia. These include: Bangladesh, Egypt, Zambia, Zimbabwe, India, Indonesia, Cambodia, Cameroon, Kyrgyzstan, Nicaragua, Niger, Pakistan, Uganda, Senegal, Tajikistan, Tanzania, and others.

The third cluster contains countries with average values of all the indicators and the small value of the index GINI. It includes the CIS countries, Latin America and some of the most developed countries of Asia and Africa. Namely, Armenia,

Albania, Algeria, Argentina, Brazil, Bolivia, Bulgaria, Bosnia and Herzegovina, Venezuela, Honduras, Guatemala, Georgia, Jordan, Kazakhstan, China, Costa Rica, Colombia, Mexico, Moldova, Peru, Paraguay, Russian Federation, Trinidad and Tobago, Tunisia, Turkey, Ukraine, Chile, South Africa, Jamaica.

# Experiment 2. $\mathbf { K } = 4$ (Table 1.9)

It is interesting to analyse dynamics of changes of clusters after transition from ${ \mathrm { K } } = 3$ to ${ \mathrm { K } } = 4$ .

The countries with the greatest values of all indicators fall to the first cluster. The structure of this cluster practically didn’t change. In the second cluster there are countries with the minimum value of an index GINI and average values of all other indicators. Here are the countries of Latin America: Argentina, Brazil, Panama, Paraguay, Peru, Uruguay, etc.

The countries with the minimum values of all indicators except GINI index fall to the third cluster. Here the countries from the second cluster of the previous clustering at ${ \mathrm { K } } = 3$ fall. Namely, Bangladesh, Benin, Zambia, Zimbabwe, India, Cambodia, Cameroon, Kenya, Mozambique, Nepal, Pakistan, Senegal, Tadzhikistan, Tanzania, Uzbekistan.

The countries with average values of all indicators fall to the fourth cluster. Here the countries from the third cluster of the previous clustering fall, namely: Venezuela, Vietnam, Ukraine, the Russian Federation, Azerbaijan, Georgia, Indonesia, Jordan, Kyrgyzstan, Sri Lanka. Value of an indicator of Chi- Beni decreased from 0.438 to 0.39492.

# Experiment 3. ${ \bf K } = { \bf 5 }$

For this experiment we present only the average data for cluster centers (see below)

<html><body><table><tr><td colspan="4">Centers of clusters</td></tr><tr><td>0.52645</td><td>0.45648</td><td>0.35255</td><td>0.37995</td></tr><tr><td>0.56042</td><td>0.67078</td><td>0.70818</td><td>0.64717</td></tr><tr><td>0.41643</td><td>0.18501</td><td>0.23361</td><td>0.22605</td></tr><tr><td>0.68519</td><td>0.75586</td><td>0.75276</td><td>0.80007</td></tr><tr><td>0.27997</td><td>0.47653</td><td>0.48824</td><td>0.45777</td></tr><tr><td>Criterion 1</td><td>9.0011</td><td>Hi Beni</td><td>0.38816</td></tr></table></body></html>

Consider the dependence of the index Hi-Beni on the number of clusters K (Fig. 1.3)

As the chart above shows, the value of Hi-Beni index significantly decreases when $K = 2 – 4$ , then its value is changing slightly. Therefore, the optimal number of clusters lies in vicinity of $K = 4$ .

# Determination the Number of Clusters in Cluster Analysis

The main drawback of the most of clustering methods, including FCM and Gustavson-Kessel methods is that for their application the number of clusters

Table 1.9 Degrees of membership of the countries to clusters   

<html><body><table><tr><td>4</td><td>Albania</td><td>0.28424</td><td>0.3116</td><td>0.072582</td><td>0.33157</td></tr><tr><td>4</td><td>Algeria</td><td>0.027483</td><td>0.071321</td><td>0.10306</td><td>0.79814</td></tr><tr><td>2</td><td>Argentina</td><td>0.22755</td><td>0.53851</td><td>0.067084</td><td>0.16686</td></tr><tr><td>4</td><td>Armenia</td><td>0.070525</td><td>0.11933</td><td>0.091308</td><td>0.71884</td></tr><tr><td>1</td><td>Australia</td><td>0.86029</td><td>0.070031</td><td>0.022093</td><td>0.047588</td></tr><tr><td>1</td><td>Austria</td><td>0.94636</td><td>0.0251</td><td>0.008865</td><td>0.019672</td></tr><tr><td>4</td><td>Azerbaijan</td><td>0.033017</td><td>0.073697</td><td>0.051201</td><td>0.84209</td></tr><tr><td>3</td><td>Bangladesh</td><td>0.042206</td><td>0.084422</td><td>0.63857</td><td>0.2348</td></tr><tr><td>1</td><td>Belgium</td><td>0.92169</td><td>0.039019</td><td>0.011551</td><td>0.027739</td></tr><tr><td>3</td><td>Benin</td><td>0.017031</td><td>0.046297</td><td>0.82568</td><td>0.111</td></tr><tr><td>2</td><td>Bolivia</td><td>0.061197</td><td>0.50498</td><td>0.18867</td><td>0.24515</td></tr><tr><td>4</td><td>Bosnia and Herzegovina</td><td>0.057183</td><td>0.1661</td><td>0.071758</td><td>0.70496</td></tr><tr><td>2</td><td>Botswana</td><td>0.060793</td><td>0.52973</td><td>0.18418</td><td>0.22529</td></tr><tr><td>2</td><td>Brazil</td><td>0.068824</td><td>0.80042</td><td>0.041411</td><td>0.089343</td></tr><tr><td>2</td><td>Bulgaria</td><td>0.14689</td><td>0.65894</td><td>0.051013</td><td>0.14315</td></tr><tr><td>3</td><td>Cambodia</td><td>0.009822</td><td>0.028878</td><td>0.90035</td><td>0.060951</td></tr><tr><td>3</td><td>Cameroon</td><td>0.009908</td><td>0.028354</td><td>0.90497</td><td>0.056772</td></tr><tr><td>1</td><td>Canada</td><td>0.92961</td><td>0.034214</td><td>0.010931</td><td>0.025244</td></tr><tr><td>2</td><td>Chile</td><td>0.18624</td><td>0.58983</td><td>0.067466</td><td>0.15646</td></tr><tr><td>4</td><td>China</td><td>0.019842</td><td>0.10456</td><td>0.078945</td><td>0.79666</td></tr><tr><td>2</td><td>Colombia</td><td>0.066882</td><td>0.7671</td><td>0.056491</td><td>0.10953</td></tr><tr><td>2</td><td>Costa Rica</td><td>0.16698</td><td>0.6328</td><td>0.060572</td><td>0.13965</td></tr><tr><td>1</td><td>Croatia</td><td>0.61489</td><td>0.18965</td><td>0.045698</td><td>0.14976</td></tr><tr><td>1</td><td>Cyprus</td><td>0.57037</td><td>0.14719</td><td>0.085695</td><td>0.19675</td></tr><tr><td>1</td><td>Czech Republic</td><td>0.91329</td><td>0.037491</td><td>0.013955</td><td>0.03526</td></tr><tr><td>1</td><td>Denmark</td><td>0.90361</td><td>0.042127</td><td>0.016682</td><td>0.037581</td></tr><tr><td>2</td><td>Dominican Republic</td><td>0.032441</td><td>0.67082</td><td>0.072181</td><td>0.22456</td></tr><tr><td>2</td><td>Ecuador</td><td>0.040697</td><td>0.79243</td><td>0.045605</td><td>0.12127</td></tr><tr><td>4</td><td>Egypt</td><td>0.04537</td><td>0.097315</td><td>0.16448</td><td>0.69284</td></tr><tr><td>2</td><td>El Salvador</td><td>0.03225</td><td>0.70707</td><td>0.054953</td><td>0.20573</td></tr><tr><td>1</td><td>Estonia</td><td>0.8311</td><td>0.091463</td><td>0.020293</td><td>0.057147</td></tr><tr><td>3</td><td>Ethiopia</td><td>0.050831</td><td>0.094557</td><td>0.63814</td><td>0.21647</td></tr><tr><td>1</td><td>Finland</td><td>0.88749</td><td>0.050062</td><td>0.019109</td><td>0.043343</td></tr><tr><td>1</td><td>France</td><td>0.94945</td><td>0.024991</td><td>0.007902</td><td>0.017653</td></tr><tr><td>3</td><td>Gambia</td><td>0.011694</td><td>0.037745</td><td>0.88941</td><td>0.061153</td></tr><tr><td>4</td><td>Georgia</td><td>0.038094</td><td>0.26718</td><td>0.053444</td><td>0.64128</td></tr><tr><td>1</td><td>Germany</td><td>0.94112</td><td>0.027184</td><td>0.009862</td><td>0.021834</td></tr><tr><td>1</td><td>Greece</td><td>0.60917</td><td>0.19229</td><td>0.051299</td><td>0.14724</td></tr><tr><td>2</td><td>Guatemala</td><td>0.052387</td><td>0.36066</td><td>0.31644</td><td>0.27051</td></tr></table></body></html>

(continued)

Table 1.9 (continued)   

<html><body><table><tr><td>4</td><td>Albania</td><td>0.28424</td><td>0.3116</td><td>0.072582</td><td>0.33157</td></tr><tr><td>3</td><td>Honduras</td><td>0.054833</td><td>0.31568</td><td>0.35575</td><td>0.27374</td></tr><tr><td>1</td><td>Hungary</td><td>0.90577</td><td>0.04526</td><td>0.013551</td><td>0.035419</td></tr><tr><td>1</td><td>Iceland</td><td>0.68922</td><td>0.12112</td><td>0.063855</td><td>0.12581</td></tr><tr><td>3</td><td>India</td><td>0.019765</td><td>0.051379</td><td>0.75142</td><td>0.17743</td></tr><tr><td>4</td><td>Indonesia</td><td>0.030765</td><td>0.093396</td><td>0.26095</td><td>0.61489</td></tr><tr><td>1</td><td>Ireland</td><td>0.96099</td><td>0.019763</td><td>0.005589</td><td>0.013659</td></tr><tr><td>1</td><td>Israel</td><td>0.61194</td><td>0.22343</td><td>0.041591</td><td>0.12304</td></tr><tr><td>1</td><td>Italy</td><td>0.86916</td><td>0.06992</td><td>0.017282</td><td>0.043638</td></tr><tr><td>2</td><td>Jamaica</td><td>0.038649</td><td>0.71492</td><td>0.050335</td><td>0.19609</td></tr><tr><td>1</td><td>Japan</td><td>0.90616</td><td>0.041501</td><td>0.016386</td><td>0.035957</td></tr><tr><td>4</td><td>Jordan</td><td>0.009514</td><td>0.034653</td><td>0.018891</td><td>0.93694</td></tr><tr><td>4</td><td>Kazakhstan</td><td>0.069722</td><td>0.12096</td><td>0.11663</td><td>0.69268</td></tr><tr><td>3</td><td>Kenya</td><td>0.013179</td><td>0.047963</td><td>0.85807</td><td>0.080792</td></tr><tr><td>1</td><td>Korea,Republic</td><td>0.85087</td><td>0.070721</td><td>0.021213</td><td>0.057195</td></tr><tr><td>4</td><td>Kyrgyzstan</td><td>0.03518</td><td>0.085876</td><td>0.22919</td><td>0.64975</td></tr><tr><td>1</td><td>Latvia</td><td>0.69365</td><td>0.16621</td><td>0.035339</td><td>0.1048</td></tr><tr><td>1</td><td>Lithuania</td><td>0.61283</td><td>0.2234</td><td>0.040208</td><td>0.12357</td></tr><tr><td>1</td><td>Luxembourg</td><td>0.58655</td><td>0.1471</td><td>0.084004</td><td>0.18234</td></tr><tr><td>3</td><td>Madagascar</td><td>0.010267</td><td>0.031539</td><td>0.90351</td><td>0.054684</td></tr><tr><td>3</td><td>Malawi</td><td>0.011209</td><td>0.029699</td><td>0.89214</td><td>0.066953</td></tr><tr><td>2</td><td>Malaysia</td><td>0.049112</td><td>0.71574</td><td>0.043663</td><td>0.19148</td></tr><tr><td>2</td><td>Mexico</td><td>0.079655</td><td>0.78924</td><td>0.03832</td><td>0.092786</td></tr><tr><td>4</td><td>Moldova, Republic</td><td>0.024628</td><td>0.095535</td><td>0.092677</td><td>0.78716</td></tr><tr><td>4</td><td>Mongolia</td><td>0.022514</td><td>0.068667</td><td>0.14794</td><td>0.76088</td></tr><tr><td>4</td><td>Morocco</td><td>0.048106</td><td>0.2518</td><td>0.17008</td><td>0.53001</td></tr><tr><td>3</td><td>Mozambique</td><td>0.014971</td><td>0.041838</td><td>0.87376</td><td>0.069428</td></tr><tr><td>2</td><td>Namibia</td><td>0.075055</td><td>0.54377</td><td>0.17888</td><td>0.20229</td></tr><tr><td>3</td><td>Nepal</td><td>0.017185</td><td>0.062621</td><td>0.81948</td><td>0.10071</td></tr><tr><td>1</td><td>Netherlands</td><td>0.9755</td><td>0.011725</td><td>0.003857</td><td>0.008913</td></tr><tr><td>1</td><td>New Zealand</td><td>0.84821</td><td>0.07761</td><td>0.023867</td><td>0.050316</td></tr><tr><td>3</td><td>Nicaragua</td><td>0.042242</td><td>0.23973</td><td>0.4443</td><td>0.27372</td></tr><tr><td>3</td><td>Niger</td><td>0.008523</td><td>0.022791</td><td>0.92278</td><td>0.045911</td></tr><tr><td>1</td><td>Norway</td><td>0.87596</td><td>0.055127</td><td>0.021828</td><td>0.047085</td></tr><tr><td>3</td><td>Pakistan</td><td>0.039064</td><td>0.080179</td><td>0.66428</td><td>0.21648</td></tr><tr><td>2</td><td>Panama</td><td>0.067097</td><td>0.81058</td><td>0.034832</td><td>0.087487</td></tr><tr><td>2</td><td>Paraguay</td><td>0.039361</td><td>0.83131</td><td>0.041076</td><td>0.088257</td></tr><tr><td>2</td><td>Peru</td><td>0.065334</td><td>0.46554</td><td>0.10782</td><td>0.3613</td></tr><tr><td>4</td><td>Philippines</td><td>0.029716</td><td>0.15589</td><td>0.21217</td><td>0.60223</td></tr></table></body></html>

(continued)

Table 1.9 (continued)   

<html><body><table><tr><td>4</td><td colspan="3">Albania</td><td>0.28424 0.3116</td><td></td><td>0.072582</td><td>0.33157</td></tr><tr><td>1</td><td colspan="2">Poland</td><td>0.76646</td><td>0.12003</td><td>0.028969</td><td></td><td>0.084542</td></tr><tr><td>1</td><td colspan="2">Portugal</td><td>0.71572</td><td>0.16448</td><td>0.033888</td><td></td><td>0.085911</td></tr><tr><td>1</td><td colspan="2">Romania</td><td>0.42991</td><td>0.22585</td><td>0.068687</td><td></td><td>0.27555</td></tr><tr><td>4</td><td colspan="2">Russian Federation</td><td>0.058523</td><td>0.27694</td><td>0.090317</td><td></td><td>0.57422</td></tr><tr><td>3</td><td colspan="2">Senegal</td><td>0.00987</td><td>0.026109</td><td>0.90456</td><td></td><td>0.059459</td></tr><tr><td>1</td><td colspan="2">Slovakia</td><td>0.82228</td><td>0.073597</td><td>0.027661</td><td></td><td>0.076458</td></tr><tr><td>1</td><td colspan="2">Slovenia</td><td>0.94376</td><td>0.027013</td><td>0.008162</td><td></td><td>0.02106</td></tr><tr><td>2</td><td colspan="2">South Africa</td><td>0.060062</td><td>0.42837</td><td>0.25723</td><td></td><td>0.25433</td></tr><tr><td>1</td><td colspan="2">Spain</td><td>0.96064</td><td>0.020311</td><td></td><td>0.005394</td><td>0.013656</td></tr><tr><td>4</td><td colspan="2">Sri Lanka</td><td>0.015491</td><td>0.078825</td><td></td><td>0.040186</td><td>0.8655</td></tr><tr><td>1</td><td colspan="2">Sweden</td><td>0.85291</td><td>0.064036</td><td>0.025878</td><td></td><td>0.057175</td></tr><tr><td>1</td><td colspan="2">Switzerland</td><td>0.91403</td><td>0.042608</td><td></td><td>0.013135</td><td>0.03023</td></tr><tr><td>3</td><td colspan="2">Tajikistan</td><td>0.040625</td><td>0.091683</td><td>0.48922</td><td></td><td>0.37848</td></tr><tr><td>3</td><td colspan="2">Tanzania</td><td>0.013224</td><td>0.032817</td><td></td><td>0.87388</td><td>0.080083</td></tr><tr><td>2</td><td colspan="2">Thailand</td><td>0.045151</td><td>0.57189</td><td></td><td>0.13572</td><td>0.24724</td></tr><tr><td>4</td><td colspan="2">Trinidad and Tobago</td><td>0.052559</td><td>0.26387</td><td></td><td>0.06346</td><td>0.62011</td></tr><tr><td>4</td><td colspan="3">Tunisia</td><td>0.049968</td><td>0.38186</td><td>0.056285</td><td>0.51189</td></tr><tr><td>4</td><td colspan="2">Turkey</td><td>0.050238</td><td>0.3103</td><td>0.058481</td><td></td><td>0.58098</td></tr><tr><td>3</td><td colspan="3">Uganda</td><td>0.002341</td><td>0.00716</td><td>0.97664</td><td>0.013863</td></tr><tr><td>4</td><td colspan="3">Ukraine</td><td>0.11937</td><td>0.15783</td><td>0.11911</td><td>0.60369</td></tr><tr><td>4</td><td colspan="3">United Arab Emirates</td><td>0.25172</td><td>0.18882</td><td>0.17458</td><td>0.38488</td></tr><tr><td>1</td><td colspan="3">Great Britain</td><td>0.91502</td><td>0.044743</td><td>0.012211</td><td>0.028022</td></tr><tr><td>1</td><td colspan="3">USA</td><td>0.69788</td><td>0.16177</td><td>0.047239</td><td>0.093105</td></tr><tr><td>1</td><td colspan="3">Uruguay</td><td>0.48376</td><td>0.33651</td><td>0.051159</td><td>0.12857</td></tr><tr><td>3</td><td colspan="3">Uzbekistan</td><td>0.038792 0.039499</td><td>0.098392</td><td>0.4853</td><td>0.37751</td></tr><tr><td>4</td><td colspan="3">Venezuela</td><td>0.027619</td><td>0.16547</td><td>0.19342</td><td>0.6016</td></tr><tr><td>4</td><td colspan="3">Vietnam</td><td>0.026225</td><td>0.082803</td><td>0.4324</td><td>0.45718</td></tr><tr><td>3</td><td colspan="3">Zambia</td><td>0.040152</td><td>0.093996</td><td>0.75376</td><td>0.12602</td></tr><tr><td>3 Number of a cluster</td><td colspan="3">Zimbabwe</td><td>1 2</td><td>0.099806</td><td>0.71609 3</td><td>0.14395 4</td></tr><tr><td colspan="7"></td></tr><tr><td colspan="2">Centers of clusters</td><td colspan="2">0.73332</td><td colspan="3">0.74677</td><td></td></tr><tr><td colspan="2">0.64429</td><td colspan="2">0.51657</td><td colspan="3">0.53844</td><td>0.74678</td></tr><tr><td colspan="2">0.29515</td><td colspan="2">0.19409</td><td colspan="3">0.23834</td><td>0.51317</td></tr><tr><td colspan="2">0.419 0.51726</td><td colspan="2">0.46924</td><td colspan="3">0.3707</td><td>0.22998 0.39482</td></tr><tr><td colspan="3"></td><td>9.4268</td><td colspan="3"></td><td></td></tr><tr><td colspan="3">Criterion 1</td><td></td><td colspan="3">Hi-Beni</td><td></td></tr><tr><td colspan="3"></td><td colspan="4"></td><td>0.39492</td></tr></table></body></html>

![](images/c3a3388bfca9119c7faa20c5aae8f6ffa275ba8282f07351f55b588cdb68dda7.jpg)  
Fig. 1.3 The dependence of the index Hi-Beni on the number of clusters K

should be given a priori. But usually it’s unknown for experts and the criteria of clustering quality such as Hi-Beni indicator and Dunn’s Index (DI) are monotonously decrease with number of clusters K. Therefore they can’t be used directly for determining optimal value of $\mathrm { K _ { o p t } }$ .

For determining the proper number of clusters in practice may be used the following approach. Assume the criterion of clustering be $\begin{array} { r } { E = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { N } w _ { k j } ^ { \beta } \Big \| c _ { j } - x _ { k } \Big \| ^ { 2 } } \end{array}$

Solve the clustering problem with criterion E with different $\mathbf { k }$ a	nd find $\boldsymbol { \mathrm { E } } ^ { * } ( \boldsymbol { \mathbf { k } } )$ .

When the following condition   
$\Delta \mathrm { E } ( \mathbf { k } ) \le \dot { \varepsilon }$ or $\Delta \mathrm { E } ( \mathrm { K } ) / \mathrm { E } ( \mathrm { K } ) \leq \delta .$ ,   
holds where d and έ are accepted thresholds then stop. Usually value d may be chosen as follows $\ S \in [ 0 . 1 \mathrm { - } 0 . 2 ]$ .

# 1.9 Conclusions

Cluster analysis includes a set of different classification algorithms. In general, whenever it is necessary to classify the “mountains” of information to suitable for further processing groups, cluster analysis is very useful and effective. Cluster analysis is needed for the classification of information, it can be used in a certain way to structure the variables and to find out which variables should be combined in the first place, and which should be considered separately.

A great advantage of the cluster analysis is that it allows to split the objects not only by one parameter but by a set of attributes as well. In addition, cluster analysis unlike most mathematical and statistical methods do not impose any restrictions on the form of these objects, and allows to treat a variety of raw data of almost arbitrary nature. This is important, for example, in the situation when indicators are diverse views, and it’s impossible to use traditional econometric approaches.

As any other method, cluster analysis has certain disadvantages and limitations: in particular, the content and the number of clusters depend on the criteria selected for partition. For the reduction of the original data set to a more compact form there may be some distortion, and characteristics of individual objects may be lost by replacing them with the characteristics of parameters of the cluster center.

The main disadvantage of the considered methods of fuzzy clustering C-means and Gustavson-Kessel is that they can only be used when the number of clusters K is known. But usually, the number of clusters is unknown, and visual observations in the multidimensional case simply don’t lead to a success.

# References

1. B. Durant, G. Smith, Cluster Analysis (Statistica, Moscow, 1987), 289 pp. (in Russian)   
2. V. Dyuk, A. Samoilenko, Data Mining (Peter Publication, Saint-Petersburg, 2001), 366 pp. (in Russian)   
3. Yu.P. Zaychenko, Fundamentals of Intellectual Systems Design (Kiev-Publishing house “Slovo”, 2004), 352 pp. (in Russian)   
4. Yu.P. Zaychenko, Fuzzy Models and Methods in Intellectual Systems (Kiev-Publishing House “Slovo”, 2008), 354 pp.   
5. R.R. Yager, D.P. Filev, Approximate clustering via the mountain method. IEEE Trans. Syst. Man Cybern 24, 1279–1284 (1994)   
6. R. Krishnapuram, J. Keller, Fuzzy and possibilistic clustering methods for computer vision. IEEE Trans. Fuzzy Syst. 1, 98–110 (1993)   
7. D.C. Park, I. Dagher, Gradient based fuzzy C-means (GBFCM) algorithm, in Proceedings of the IEEE International Conference On Neural Networks (1984), pp. 1626–1631   
8. Ye. Bodyanskiy, Ye. Gorshkov, I. Kokshenev, V. Kolodyazhniy, Robust recursive fuzzy clustering algorithms, in Proceedings of the East West Fuzzy Colloquium 2005 (HS, Zittau/ Goerlitz, 2005), pp. 301–308   
9. Ye. Bodyanskiy, Ye. Gorshkov, I. Kokshenev, V. Kolodyazhniy, Outlier resistant recursive fuzzy clustering algorithm, in Computational Intelligence: Theory and Applications, ed. by B. Reusch. Advances in Soft Computing, vol. 38 (Springer, Berlin, Heidelberg, 2006), pp. 647– 652   
10. Ye. Bodyanskiy, Computational Intelligence Techniques for Data Analysis. Lecture Notes in Informatics, V. P-72 (GI, Bonn, 2005), pp. 15–36   
11. Ye. Bodyanskiy, Ye. Gorshkov, I. Kokshenev, V. Kolodyazhniy, O. Shilo, Robust recursive fuzzy clustering-based segmentation of biomedical time series, in Proceedings of the 2006 International Symposium on Evolving Fuzzy Systems, Lancaster, UK (2006), pp. 101–105

# Chapter 2 Deep Neural Networks and Hybrid GMDH-Neuro-fuzzy Networks in Big Data Analysis

# 2.1 Introduction

One of the modern and efficient tools for big data analytics are deep networks [1–4]. At present time theory and practice of machine learning live over real “deep revolution” inspired by successful application of deep learning networks which represent the third generation of neural networks. In difference from classic neuron networks (second generation) 80–90 years of 20-th century new training paradigms allowed to get rid of some problems which hindered successful application of traditional neural networks. Neural networks trained with deep learning algorithms not only overcame by accuracy best alternative approaches but in some cases displayed understanding of sense of input information (in image recognition, text analysis and other problems).

The most successful industrial systems of computer vision and speech recognition are built on deep networks and giants of IT-industry such as Apple, Google, Facebook created large research teams dealing with deep learning. Term “deep network” means big neural network with many hidden layers of neurons [1, 2]. Deep learning represents a set of methods and techniques for training complex neural networks (NN) with many layers. For such networks traditional machine learning algorithms developed for conventional NN had become inadequate due to some drawbacks in particular problem of decay and explosion of gradient in back propagation algorithm [3, 4]. Therefore large dimensions of modern neural networks with applications for 3-D images recognition and automatic speech recognition demanded development of new efficient training methods called deep learning.

But the most serious drawback of deep learning networks is a problem of determination of its proper structure, how to choose adequate number of their layers.

To the present time the problem of choice of number of DN layers is based on knowledge and experience of an expert and refers to the art. The adequate solution to this problem is connected with new class of hybrid neural networks—so-called

GMDH-neo-fuzzy networks representing a combination of self-organization method GMDH and fuzzy neural networks. Due to principle of self-organization and small number of tuning parameters GMDH enables to simplify and accelerate the training of DN. In this chapter in the Sects. 2.8–2.10 several variants of this class hybrid networks are considered and algorithms of their structure synthesis based on GMDH are suggested and analyzed. Training algorithms for hybrid deep networks are free from problem of gradient vanishing or explosion and besides the application of GMDH enables to reduce dimensionality of training DN and accelerate the convergence of training DN and by this solve some problems of BD.

# 2.2 Autoassociators. Autoencoders

Implementation of deep learning has led to development of the special learning structure based on application of so-called autoassociators [3].

The main task of autoassociator is to obtain at the output the most accurate mapping of the input vector (pattern).

The first autoassociator (AA) was neo-cognitron suggested by Fukushima. Its schema is presented in Fig. 2.1.

There are exist two types of AA: generating and synthesizing ones.

As the first type are used restricted Boltzmann Machine, (RBM), as the second type—autoencoders (AE) are used.

![](images/231fe238ae8825c7d106c1e53be2450485eac23ad2d576a07163738f06405f83.jpg)  
Fig. 2.1 Neo-cognitron of Fukushima

# Autoencoder

One of the first deep learning algorithms is auto-encoder. It’s an algorithm of non-supervised learning whose output vector equals to input vector [5]. One of the most spread auto-encoder architectures is feedforward neural network containing input, hidden and output layers.

Unlike perceptron output autoencoder layer has the same number of neurons as the input layer. The data at the input layer are compressed and restored so the hidden features are retrieved.

The goal of autoencoder is to attain that NN output to be maximal close to input vector. That to make non-trivial solution of this problem the special constraints are set on network topology:

(1) the number neurons of hidden layer should be less than the number of input neurons;   
(2) the number of non-active neurons in hidden layer should significantly exceed the number of active neurons.

The first constraint enable to compress data while transfer input signal to network output. Such compression is possible if there are hidden interconnections in data, correlation among features. The second constraint—demand of great number of non-active neurons allows to obtain non-trivial results even when the number of neurons in hidden layer excesses the dimensionality of input data/ In other words the goal of autoencoder is to obtain the most significant features.

Let consider a neuron be active if its activation is close to one, and non-active its activation is close to zero. These constraints force autoencoder to search correlations and generalization in input data and perform its compression.

By this the network automatically learns to extract in input data general features which are encoded in network weights. Its necessary that mean value of transfer function of each hidden neuron to get the value maximal close to a given sparsity parameter about $\mathrm { s } = 0 . 0 5$ for this in each neuron of hidden layer was introduced sparsity parameter $p$ :

$$
\hat { \rho } _ { J } = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \Big [ a _ { j } ^ { ( 2 ) } \Big ( x ^ { ( i ) } \Big ) \Big ] .
$$

It’s necessary that mean value of transfer function of each hidden neuron takes most close value to $p$ :

$$
{ \hat { \rho } } _ { J } = p .
$$

Introduce a penalty function:

$$
S = \sum _ { j = 1 } ^ { S _ { 2 } } K L ( \rho | \hat { \rho } _ { J } ) ,
$$

where

$$
K L ( \rho | \hat { \rho } _ { J } ) = p \log \frac { \rho } { \hat { \rho } _ { J } } + ( 1 - \rho ) \log \frac { 1 - \rho } { 1 - \hat { \rho } _ { J } }
$$

Remarkable property of the penalty function is its derivative:

$$
\frac { \partial K L ( \rho | \hat { \rho } _ { J } ) } { \partial \rho _ { j } } { = } - \frac { \rho } { \hat { \rho } _ { J } } + \frac { 1 - \rho } { 1 - \hat { \rho } _ { J } }
$$

The example of encoder is presented in Fig. 2.2. Autoencoder tends to build function $\mathbf { h } ( \mathbf { x } ) = \mathbf { x }$ . In other words it tends to find such approximation of this function that the neural network output be equal to input vector. That to make the solution of this problem non-trivial the number of hidden layer neurons should be less than the dimensionality of input data (see Fig. 2.2).

This allow to obtain data compressing by transfer of input signal to output. For example, if input vector presents a set of brightness levels of an image $1 0 \times 1 0$ pixels (all in all 100 features), the number of hidden later neurons is 50, the network is forced to learn to compress an image.

Really, the demand $\mathbf { h } ( \mathbf { x } ) = \mathbf { x }$ means that on the base of activation levels of 50 neurons the output layer should restore 100 pixels of initial image. Such compression is possible if there is hidden interconnections, correlation in features, and in general a certain structure in data. In this way functions of autoencoder very resembles Principal Components Algorithm (PCA) in the sense of cutting dimensionality of input data.

![](images/38da5abf6529ac64de5363cbba53b43e9398dd26cff18fcd4b31796197a27179.jpg)  
Fig. 2.2 Architecture of autoencoder

![](images/79fe63cd36232b9de2ea7c145434d5e9c85af1b56ba05e7584cdcff8a5ca3106.jpg)  
Fig. 2.3 Structure of denoising autoencoder

Later as sparsity idea has been stated so-called the sparse Autoencoder appeared and got wide application [5, 6]. Sparse autoencoder is an autoencoder with number of hidden neurons much greater than the dimensionality of input vector. Sparse activation means that the number of non-active neurons in the hidden layer exceeds significantly the number of active ones. If describe sparsity informal then a neuron is considered active if its transfer function is about 1. If the sigmoidal transfer function is used then for non-active neuron its value should be close to 0 (for tanh—close to $^ { - 1 }$ ).

There is a variant of autoencoder called denoising autoencoder [5]. It’s the same autoencoder but its training is specific. While training randomly distorted data (several input values are changed to 0) is fed into input. By this for comparison with output are shown non-distorted values. In this way autoencoder is compelled to restore distorted input data (Fig. 2.3).

Artificial feed-forward neural networks (ANN) with large number of layers are badly trained by conventional methods which are good for ANN with small number of hidden layers due to the problem of decaying gradient [4], the farther is layer from output the less are the values of gradient norm.

This problem may be solved by correctly chosen initial weights. In this case it doesn’t need to change them significantly during the training process.

# 2.3 Boltzmann Machines (BM)

# 2.3.1 Energetic Models

Boltzmann machines represent a special form of log-linear Markov’s field (MRF), i.e. its energy function is linear by parameters. Therefore let’s consider first energy-based models (EBM). EBM connect scalar energy with each configuration of variables. The training corresponds to modification of energy function so that its form obtain the desired properties. For example, we would like that the desired configurations have low energy. Probabilistic models energy-based determine the probability distribution so:

$$
p ( x ) = { \frac { e ^ { - E ( x ) } } { z } }
$$

Normalizing multiplier $Z$ is called statistical sum by analogy with physical systems

$$
Z = \sum _ { x } e ^ { - E ( x ) }
$$

Energy-based model may be explored by using stochastic gradient descent at the empirical negative-logarithmic probability function of data.

As for logistic regression we first determine logarithmic-likelihood function and then loss function as negative logarithmic-likelihood function.

$$
l ( \theta , D ) = \frac { 1 } { N } \sum _ { x ^ { ( i ) } } \log p ( x ^ { ( i ) } )
$$

$$
l ( \theta , D ) = - L ( \theta , D )
$$

# 2.3.2 Restricted Boltzmann Machine (RBM)

The history of developing RBM begun from recurrent neural (RNN). Representing the networks with backfeed which are difficult to train. Therefore scientists started to invent more restricted recurrent models for which more simple training algorithms may be applied. One of such models was Hopfield network, Hopfield introduced also energy concept after comparing neurodynamics with thermodynamics.

The next step was usual Boltzmann machines which differ from Hopfield network by stochastic nature and its neurons are divided into two groups: which describe hidden and visible states.

The restricted Boltzmann machines differs from usual one that there are no connections among neurons of the same layer (similar to hidden Markov models).

In Fig. 2.4 the structure of RBM is presented.

The property of this model is that at given state of one group of neurons the states of another group of neurons would be independent each of other. Now consider some theoretical results wherein this property plays a key role.

RBM interpretation. RBM are interpreted like hidden Markov models. They have a layer of states which we can observe (visible neurons) and a layer of states

Fig. 2.4 RBM structure

![](images/90d76925ecd2054198534d8c077a5ada75ed31e109e914fdea128de6257b019c.jpg)

which are hidden and we can’t see them (hidden neuron). But we can make probabilistic inference concerning hidden states basing on visible ones. After training such model we also get opportunity to make conclusions about visible states knowing hidden ones (using Bayes theorem) and by this generate data from that probabilistic distribution on which model was trained.

Therefore we can formulate RBM training goal: it’s necessary to tune model parameters so that restored vector would be maximal close to original.

By restored vector we imply vector obtained by probabilistic inference from visible states.

# RBM Algorithm

Often we are not interested to observe completely the instance $\mathrm { \Delta X }$ or we want to introduce some not-observed variables that to increase the model descriptive force. So let consider visible part of model (denote by X) and invisible part denoted as h. Then we can write:

$$
P ( x ) = \sum _ { h } P ( x , h ) = \sum _ { h } { \frac { e ^ { - E ( x , h ) } } { Z } } .
$$

Energy function $\mathbf { E ( v , h ) }$ of restricted Boltzmann machine is presented so:

$$
E ( \nu , h ) = - b ^ { \prime } \nu - c ^ { \prime } h - h ^ { \prime } W \nu
$$

where $\mathrm { ~ w ~ }$ are weights connecting visible and non-visible neurons, b, c—are biases of visible and hidden layers correspondingly.

This is transferred directly to the following formula for free energy:

$$
\mathcal { F } ( \nu ) = - b ^ { \prime } \nu - \sum _ { i } \log \sum _ { h _ { i } } e ^ { h _ { i } ( c _ { i } + W _ { i } \nu ) } .
$$

Owing to specific RBM structure visible and non-visible are conditionally dependent each of other. Using this property we can write down:

$$
\begin{array} { l } { p ( h | \nu ) = \displaystyle \prod _ { i } p ( h _ { i } | \nu ) } \\ { p ( \nu | h ) = \displaystyle \prod _ { j } p ( \nu _ { j } | h ) . } \end{array}
$$

The network consists of stochastic neurons taking 0 or 1 (where $\nu _ { j }$ and $h _ { i } \in \{ 0 , 1 \} ,$ ). From formulas (2.10) and (2.11) obtain the probabilistic variant of usual neuron activation

$$
p ( h = 1 | \nu , W , b _ { h } ) = \sigma ( W * \nu + b _ { h } ) ,
$$

where v—is neuron input, W is weight vector (matrix 0, $ { \mathbf { b } } _ { \mathrm { h } }$ -bias, $\sigma ( \mathbf { x } )$ —sigmoidal function.

This is basic variant for binary inputs (Bernoulli-Bernoulli RBM), there are also modifications for real inputs (Gaussian-Bernoulli RBM и дp.).

Algorithm of RBM runs as follows.

1. Set initial values for input variables $\mathbf { V } \colon = \mathbf { X }$   
2. Compute probabilities $\mathtt { p _ { h } }$ of change neuron states of the second layer (non-visible) $p _ { h } = \sigma ( \nu * W + b _ { \nu } )$ ;

where W—weight matrix, $b _ { \nu }$ —is bias vector of the first layer, $\sigma$ —activation function (sigmoid).

Store the old values of input neurons $\mathbf { \nabla } \mathbf { V } ^ { \prime } \colon = \mathbf { \nabla } \mathbf { V }$ .

3. Determine the states of the second layer neurons $\mathbf { h }$ , assign to neurons states 0 or 1 with probability ph 4. Compute the probabilities $p _ { \nu }$ of change states of the first layer neurons

$$
p _ { \nu } : = \sigma \big ( h \ast W ^ { T } + b _ { h } \big ) ,
$$

where $b _ { h }$ —bias vector of the second layer, $\sigma$ —activation function (sigmoid), and assign neurons states 1 with probabilities $\mathtt { p _ { v } }$ (or 0 with probabilities $1 - { \mathfrak { p } } _ { \mathrm { v } } )$

5. If $\mathbf { v } \neq \mathbf { v } ^ { \prime }$ then repeat from step 2. Otherwise go to the next step.   
6. Release result v.   
7. End.

# 2.4 Training Method Contrastive Divergence (CD)

RBM training algorithm is called contrastive divergence and represent itself the modified gradient descent. As the estimation function to be optimized likelihood function $\mathrm { ~ L ~ }$ is used. Let search its maximum. Likelihood Function L for parameters $( \mathbb { W } , b _ { \nu } , b _ { h } )$ and pattern v is determined under given values of parameters W, h as

$$
\begin{array} { c } { { p ( \nu , h ) = \displaystyle \frac { 1 } { z } e ^ { - E ( \nu , h ) } } } \\ { { { } } } \\ { { L ( \theta | \nu ) = p ( \nu | \theta ) } } \\ { { { } } } \\ { { { } { \displaystyle { { \cal L } ( W , b _ { \nu } , b _ { h } | \nu ) = p ( \nu | W , b _ { \nu } , b _ { h } ) } } } } \end{array}
$$

For simplicity of computations we’ll use logarithm:

$$
\begin{array} { l } { { \displaystyle \ln { \cal L } ( \theta | \nu ) = \ln p ( \theta | \nu ) = \ln \frac { 1 } { z } \sum _ { h } \exp ( - E ( \nu , h ) ) = \ln \sum _ { h } \exp ( - E ( \nu , h ) ) } } \\ { { \displaystyle ~ - \ln \sum _ { \nu , h } \exp ( - E ( \nu , h ) ) } } \end{array}
$$

Under great number of visible and hidden neurons numerical methods like gradient ascend are usually applied for finding maximum this function logarithmic likelihood. Maximization of likelihood function is equivalent to minimization of weights as the weights arte linearly connected with energy function E (see (2.16))

$$
E ( \nu , h ) = - ( b _ { \nu } * \nu + b _ { h } * h + \nu * h * W )
$$

As it follows from (2.16) minimization of weights leads to minimization of energy function E. At each iteration of gradient ascend algorithm parameters are adjusted in dependence of likelihood function whose derivatives are presented below:

$$
\begin{array} { l } { \displaystyle \frac { \partial \ln { \cal L } ( \theta | \nu ) } { \partial \theta } = \frac { \partial } { \partial \theta } \left( \ln \sum _ { h } e ^ { - E ( \nu , h ) } \right) - \frac { \partial } { \partial \theta } \left( l n \sum _ { \nu , h } e ^ { - E ( \nu , h ) } \right) } \\ { \displaystyle \qquad = - \frac { 1 } { \sum _ { h } e ^ { - E ( \nu , h ) } } \sum _ { h } e ^ { - E ( \nu , h ) } \frac { \partial E ( \nu , h ) } { \partial \theta } + \frac { 1 } { \sum _ { h , \nu } e ^ { - E ( \nu , h ) } } \sum _ { h , \nu } e ^ { - E ( \nu , h ) } \frac { \partial E ( \nu , h ) } { \partial \theta } } \\ { \displaystyle \qquad = - \sum _ { h } p ( h | \nu ) \frac { \partial E ( \nu , h ) } { \partial \theta } + \sum _ { h , \nu } p ( h , \nu ) \frac { \partial E ( \nu , h ) } { \partial \theta } . } \end{array}
$$

Gradient of this function may be divided on three parts as follows:

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial I n L ( { \boldsymbol W } , { \boldsymbol b } _ { \nu } , { \boldsymbol b } _ { h } | { \boldsymbol \nu } ) } { \partial W } = \nabla { \boldsymbol W } = ( \nu * h ) _ { d a t a } - ( \nu * h ) _ { m o d e l } } \\ { \displaystyle \frac { \partial I n L ( { \boldsymbol W } , { \boldsymbol b } _ { \nu } , { \boldsymbol b } _ { h } | { \boldsymbol \nu } ) } { \partial b _ { \nu } } = \nabla { \boldsymbol b } _ { \nu } = ( \nu ) _ { d a t a } - ( \nu ) _ { m o d e l } } \\ { \displaystyle \frac { \partial I n L ( { \boldsymbol W } , { \boldsymbol b } _ { \nu } , { \boldsymbol b } _ { h } | { \boldsymbol \nu } ) } { \partial b _ { h } } = \nabla b _ { h } = ( h ) _ { d a t a } - ( h ) _ { m o d e l } } \end{array} \right.
$$

where ( ) data—is values of layer states at the initial state of RBM, ( ) model—is mathematical expectation of layer states.

Mathematical expectation of neuron states are calculated by so-called sampling i.e. ( ) model is layer state after some iterations (at practice for algorithm work it’s enough one step of sampling (one iteration). The weights are changed as follows

$$
\left\{ \begin{array} { l l } { W : = \varepsilon \ast \left( \nabla W + \mu \ast \Delta W \right) } \\ { b _ { \nu } : = \varepsilon \ast \left( \nabla b _ { \nu } + \mu \ast \Delta b _ { \nu } \right) , } \\ { b _ { h } : = \varepsilon \ast \left( \nabla b _ { h } + \mu \ast \Delta b _ { h } \right) } \end{array} \right.
$$

where $\mu$ is so-called moment parameter, e is training speed, DW; $\Delta { b _ { \nu } } \Delta { b _ { h } }$ —are parameters change at the previous iteration.

As stop criterion we’ll use MSE between input and output of BRM— $E ( \nu _ { 0 } , \nu _ { k } )$ , this value should decrease to the established threshold Emin.

Training algorithm consists of the following steps:

1. Initialize (by zeros) weight matrix W and bias vectors $b _ { \nu } , b ; _ { h }$   
2. Choose random mini-batch out of all training set (mini-batch) X;   
3. For all the examples in mini-batch assign initial values to first layer $\mathbf { V } \colon = \mathbf { X }$ .   
4. Execute $\mathbf { k }$ cycles in network, determine initial and final states of layers cлoёв   
$\mathbf { \Omega } _ { \nu _ { 0 } , h _ { 0 } }$ , $\nu _ { k }$ , $h _ { k }$ , (гдe k—пapaмeтp)   
5. Compute gradient according to (2.18) and adjust weights by (2.18).   
6. Calculate network MSE E;   
7. if $\mathbf { E } < \mathbf { E } \mathbf { m i n }$ then go to 8, otherwise go to 2;   
8. end.

# 2.4.1 Training Algorithm Contrastive Divergence (CD-k)

This algorithm was developed by professor Hinton in 2002, and it differs by simplicity. The main idea lies in that the mathematical expectation are replaced by certain values The concept of sampling is introduced (Gibbs sampling).

Algorithm CD-k runs as follows:

1. States of visible neurons are set equal to input pattern;   
2. The probabilities of hidden layer neurons are calculated;   
3. Each neuron of hidden layer the state “1” is assigned with probability equal to its current state;   
4. The probabilities of states of visible layer are determined basing at the states of hidden layer;   
5. If number of current iteration is less than $\mathbf { k }$ , return to step 2;   
6. The probabilities neuron states of hidden layer are obtained The work of corresponding algorithm is presented in Fig. 2.5.   
The longer we make sampling the more accurate works CD-algorithm.

![](images/cd39109cf2fbf467913004f08fe60193518c90a0aa59291b407e470bdebe055b.jpg)  
Fig. 2.5 Training algorithm CD-k

# 2.4.2 Example

Consider the implementation of above presented model. At the start in the memory are stored several images of Latin letters. After then to system are shown another alike patterns distorted and using them the original patterns should be restored. Training set is presented below

A B C D E F G H 1 J K L M N 。 P Q R s T U V W X Y Z

Results of algorithm work

![](images/584a53df1ca89d1bde21e9856b5ddd60ae884dd36637f4034a9a946f861eb933.jpg)

Flow charts of training error are presented in Fig. 2.6a, b in Fig. 2.7 weight maps of hidden layer are presented.

V W W W W W W W 福1 V V W w W W w w w w w X XX X X X 区 Y Y Y Y YX X X X X X Y Y T Y Y Y YZ Z Z Z Z jZ Z Z Z Z Z Z Z 7约 N N N N ○ O o C O 0 2 O OH N N N N N □ 。 Q 0 。 。 Q 。 GP P P P P D P P Q Q Q Q Q CP P P P P F F P P Q Q Q Q Q QQ Q R R R R R R R R R S S SQ Q Q R R R R R R R R R S S BS S S S S S 工 T T T T T T TBbIxOA S S B B S B T T Y T TU U U U U U U 0 T T V0 H D U U U U D V V V V V V

# 2.5 Stacked Autoassociators Networks

# 2.5.1 Stacked Autoencoder (SAE)

For retrieving high-level abstractions out of input set autoassociators are stacked in network. In Fig. 2.8 the structure schema of stacked autoencoder is shown which in a whole represent deep learning network with weights initialized by stacked Autoencoder.

# 2.5.2 Stacked RBM

In Fig. 2.9 structure schema of stacked restricted Boltzmann (SRBM) and neural network are presented which represents Deep neural network with weights initialized by SRBM.

![](images/121e46f305afb18f24a63fe6616755d4ec8dad76eb2a59a5bc909ef4a6b7a736.jpg)  
Fig. 2.6 a Flow chart of error versus number of iterations (1–136). b Flow chart of error versus number of iterations (137–272)   
Fig. 2.7 Weights map by number of the second (hidden layer)

T 拉 E W W 美 P 国 2 1 线 石 E W 5 R 2 G 5 2 国 E 成 H 中 医 汉 中 出 V 慧 国 医 国 Y 5 1 中 H W 交 运 8 医 1 国 W d 0 M 色 图 J 经 V 阳 国 过 万 我 R 8 半 南 0 8 起 工 江 E √ 网 区 R 1 3 M 总 G 商 S L C + 國 E 甘 西 H 江 区 陵 U 1 建 医 豆 8 1 0 集 售 A 1 始 营 S S 购 G 电 国 ① 请 3 T M W 运 日 从 R 使 8 K 谐 东 区 Y 1 M 厦 福 9 H Y 队 R 4 1 S 5 4 G G 国 建 D 1 税 G 起 Q 5 R T 虹 内 S C 爱 始 1 口 品 子 迎 B M 区 1 园 3 1 R 5 E 江 药 R 医 U 盛 日 1 福 惠 压 银 H 国 C 日 U M 101 13 心 日 5 0 彩 9 O 白 E X 家 江 B 1 厦 第 经 G H 国 出 非 上 F y 福 出 其 9 南 8 B W # 6 5 1 T T 区 V 心 8 H J 东 M L R E 建 T 5 U 京 9 E 8 常 T 第 E

![](images/ded7b82523c026f3a3f4ca9b8b8916aed1c382b8decd317decde25ab7a06977e.jpg)  
Fig. 2.8 Deep network with SAE structure

![](images/3b0de268f4b079f5d1f7b483c0111d8630e28f5ac31927021a9baa34f7742e94.jpg)  
Fig. 2.9 Structure of DN SRBM

Structures of deep networks are shown just in such a way underlining that information is retrieved upward (from bottom to top).

# 2.6 Deep Networks Learning

Process of learning deep networks is split in two stages [5–7]:

1. Pretraining;   
2. Weights fine-tuning.

# 2.6.1 Deep Network Pretraining

At the first stage auto-associative network (SAE или SRBM) is non-supervised trained at an array of not-marked data after that neurons of MLP hidden layer are initialized with weights obtained after training. In Fig. 2.9 this process of training and transfer is shown. After training of the first AE/RBM weights of hidden layer neurons become inputs of the second layer and so on. By this more and more general information about structure of data (line, contour etc.) is retrieved out of data.

Let’s consider the pretraining procedure more detail. Pretraining represents the following procedure: we take pairs of neighbor layers of deep learning network beginning from the first layer and construct from this pair autoencoder, by adding output layer identical to input one. This procedure is repeated sequentially for all network layers. This procedure may be described as follows.

1. Load a training data set X0;   
2. Determine a network parameters—a number $( \Nu )$ and size of layers;   
3. Set the number of current layer $\dot { \mathbf { i } } = 0$ ;   
4. Build autoencoder for layers i, $\mathrm { i } + 1$ ;   
5. Train autoencoder at the set $X _ { \mathrm { i } }$ ;   
6. Take away auxiliary (output) layer of autoencoder;   
7. Preserve connection weights of layers i, $\dot { \mathrm { ~ i ~ } } + \mathrm { ~ 1 ~ }$ ;   
8. If there are still pair of layers to be processed $( \mathrm { i } < \Nu - 2 ) ,$ ), then go to the next   
step, otherwise go to step 10.   
9. Generate data set $\mathbf { X } _ { \mathrm { i + 1 } }$ for next autoencoder for this propagate through pair of   
layers i, $\dot { \mathrm { ~ i ~ } } + 1$ data set Xi, and go to step 3;   
10. End of work.

After this procedure the network is trained as a whole by one of the gradient methods.

Besides, for deep networks with number of hidden layers more than three D. Hinton suggested to perform fine tuning also in two stages. At the first stage train only two upper layers and only after than to train the whole network. It worth to note that with non-supervised learning SRBM gives less stable results than SAE.

# 2.6.2 Fine-Tuning

At the second stage fine-tuning of MLP weights (training with teacher) is performed by known methods. It was proved practically that such initialization set weights of neurons of MLP hidden layers in the region of global minimum and next fine-tuning is performed for very short time. Fine-tuning is a process of weights small changes for improving or optimization of results. As a rule it is aimed to increase process efficiency. Fine-tuning may be executed by a number of methods which are dependent on optimized processes which include gradient methods of first order, gradient methods of second order: Newton and quasi-Newton methods and other.

# 2.7 Deep Learning Regularization

In problem of neural networks training exists two types of errors: (1) so-called training error $\ \varepsilon _ { t r }$ and generalization error $\varepsilon _ { g e n }$ . Training error is the error at the training sample while generalization error is error at test sample. These two errors are functions of the number of training iterations $\mathfrak { n }$ and display different behavior: $\varepsilon _ { t r }$ monotonous decrease with n, while generalization error $\varepsilon _ { g e n }$ first decrease then attains minimum and then begins to rise with increase of n (this phenomenon is called overfitting). The goal of training lies in minimization of generalization error.

Regularization is any modification of training algorithm aimed to decrease generalization error at the expense of certain increase of training error. Regularization refers to one of the central problems in machine learning competing by its significance with problem of optimization.

Due to the theorem of costless breakfast the best algorithm of machine training doesn’t exists in particularly, there is no the best method of regularization.

Instead we need choose the regularization form which fits well to our problem to be solved. Philosophy of deep learning in a whole lies therein wide range of problems (such as all the intelligent problems) can be efficiently solved with application of general forms (methods) of regularization. Consider the most popular regularization methods and their models.

# 2.7.1 $\mathbf { { { L } _ { p } } }$ -Regularization of Linear Regression

Consider the classic linear regression model

$$
t = \sum _ { j = 1 } ^ { d } w _ { j } x ( j ) + \varepsilon , \varepsilon \sim N \big ( 0 , \sigma ^ { 2 } \big ) .
$$

![](images/672417a8bb1f551f4d33e185020c684f814de3495e4b2e246dae52382fabf34e.jpg)  
Fig. 2.10 Graffic illustration of linear regression

Search of weights $w$ by maximization of likelihood function of sample in this model is equivalent to LSM method:

$$
\sum _ { n = 1 } ^ { N } [ t _ { n } - \sum _ { j = 1 } ^ { d } w _ { j } x _ { n } ] ^ { 2 } = \| t - w _ { 1 } x _ { 1 } - \cdot \cdot \cdot - w _ { d } x _ { d } \| ^ { 2 } = \| t - X w \| ^ { 2 } {  } \operatorname* { m i n } _ { w } .
$$

where $x _ { i } \in R ^ { N }$ is a value of $i \cdot$ -th feature for all objects in the sample $X = [ \pmb { x } _ { 1 } , . . . , \pmb { x } _ { d } ]$ . Note that introduced here denotation $\mathbf { \lambda } _ { \pmb { x } _ { i } }$ differs from standard when by $x i$ is implied $i \cdot$ -th sample object. Here and further the sample is assumed normalized.

Problem (2.21) has simple geometric interpretation—search a projection of vector t onto hyperplane with direction vectors $[ x 1 , x 2 , . . . , x d ]$ (see Fig. 2.10). This problem can be solved analytically:

$$
\boldsymbol { w } = \left( X ^ { T } X \right) ^ { - 1 } \boldsymbol { X } ^ { T } t , t _ { p r } = X \boldsymbol { w } = \boldsymbol { X } \big ( X ^ { T } \boldsymbol { X } \big ) ^ { - 1 } \boldsymbol { X } ^ { T } t .
$$

The solution for $w$ corresponds to pseudo-solution of system of linear equations $X \pmb { w } = \pmb { t }$ .

That to prevent to overfitting of linear regression it’s necessary to set constraints on the variability of decision. This may be done by introduce of constraint on the norm of weight vector $\pmb { w }$ :

$$
\begin{array} { c } { \left\| t - X w \right\| ^ { 2 } \longrightarrow \underset { w } { \operatorname* { m i n } } , } \\ { \left\| w \right\| _ { L _ { p } } ^ { p } \le b . } \end{array}
$$

Traditionally instead of solving problem (2.23) the problem of optimization of the following regularized functional is considered

$$
\Vert t - X w \Vert ^ { 2 } + \lambda \Vert w \Vert _ { L _ { p } } ^ { p } \longrightarrow \operatorname* { m i n } _ { w } , \lambda \ge 0 .
$$

It’s easy to show that optimization problems (2.23), (2.24) и (2.25) are equivalent under condition

$p \geq 1$ , i.e. when all the considered functions are convex.

$$
\mathrm { I n t r o d u c e \underline { { L a g r a n g i a n } } } L ( w ; \lambda ) = \left. t - X w \right. ^ { 2 } + \lambda \Bigl ( \left. w \right. _ { L _ { p } } ^ { p } - b \Bigr ) .
$$

Then due to variant Kuhn-Tacker theorem for convex functions necessary and sufficient conditions for existence of solution $\hat { w }$ in the problem (2.23), (2.24) is existence of $\lambda \geq 0$ , for which the following conditions will be true:

1. Principle of minimum: $L ( \hat { w } ; \lambda ) = m i n _ { w } L ( w ; \lambda )$ , that is, $\nabla \mathrm { L } ( \mathrm { w } , \lambda ) = 0$ :   
2. Condition of complementary non-fixedness: $\lambda \Big ( \| w \| _ { L _ { p } } ^ { p } - b \Big ) = 0$ :

Note that for sufficiency of 1 and 2 it’s demanded also the fulfillment of so-called “Slater condition”, i.e. existence such solution ${ \pmb w }$ : $\| \pmb { w } \| _ { L _ { p } } ^ { p } < b$ :

It’s clear that this condition holds when $b > 0$ .

Optimization problem (2.25) is equivalent to condition 1. Consider the condition 2. This condition is equivalent to occurrence one of two events: $\lambda = 0$ or $\| \pmb { w } \| _ { L _ { p } } ^ { p } = b$ :

If $\lambda = 0$ , then optimal point $\hat { w }$ lies inside the region $\| \pmb { w } \| _ { L _ { p } } ^ { p } < b$ : Consequently constraint $\| \pmb { w } \| _ { L _ { p } } ^ { p } \le b$ becomes obvious and optimization problem (2.23) transforms into optimization problem without constraints that is equivalent to the problem (2.25) under $\lambda = 0$ : ∇

Let be $\lambda > 0$ ; $\| \pmb { w } \| _ { L _ { p } } ^ { p } = b$ : The accomplishment of this constraint is easy to obtain in the problem (2.25), just simply denote by $b$ the value of vector w norm, optimal referring for problem (2.25).

Consider optimal solution of problem (2.23), (2.24) under different $p$ . It’s can be shown that in case of $p \ \leq \ 1$ optimal solution has sparsity property, i.e. a portion of weights are exactly equal to zero. In case $p > 1$ strictly zero weights in optimal solution are practically impossible. Note that situation $p = 1$ is distinguished, as in this case optimized functional (2.25) is convex and optimal solution is sparse.

Method of adjustment weights in linear regression by solving problem (2.24) or (2.25) with $L 1$ -norm was called LASSO (abbr. from Least Absolute Shrinkage and Selection Operator).

# 2.7.2 Early Stopping

Early stopping assumes the division or training process on stages of indeed training and validation. In stead of training network on the restricted number of iterations we train network until its performance begins to fall. In fact this prevent to network to

![](images/54faac519bf3442fb35dd0305e0d3c96d78987eb05bdf2939ed1ae43283828d4.jpg)  
Fig. 2.11 Possible stop points

![](images/4bb96908b983093f5ae6954f257cf3788476d3bee87216fca02b3a3d4ef7d2da.jpg)  
Fig. 2.12 Possible ways of network behavior

simple remembering patterns. Below in Fig. 2.11 two possible stop points are shown:

Figure 2.12 shows the performance and degree of overfitting after stop at these points (a, b):

Regularization penalize network for use of complicated structure. Complexity in this case is measured by network size and weights. It established by addition of interval to loss function which is tied to size and weight.

$$
\epsilon = \beta \sum _ { p = 1 } ^ { P _ { t } } { \left( t _ { p } - O _ { p } \right) } ^ { 2 } + \alpha \sum _ { j = 1 } ^ { n } \nu _ { j } ^ { 2 }
$$

where n—is a number of loads (weights) in a neural network.

The parameters $\textsf { \textsf { a } }$ and $\beta$ control a level after which under-fitting or overfitting take place. The corresponding values for them can be found by optimization or Bayes analysis (Fig. 2.13).

![](images/2a592dffa745461369a7d6776b89983f8230153e444a4f28c4c939ed5ec8a804.jpg)  
Fig. 2.13 Possible variants for parameters $\textsf { \textsf { a } }$ and $\beta$

# 2.7.3 Dropout

The main idea of Dropout is instead of training one DNN to train an ensemble of several DNN and then to average the obtained results [3, 4].

Networks for training are obtained by excluding from a network (dropping out) neurons with probability p, so that the probability that neuron will remain in the network is equal ${ \mathsf { q } } = 1 - { \mathsf { p } }$ . “Dropout” of a neuron means that under any input data it return value 0.

Excluded neurons don’t contribute in training process at all stages of algorithm backpropagation; therefore dropout even one neuron is equivalent to training new neural network.

The probabilities of dropout each of neurons are equal. It means the following. Using conditions, that:

• $\mathbf { h } ( \mathbf { x } ) = \mathbf { x W } + \mathbf { b }$ is linear projection of input vector X in the space of dimension $\mathrm { d } _ { \mathrm { i } }$ on $\mathbf { d } _ { \mathrm { h } }$ -dimensional space of output variables; $\mathrm { a ( h ) }$ is activation function,

the application of Dropout to this projection at the training stage is possible to present as a modified activation function:

$$
f ( h ) = D \odot a ( h ) ,
$$

where $D = ( x 1 , x 2 , \ldots x _ { d h } ) - \mathrm { d _ { h } } .$ -dimensional vector of random variables $X _ { i }$ , distributed by Bernoulli law.

Then $X _ { i }$ has the following probability distribution:

$$
f ( k ; p ) = { \left\{ \begin{array} { l l } { p , } & { i f \quad k = 1 , } \\ { 1 - p , } & { i f \quad k = 0 , } \end{array} \right. }
$$

where $\mathbf { k }$ are all possible output values.

It’s evident that this random variable ideally matches to Dropout procedure, applied to one neuron. Indeed, a neuron is switched off with probability $p = P ( k = 1 )$ , otherwise it remains switched on. Consider the application of Dropout to $i$ -th neuron:

$$
O _ { i } = X _ { i } a \left( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \right) = \left\{ a \left( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \right) , i f X _ { i } = 1 \atop 0 , \quad i f X _ { i } = 0 .  \right.
$$

where $P ( X _ { i } = 0 ) = p$ :

As at the training stage a neuron remains switched on with probability $q$ , at the test stage we need emulate the behavior of ensemble of neurons which used was at the training stage. For that it was suggested at the test stage to multiply activation function at a coefficient $q$ . So, we have

$$
{ \mathrm { A t t r a i n i n g ~ s t a g e : ~ } } O _ { i } = X _ { i } a \left( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \right)
$$

$$
{ \mathrm { A t t e s t s t a g e : ~ } } O _ { i } = q a \left( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \right)
$$

It’s possible to use other approach—so-called back Dropout. In this case we multiply activation function at the proper coefficient not at the test stage but at the training stage. This coefficient is equal to the inverse value of probability that neuron remains in a network switched on: $\begin{array} { r } { \frac { 1 } { 1 - p } = \frac { 1 } { q } , } \end{array}$

In this case output of the ith hidden neuron is equal:

$$
\begin{array} { r l } & { \mathrm { A t ~ t h e ~ t r a i n i n g ~ s t a g e } \colon \mathrm { A t } \mathrm { t h e ~ t r a i n i n g ~ s t a g e } : O _ { i } = \frac { 1 } { q } X _ { i } a \Bigl ( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \Bigr ) } \\ & { \mathrm { A t ~ t h e ~ t e s t ~ s t a g e } \colon \mathrm { A t ~ t h e ~ t e s t ~ s t a g e } : O _ { i } = a \Bigl ( \sum _ { k = 1 } ^ { d _ { i } } w _ { k } x _ { k } + b \Bigr ) } \end{array}
$$

In the case of direct Dropout we are compelled to change a neural network for testing as without multiply $q$ a neuron will return the signal higher than those which

next neurons are waiting to get: therefore implementation of inverse Dropout is used more often.

# 2.7.4 Bagging (Ensemble Method)

One of ways to get ensemble of networks is application training by different training samples which are obtained as a result of random process so called bagging. Bagging (short for bootstrap aggregating)—is a method of decrease of generalization error by aggregating several models [4]. The idea lies in that to train several different models separately and then all models vote at output at test sample. This is an example of general strategy of machine learning called averaging model.

Methods using this strategy are known as ensemble methods. The cause to use averaging lies that usually different models make different errors in test sample. Consider for instance a set of $\mathbf { k }$ regression models. Assume that each model make error $\epsilon _ { i }$ for each pattern i obtained from multivariate normal distribution with variances $E \big [ \epsilon _ { i } ^ { 2 } \big ] = \nu$ and covariance $E \big [ \epsilon _ { i } \epsilon _ { j } \big ] = c$ :

Then the averaged prediction error made by whole ensemble is equal $\mathfrak { s } - \frac { 1 } { k } \sum _ { i } c _ { i }$ . And mean squared error of ensemble is:

$$
E \left[ \left( { \frac { 1 } { k } } \sum _ { i } c _ { i } \right) ^ { 2 } \right] = { \frac { 1 } { k ^ { 2 } } } E \left[ \sum \left( \epsilon _ { i } ^ { 2 } + \sum _ { j \neq 1 } \epsilon _ { i } \epsilon _ { j } \right) \right] = { \frac { 1 } { k } } \nu + { \frac { k - 1 } { k } } c
$$

In the case when all errors completely correlated and $\mathrm { { \boldsymbol { c } } = \mathrm { { \boldsymbol { v } } } }$ , MSE is equal to $\mathbf { v }$ , therefore the averaging of models doesn’t help at all. But in case when errors of different models are non-correlated $\mathrm { ~ c ~ } = 0$ , MSE of ensemble is equal ${ \frac { 1 } { k } } \nu$ :

This means that MSE of ensemble linearly decreases with the size of ensemble. In other words in average the ensemble will behave at least not worse as any of its members and if all members make independent errors the ensemble will behave much better than its members.

# 2.8 Cascade Neo-fuzzy Neural Networks Structure Synthesis and Learning with Application of GMDH

# Introduction

Last years the problem of stock prices and market indexes forecasting is of great importance. For its solution various approaches were applied. The most prospective methods of forecasting at markets are neural networks, especially fuzzy neural networks and the GMDH. Earlier it was proved that neural networks are universal approximators [4] and have some remarkable properties, such as parallel processing of information, ability to work with incomplete noisy input data, and learning possibilities to achieve the desired response (output).

The GMDH, from the other side, uses the principle of self-organization that allows to construct an optimal structure of the forecasting model during the algorithm operation [8–12]. It’s very promising to combine advantages of these both approaches for the solution of the problem—constructing an efficient model for the financial markets forecasting under BD conditions.

In the following presentation synthesis algorithm of the Neo-Fuzzy deep network using the GMDH is considered and its application for financial processes forecasting at stock markets is described. Experimental investigations of the efficiency of the proposed approach and its comparison with application of Neo-Fuzzy Neural Network with constant architecture are also presented.

# 2.8.1 The Neo-fuzzy Neuron

The architecture of the neo-fuzzy neuron (NFN) was proposed by Takeshi Yamakawa and co-authors in [13–15]. The authors of the NFN admit among its most important advantages, the high rate of learning, computational simplicity, the possibility of finding the global minimum of the learning criterion in real time and also that it is characterized by fuzzy linguistic “if-then” rules. The neo-fuzzy neuron is a nonlinear multi-input single-output system shown in Fig. 2.14.

It realizes the following mapping:

$$
{ \hat { y } } = \sum _ { i = 1 } ^ { n } f _ { i } ( x _ { i } ) ,
$$

where $x _ { i }$ is the $i \cdot$ -th input $( i = 1 , 2 , . . . , n )$ , $\hat { y }$ is a system output. Structural blocks of neo-fuzzy neuron are nonlinear synapses $\mathrm { N S _ { i } }$ which perform transformation of $i$ -th input signal in the from

$$
f _ { i } ( x _ { i } ) = \sum _ { j = 1 } ^ { h } w _ { j i } \mu _ { j i } ( x _ { i } )
$$

and realize fuzzy inference

$$
\mathrm { I F } x _ { i } \mathrm { I S } x _ { j i } \mathrm { T H E N T H E O U T P U T I S } w _ { j i }
$$

where $x _ { j i }$ is a fuzzy set which membership function is $\mu _ { j i } , w _ { j i }$ is a singleton (synaptic weight) in consequent. As it can be readily seen nonlinear synapse in fact realizes Takagi-Sugeno fuzzy inference of zero order [16, 17].

![](images/bb457421e63863dcbabd39f6fb125ae467f6f9de7802008bd00a0f8805d2cc92.jpg)  
Fig. 2.14 The neo-fuzzy neuron

Conventionally the membership functions $\mu _ { j i } ( x _ { i } )$ in the antecedent are complementary triangular functions as shown in Fig. 2.15.

For preliminary normalized input variables $x _ { i }$ (usually $0 \leq x _ { i } \leq 1$ ), membership functions can be expressed in the form:

$$
\begin{array} { r l } & { \mu _ { j i } ( x _ { i } ) = \left\{ \begin{array} { l l } { \frac { x _ { i } - c _ { j - 1 , i } } { c _ { j i } - c _ { j - 1 , i } } , x \in [ c _ { j - 1 , i } , c _ { j i } ] , } \\ { \frac { c _ { j + 1 , i } - x _ { i } } { c _ { j + 1 , i } - c _ { j i } } , x \in [ c _ { j i } , c _ { j + 1 , i } ] , } \\ { 0 - o t h e r w i s e , } \end{array} \right. } \end{array}
$$

where $c _ { j i }$ are arbitrarily selected centers of corresponding membership functions. Usually they are equally spaced on interval [0, 1]. This contributes to simplify the fuzzy inference process. That is, an input signal $x _ { i }$ activates only two neighboring

![](images/c23c713638ff4aa6aa7f6fc8b39455191a0f2b0857a02710becf4b1b3e421626.jpg)  
Fig. 2.15 Triangular membership functions

membership functions simultaneously and the sum of the grades of these two membership functions equals to unity (so-called Ruspini partitioning), i.e.

$$
\mu _ { j i } ( x _ { i } ) + \mu _ { j + 1 , i } ( x _ { i } ) = 1 .
$$

Thus, the fuzzy inference result produced by the Center-of-Gravity defuzzification method can be given in the very simple form

$$
f _ { i } ( x _ { i } ) = w _ { j i } \mu _ { j i } ( x _ { i } ) + w _ { j + 1 , i } \mu _ { j + 1 , i } ( x _ { i } ) .
$$

By summing up $f _ { i } ( x _ { i } )$ , the output $\hat { y }$ of Eq. (2.1) is produced.

It should be noticed that triangular activation functions provide only piecewise-linear approximation and this fact can in most of the cases can lead to decreasing of the received results accuracy. To minimize its negative effect we can increase number of membership functions. But it results in increasing of synaptic weight coefficients quantity and therefore complexity of our architecture is rising as well as time required for its learning.

To avoid this disadvantage we propose to use the cubic-spline membership functions (2.32) that can be written down in the following form:

$$
\begin{array} { r } { \mu ( x ) = \left\{ \begin{array} { l l } { 0 . 2 5 \bigg ( 2 + 3 \frac { 2 x - x _ { i } - x _ { i - 1 } } { x _ { i } - x _ { i - 1 } } - \left( \frac { 2 x - x _ { i } - x _ { i - 1 } } { x _ { i } - x _ { i - 1 } } \right) ^ { 3 } \bigg ) , } & { x \in [ x _ { i - 1 } , x _ { i } ] , } \\ { 0 . 2 5 \bigg ( 2 - 3 \frac { 2 x - x _ { i + 1 } - x _ { i } } { x _ { i + 1 } - x _ { i } } + \left( \frac { 2 x - x _ { i + 1 } - x _ { i } } { x _ { i + 1 } - x _ { i } } \right) ^ { 3 } \bigg ) , } & { x \in ( x _ { i } , x _ { i + 1 } ] . } \end{array} \right. } \end{array}
$$

and shown in Fig. 2.16.

![](images/ffb848de997ceaece79f539f3713017323d89ca1ed3837eedcd83c019e5fcf78.jpg)  
Fig. 2.16 Cubic-spline activation functions

The cubic-spline activation functions (2.32) satisfy all requirements of the Ruspini partitioning (2.31) and it is considerably contributes to simplify the fuzzy inference process. On the other hand, usage of the cubic spline activation functions provides smooth polynomial approximation instead of piecewise-linear approximation and makes possible to perform a high quality modeling of significantly nonlinear non-stationary signals and processes.

When a vector signal $x ( k ) = ( x _ { 1 } ( k ) , x _ { 2 } ( k ) , . . . , x _ { n } ( k ) ) ^ { T }$ (here $k = 1 , 2 , \ldots$ is a discrete time) is fed to the input of the neo-fuzzy neuron, the output of this neuron is determined by both the membership functions $\mu _ { j i } ( x _ { i } ( \boldsymbol { k } ) )$ and tunable synaptic weights $w _ { j i } ( k - 1 )$ , which have been obtained at the previous training epoch:

$$
{ \hat { y } } ( k ) = \sum _ { i = 1 } ^ { n } f _ { i } ( x _ { i } ( k ) ) = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { h } w _ { j i } ( k - 1 ) \mu _ { j i } ( x _ { i } ( k ) )
$$

and thereby neo-fuzzy neuron contains $h \ ^ { * } n$ synaptic weights which should be determined.

# 2.8.2 The Neo-fuzzy Neuron Learning Algorithm

The learning criterion (goal function) is the standard local quadratic error function:

$$
E ( k ) = { \frac { 1 } { 2 } } { \big ( } y ( k ) - { \hat { y } } ( k ) { \big ) } ^ { 2 } = { \frac { 1 } { 2 } } e ( k ) ^ { 2 } = { \frac { 1 } { 2 } } \left( y ( k ) - \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { h } w _ { j i } \mu _ { j i } ( x _ { i } ( k ) ) \right) ^ { 2 }
$$

It is minimized via the conventional gradient stepwise algorithm. And as a result the following weight update procedure is obtained:

$$
\begin{array} { l } { w _ { j i } ( k + 1 ) = w _ { j i } ( k ) + \eta e ( k + 1 ) \mu _ { j i } ( x _ { i } ( k + 1 ) ) \qquad } \\ { \qquad = w _ { j i } ( k ) + \eta \biggl ( y ( k + 1 ) - \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { h } w _ { j i } ( k ) \mu _ { j i } ( x _ { i } ( k + 1 ) ) \biggr ) \mu _ { j i } ( x _ { i } ( k + 1 ) ) , } \end{array}
$$

where $y ( k )$ is the target value of the output, $\eta$ is the scalar learning rate parameter which determines the speed of convergence and is chosen empirically.

For the purpose of increasing training speed Kaczmarz-Widrow-Hoff optimal one-step algorithm [10, 11] is applied

$$
w ( k + 1 ) = w ( k ) + \frac { y ( k + 1 ) - w ^ { T } ( k ) \mu ( x ( k + 1 ) ) } { \left\| \mu ( x ( k + 1 ) ) \right\| ^ { 2 } } \mu ( x ( k + 1 ) ) ,
$$

where

$$
\begin{array} { r l } & { \mu ( x ( k + 1 ) ) = ( \mu _ { 1 1 } ( x _ { 1 } ( k + 1 ) ) , . . . , \mu _ { h 1 } ( x _ { 1 } ( k + 1 ) ) , . . . , \mu _ { h 2 } ( x _ { 2 } ( k + 1 ) ) , . . . , \mu _ { t _ { i n } } ( x _ { n } ( k + 1 ) ) ) ^ { T } , } \\ & { \quad \quad \quad \quad \quad \quad - w ( k ) = \left( w _ { 1 1 } ( k ) , . . . , w _ { h 1 } ( k ) , . . . , w _ { h 2 } ( k ) , . . . , w _ { j i } ( k ) , . . . , w _ { h n } ( k ) \right) ^ { T } } \end{array}
$$

$( h n ) \times 1$ vectors, generated by the corresponding variables, and its exponentially weighted modification

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { w ( k + 1 ) = w ( k ) + r ^ { - 1 } ( k + 1 ) ( y ( k + 1 ) - w ^ { T } ( k ) \mu ( x ( k + 1 ) ) ) \mu ( x ( k + 1 ) ) , } \\ { r ( k + 1 ) = z r ( k ) + \| \mu ( x ( k + 1 ) ) \| ^ { 2 } , 0 \leq \alpha \leq 1 , } \end{array} \right. } \end{array}
$$

which possesses both smoothing and filtering properties.

In case we have priori defined data set training process can be performed in a batch mode for one epoch using conventional least squares estimation. The neo-fuzzy neuron can be used as an elementary node of the architecture called the Neo-Fuzzy Neural Network.

# 2.8.3 The Neo-fuzzy Neural Network and Its Architecture Optimization Using the Group Method of Data Handling

The Neo-Fuzzy Neural Network is a multilayer feedforward architecture that consists of neo-fuzzy neurons. 3-layers Neo-Fuzzy Neural Network [11] with $n$ inputs and m outputs is shown of Fig. 2.17.

Given architecture is completely coincide with the structure of the 3-layer perceptron, except that the neo-fuzzy neurons are used here as an elementary nodes instead of Rosenblatt perceptrons. Therefore, for the adjustment of the weight coefficients of such architecture it is necessary to use backpropagation algorithms. As it generally known, such algorithms are quite complex from the computational point of view and they operate slowly especially in Deep Neural networks with many layers.

![](images/146754d8963c42d54f79f96840ac1871597e5ed3c527a08adcf96bdb1fee8869.jpg)  
Fig. 2.17 The neo-fuzzy neural network general structure

If we use neo-fuzzy neurons that have only two inputs, the GMDH can be applied for the synthesis of the Neo-Fuzzy Neural Network with optimal architecture.

The main idea of the GMDH algorithm lay in successive synthesis of the neuron layers until the external criterion begins to increase.

# Algorithm description [11]:

(1) Form pairs from the neo-fuzzy neuron outputs of the current layer (at the first iteration we use the set of input signals). Each pair is fed to the corresponding neo-fuzzy neuron.   
(2) Using the learning subsample adjust synaptic weight coefficient of each neo-fuzzy neuron.   
(3) Using the test subsample calculate the value of the external criterion (regularity) for each neo-fuzzy neuron:

$$
\varepsilon _ { p } ^ { [ s ] } = \frac { 1 } { N _ { t e s t } } \sum _ { i = 1 } ^ { N _ { t e s t } } \left( y ( i ) - \hat { y } _ { p } ^ { [ s ] } ( i ) \right) ^ { 2 }
$$

where $N _ { t e s t }$ is a size of the test subsample, $s$ is the layer number, $p$ is a neuron number in the current layer $p = \overline { { 1 , \mathfrak { n } _ { \mathrm { s } } } } , \hat { y } _ { p } ^ { [ s ] } ( i )$ is the $p$ -th neuron of the $s$ -th layer response signal for the $i \cdot$ -th input vector.

(4) Find the minimal value of the external criteria for all neo-fuzzy neurons of the current layer

$$
\varepsilon ^ { [ s ] } = \operatorname* { m i n } _ { p } \varepsilon _ { p } ^ { [ s ] } .
$$

Check the condition

$$
\varepsilon ^ { [ s ] } \geq \varepsilon ^ { [ s - 1 ] }
$$

where $\varepsilon ^ { [ s ] } , \varepsilon ^ { [ s - 1 ] }$ are the criterion values for the best neurons of the and s-th and $( s - 1 )$ -th layers correspondingly. If the condition (2.36) is true then return to the previous layer and find the best neuron that has minimal value of the criterion (2.35). Otherwise, select $F$ best neurons according to the criterion (2.35) value and go to the step 1 to construct the next layer of neurons.

(5) Determine the final structure of the network. Moving backward from the best neuron of the $( \mathsf { m } - 1 )$ -th layer along the input connections and passing successively all the layers of neurons, preserve in the final structure only such neurons that are used in the next layer.

After the GMDH stops it can be said that the final optimal structure of the Neo-Fuzzy Neural Network is synthesized. As it can be readily seen we obtain not only optimal structure, but also trained neural network that is ready to process new data.

One of the most important advantages of GMDH application for the Deep neural networks architecture synthesis is a capability to use simple but very quick learning procedures for the neo-fuzzy neuron weights adjustment because network is trained layer-by-layer.

# 2.8.4 The Experimental Investigations of Forecasting with Neo-fuzzy Neural Network

The experimental investigations of neo-fuzzy neural network in the problem of forecasting were carried out [11]. The goal contained in RTS index forecasting on the base of current stock prices of the leading Russian companies.

Input data: daily stock prices and the value of RTS index in the period from 5 of February till 5 of May 2009.

The output is RTS index on the next day.

Sample size was 100 values.

Forecast criteria were the following:

1. mean squared error (MSE);   
2. mean absolute percentage error (MAPE).

# Types of experiments for Neo-fuzzy neural network:

(1) Variation of ratio learning/ test samples in the range: 25:75, 50:50, 75:25;   
(2) Change the number of layers: 1-3-5;   
(3) Change the number of iterations: 1000, 10,000, 100,000;   
(4) Variation of a number of points to be forecasted: 1-3-5;   
(5) Change of maximal error—the condition of stop: 0.01 тa 0.09;

Some of the obtained experimental results are presented below. Experiment $A$ ) ratio 75:25, $\mathrm { M S E } = 0 . 0 5 0 1 5 8$ . The results are presented on Fig. 2.18. Experiment $B$ ) ratio $5 0 { : } 5 0 \ \mathrm { M S E } = 0 . 0 5 3 5 6 2$ Experiment $C$ ) ratio learning/test—25:75. The results are presented on Fig. 2.19. $\mathrm { M S E } = 0 . 0 6 8 4 8 9$

# Experiment Type 2. Variation of Layers Number

Comparison of algorithm work when number of layers is varied: 1-3-5-7 while forecast at 1 point under ratio learning/test sample 75:25

![](images/17b0a71d9b139f49d83667b4d69ea820054b5e2705ed40d2348527c8a65eba81.jpg)  
Fig. 2.18 Forecasted results under ratio learning/test sample 75:25

![](images/44a9bf2c4c9c9b81ef07ab28054152f52e316b109d42b81e55f65be21bad6800.jpg)  
Fig. 2.19 Forecasted results under ratio learning/test sample 25:75

![](images/726edb975bce506cf37144d8d108d4e35d69f4f84837296443035012406b3752.jpg)  
Fig. 2.20 Forecasted results with one layer

Experiment A) layers number— $1 ~ \mathrm { M S E } = 0 . 0 4 6 6 2$ . The results are presented on Fig. 2.20.

Experiment $B ^ { ' }$ ) layers number—3, $\mathrm { M S E } = 0 . 0 3 8 1$ Experiment $C$ ) layers number—5, $\mathrm { M S E } = 0 . 0 4 4 6$ Experiment $D$ ) layers number—7, $\mathrm { M S E } = 0 . 0 5 4 4$

# Experiments Type 3. Variation of Iterations Number: 1000, 10,000, 100,000

Experiment $B$ ) iterations number—10,000, $\mathbf { M S E } = 0 . 0 5 7 5$ Experiment $C$ ) iterations number—100,000, $\mathbf { M S E } = 0 . 0 5 2 5$

# Experiments Type 4. Variation of Number of Forecasted Points

Comparison of algorithm forecasting accuracy when varying a number of forecasted   
points 1-3-5, using ratio learning/test sample 75:25 Experiment A) a number of forecasted points— $1 ~ \mathrm { M S E } = 0 . 0 4 9 5$ Experiment $B$ ) a number of forecasted points—3, $\mathbf { M S E } = 0 . 4 4 6 9$ Experiment $C$ ) a number of forecasted points—5, $\mathbf { M S E } = 1 . 0 4 1 8$

# Conclusions on Experimental Results

After having carried out the series of experiments with neo-fuzzy neural network of full structure and of optimal structure constructed by GMDH the following results were obtained which are presented in Table 2.1.

The best results are highlighted with the grey color. As it can be readily seen the Neo-Fuzzy Neural Network with optimal structure constructed by GMDH gives better results than the conventional network with full structure (full network).

This may be explained by the utilization of self-organization mechanism for constructing not full network. But at the same time there are some disadvantages of this approach—the rate of convergence is slower in comparison with full network. But taking into account the better criterion values this disadvantage may be neglected.

For better estimation of the suggested approach the forecasting error obtained at the experiments is presented on Figs. 2.21 and 2.22. These are the charts of MAPE obtained by Neo-fuzzy neural network constructed by GMDH.

Table 2.1 Comparison of the neo-fuzzy neural network with full structure and structure constructed by the GMDH   

<html><body><table><tr><td>Type of the experiment</td><td>Experiment parameters</td><td>CNFNN synthesized by GMDH</td><td>Full structure CNFNN</td></tr><tr><td rowspan="3">Variation of ratio training/ testing sample</td><td>75%:25%</td><td>0.0484</td><td>0.0501</td></tr><tr><td>50%:50%</td><td>0.0532</td><td>0.0536</td></tr><tr><td>25%:75%</td><td>0.0608</td><td>0.0684</td></tr><tr><td rowspan="3">Number of layers variation</td><td>1</td><td>0.0628</td><td>0.0626</td></tr><tr><td>3</td><td>0.0381</td><td>0.0544</td></tr><tr><td>5</td><td>0.0434</td><td>0.0652</td></tr><tr><td rowspan="3">Iterations number</td><td>1000</td><td>0.0588</td><td>0.0674</td></tr><tr><td>10.000</td><td>0.0479</td><td>0.0485</td></tr><tr><td>100.000</td><td>0.0459</td><td>0.0482</td></tr><tr><td rowspan="3">Number of forecasted points</td><td>1</td><td>0.0495</td><td>0.0587</td></tr><tr><td>3</td><td>0.4469</td><td>1.0844</td></tr><tr><td>5</td><td>1.0418</td><td>1.3901</td></tr></table></body></html>

![](images/689f3c7f84c6b0b185032e4a0615209250fe42b71bcedaba52cc1c80bff1bfc8.jpg)  
Fig. 2.21 The curves of error (MAPE) while forecasting 1, 3 or 5 points

As we may see while forecasting 1 point ahead we obtain rather high precision— less than $1 5 \%$ . In case of increase the number of points forecasted the accuracy drops—the error lies in the range $1 5 \mathrm { - } 4 5 \%$ .

Analyzing the presented curves we conclude that the Neo-Fuzzy Neural Network with one hidden layer error is also not high but is not uniformly distributed and may exceed $30 \%$ . For 5 hidden layers the MAPE increases and may reach $3 5 \%$ . And finally with 7 layers MAPE reaches $60 \%$ . Thus the maximal precision we obtain with 3 hidden layers.

![](images/cb27e77a41d44ed3536ece19b06275982090d30e0cdb07606d778ea4c9b78169.jpg)  
Fig. 2.22 Forecasting error (MAPE) versus number of layers (1, 3, 5, 7) of neo-fuzzy network

Besides, in process of experimental investigations were found the optimal parameters for algorithms for full and constructed by GMDH neo-fuzzy networks [11]:

The ideal ratio of learning and test samples— $7 5 \% : 2 5 \%$ . The best number of layers—3. The best result at 100,000 iterations The best result with 1 forecasted point. • The best result with maximal error (threshold of algorithm stop)—0.01.

# Solving of the Classification Problem Using the Neo-Fuzzy Neural Network

We have applied proposed Neo-Fuzzy Neural Network synthesized by the GMDH to solve the ‘breast cancer in Wisconsin’ benchmark classification problem [11].

Dataset containing 699 points have been used for this purpose (ftp://cs.wisc.edu/ math-prog/cpo-dataset/machine-learn/cancer/cancer1/datacum). 16 points had parameters with missed values so they have been eliminated from the dataset and remaining 683 points have been separated on training set—478 points $( 7 0 \% )$ and test set—205 points $( 3 0 \% )$ .

Each point has 9-dimensional feature vector and 1 class parameter which should be determined and identifies either benign or malignant tumor has current examined patient. Features values have been normalized on interval $[ - 1 ; 1 ]$ .

For comparison the same classification problem was solved using the conventional Neo-Fuzzy Neural Network with full 3-layer structure: 10 NFNs in the first layer, 5 in the seconds, and 1 output NFN. Obtained results of classifications can be found in Table 2.2.

Table 2.2 Comparison of the neo-fuzzy neural network with full structure and structure constructed by the GMDH for the ‘breast cancer in Wisconsin’ benchmark classification problem   

<html><body><table><tr><td>ANN Architecture</td><td>Accuracy on training set/points outside the ‘belief zone'</td><td>Accuracy on testing set/points outside the ‘belief zone'</td></tr><tr><td>Network constructed by the GMDH</td><td>99.8%/1</td><td>98%/4</td></tr><tr><td>Full network</td><td>98%/3</td><td>94%/15</td></tr></table></body></html>

![](images/c2cf70e2210b6c68542d18a8b18d3d722c416e9f7b1d46ce0c642e58e20ecddf.jpg)  
Fig. 2.23 The architecture of the neo-fuzzy neural network for solving the ‘breast cancer in Wisconsin’ benchmark classification problem synthesized by the GMDH

When output signal be found within the range [0.3; 0.7] it is lesser probability that classification was correct. We quantify and marked out such classified samples as points outside the ‘belief zone’.

We can see that the Neo-Fuzzy Neural Network with architecture synthesized by the GMDH shows very good results of classification and sufficiently exceeds in the classification quality as compared with the full network, especially on the testing set. It can be explained by fact, that full network is a more complex model and as generally known, complexness of the model leads to generalization loss and therefore classification accuracy decreases. The GMDH allows to synthesis the optimal structure that neglects inputs which are not significant.

In Fig. 2.23 the architecture of the Neo-Fuzzy Neural Network constructed by the GMDH is shown. It is considerably simpler, than the full network, but in spite of this it allows to achieve higher classification quality.

# 2.9 Evolving GMDH-Neuro-fuzzy Network with Small Number of Tuning Parameters

# Introduction

Nowadays artificial neural networks (ANNs) and neuro-fuzzy systems (NFSs) are widely used for solving different Data Mining tasks, presented either in the form of “object—property” tables or in the form of multidimensional time series, often produced by stochastic or chaotic non-stationary nonlinear systems. The advantages of these computational intelligence systems derive, first of all, from their universal approximating capabilities, learning possibility, transparency and interpretability (in case of the NFSs) of the results.

Conventionally “learning” is defined as a process of adjusting synaptic weights using an optimization of a given learning criterion. The quality of this process can be significantly improved by adjusting not only its synaptic weights but also the architecture of the ANNs and NFSs. This idea is the foundation of evolving computational intelligence systems (ECIS), that are used more widely in the recent years [18, 19].

It should be noticed that the multilayered neuro-fuzzy systems of TSK- or ANFIS-type [16, 17, 20–22] are the base of the majority of the known ECIS.

At the same time, speaking of evolving systems, we should mention the Group Method of Data Handling (GMDH) [12, 23–26], which is a powerful approach of the information processing system of self-organization. It can synthesize sufficiently simple and effective computational architectures. It is clear that this approach attracted the attention of the computational intelligence experts. The GMDH-neural networks having active neurons [26–28], N-adalines [29], R-neurons [30, 31], Q-neurons [3] as nodes were developed; in the area integrating fuzzy GMDH [32] and neural networks the GMDH-neuro-fuzzy systems [31, 33] and GMDH-neo-fuzzy systems (see previous section) [11] were developed; GMDH-wavelet-neuro-fuzzy systems [8, 10, 34] and GMDH-fuzzy-spiking neural network [9] were also elaborated.

These systems demonstrated their efficiency in solving a wide range of tasks, however they lost the main advantages of the original GMDH, namely small number of tuning parameters in each node. It should be noted that initially elementary regression models with two inputs and three estimated coefficients were developed on the basis of GMDH. These properties of GMDH are especially important for deep neural networks with multiple hidden layers.

Due to this problem, it seems reasonable to develop a GMDH-system, that combines advantages of the traditional GMDH, hybrid systems of the computational intelligence and that is trained with simple learning procedures, used in regression analysis and linear identification theory. The developed approach to this problem solution is considered below.

# 2.9.1 Evolving GMDH-Neuro-fuzzy System Architecture

The architecture of the evolving GMDH-system is shown in Fig. 2.24. To the input layer of the system $( n \times 1 )$ -dimensional vector of input signals $x = \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right) ^ { T }$ is fed. Then this signal is fed to the first hidden layer, that contains $n _ { 1 } = c _ { n } ^ { 2 }$ nodes-neurons, each of which has only two inputs. At the node outputs $N ^ { [ { 1 } ] }$ of the first hidden layer the output signals $\hat { y } _ { l } ^ { [ 1 ] }$ , $l = 1 , 2 , . . . , 0 , 5 n ( n - 1 ) = c _ { n } ^ { 2 }$ are formed. Then these signals are fed to the selection block of the first hidden layer $S B ^ { [ 1 ] }$ , that selects among the output signals $\hat { y } _ { l } ^ { [ 1 ] } n _ { 1 } *$ best signals $( n _ { 1 } * \leq n$ , where $n _ { 1 } * = \mathrm { F }$ is so called Freedom of choice) most precise by accepted criterion (mostly by the mean squared error $\sigma _ { y _ { l } ^ { [ 1 ] } } ^ { 2 } .$ ).

![](images/1deb51bac1e6a1ccc972cc387adf4eab3aaec79fc67b8a3c70b79a51e5e17748.jpg)  
Fig. 2.24 Evolving GMDH-system

From these $n _ { 1 } *$ best outputs of the first hidden layer $\hat { y } _ { l } ^ { [ 1 ] } * n _ { 2 }$ pairwise combineatuironss $\hat { y } _ { l } ^ { [ 1 ] } { * } , \hat { y } _ { p } ^ { [ 1 ] } { * }$ oanrge fhoersmigedn,altshaotf tahries fleadyetro e hsecsoenledcthiiodndeblnolcaky osremlecd s $N ^ { [ 2 ] }$ $\hat { y } _ { l } ^ { [ 2 ] }$ $S B ^ { [ 2 ] }$ $\mathrm { ~ F ~ }$ best neurons by accuracy (e.g. by $\sigma _ { y _ { l } ^ { [ 2 ] } } ^ { 2 } .$ ) if the best signal of the second layer is better than the best one of the first hidden layer $\hat { y } _ { 1 } ^ { [ 1 ] } \ast$ : Other hidden layers forms signals similarly to the second hidden layer. The system evolution process continues until the best signal of the selection block $S B ^ { [ s + 1 ) }$ would be worse than the best signal of the previous (s) layer, that is $\sigma _ { y _ { l } ^ { [ s + 1 ] } } ^ { 2 } > \sigma _ { y _ { l } ^ { [ s ] } } ^ { 2 }$ . Then we return to the previous layer and choose its best node neuron $N ^ { [ s ] }$ in order to form the system output signal $\hat { y } ^ { [ s ] }$ .

It should be stressed that we obtain not only optimal network structure but well-trained network as well due to GMDH algorithm. Besides, since the training is performed sequentially layer by layer the problems of high dimensionality as well as decaying or exploding gradient vanish.

This is very important for deep learning networks.

As it was already mentioned, as nodes of GMDH-systems we can use different types of neurons, e.g. N-Adalines [29], active [26, 27, 35], R-[30, 36], Q-[34], spiking-[9], wavelet-[8, 10, 34], neo-fuzzy-neurons [11] and other similar computational intelligence systems units, that has the required approximating capabilities and learning capacities. However, the main advantage of the original GMDH may be lost, namely the ability to work with small training sets (short samples). Therefore in the next section NFN network with small number of tuning parameters is considered.

# 2.9.2 Neuro-fuzzy Network with Small Number of Tuning Parameters as a Node of GMDH-System

Let us consider the node architecture, shown in Fig. 2.25 and proposed as a neuron of the suggested evolving GMDH-system. This architecture is in fact a Wang– Mendel neuro-fuzzy system [22, 37] with only two inputs $x _ { i }$ and $x _ { j }$ , and one output $\hat { y } _ { l }$ . To the node input a two-dimensional vector of signals $x ( k ) = \left( x _ { i } ( k ) , x _ { j } ( k ) \right) ^ { T }$ is fed, where $k = 1 , 2 , . . . , N$ is either the observation number in training set or the current discrete time.

![](images/d04ce7fef4533c09e784bdd1486246eca2ca1b783d2ad96cb1e8865d72a56733.jpg)  
Fig. 2.25 GMDH-neuro-fuzzy system node

The first layer of a node contains $2 h$ membership functions $\mu _ { p i } ( x _ { i } ( { \boldsymbol { k } } ) )$ , $\mu _ { p j } \big ( x _ { j } ( k ) \big )$ , $p = 1 , 2 , . . . , h$ and provides fuzzification of input variables. The bell-shaped constructions with nonstrictly local receptive support are usually used as membership functions. It allows to avoid appearing of “gaps” in the fuzzified space while using scatter partitioning of input space [35]. Usually the Gaussians are used as membership functions of the first layer

$$
\mu _ { p i } ( x _ { i } ( k ) ) = \mathrm { e x p } \left( - \frac { \left( x _ { i } ( k ) - c _ { p i } \right) ^ { 2 } } { 2 \sigma _ { i } ^ { 2 } } \right) , \mu _ { p j } \bigl ( x _ { j } ( k ) \bigr ) = \mathrm { e x p } \left( - \frac { \left( x _ { j } ( k ) - c _ { p j } \right) ^ { 2 } } { 2 \sigma _ { j } ^ { 2 } } \right) ,
$$

where $c _ { p i } , c _ { p j }$ are parameters, that define the centers of the membership functions, ${ \sigma } _ { i } , { \sigma } _ { j }$ are width parameters of these functions. The second layer provides aggregation of the membership levels. It consists of $h$ multiplication units and forms two-dimensional radial basis activation functions

$$
\tilde { x } _ { p } ( k ) = \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } \bigl ( x _ { j } ( k ) \bigr ) ,
$$

and for Gaussians with the same values $\sigma _ { i } = \sigma _ { j } = \sigma$ we can write

$$
\tilde { x } _ { p } ( k ) = \exp \left( - \frac { \left\| x ( k ) - c _ { p } \right\| ^ { 2 } } { 2 \sigma ^ { 2 } } \right)
$$

(here $\boldsymbol { c _ { p } } = \left( c _ { p i } , \ c _ { p j } \right) ^ { T } )$ , i.e. the elements of the first and the second layers process the input signal similarly to the R-neurons of the radial basis function neural networks.

The third layer is one of synaptic weights that are adjusted during learning process. The outputs of this layer are values

$$
w _ { l p } ^ { i j } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } \bigl ( x _ { j } ( k ) \bigr ) = w _ { l p } ^ { i j } \tilde { x } _ { p } ( k ) ,
$$

The fourth layer is formed by two summation units and computes the sums of output signals of the second and the third hidden layers

$$
\sum _ { p = 1 } ^ { h } w _ { l p } ^ { i j } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } ( x _ { j } ( k ) ) = \sum _ { p = 1 } ^ { h } w _ { l p } ^ { i j } \tilde { x } _ { p } ( k ) , \sum _ { p = 1 } ^ { h } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } ( x _ { j } ( k ) ) = \sum _ { p = 1 } ^ { h } \tilde { x } _ { p } ( k ) ,
$$

And finally in the fifth layer of the neuron normalization is realized, as a result the node output signal $\hat { y } _ { l }$ is formed:

$$
\begin{array} { c } { { \hat { y } _ { l } ( k ) = \displaystyle \frac { \sum _ { p = 1 } ^ { h } w _ { l p } ^ { i j } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } \bigl ( x _ { j } ( k ) \bigr ) } { \sum _ { p = 1 } ^ { h } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } \bigl ( x _ { j } ( k ) \bigr ) } = \displaystyle \frac { \sum _ { p = 1 } ^ { h } w _ { l p } ^ { i j } \tilde { x } _ { p } ( k ) } { \sum _ { p = 1 } ^ { h } \tilde { x } _ { p } ( k ) } } } \\ { { = \displaystyle \sum _ { p = 1 } ^ { h } w _ { l p } ^ { i j } \varphi _ { p } ^ { i j } ( x ( k ) ) = \bigl ( w _ { l } ^ { i j } \bigr ) ^ { T } \varphi ^ { i j } ( x ( k ) ) \quad ( 6 ) } } \end{array}
$$

$$
\begin{array} { r l r } & { \mathrm { w h e r e } } & { w _ { l } ^ { i j } = \left( w _ { l 1 } ^ { i j } , . . . , w _ { l p } ^ { i j } , . . . , w _ { l h } ^ { i j } \right) ^ { T } , } \\ & { \varphi _ { p } ^ { i j } ( x ( k ) ) = \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } ( x _ { j } ( k ) ) \left( \sum _ { p = 1 } ^ { h } \mu _ { p i } ( x _ { i } ( k ) ) \mu _ { p j } ( x _ { j } ( k ) ) \right) ^ { - 1 } , } \\ & { \varphi ^ { i j } ( x ( k ) ) = \left( \varphi _ { 1 } ^ { i j } ( x ( k ) ) , . . . , \varphi _ { p } ^ { i j } ( x ( k ) ) , . . . , \varphi _ { p } ^ { i j } ( x ( k ) ) \right) ^ { T } . } \end{array}
$$

It is easy to see that the node implements nonlinear mapping of input signals to output signal like normalized radial basis function neural network, however the NFS contains significantly lower number $h$ of adjusted parameters comparing with the neural network.

Using introduced notation and writing transformations in every node of the standard GMDH in the form

$$
\hat { y } _ { l } ( k ) = w _ { l 0 } ^ { i j } + w _ { l 1 } ^ { i j } x _ { i } ( k ) + w _ { l 2 } ^ { i j } x _ { j } ( k ) ,
$$

that contains three unknown parameters, it is easy to see that with three membership functions being on the each input of the proposed node we get the same three synaptic weights that should be adjusted.

In the simplest case the estimation of these synaptic weights can be realized with the conventional least squares method (LSM), traditionally used in the GMDH. If the entire training set is presented, we can use the LSM in its batch form

$$
w _ { l } ^ { i j } ( N ) = \left( \sum _ { k = 1 } ^ { N } \varphi ^ { i j } ( x ( k ) ) \left( \varphi ^ { i j } ( x ( k ) ) \right) ^ { T } \right) ^ { + } \sum _ { k = 1 } ^ { N } \varphi ^ { i j } ( x ( k ) ) y ( k )
$$

(here $y ( k )$ —external reference signal). If training samples are fed sequentially in on-line mode, the recurrent form of the LSM is used

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { w _ { l } ^ { i j } ( k ) = w _ { l } ^ { i j } ( k - 1 ) + \frac { \mathrm { P } ^ { i j } ( k - 1 ) \big ( y ( k ) - \big ( w _ { l } ^ { i j } ( k - 1 ) \big ) ^ { T } \varphi ^ { i j } ( x ( k ) ) \big ) \varphi ^ { i j } ( x ( k ) ) } { 1 + \big ( \varphi ^ { i j } ( x ( k ) ) \big ) ^ { T } \mathrm { P } ^ { i j } ( k - 1 ) \varphi ^ { i j } ( x ( k ) ) } , } \\ { \mathrm { P } ^ { i j } ( k ) = \mathrm { P } ^ { i j } ( k - 1 ) - \frac { \mathrm { P } ^ { i j } ( k - 1 ) \varphi ^ { i j } ( x ( k ) ) \big ( \varphi ^ { i j } ( x ( k ) ) \big ) ^ { T } \mathrm { P } ^ { i j } ( k - 1 ) } { 1 + \big ( \varphi ^ { i j } ( x ( k ) ) \big ) ^ { T } \mathrm { P } ^ { i j } ( k - 1 ) \varphi ^ { i j } ( x ( k ) ) } . } \end{array} \right. } \end{array}
$$

# 2.9.3 Computational Experiments

The efficiency of the proposed approach was demonstrated by solving the problem of the forecasting at the stock exchange.

The experimental investigations for stock prices forecasting were carried out. As a forecasted variable the RTS index in 2013 with time step one week was chosen. As external regressors (inputs) stock prices of the leading companies were used. Total sample had 55 points that was used while searching the optimal partial description in the GMDH. At each layer we selected 6 best models (freedom choice $\mathrm { F } = 6 \$ ). The mathematical model had the general form $y = f ( x _ { 1 } , \ x _ { 2 } , \ x _ { 3 } , \ x _ { 4 } )$ .

As the quality criteria of the obtained models MAPE and RMSE were used. The flow charts of real and simulated values of the RTS index are presented in Fig. 2.26 for $N = 2$ (here $N$ is a number of fuzzy inputs). The results of experiments are presented in Table 2.3. The flow charts of criteria values are presented in Figs. 2.27 and 2.28. As one can see, with number of inputs increasing the error values first fall down, but then begin to grow. So increasing the number of inputs until the error value starts to grow we can obtain the optimal inputs number (Figs. 2.27 and 2.28).

![](images/8136bf44f1068974b7bb30ac84100026140af2e6895baa17f443bb775407c9dc.jpg)  
Fig. 2.26 GMDH-neuro-fuzzy network $5 0 \%$ —training sample size, Freedom choice $= 6$ , ${ \bf N } = 2$ )

Table 2.3 Dependence of forecasting accuracy (MAPE and RMSE) on number of inputs   

<html><body><table><tr><td>Maximum number of membership functions</td><td>MAPE</td><td>RMSE</td></tr><tr><td>2</td><td>0.07085</td><td>11.2743</td></tr><tr><td>3</td><td>0.05692</td><td>9.48098</td></tr><tr><td>4</td><td>0.05505</td><td>9.29596</td></tr><tr><td>5</td><td>0.05796</td><td>9.76549</td></tr><tr><td>6</td><td>0.05606</td><td>9.30073</td></tr><tr><td>7</td><td>0.04921</td><td>8.31249</td></tr><tr><td>8</td><td>0.04534</td><td>7.83328</td></tr><tr><td>9</td><td>0.06061</td><td>15.1446</td></tr></table></body></html>

![](images/749464949b12f1039a925b4ea7df1b7b7d37b307d00be396561a01d9632882ff.jpg)  
Fig. 2.27 Flow chart of MAPE versus number of inputs N

![](images/be6465b6fdc9fbc6cb4345fa9ecf4f9730bfff1d2dc743f595c97a842e4fdd8d.jpg)  
Fig. 2.28 Flow chart of RMSE values versus number of inputs

![](images/d5780c46333a7415ca8a609333b1e3798ca9ed987d1d7c80a0392ecc395dc49d.jpg)  
Fig. 2.29 Flow charts of real and predicted values of the RTS index using GMDH

Table 2.4 MAPE criterion for GMDH-NFN and full cascade NFN   

<html><body><table><tr><td>Fuzzification inputs number</td><td>MAPE for GMDH-NFN</td><td>MAPE forfull cascade NFN</td></tr><tr><td>2</td><td>0.040376</td><td>0.060309</td></tr><tr><td>4</td><td>0.039496</td><td>0.051411</td></tr><tr><td>6</td><td>0.039979</td><td>0.044253</td></tr><tr><td>8</td><td>0.042479</td><td>0.043964</td></tr><tr><td>10</td><td>0.049349</td><td>0.051706</td></tr><tr><td>12</td><td>0.040835</td><td>0.044645</td></tr></table></body></html>

For a comparison models using classical GMDH with linear partial descriptions and cascade neuro-fuzzy network were constructed. The following parameters for models construction were set:

classical GMDH, $50 \%$ is training sample size, freedom choice—best 6 models;   
cascade neuro-fuzzy network with different inputs number.

The simulation results for the classical GMDH are presented in Fig. 2.29. The MAPE value is 0.09845, the RMSE value is 15.1446.

Now let’s construct the model using full cascade neuro-fuzzy network with different inputs number. The MAPE values for GMDH-neuro-fuzzy network and for full cascade NFN are presented in Table 2.4.

The flow charts of MAPE for these networks are presented in Fig. 2.30. As one can see, the GMDH-neuro-fuzzy network showed much better results than the full cascade neuro-fuzzy network due to more optimal network structure. Also GMDH-neuro-fuzzy network showed better results comparing with classical GMDH. The MAPE value for classical GMDH is 0.09845, while the best GMDH-neuro-fuzzy model has MAPE value 0.039496.

![](images/6e3a6bada5d84f8a5b7578ddebeb0a0ba38a0daf3b0f3c99e443826b6e6b799a.jpg)  
Fig. 2.30 MAPE values for GMDH-neuro-fuzzy network and full cascade neuro-fuzzy network versus the number of inputs

The further experiments were carried out. We added to the inputs several output values in the prehistory. The other models parameters are the same. The model is presented in form $y ( k ) = f ( x _ { 1 } ( k ) , x _ { 2 } ( k ) , x _ { 3 } ( k ) , y ( k - 1 ) , y ( k - 2 ) )$ .

Number of inputs is 5. The MAPE value is 0.02040, the RMSE value is 3.59614. As one can see, after adding the values of the RTS index to inputs prehistory the model quality has increased.

Let’s consider the prediction quality of the GMDH-neuro-fuzzy model using another sample. As input sample the stock prices of Microsoft corp. since 01.11.14 to 29.12.14 were used. The sample size is 64 points. A model is constructed using 62 points. The forecast is made for 4 steps ahead, the first two steps are checked with available data. Autoregression model with number of lags 5 is used. As a result we obtained a GMDH-neuro-fuzzy network with 6 fuzzy inputs. The obtained results are presented in Tables 2.5 and 2.6.

Table 2.5 Forecasting results for two steps ahead   

<html><body><table><tr><td>Date</td><td>Real value</td><td>Predicted value</td><td>Absolute error</td><td>Relative error (%)</td></tr><tr><td>26.12.14</td><td>18,030.21</td><td>17,971.63</td><td>58.57668</td><td>0.324881</td></tr><tr><td>24.12.14</td><td>18,053.71</td><td>17,991.94</td><td>61.77189</td><td>0.342156</td></tr></table></body></html>

Table 2.6 Forecasting results for different neuro-fuzzy networks and GMDH   

<html><body><table><tr><td>Real value</td><td>GMDH-neuro-fuzzy network</td><td>GMDH system</td><td>Cascade-neuro-fuzzy network</td></tr><tr><td>48.14</td><td>48.44502</td><td>48.71953</td><td>46.50050</td></tr><tr><td>47.88</td><td>48.89899</td><td>48.80680</td><td>46.66598</td></tr><tr><td></td><td>48.76889</td><td>48.88288</td><td>46.49011</td></tr><tr><td>1</td><td>49.07061</td><td>48.92689</td><td>46.43442</td></tr><tr><td>1</td><td>49.33117</td><td>48.92077</td><td>46.42505</td></tr></table></body></html>

Table 2.7 Training time for different fuzzy neural models   

<html><body><table><tr><td>Inputs number</td><td>Time for GMDH-neuro-fuzzy network (s)</td><td>Time for full cascade network (s)</td></tr><tr><td>2</td><td>0.004</td><td>0.015</td></tr><tr><td>4</td><td>0.009</td><td>0.021</td></tr><tr><td>6</td><td>0.013</td><td>0.037</td></tr><tr><td>8</td><td>0.021</td><td>0.048</td></tr><tr><td>10</td><td>0.030</td><td>0.053</td></tr></table></body></html>

As one can see, the GMDH-neuro-fuzzy network shows more accurate forecast than the classical GMDH and the cascade neuro-fuzzy network. Its MAPE value doesn’t exceed $1 \%$ (0.32 and $0 . 3 4 \%$ while forecasting for 1 and 2 steps ahead).

As the final experiment let’s compare the training time for GMDH-neuro-fuzzy model and full cascade model. In Table 2.7 the training time in seconds for GMDH-neuro-fuzzy network and full cascade neuro-fuzzy network is presented. As an initial sample we used Microsoft stock prices in the period since 01.11.14 to 29.12.14, a sample size is 64 points.

# Conclusion

In this section the elementary neuro-fuzzy networks with scatter partitioning of input space and small number of tuning parameters are proposed as nodes of the GMDH-system. The system architecture can evolve in on-line mode as the synaptic weights of the proposed neuro-fuzzy nodes-neurons are adjusted. The distinguishing feature of the proposed approach is the ability to work with very small training sets.

The experimental investigations of the neuro-fuzzy network in the problem of stock prices forecasting were carried out. After investigations results analysis the following conclusions were made:

– the variation of inputs number in GMDH-neuro-fuzzy network influences the model quality: as a number of inputs increases the error first falls down, and then begins to grow; it enables to choose the optimal inputs number; the application of the proposed approach for optimal structure search allows to decrease training time and to increase the forecasting quality of the model comparing with full-cascade deep fuzzy network.

# 2.10 A Deep GMDH System Based on the Extended Neo-fuzzy Neuron and Its Training

# Introduction

During the last few years, evolving intelligent systems have become widely spread and popular for handling any sort of dynamic modeling and training requirements in real-world (online) applications, especially under conditions of a growing effect of the dynamic data context, sequential video analysis, and web mining. This demand is justified by the growing dynamic and complexity of current problems as well as the ascending volumes of data bases (BD), which lead to the fact that traditional batch training is not possible any more to be applied within some reasonable time period and tolerable accuracy [1–4]. The evolving incremental learning systems should process huge amounts of data, analyze the data rapidly and extract data features on the fly. Since the data is transforming permanently, these systems must be capable of adapting their topology.

From the algorithmic point of view, the evolving system should be able to carry out some parametric adaptation. Stated another way, it has to be contributed by a set of parameters along with adaptation of the required tweaks to be implemented effectively [20, 21, 26–28, 35].

It’s well-known that deep neural networks (DNNs) [1–4] have gained a high impact on data processing recently. Although this class of networks is quite bulky when speaking of the computational implementation. And there’s a high possibility that the overfitting problem takes a place while dealing with a short training data set.

As an alternative view, it is also reasonable to generate DNN architectures on the grounds of the Group Method of Data Handling (GMDH) [8–12, 23–25]. In this connection, various systems from the area of Computational Intelligence usually enhance automatically a number of their structure layers for information handling in order to obtain the precision on demand for results. That’s a great deal of sense to separate an initial space somehow into a suite of subspaces in lower dimensions and combine the results obtained. The Group Method of Data Handling (GMDH) possesses an apparent benefit from a computational point of view. But its huge drawback is its rather poor adaptation for an online mode. That is a rather smart decision to apply GMDH characteristics to evolving cascade neural networks [8– 11, 34], although some of these systems might freeze their parameter values.

A specifically new subject of interest is a combination of hybrid systems of computational intelligence and the GMDH concepts with the general aim of new computational and theoretical results especially for Big Data Mining and Data Stream Mining [38, 39]. The GMDH-ANN topologies have been considered in [5] in terms of using specific two-input $N .$ -Adalines as structural elements. A main purpose of this topological element was to guarantee a quadratic approximation for recovering a non-linear mapping. Meanwhile, estimating the achieved quality could lead to a substantial quantity of hidden layers.

In the previous sections cascade GMDH-neo-fuzzy network and evolving GMDH-neuro-fuzzy networks and their training algorithms were considered which showed high operating speed and high approximating abilities as main performance indicators. Although both its parameters and framework are being adjusted in an online mode, but it still claims long enough training data sets.

That’s a very challenging task when there’s an obvious lack of incoming data (a short data set), and the system is not capable of tuning its parameters.

In this regard, it’s highly important to offer a hybrid neuro-fuzzy system to be trained in an online fashion and to be able of optimizing its topology while being trained. That’s also very topical to introduce the system that keeps in possession an appreciably lower number of attributes to be tweaked in comparison with other well-known compatible systems.

# 2.10.1 An Architecture of the Deep GMDH Neuro-fuzzy System

A structure of the deep GMDH neuro-fuzzy system is given in Fig. 2.31. The receptive (zero) layer of the system contains a $( n \times 1 )$ -dimensional vector of input signals ${ \boldsymbol { x } } ( { k } ) = \left( x _ { 1 } ( { k } ) , x _ { 2 } ( { k } ) , . . . , x _ { n } ( { k } ) \right) ^ { \mathrm { { T } } } ( { k } = 1 , 2 , . . . , N$ denotes in this case either an observation in a training set or an index of the current discrete time). This vector is subsequently addressed to the first hidden layer that comprises $n _ { 1 } = c _ { n } ^ { 2 }$ elements (every element owns only two inputs).

There is a special type of elements (the selection block) that accounts for choosing the best node in the strict sense of precision (in terms of an accepted criterion). For instance, the selection block in the first layer $S B ^ { [ 1 ] }$ selects $\boldsymbol { n } _ { 1 } ^ { * } \left( \boldsymbol { n } _ { 1 } ^ { * } \leq \boldsymbol { n } \right)$ signals with the highest accuracy among the output signals $\hat { y } _ { m } ^ { [ 1 ] } ( k ) ~ ( m =$ $1 , 2 , \ldots , 0 , 5 n ( n - 1 ) = c _ { n } ^ { 2 } )$ of the first layer nodes $N ^ { [ { 1 } ] }$ .

Afterwards, $n _ { 2 }$ pairwise combinations $\hat { y } _ { l } ^ { [ 1 ] * } ( k ) , \hat { y } _ { p } ^ { [ 1 ] * } ( k )$ are composed (in most cases, $n \leq n _ { 2 } \leq 2 n )$ among the mentioned above $n _ { 1 } ^ { * }$ best outputs. The signals obtained are later propagated to the second hidden layer composed by nodes $N ^ { [ 2 ] }$ in a similar manner to the neurons $N ^ { [ { 1 } ] }$ . The selection block of the second hidden layer $S B ^ { [ 2 ] }$ takes only signals which are better than $\hat { y } _ { 1 } ^ { [ 1 ] * } ( k )$ in accuracy among output signals ${ \hat { y } } _ { m } ^ { [ 2 ] } ( k )$ in the second hidden layer. The system’s evolution goes on until only two best signals $\hat { y } _ { 1 } ^ { [ s - 1 ] * } ( k )$ and $\hat { y } _ { 2 } ^ { [ s - 1 ] * } ( k )$ are being obtained at the $S B ^ { [ s - 1 ] }$ outputs. These two signals are then sent to the output node $N ^ { [ s ] }$ that calculates the system’s output signal ${ \hat { y } } ^ { [ s ] } ( k )$ .

![](images/75eb659a4894b108b3912660027e41180c7ef3e1906a772734c28e4bf4a6a005.jpg)  
Fig. 2.31 A structure of the deep GMDH neuro-fuzzy system

# 2.10.1.1 The Extended Neo-fuzzy Neuron

A model of the extended NFN was put forward in [40] as a further development and evolution of an ordinary neo-fuzzy neuron submitted by Yamakawa, Miki and Uchino [13–15].

A traditional version of the neo-fuzzy neuron is a MISO (multiple inputs and a single output) non-linear system that accounts for the permutation

$$
{ \hat { y } } = \sum _ { i = 1 } ^ { n } f _ { i } ( x _ { i } )
$$

where $x _ { i }$ signifies an $i$ component in the input vector $x = ( x _ { 1 } , . . . , x _ { i } , . . . , x _ { n } ) ^ { \mathrm { T } } \in R ^ { n }$ (of the dimensionality $n$ ), $\hat { y }$ marks a scalar output of the neo-fuzzy neuron. In its usual form, NFN embodies multiple (non-linear) synapses $N S _ { i }$ . Their purpose is to modify the ith vector element in $x _ { i }$ into

$$
f _ { i } ( x _ { i } ) = \sum _ { l = 1 } ^ { h } w _ { l i } \mu _ { l i } ( x _ { i } )
$$

where $h$ is the number of membership functions, $w _ { l i }$ defines a synaptic weight $l$ in the ith non-linear synapse, $l = 1 , 2 , . . . , h , i = 1 , 2 , . . . , n ; \mu _ { l i } ( x _ { i } )$ describes the lth membership function in the non-linear synapse $i$ that makes a great impact on fuzzification of a crisp element $x _ { i }$ . By such manners, the permutation ensured by the NFN could be noted down like

$$
{ \hat { y } } = \sum _ { i = 1 } ^ { n } \sum _ { l = 1 } ^ { h } w _ { l i } \mu _ { l i } ( x _ { i } )
$$

The NFN provides the fuzzy inference rule put into action in the form

$$
\begin{array} { r l } & { I F x _ { i } I S X _ { l i } T H E N T H E O U T P U T I S } \\ & { w _ { l i } , l = 1 , 2 , . . . , h } \end{array}
$$

which consequently infers that the synapse truthfully endows the 0th order fuzzy inference by Takagi-Sugeno [16, 17].

As mentioned previously, the NFN’s synapse $N S _ { i }$ covers the 0-order inference by Takagi-Sugeno only producing the simplest Wang-Mendel neuro-fuzzy system [41, 42]. It seems quite valid to expand approximating capabilities of this computational node by introducing a specified topological element to have been called an “extended nonlinear synapse” [40] $\left( E N S _ { i } \right)$ and to develop the “extended neo-fuzzy neuron” (ENFN) that embraces $E N S _ { i }$ units instead of conventional synapses $N S _ { i }$ .

Considering in detail additional parameter values

$$
\varphi _ { l i } ( x _ { i } ) = \mu _ { l i } ( x _ { i } ) \left( w _ { l i } ^ { 0 } + w _ { l i } ^ { 1 } x _ { i } + w _ { l i } ^ { 2 } x _ { i } ^ { 2 } + \cdot \cdot \cdot + w _ { l i } ^ { p } x _ { i } ^ { p } \right) ,
$$

$$
\begin{array} { r l r } {  { f _ { i } ( x _ { i } ) = \sum _ { l = 1 } ^ { h } \mu _ { l i } ( x _ { i } ) \big ( w _ { l i } ^ { 0 } + w _ { l i } ^ { 1 } x _ { i } + w _ { l i } ^ { 2 } x _ { i } ^ { 2 } + \cdots + w _ { l i } ^ { p } x _ { i } ^ { p } \big ) } } \\ & { } & { \qquad = w _ { 1 i } ^ { 0 } \mu _ { 1 i } ( x _ { i } ) + w _ { 1 i } ^ { 1 } x _ { i } \mu _ { 1 i } ( x _ { i } ) + \ldots + w _ { 1 i } ^ { p } x _ { i } ^ { p } \mu _ { 1 i } ( x _ { i } ) } \\ & { } & { \qquad + w _ { 2 i } ^ { 0 } \mu _ { 2 i } ( x _ { i } ) + \cdots + w _ { 2 i } ^ { p } x _ { i } ^ { p } \mu _ { 2 i } ( x _ { i } ) + \cdots + w _ { h i } ^ { p } x _ { i } ^ { p } \mu _ { h i } ( x _ { i } ) , } \end{array}
$$

$$
\begin{array} { r l } & { w _ { i } = \big ( w _ { 1 i } ^ { 0 } , w _ { 1 i } ^ { 1 } , . . . , w _ { 1 i } ^ { p } , w _ { 2 i } ^ { 0 } , . . . , w _ { 2 i } ^ { p } , . . . , w _ { h i } ^ { p } \big ) ^ { \mathrm { T } } , } \\ & { \quad \quad \tilde { \mu } _ { i } ( \boldsymbol { x } _ { i } ) = \big ( \mu _ { 1 i } ( \boldsymbol { x } _ { i } ) , x _ { i } \mu _ { 1 i } ( \boldsymbol { x } _ { i } ) , . . . , x _ { i } ^ { p } \mu _ { 1 i } ( \boldsymbol { x } _ { i } ) , } \\ & { \quad \quad \mu _ { 2 i } ( \boldsymbol { x } _ { i } ) , . . . , x _ { i } ^ { p } \mu _ { 2 i } ( \boldsymbol { x } _ { i } ) , . . . , x _ { i } ^ { p } \mu _ { h i } ( \boldsymbol { x } _ { i } ) \big ) ^ { \mathrm { T } } , } \end{array}
$$

present them in the following abridged form

$$
f _ { i } ( x _ { i } ) = w _ { i } ^ { T } \tilde { \mu } _ { i } ( x _ { i } ) ,
$$

$$
\hat { y } = \sum _ { i = 1 } ^ { n } f _ { i } ( x _ { i } ) = \sum _ { i = 1 } ^ { n } w _ { i } ^ { \mathrm { T } } \tilde { \mu } ( x _ { i } ) = \tilde { w } ^ { \mathrm { T } } \tilde { \mu } ( x )
$$

where $\tilde { \mu } ( x ) = \big ( \tilde { \mu } _ { 1 } ^ { T } ( x _ { 1 } ) , . . . , \tilde { \mu } _ { i } ^ { T } ( x _ { i } ) , . . . , \tilde { \mu } _ { n } ^ { T } ( x _ { n } ) \big ) ^ { \mathrm { T } } ,$

$$
\boldsymbol { \tilde { w } } ^ { T } = \left( w _ { 1 } ^ { T } , . . . , w _ { i } ^ { T } , . . . , w _ { n } ^ { T } \right) ^ { T } .
$$

It can be noted easily that the ENFN holds $( p + 1 ) h n$ parameters (synaptic weights) to be adapted and the fuzzy inference realized by each $E N S _ { i }$ is

$$
\begin{array} { r l } & { I F x _ { i } I S X _ { l i } T H E N T H E O U T P U T I S } \\ & { w _ { l i } ^ { 0 } + w _ { l i } ^ { 1 } x _ { i } + . . . + w _ { l i } ^ { p } x _ { i } ^ { p } , \quad l = 1 , 2 , . . . , h } \end{array}
$$

which ties up to the Takagi-Sugeno inference of the $p$ th order.

The ENFN’s framework is not so complicated in comparison with the conventional neuro-fuzzy system. The architecture of the extended neo-fuzzy neuron and the extended neo-fuzzy synapse are given in Figs. 2.32 and 2.33.

The usage of the scatter partitioning of the input space [21] can cause the appearing of “gaps” in the fuzzified space. To avoid this problem one can use the bell-shaped constructions with non-strictly local receptive support as membership functions. Mostly the Gaussians are used as membership functions of the first layer

![](images/726288ff14d267ea7950558a6f4d9ecda939698aa72ed8ef099231496f60d6b4.jpg)  
Fig. 2.32 An extended neo-fuzzy neuron

![](images/edc56b63282731b89ed65235a99b8a2636a95253278fc130d3c93a0982bb03e1.jpg)  
Fig. 2.33 An extended neo-fuzzy synapse

$$
\mu _ { l i } ( x _ { i } ( k ) ) = \exp \left( - \frac { ( x _ { i } ( k ) - c _ { l i } ( k ) ) ^ { 2 } } { 2 \sigma _ { l i } ^ { 2 } ( k ) } \right)
$$

where $c _ { l i } ( k )$ is the parameter that defines the center of the membership function, $\sigma _ { l i } ( k )$ is the width parameter of this function.

# 2.10.2 The Adjustment Procedures for All Parameters of the System

With regard to the fact that the reference signal $\hat { y } _ { s } ^ { [ 1 ] } ( k )$ in every system node is in linear dependence on the configurable synaptic weights $w _ { l i }$ , one can make use of both either the established least squares method or its recurrent fashion to tune them. If the data to be trained is not stationary, it is feasible enough to apply the exponentially weighted recurrent least squares algorithm to adjust the weights as represented by

$$
\left\{ \begin{array} { l l } { \tilde { w } ( k ) = \tilde { w } ( k - 1 ) + \frac { P ( k - 1 ) \Big ( y ( k ) - ( \tilde { w } ( k - 1 ) ) ^ { \mathrm { T } } \tilde { \mu } ( x ( k ) ) \Big ) \tilde { \mu } ( x ( k ) ) } { \alpha + ( \tilde { \mu } ( x ( k ) ) ) ^ { \mathrm { T } } P ( k - 1 ) \tilde { \mu } ( x ( k ) ) } , } \\ { P ( k ) = \frac { 1 } { \alpha } \left( P ( k - 1 ) - \frac { P ( k - 1 ) \tilde { \mu } ( x ( k ) ) ( \tilde { \mu } ( x ( k ) ) ) ^ { \mathrm { T } } P ( k - 1 ) } { \alpha + ( \tilde { \mu } ( x ( k ) ) ) ^ { \mathrm { T } } P ( k - 1 ) \tilde { \mu } ( x ( k ) ) } \right) } \end{array} \right.
$$

(where $0 < \alpha \leq 1$ denotes a forgetting feature, and $y ( k )$ implies the reference signal) or the exponentially weighted gradient learning procedure

$$
\left\{ \begin{array} { l l } { \tilde { w } ( k ) = \tilde { w } ( k - 1 ) + \frac { \Big ( y ( k ) - ( \tilde { w } ( k - 1 ) ) ^ { \mathrm { T } } \tilde { \mu } ( x ( k ) ) \Big ) \tilde { \mu } ( x ( k ) ) } { \beta ( k ) } , } \\ { \beta ( k ) = \alpha \beta ( k - 1 ) + \| \tilde { \mu } ( x ( k ) ) \| ^ { 2 } , 0 \leq \alpha \leq 1 . } \end{array} \right.
$$

A process of tuning both parameters of the centers and the synaptic weights may be implemented by means of the gradient procedures for minimization of the learning criterion

$$
E ( k ) = { \frac { 1 } { 2 } } { \big ( } y ( k ) - { \hat { y } } ( k ) { \big ) } ^ { 2 } = { \frac { 1 } { 2 } } { \Big ( } y ( k ) - { \big ( } { \tilde { w } } ( k ) { \big ) } ^ { \mathrm { T } } { \tilde { \mu } } ( x ( k ) ) { \Big ) } ^ { 2 }
$$

in the form of

$$
\left\{ \begin{array} { l l } { c _ { r i } ( k ) = c _ { r i } ( k - 1 ) - \eta _ { c } \frac { \partial E ( k ) } { \partial c _ { r i } } , } \\ { \tilde { \sigma } _ { r i } ^ { 2 } ( k ) = \tilde { \sigma } _ { r i } ^ { 2 } ( k - 1 ) - \eta _ { \sigma } \frac { \partial E ( k ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } } \end{array} \right.
$$

where $r = 1 , 2 , . . . , h ; \eta _ { c } , \eta _ { \sigma }$ signify learning rates for the centers’ and the widths’ parameters are denoted correspondingly, $\tilde { \sigma } _ { r i } ^ { 2 } ( k ) = - 0 , 5 \sigma _ { r i } ^ { - 2 } ( k )$ . Based on the previous expressions, the following expressions are obtained

$$
\left\{ \begin{array} { l } { \frac { \partial E ( k ) } { \partial c _ { r i } } = \Big ( ( \tilde { w } ( k ) ) ^ { \mathrm { T } } \tilde { \mu } ( x ( k ) ) - y ( k ) \Big ) \frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial c _ { r i } } , } \\ { \frac { \partial E ( k ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } = \Big ( ( \tilde { w } ( k ) ) ^ { \mathrm { T } } \tilde { \mu } ( x ( k ) ) - y ( k ) \Big ) \frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } . } \end{array} \right.
$$

Following on from (2.50), the derivatives $\frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial c _ { r i } }$ and $\frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } }$ could be presented in the form:

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial c _ { r i } } = \frac { \partial \varphi _ { r i } ( x _ { i } ( k ) ) } { \partial c _ { r i } } = \sum _ { t = 0 } ^ { p } w _ { r i } ^ { t } x _ { i } ^ { t } \frac { \partial \mu _ { r i } ( x _ { i } ( k ) ) } { \partial c _ { r i } } , } \\ { \displaystyle \frac { \partial f _ { i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } = \frac { \partial \varphi _ { r i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } = \sum _ { t = 0 } ^ { p } w _ { r i } ^ { t } x _ { i } ^ { t } \frac { \partial \mu _ { r i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } , } \end{array} \right.
$$

Basing on (2.45), the derivatives $\frac { \partial \mu _ { r i } ( x _ { i } ( k ) ) } { \partial c _ { r i } }$ and @lri xiðkÞÞ can be presented as

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial \mu _ { r i } ( x _ { i } ( k ) ) } { \partial c _ { r i } } = \frac { x _ { i } ( k ) - c _ { r i } ( k ) } { \sigma _ { r i } ^ { 2 } ( k ) } \mathrm { e x p } \left( - \frac { \left( x _ { i } ( k ) - c _ { r i } ( k ) \right) ^ { 2 } } { 2 \sigma _ { r i } ^ { 2 } ( k ) } \right) , } \\ { \displaystyle \frac { \partial \mu _ { r i } ( x _ { i } ( k ) ) } { \partial \tilde { \sigma } _ { r i } ^ { 2 } } = ( x _ { i } ( k ) - c _ { r i } ( k ) ) ^ { 2 } \mathrm { e x p } \left( - \frac { \left( x _ { i } ( k ) - c _ { r i } ( k ) \right) ^ { 2 } } { 2 \sigma _ { r i } ^ { 2 } ( k ) } \right) . } \end{array} \right.
$$

In this way, all the system nodes’ parameters (synaptic weights, centers and width parameters for the membership functions) may be adjusted. Concerning the successive layers, the nodes’ parameters are usually tuned quite the same way as the nodes in the first hidden layer.

It’s worth to note that inputs of the $s$ -th layer are a pairwise combination of the signals $\hat { y } _ { l } ^ { [ s - 1 ] * } , \hat { y } _ { p } ^ { [ s - 1 ] * }$ formed by the selection block $S B ^ { [ s - 1 ] }$ . The reference signal $y ( k )$ is the same one for all the blocks of the evolving complex system. The algorithm operates until the stopping criterion holds—MSE of the best node of current layer s starts to rise. Then the best neuron of the previous layer determines optimal deep network structure.

# 2.10.3 An Experimental Study

The Darwin sea level pressure data set was chosen from the Data Market data storage to showcase a advantage of the offered deep GMDH system and its learning schemes. It was mainly used for non-stationary signals’ prediction. The data set presents chiefly a monthly sea level pressure for a period of more than a century (1882–1998). A general size of this data sample is 1400 observations. The system used 1100 observations to get trained and 300 observations to get tested. To estimate the efficiency of the proposed neuro-fuzzy system is, we also considered a multilayer perceptron, a radial-basis function neural network, and ANFIS for solving the same task. The results obtained were estimated according to the MSE criterion. Table 2.8 gives a demonstration of the systems’ performance. The proposed deep GMDH system illustrated quite good results while handling the prediction task. It is worth mentioning that its training time was short enough compared to analogues. At the same time, its forecasting results were the best ones for this data set. Figure 2.34 demonstrates a fragment of the learning process.

Table 2.8 Experimental results   

<html><body><table><tr><td>A system</td><td>A learning error</td><td>A test error</td><td>Training time (s)</td></tr><tr><td>The proposed deep GMDH system</td><td>0.0146</td><td>0.0156</td><td>0.2067</td></tr><tr><td>MLP</td><td>0.0150</td><td>0.0168</td><td>0.2500</td></tr><tr><td>ANFIS</td><td>0.0157</td><td>0.0165</td><td>0.2031</td></tr><tr><td>RBFNN</td><td>0.0172</td><td>0.0224</td><td>0.2391</td></tr></table></body></html>

![](images/6b8accaa7b54ff6bd7af51f4155e52cc1f5824e8bfe2a186b6ad11ef42707630.jpg)  
Fig. 2.34 Prediction results

# Conclusion

In this chapter new class of neural networks—Deep networks are considered and their learning algorithms are presented and discussed. For deep learning implementation encoders-decoders, restricted Boltzman machines (RBM) and stacked RBM are used. The main problems connected with Deep learning—vanishing and exploding gradient are considered and methods of their solution are presented and discussed.

New approach to Deep learning based on application of GMDH to synthesis and learning of neuro-fuzzy networks is suggested and developed in this chapter.

The deep evolving neuro-fuzzy system presented here doesn’t require any high data volumes to get trained. The hybrid system is grounded on both the Group Method of Data Handling and the concept of evolving systems that makes it possible to define both optimal parameter values and the best structure in every specific case. Adjusting parameters in a parallel fashion gives an option of increasing a processing speed of data handling. The system’s architecture may be evolving in an online mode as the synaptic weights, centers and widths’ parameters of the proposed neuro-fuzzy nodes are being tuned. This approach enables to overcome some problems of Big Data dimensionality in practical tasks of forecasting, classification and pattern recognition.

# References

1. G. Hinton, S. Osindero, Y.-W. Teh, A fast learning algorithm for deep belief nets. Neural Comput. 18(7), 1527–1554 (2006) 2. I. Goodfellow, Y. Bengio, A. Courville, Deep Learning (MIT Press, 2016) 3. Y. Bengio, Y. LeCun, G. Hinton, Deep learning. Nature 521, 436–444 (2015) 4. J. Schmidhuber, Deep learning in neural networks: an overview. Neural Netw. 61   
5. E. Lughofer, Evolving Fuzzy Systems—Methodologies, Advanced Concepts and Applications (Springer, Berlin, 2011, 2015), pp. 85–117   
6. Z. Hu, Y.V. Bodyanskiy, O.K. Tyshchenko, A cascade deep neuro-fuzzy system for high-dimensional online possibilistic fuzzy clustering, in Proceedings of the XI-th International Scientific and Technical Conference “Computer Science and Information Technologies” (CSIT 2016) (2016), pp. 119–122. https://doi.org/10.1109/stc-csit.2016. 7589884   
7. P. Angelov, D. Filev, N. Kasabov, Evolving Intelligent Systems: Methodology and Applications (Willey, 2010)   
8. Y.V. Bodyanskiy, O.A. Vynokurova, A.I. Dolotov, Self-learning cascade spiking neural network for fuzzy clustering based on group method of data handling. J. Autom. Inform. Sci. 45(3), 23–33 (2013) 9. Y. Bodyanskiy, O. Vynokurova, A. Dolotov, O. Kharchenko, Wavelet-neuro-fuzzy network structure optimization using GMDH for the solving forecasting tasks, in Proceedings of the 4th International Conference on Inductive Modelling ICIM 2013, Kyiv (2013), pp. 61–67   
10. Y. Bodyanskiy, O. Vynokurova, N. Teslenko, Cascade GMDH-wavelet-neuro-fuzzy network, in Proceedings of the 4th International Workshop on Inductive Modeling «IWIM 2011» , Kyiv, Ukraine (2011), pp. 22–30   
11. Y. Bodyanskiy, Y. Zaychenko, E. Pavlikovskaya, M. Samarina, Y. Viktorov, The neo-fuzzy neural network structure optimization using the GMDH for the solving forecasting and classification problems, in Proceedings of the International Workshop on Inductive Modeling, Krynica, Poland (2009), pp. 77–89   
12. A.G. Ivakhnenko, Heuristic self-organization in problems of engineering cybernetics. Automatica 6(2), 207–219 (1970)   
13. T. Yamakawa, E. Uchino, T. Miki, H. Kusanagi, A neo fuzzy neuron and its applications to system identification and prediction of the system behavior, in Proceedings of the 2nd International Conference on Fuzzy Logic and Neural Networks (1992), pp. 477–483   
14. E. Uchino, T. Yamakawa, Soft computing based signal prediction, restoration and filtering, in Intelligent Hybrid Systems: Fuzzy Logic, Neural Networks and Genetic Algorithms (Kluwer Academic Publisher, Boston, 1997), pp. 331–349   
15. T. Miki, T. Yamakawa, Analog implementation of neo-fuzzy neuron and its on-board learning, in Computational Intelligence and Applications (WSES Press, Piraeus, 1999), pp. 144–149   
16. M. Sugeno, G.T. Kang, Structure identification of fuzzy model. Fuzzy Sets Syst. 28, 15–33 (1998)   
17. T. Takagi, M. Sugeno, Fuzzy identification of systems and its applications to modeling and control. IEEE Trans. Syst. Man Cybern. 15, 116–132 (1985)   
18. N. Kasabov, Evolving Connectionist Systems (Springer, London, 2003)   
19. E. Lughofer, Evolving Fuzzy Systems—Methodologies, Advanced Concepts and Applications (Springer, Berlin, 2011)   
20. R.J.-S. Jang, ANFIS: adaptive-network-based fuzzy inference systems. IEEE Trans. Syst. Man Cybern. 23, 665–685 (1993)   
21. R.J.-S. Jang, C.-T. Sun, E. Mizutani, Neuro-Fuzzy and Soft Computing: A Computational Approach to Learning and Machine Intelligence (Prentice Hall, Upper Saddle River, 1997)   
22. S. Osowski, Sieci neuronowe do przetwarzania informacji (Oficyna Wydawnicza Politechniki Warszawskiej, Warszawa, 2006)   
23. A.G. Ivakhnenko, Long-Term Forecasting and Control of Complex Systems (Technica, Kiev, 1975)   
24. A.G. Ivakhnenko, Polynomial theory of complex systems. IEEE Trans. Syst. Man. Cybern. 1 (4), 364–378 (1971)   
25. A.G. Ivakhnenko, Self-Learning Systems of Recognition and Automatic Control (Technica, Kiev, 1969)   
26. A.G. Ivakhnenko, D. Wuensch, G.A. Ivakhnenko, Inductive sorting-out GMDH algorithms with polynomial complexity for active neurons of neural networks. Neural Netw. 2, 1169– 1173 (1999)   
27. A.G. Ivakhnenko, G.A. Ivakhnenko, J.A. Mueller, Self-organization of the neural networks with active neurons. Pattern Recognit. Image Anal. 4(2), 177–188 (1994)   
28. G.A. Ivakhnenko, Self-organization of neuronet with active neurons for effects of nuclear test explosions forecasting. Syst. Anal. Model. Simul. 20, 107–116 (1995)   
29. K.S. Narendra, K. Parthasarathy, Identification and control of dynamical systems using neural networks. IEEE Trans. Neural Netw. 1, 4–26 (1990)   
30. T. Kondo, Identification of radial basis function networks by using revised GMDH-type neural networks with a feedback loop, in Proceedings of the SICE Annual Conference, Tokyo, Japan (2002), pp. 2882–2887   
31. T. Ohtani, Automatic variable selection in RBF network and its application to neurofuzzy GMDH, in Proceedings of the Fourth International Conference on Knowledge-Based Intelligent Engineering Systems and Allied Technologies, vol. 2 (2000), pp. 840–843   
32. Yu. Zaychenko, The fuzzy group method of data handling and its application for economical processes forecasting. Sci. Inq. 7(1), 83–96 (2006)   
33. T. Ohtani, H. Ichihashi, T. Miyoshi, K. Nagasaka, Y. Kanaumi, Structural learning of neurofuzzy GMDH with Minkowski norm, in Proceedings of the 1998 Second International Conference on Knowledge-Based Intelligent Electronic Systems, vol. 2 (1998), pp. 100–107   
34. Y. Bodyanskiy, O. Vynokurova, I. Pliss, Hybrid GMDH-neural network of computational intelligence, in Proceedings of the 3rd International Workshop on Inductive Modeling, Krynica, Poland (2009), pp. 100–107   
35. A.G. Ivakhnenko, V.S. Stepashko, Disturbance Tolerance of Modeling (Naukova Dumka, Kiev, 1985)   
36. Y. Bodyanskiy, N. Teslenko, P. Grimm, Hybrid evolving neural network using kernel activation functions, in Proceedings 17th Zittau East-West Fuzzy Colloquium, Zittau/Goerlitz, HS (2010), pp. 39–46   
37. D.T. Pham, X. Liu, Neural Networks for Identification, Prediction and Control (Springer, London, 1995)   
38. A. Bifet, Adaptive Stream Mining: Pattern Learning and Mining from Evolving Data Streams (IOS Press, Amsterdam, 2010)   
39. C.C. Aggarwal, Data Streams: Models and Algorithms (Advances in Database Systems) (Springer, New York, 2007)   
40. Y. Bodyanskiy, O. Tyshchenko, D. Kopaliani, An extended neo-fuzzy neuron and its adaptive learning algorithm. Int. J. Intell. Syst. Appl. (IJISA) 7(2), 21–26 (2015)   
41. L.-X. Wang, Adaptive Fuzzy Systems and Control. Design and Statistical Analysis (Prentice Hall, Upper Saddle River, 1994)   
42. L.-X. Wang, J.M. Mendel, Fuzzy basis functions, universal approximation, and orthogonal least-squares learning. IEEE Trans. Neural Netw. 3(5), 807–814 (1992)

# Chapter 3 Pattern Recognition in Big Data Analysis

# 3.1 Introduction

Data classification and pattern recognition substitute one of the widely used class of problems in Data Mining. Up to date many methods and algorithms were developed for pattern recognition in different spheres of science and technology. Most of the modern methods of classification may be divided into following classes:

(1) methods based on statistical decision-making theory, incl. Bayesian methods based on application of conditional probability distributions;   
(2) methods of discriminant analysis, incl. well-known SVM method and its derivatives;   
(3) algebraic and linguistic methods;   
(4) neural networks;   
(5) fuzzy logic systems and fuzzy neural networks (FNN);   
(6) special methods.

But for solution of classification problems with BD it’s extremely important is the development of new adequate methods or further improvement of existing methods which take into account the high dimension of BD warehouses. Most of them use various approaches and algorithms of dimensionality reduction, e.g. Principal component method (PCM) and similar techniques.

Another constructive approach for BD dimensionality reduction is hierarchical organization of data.

In this chapter classification method based FNN is considered and some algorithms of classification problems dimensionality reduction are presented and discussed. In the Sect. 3.2 FNN NEFClass is considered Its architecture and training algorithm is presented and investigated. In the Sect. 3.3 modified FNN NEFClass M is described free of some drawbacks of basic FNN NEFCLass its training algorithms are described and analyzed.

In Sect. 3.5 application of FNN NEFClass M for optical images recognition obtained with multi spectral system is presented and analyzed. In the Sect. 3.6 implementation of FNN for medical images of uterus classification in the problem of express diagnostics is considered.

In the Sect. 3.7 the hybrid CNN-FNN network is considered which was suggested for medical images of breast tumor recognition in the problem of medical diagnostics. The experimental of the suggested approach are presented and its practical implementation for medical images classification and is described. The reduction of features dimensionality in his problem was considered and for its solution Principal components method was suggested and its efficiency was estimated. The suggested approach may be used for solution BD classification problems.

# 3.2 FNN NEFClass. Architecture, Properties, the Algorithms of Learning of Base Rules and Membership Functions

A classification problem is one of the most actual spheres of application of the computational intelligence systems. For its decision different approaches and methods were suggested, among which popular solutions were offered, combining neural networks and fuzzy inference systems. One of such decisions is the system NEFClass (NEuro-Fuzzy CLASSifier), based on the generalized architecture of fuzzy perceptron and suggested by D. Nauck and R. Kruse in [1–3].

Both original and modified model of NEFClass are derivative from the general model of fuzzy perceptron [4]. A model purpose is a development of fuzzy rules from a set of data which can be divided into the several non-overlapping classes. The fuzziness arises up due to the imperfect or incomplete measuring of properties of objects, subject to classification.

Fuzzy rules, describing expert information, have the following form:

if is $\mu _ { 1 i }$ and $x _ { 2 }$ is $\mu _ { 2 i }$ and … and $x _ { n }$ is $\mu _ { n i }$ , then pattern $\left( x _ { 1 } , x _ { 2 } , . . . . , x _ { n } \right)$ belongs to the class of $i$ ,

where $\mu _ { 1 i } , . . . , \mu _ { n i }$ ; are MF of fuzzy sets.

The goal of NEFClass is to define these rules, as well as parameters of membership functions for fuzzy sets. It was assumed here, that intersection of two different sets is empty.

The system NEFClass has 3-layer successive architecture (see Fig. 3.1). The first layer $U _ { 1 }$ contains inputs neurons which inputs patterns are fed in. Activating of these neurons does not change usually input values. The hidden layer $U _ { 2 }$ contains fuzzy rules, and the third layer $U _ { 3 }$ consists of output neurons (classifiers).

![](images/6184dbbb0c187a8d54cae28506d942f88d974d40847d887e34d76c35ffb51ffb.jpg)  
Fig. 3.1 Structure of FNN NEFCLASS

Activations of rule neurons and neurons of output layer with the pattern of $\boldsymbol { \mathrm { ~ p ~ } }$ are calculated so:

$$
a _ { R } ^ { ( p ) } = \operatorname* { m i n } _ { x \in U _ { 1 } } \Bigl \{ W ( x , R ) ( a _ { x } ^ { ( p ) } ) \Bigr \} ,
$$

$$
a _ { C } ^ { ( p ) } = \sum _ { R \in U _ { 2 } } W ( c , R ) \cdot a _ { R } ^ { ( p ) } ) ,
$$

or alternatively

$$
a _ { C } ^ { ( p ) } = \operatorname* { m a x } _ { R \in U _ { 2 } } \Bigl \{ a _ { R } ^ { ( p ) } \Bigr \} ,
$$

where $W ( x , r )$ is a fuzzy weight of connection of input neuron $x$ with a rule neuron $R$ , and $W ( R , c )$ —fuzzy weight of connection of a rule neuron $R$ with the neuron $c$ of output layer. Instead of application of operations of maximum and minimum it is possible to use other functions of so-called “t-norm” and “t-co-norm” accordingly [1].

A rule base is approximation of unknown function and describes a classification task $\phi ( x )$ , such, that $c _ { i } = 1 , ~ c _ { j } = 0 ~ ( j = 1 , . . . , m , \forall ~ j \neq i )$ , if pattern $x$ belongs to the class $C _ { i }$ .

Every fuzzy set is marked a linguistic term, such as «large», «small», «middle» et cetera. Fuzzy sets and linguistic rules present approximation of classifying function and determine the result of the system NEFClass. They are obtained from a sample by learning. It’s necessary, that for every linguistic value (for example, $\mathfrak { K } _ { 1 }$ is positive and large») there should be only one presentation of fuzzy set.

# Learning in the System NEFClass

The system NEFClass can be built on partial knowledge about patterns. An user must define the amount of initial fuzzy sets for each of object features (number of terms) and set the value $k _ { m a x }$ that is a maximal number of rule nodes, which can be created in the hidden layer. For learning triangular MF are used.

Consider the system of NEFClass with n input neurons $x _ { 1 } , . . . , x _ { n } , k \left( k \leq k _ { \operatorname* { m a x } } \right)$ rule neurons and $m$ output neurons $c _ { 1 } , . . . , c _ { m } ,$ . The learning sample of patterns is also given: $L = \{ ( p _ { 1 } , t _ { 1 } ) , . . . , ( p _ { s } , t _ { s } ) \}$ , each of which consists of input pattern $p \in$ $R ^ { n }$ and desired pattern $t \in \{ 0 , 1 \} ^ { m }$ .

A learning algorithm consists of two stages.

Stage 1. Generation of rule base.

The first stage whose purpose is to create rule neurons of the system NEFClass consists of the followings steps [1–3]:

1. Choose a next pattern $( p , t )$ from sample $L$ .   
2. For every input neuron $x _ { i } \in U _ { 1 }$ find such membership $\mu _ { J _ { i } } ^ { i }$ that

$$
\mu _ { J i } ^ { ( i ) } = \operatorname* { m a x } _ { j \in 1 , . . q _ { 1 } } \{ \mu _ { j i } ^ { ( i ) } ( p _ { i } ) \} ,
$$

where xi pi

3. If a number of rule nodes $k$ is less than $k _ { \mathrm { m a x } }$ and there is no rule node $R$ such, that

$$
W ( x _ { 1 } , R ) = \mu _ { J 1 } , . . . , W ( x _ { n } , R ) = \mu _ { J n }
$$

then create such node and connect it with an output node $c _ { i }$ , if $t _ { i } = 1$ , and connect it with all input neurons and assign the corresponding weights $\mu _ { J _ { i } } ^ { i }$ to connections.

4. If there are still not-processed patterns in $L$ and $k < k _ { \mathrm { m a x } }$ , then go to the step 1 and continue learning using next pattern, and otherwise stop.   
5. Determine a rule base by one of three procedures: a. “Simple” rules learning: we leave the first $k$ rules only (stop creation of rules, if it was created $k = k _ { \mathrm { m a x } }$ rules). b. The “best” learning rules: we process patterns in $L$ and accumulate activating of every rule neuron for every class of patterns which were entered into system NEFClass. If rule neuron $R$ shows the greater accumulation of activating for a class $C _ { j }$ than for a class $C _ { R }$ , which was specified initially for

this rule, then change implication of rule $\mathrm { ~ \bf ~ R ~ }$ from $C _ { R }$ to $C _ { j } ,$ that means connect $R$ with the output neuron $c _ { j } .$ We continue processing of patterns in $L$ farther and calculate for every rule neuron the activation function:

$$
V _ { R } = \sum _ { p \in L } { a _ { R } ^ { ( p ) } \cdot e _ { p } }
$$

where

$$
e _ { p } = \left\{ \begin{array} { c l } { { 1 , } } & { { i f p a t t e r n p i s c l a s s i f i e d c o r r e c t l y } } \\ { { - 1 , } } & { { o t h e r w i s e } } \end{array} \right.
$$

We leave $k$ rule neurons with the greatest values of $V _ { R }$ and delete other rule neurons from the system NEFClass.

c. The “best for every class” algorithm of learning: we operate as in the previous case, but leave for each class $C _ { j }$ only those best $\bigg [ \frac { k } { m } \bigg ]$ rules, the consequences of which relate to the class $C _ { j }$ (where $[ x ]$ is integer part from $x$ ).

# Learning of Fuzzy Sets MF

# Stage 2

On the second stage learning of parameters of membership functions (MF) of fuzzy sets is performed. A learning algorithm with teacher of the system NEFClass must adapt MF of fuzzy sets. The algorithm cyclic runs through all learning patterns of the sample L, executing the following steps, until one of stop criteria will be fulfilled [1–3].

Steps:

1. Choose a next pattern $( p , t )$ from sample $L$ , enter it into FNN NEFclass and determine an output vector $c$ .   
2. For every output neuron $\mathbf { c _ { i } }$ calculate the value $\delta _ { C _ { i } }$

$$
\delta _ { { \cal C } _ { i } } = t _ { i } - a _ { { \cal C } _ { i } } ,
$$

where $t _ { i }$ is a desired output, $\boldsymbol { a } _ { c _ { i } }$ is an real output of neuron $c _ { i }$ .

3. For every rule neuron $R$ , for which output is $a _ { R } > 0$ execute:

a. determine a value $\delta _ { R }$ , equal

$$
\delta _ { R } = a _ { R } \cdot ( 1 - a _ { R } ) \cdot \sum _ { C \in U _ { 3 } } W ( R , C ) \delta _ { C }
$$

b. Find such $x ^ { \prime }$ , that

$$
W ( x ^ { \prime } , R ) ( a _ { x ^ { \prime } } ) = \operatorname* { m i n } _ { x \in U _ { 1 } } \bigl \{ W ( x , R ) ( a _ { x } ) \bigl \} .
$$

c. For fuzzy sets $W ( x ^ { \prime } , R )$ determine displacement (shift) of parameters of MF $\Delta _ { a } , \Delta _ { b } , \Delta _ { c }$ , using learning speed $\sigma > 0$ :

$$
\begin{array} { c } { \Delta _ { b } = \sigma \cdot \delta _ { R } \cdot ( c - a ) \cdot \mathrm { s g n } ( a _ { x ^ { \prime } } - b ) , } \\ { \Delta _ { a } = - \sigma \cdot \delta _ { R } \cdot ( c - a ) + \Delta _ { b } , } \\ { \Delta _ { c } = \sigma \cdot \delta _ { R } \cdot ( c - a ) + \Delta _ { b } . } \end{array}
$$

and execute the changes of $W ( x ^ { \prime } , R )$ .

d. Calculate an rule error:

$$
E = a _ { R } \cdot ( 1 - a _ { R } ) \cdot \sum _ { c \in U _ { 3 } } \left( 2 \cdot W ( R , c ) - 1 \right) \cdot | \delta _ { c } | .
$$

End of iteration. Repeat the described iterations until condition of stop will be fulfilled. It is possible to use as criteria of stop, for example, such:

1. An error has not decreased during n iterations.   
2. Stop learning after achievement of the defined (desirably close to the zero) error value.

# 3.3 Analysis NEFClass Properties. The Modified System NEFClassM

FNN NEFClass has several obvious advantages, distinguishing it among the other classification systems. The most important are: easiness of implementation, high-speed algorithms of learning, as well as that is the most important, high accuracy of data classification—at the level of the best systems in this area. However, the basic system NEFClass has some shortcomings:

1. formulas used for parameters learning are empirical in nature, in addition, 2. it is not clear how to choose in the learning algorithm the learning speed parameter $\sigma$ .

Therefore, these shortcomings were deleted in the modification of basic system – so-called system NEFClass-M (modified) developed in [5].

Randomization and careful selection rate constants learning $\sigma$ are inherent properties of the system NEFCLASS-M. These properties have been designed to mitigate the impact some of the shortcomings the original model and have made it possible to achieve a significant improvement in the quality of classification.

Randomization. Because of the nature of the training algorithm “simple” rules base and learning algorithm of fuzzy sets, the outcome of the training network for these algorithms are highly dependent on order, in which samples are represented in a learning sample. If, for example, the samples will be sorted by classes, the system will better classify the patterns of one class and substantially worse—the patterns of the other class. Ideally, the patterns in the training sample must be randomly mixed, in order to avoid the negative effect.

Implementation of the system NEFClassM [5] avoids this complexity by “randomization of patterns order in a learning sample after its boot. Moreover, such “randomization” occurs before each iteration of learning algorithm. As further experiments had shown, this allows to achieve a more stable and, often, the better classification results, which do not depend on the order in which patterns in a learning sample has been submitted by a user.

Choice of speed training. In the learning algorithm of fuzzy sets in the model NEFCLASS is used parameter training speed $\sigma$ . As experiments had shown, carried out in the course of developing the NEFClass M, this parameter plays a vital role in the success of the training.

The experiments had shown that, under other parameters being equal, for each specific task training there exists a certain value $\sigma$ , which ensures a minimum percentage of erroneous classification after the training. Unfortunately, to obtain analytical dependence for optimal parameter value is very difficult because learning algorithm NEFCLASS as a whole is empirical; however, using search and try method it was found that for many tasks optimal value $\sigma$ lies in the narrow range [0.06–0.1], in particular it may be equal to 0.07. This value has been set for the program which implements a modified model NEFClass M [5].

# 3.3.1 The Modified Model NEFCLASS

Consider the basic shortcomings in the NEFCLass learning algorithm.

The analysis of the drawbacks of NEFCLASS has shown that their principal cause lies mostly in an empirical learning algorithm of fuzzy sets. Therefore, a natural approach, aimed to correct the situation, was the replacement of empirical learning algorithm by the strict optimization algorithm with all the ensuing consequences for network architecture and algorithms.

Both the original and modified model NEFCLASS are based on the architecture of a fuzzy perceptron [1, 5, 6]. Architectural differences of the original and the modified model lie in the form of membership functions of fuzzy sets, function t-norm for calculation rules activations of neurons, as well as aggregating function (t-conorms), determining the activation of output neurons.

The application of numerical optimization methods requires differentiability of the membership functions of fuzzy sets—condition to which the triangular membership functions don’t satisfy. Therefore the modified model of fuzzy sets uses the Gaussian membership functions, described as

$$
\mu ( x ) = \exp \left\{ - \frac { ( x - a ) ^ { 2 } } { 2 b ^ { 2 } } \right\} .
$$

This membership function is defined by two parameters— $\mathbf { \nabla } \cdot \mathbf { } a$ and $b$ . The requirement of differentiability also dictates the choice of t-norms (intersections) for calculating neuron activation rules. In the system NEFCLASS for this operation is used minimum; in the modified system NEFCLASS-M -product of the corresponding values.

Finally, the kind of aggregate function (t-conorm) for modified model is limited only by the weighted sum. The reason consists in the fact that the maximum function which is used in the original system also does not satisfy the condition of differentiability. The main change is obviously relates to a learning algorithm of fuzzy sets. The objective function in the modified system NEFClass is minimization of the mean squared error on the training sample by analogy with the classical (clear) neural networks:

$$
\operatorname* { m i n } E = \frac { 1 } { N } \sum _ { p = 1 } ^ { N } \left\| a _ { c } ^ { ( p ) } - a _ { c } ^ { ( p ) * } \right\| ^ { 2 }
$$

where the N—number of patterns in the training sample, $a _ { c } ^ { ( p ) }$ is an activation vector of neurons in the output layer for the next training sample $p$ , $a _ { c } ^ { ( p ) * }$ is a target value of this vector for the pattern p. The components of the target vector for the pattern $\boldsymbol { \mathrm { ~ p ~ } }$ are equal:

$$
a _ { i j } ^ { ( p ) * } = \left\{ { 0 , \ i \neq j } \atop { 1 , \ i = j } \right.
$$

where $j$ is a index of the true class to which this pattern p belongs, $i$ is classification of pattern $\boldsymbol { \mathrm { ~ p ~ } }$ by NEFClass. The argument of numerical optimization aimed at reducing MSE for the training set is the aggregate vector of parameters $a$ and $b$ of FNN. As a specific training method can be used any method unconstrained optimization such as the gradient method or the conjugate gradient method, these both methods were implemented in this investigation.

# 3.4 Experimental Studies. Comparative Analysis of FNN NEFClass and NEFClass-M in Classification Problems

Experiments were conducted on the classification of the two sets of data IRIS and WBC [5, 6]. Selection of IRIS and WBC test kits was dictated by two considerations: firstly, these sets can be considered standard for classification problems, and secondly, in the original works of authors NEFCLASS model was tested on these data sets [1–3]. This allows to compare the results of the base system NEFCLASS with a modified NEFCLASS_M and estimate the effect of introduced improvements.

# IRIS Data Set

IRIS set contains 150 samples belonging to three different classes (Iris Setosa, Iris Versicolour, and Iris Virginica), 50 samples of each class. Each sample is characterized by four properties. IRIS is the only one set by classification simplicity for which even a simple strategy of rules selection gives good results.

In the first experiment, in a modified model NEFClass-M “simple” rules learning algorithm was used, and their number was limited to 10 with 3 fuzzy sets per variable (all other parameters were set to the default values). As a result, the system has created 10 rules and achieved only 4 classification errors of the 150 (i.e. $9 7 . 3 \%$ correct) patterns.

The best result, which was managed to achieve with the “simple” rules learning algorithm is three rules with two essential variables, $x _ { 3 }$ and $x _ { 4 }$ , and the same order of misclassification (4 errors) [5]:

R1: IF (any, any, large, large) THEN Class 3   
R2: IF (any, any, medium, medium) THEN Class 2   
R3: IF (any, any, small, small) THEN Class 1

The same result was achieved for the “better” and “best in class” rules learning algorithms. However, for the last two algorithms it’s possible further reduction in the number of fuzzy sets for variable $x _ { 3 }$ and $x _ { 4 }$ under the following rules (6 erroneous classification):

R1: IF (any, any, small, small) THEN Class 1   
R2: IF (any, any, large, small) THEN Class 2   
R3: IF (any, any, large, large) THEN Class 3

The authors model NEFCLASS obtained the similar results, except that in their experiments, they used three fuzzy sets (linguistic values) for $x _ { 3 }$ and $x _ { 4 }$ [1, 2]. Thus, for a set of data IRIS it was managed to achieve better results than in the original works—exclusively simple set rules of two variables with only two decomposing sets for each variable.

# Dataset WBC

The next test sample for classification was standard data sample Wisconsin Breast Cancer (WBC). When processing sample Wisconsin Breast Cancer using system

NEFClass-M interesting results were obtained which didn’t always coincide with the results of the basic model NEFCLASS.

Following the course of the experiments by the authors of NEFCLASS [1, 2] for system training rule base learning algorithm with the “best in the class” (three sets in the variable). was used with maximum 4 rules. The resulting error of misclassification obtained for the system NEFClass-M was 28 patterns of 663 $( 9 5 . 7 \%$ correct) [7]. Very interesting is the fact that for model NEFClass for similar parameters correct classification value was only $8 0 . 4 \%$ (135 misclassification).

This is a significant advantage of the modified system NEFClass-M which can be explained by suggested modifications that distinguish this model from basic NEFCLASS model, namely, the use of randomization algorithm, the choice of learning rate and application of numerical algorithm of optimization (gradient method for MF learning.

The best result that was managed to obtain for the data set WBC is the rule base of 8 rules with five essential variables $x _ { 1 } , x _ { 2 } , x _ { 4 } , x _ { 6 }$ and $x _ { 9 }$ (misclassification—19 errors) [5]:

R1: IF (small, small, any, small, any, small, any, any, small) THEN Class 1   
R2: IF (small, small, any, large, any, small, any, any, small) THEN Class 1   
R3: IF (small, small, any, small, any, small, any, any, large) THEN Class 1   
R4: IF (large, large, any, small, any, large, any, any, small) THEN Class 2   
R5: IF (large, large, any, large, any, small, any, any, small) THEN Class 2   
R6: IF (small, large, any, small, any, large, any, any, small) THEN Class 2   
R7: IF (large, small, any, small, any, small, any, any, small) THEN Class 2   
R8: IF (large, small, any, small, any, small, any, any, large) THEN Class 2

Comparable results (24 misclassification) were obtained with the use of a maximum of 2 rules (“the best in the class”) with all the important variables, except $x _ { 5 }$ and $x _ { 7 }$ :

R1: IF (small, small, small, small, any, small, any, small, small) THEN Class 1   
R2: IF (large, large, large, small, any, large, any, large, small) THEN Class 2

Thus, the results obtained by NEFCLASS-M are superior over basic model NEFCLASS both in number of rules/significant variables and classification accuracy. This confirms the efficiency of the modifications made to the model NEFClass: randomization, the correct choice of speed training and application of numerical optimization algorithms.

# 3.5 Application of NEFClass in the Problem of Objects Recognition at Electro-Optical Images

Using multi-spectral electro system operating in three ranges—red, green and blue images were obtained of the ocean and the coastal surface. It was required to recognize objects in the form of geometric shapes on water surface and on the sand [8, 9]. For these purposes, accounting the complexity of the problem as well as a large level of noise it was suggested to use fuzzy neural networks, in particular NEFClass. In order to organize the training of FNN NEFClass a number of learning algorithms were developed—gradient, conjugate gradient and genetic ones and their efficiency was investigated and compared to the basic training algorithm of the system NEFClass [1, 2].

# 3.5.1 Gradient Learning Algorithm for NEFClass

For the first stage of the algorithm—learning rule base the first phase of the basic algorithm NEFClass is used. The second stage uses a gradient algorithm for training the feedforward neural network, which is described below [5, 8].

Let the criterion of training fuzzy neural network, which has 3 layers (one hidden layer), be as follows:

$$
e ( W ) = \sum _ { i = 1 } ^ { M } { ( t _ { i } - N E T _ { i } ( W ) ) ^ { 2 } } \mathrm { { \to } \operatorname* { m i n } }
$$

where $t _ { i }$ —the desired value of the i-th output of neural network;

$N E T _ { i } ( W )$ —the actual value of the i-th neural network output for the weight matrix

$$
\begin{array} { r } { W = \big [ W ^ { I } , W ^ { 0 } \big ] , W ^ { I } = W ( x , R ) = \mu _ { j } ( x ) , W ^ { O } = W ( R , C ) . } \end{array}
$$

Let activation function for the hidden layer neurons (neurons of rules) be such:

$$
O _ { R } = \prod _ { i = 1 } ^ { N } \mu _ { j _ { i } } ^ { ( i ) } ( x _ { i } ) , j = 1 , . . . , q _ { i } ,
$$

where $\mu _ { j i } ( x )$ —membership function, which has the form (Gaussian):

$$
\mu _ { j _ { i } } ^ { ( i ) } ( x ) = e ^ { - \frac { ( x - a _ { j i } ) ^ { 2 } } { b _ { j i } ^ { 2 } } } ,
$$

and the activation function of neurons in the output layer (weighted sum):

$$
O _ { C } = \frac { \displaystyle \sum _ { R \in U _ { 2 } } W ( R , C ) \cdot O _ { R } } { \displaystyle \sum _ { R \in U _ { 2 } } W ( R , C ) } ,
$$

or maximum function:

$$
O _ { C } = \mathrm { m a x } W ( R , C ) \cdot O _ { R } .
$$

Consider the gradient learning algorithm of fuzzy perceptron.

1. Let $W ( n )$ —be the current value of the weights matrix. The algorithm has the following form:

$$
W ( n + 1 ) = W ( n ) - \gamma _ { n + 1 } \nabla _ { w } e ( W ( n ) ) ,
$$

where $\gamma _ { n }$ —the step size at $n$ -th iteration;

$\nabla _ { \boldsymbol { w } } e \big ( W ( n ) \big )$ —gradient (direction), which reduces the criterion (3.12).

2. At each iteration, we first train (adjust) the input weight $W$ , which depend on the parameters $a$ and $b$ (see the expression 3.14)

$$
\begin{array} { l } { \displaystyle a _ { j i } ( n + 1 ) = a _ { j i } ( n ) - \gamma _ { n + 1 } \frac { \partial e ( W ) } { \partial a _ { j i } } , } \\ { \displaystyle b _ { j i } ( n + 1 ) = b _ { j i } ( n ) - \gamma _ { n + 1 } ^ { \prime } \frac { \partial e ( W ) } { \partial b _ { j i } } , } \end{array}
$$

where $\gamma _ { n + 1 } ^ { \prime }$ —step size for parameter $b$ .

$$
\frac { \partial e ( W ) } { \partial a _ { j i } } = - 2 \sum _ { k = 1 } ^ { M } \left( \left( t _ { k } - N E T _ { k } ( w ) \right) \cdot W ( R , C ) \right) \cdot O _ { R } \cdot \frac { ( x - a _ { j i } ) } { b _ { j i } ^ { 2 } } ,
$$

$$
\frac { \partial e ( W ) } { \partial b _ { j i } } = - 2 \sum _ { k = 1 } ^ { M } \left( \left( t _ { k } - N E T _ { k } ( w ) \right) \cdot W ( R , C ) \right) \cdot O _ { R } \cdot \frac { \left( x - a _ { j i } \right) ^ { 2 } } { b _ { j i } ^ { 3 } } .
$$

3. We find (train) output weight:

$$
\frac { \partial e ( W ^ { O } ) } { \partial W ( R , C _ { k } ) } = - \big ( t _ { k } - N E T _ { k } \big ( W ^ { O } ) \big ) O _ { R } ,
$$

$$
W _ { k } ^ { O } ( n + 1 ) = W _ { k } ^ { O } ( n ) - \gamma _ { n + 1 } ^ { \prime \prime } \frac { \partial e ( W ^ { O } ) } { \partial W ( R , C _ { k } ) } .
$$

4. $n : = n + 1$ and go to the next iteration.

The gradient method is the first proposed learning algorithm, it is easy to implement, but has the disadvantages:

1. converges slowly;   
2. only finds a local extremum.

# Conjugate Gradient Method for the System NEFClass

Conjugate gradient algorithm, as well as more general algorithm of conjugate directions, was used in the field of optimization thanks to a wide class of problems for which it ensures the convergence to the optimal solution for a finite number of steps. Its description is considered in [9] and isn’t described here.

# 3.5.2 Genetic Method for Training System NEFClass

Consider the implementation of a genetic algorithm to train NEFCLASS. This algorithm is a global optimization algorithm. It uses the following mechanisms [9]:

1. crossing-over pairs of parents and generation of descendants;   
2. mutation (random effects of the action);   
3. the natural selection of the best (selection).

The purpose of training—to minimize the mean square error:

$$
E ( W ) = \frac { 1 } { M } \sum _ { k = 1 } ^ { M } { \left( t _ { k } - N E T _ { k } ( W ) \right) ^ { 2 } } ,
$$

where $\mathbf { M }$ is the number of classes; $t _ { k }$ is the desired classification;

$N E T _ { k } ( W ) .$ —classification result of NEFCLASS; $W = [ W _ { I } , W _ { O } ]$ , $W _ { I } = \left. \boldsymbol { w } _ { i j } ^ { I } \right.$ are inputs weights, $W _ { O } = \left. w _ { i j } ^ { O } \right. .$ —output weights. Any individual (specimen) is describedby the appropriate vector of weights $W$ . Set the initial population of $\mathbf { N }$ individuals $\left[ W _ { I } ( 0 ) , . . . , W _ { i } ( 0 ) , . . . , W _ { N } ( 0 ) \right]$ . Calculate the index of fitness (FI), and evaluate the quality of recognition:

$$
F I ( W _ { i } ) = C - E ( W _ { i } ) \to \operatorname* { m a x } ,
$$

where $C$ —a constant.

Next step is the crossing of parental pairs. When selecting parents a probabilistic mechanism is used. Let $P _ { i }$ be the probability of selecting the i-th parent

$$
P _ { i } = \frac { { \cal F I } ( W _ { i } ( 0 ) ) } { \displaystyle \sum _ { i = 1 } ^ { N } { \cal F I } ( W _ { i } ( 0 ) ) } ,
$$

Then the crossing of selected pairs is performed.

It’s possible to apply different mechanisms of crossing. For example: for the first offspring even components of the vector of the first parent and the odd components of the vector of the other parent are taken, and for the second on the contrary:

$$
W _ { i } ( 0 ) \oplus W _ { k } ( 0 ) = W _ { i } ( 1 ) + W _ { k } ( 1 )
$$

$$
\begin{array} { r l } & { w _ { i j } ( 1 ) = \left\{ \begin{array} { c } { w _ { i j } ( 0 ) , i f j = 2 m } \\ { w _ { k j } ( 0 ) , i f j = 2 m - 1 } \end{array} \right. } \\ & { w _ { k j } ( 1 ) = \left\{ \begin{array} { c } { w _ { k j } ( 0 ) , i f j = 2 m } \\ { w _ { i j } ( 0 ) , i f j = 2 m - 1 } \end{array} \right. } \end{array}
$$

where $W _ { i } = \left[ w _ { i j } \right] _ { j = 1 , R }$ , $m \leq R / 2$ .

Choose $\frac { N } { 2 }$ pairs of parents and generate $N$ descendants.

After generating offsprings, the mutation acts on the new population:

$$
w _ { i j } ^ { \prime } ( n ) = w _ { i j } ( n ) + \xi ( n )
$$

where $a = c o n s t \in [ - 1 ; + 1 ]$ ;

$\xi ( n ) = a e ^ { - \alpha n }$ ; $\alpha$ —mutation rate of extinction;

$\boldsymbol { \alpha }$ —is selected randomly from the interval [0, 1].

Then, after the effect of mutation selection procedure is performed in a population, which allows to choose the “fittest” individuals. Different mechanisms of selection may be used.

1. Complete replacement of the old to the new population.   
2. Selecting the best $N$ of all existing species $N _ { p a r } + N _ { c h }$ by the criterion of maximum FI

After the crossing, mutation and selection of the current iteration ends. The iterations are repeated until one of the stop criteria will be fulfilled.

# 3.5.3 Experiments on Objects Recognition on Optical Images

For images processing the electro-optical imaging system ENVI was used and its ability to map, that is, to combine the images of the check points, obtained from the different spectral cameras [8]. This enables to get a multispectral image. In the Fig. 3.2 initial data for mapping are shown.

![](images/f8a4e1e81315bcb6404ed518bcf4d10e33870fe71703c457230c5f18b5cc2544.jpg)  
Fig. 3.2 Initial data

After selecting the 15 control points in the images in different spectrum (this function is not automated) images are merged and we get the so-called multispectral cube. The result is shown in Fig. 3.3.

On the images there were nine different types of surfaces that need to be classified. For analysis and processing, so-called ROI (Region of Interest) on images were used. On the image homogeneous region was determined, for example, sand, water, foam, target red target white color and so on. The result of this detection can be seen in Fig. 3.4.

Next, using a processing system the mean value and the variance of the selected region were received. The data obtained were later tabulated.

![](images/93ed01635a70e0b590abfb9e4c58e03471df26be4fe8ad5523dd0d00488f2674.jpg)  
Fig. 3.3 Multispectral image

![](images/6ad3bf6ea4adcb2ef5761e26b55d25cdcc5c00d9672a898af5e07cc09fff9c68.jpg)  
Fig. 3.4 Image of ROI

These data characterize the nine classes of surface areas [8]:

• white target; red target; green target; blue target; yellow target; foam; water; dry sand; wet sand.

For classification of objects it was suggested to use FNN NEFClass_M [8]. These types of surfaces correspond to nine output nodes in the system NEFClass_M.

The total number of features used to classify the kinds of surfaces is four, namely:

the brightness in the red spectrum (RS);   
the brightness in the blue spectrum (BS);   
the brightness in the green spectrum (GS);   
brightness in the infrared spectrum (IS).

The total number of data is 99, 11 for each class.

Present the main statistical characteristics of the data set obtained by multispectral system «Mantis» (Tables 3.1 and 3.2) [8].

To explore the effectiveness of various learning algorithms in the problem of electro-optical image recognition using NEFClass software kit was developed named NEFClass- BGCGG (Basic, Gradient, Conjugate Gradient, Genetic) [8, 9].

Further experiments were carried out with the software kit NEFClass-BGCGG. According to the basic principle of model investigation experiments were carried out by changing only one parameter each time. Of the available 99 patterns 54 patterns served as a training sample. The other 45 patterns were used for testing. The values of the basic parameters of the simulation algorithm were set to the starting positions (see Table 3.3):

During the process of training 15 rules was generated presented in the Table 3.4.

Table 3.1 Statistical characteristics of multispectral system “Mantis”   

<html><body><table><tr><td>Evidence</td><td>Minimum</td><td>Maximum</td><td>Average</td><td>Pattern deviation</td><td>The correlation between the symptoms and the class</td></tr><tr><td>Brightness in the RS</td><td>28.81</td><td>255.00</td><td>165.40</td><td>76.14</td><td>-0.46</td></tr><tr><td>Brightness in the BS</td><td>72.93</td><td>255.00</td><td>165.43</td><td>68.62</td><td>-0.32</td></tr><tr><td>Brightness in the GS</td><td>44.34</td><td>254.89</td><td>121.57</td><td>57.64</td><td>-0.52</td></tr><tr><td>Brightness in the IS</td><td>17.03</td><td>255.00</td><td>140.84</td><td>81.58</td><td>-0.49</td></tr></table></body></html>

Table 3.2 The correlation between the features   

<html><body><table><tr><td></td><td>Brightness in the RS</td><td>Brightness in the BS</td><td>Brightness in the GS</td><td>Brightness in the IS</td></tr><tr><td>Brightness in the RS</td><td>1</td><td>0.7</td><td>0.58</td><td>0.95</td></tr><tr><td>Brightness in the BS</td><td></td><td>1</td><td>0.77</td><td>0.7</td></tr><tr><td>Brightness in the GS</td><td></td><td></td><td>1</td><td>0.59</td></tr><tr><td>Brightness in the IS</td><td></td><td></td><td></td><td>1</td></tr></table></body></html>

Table 3.3 The values of the parameters for the program   

<html><body><table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Algorithm generation rules</td><td>The best for the class</td></tr><tr><td>The learning algorithm</td><td>Classic,gradient, Genetic, CG</td></tr><tr><td>Number of generatingrules</td><td>Maximum</td></tr><tr><td>The aggregation function</td><td>Weighted sum</td></tr><tr><td>The number of terms (values) for each feature</td><td>5 for all</td></tr><tr><td>Speed training for weight coefficients between the input nodes and therule nodes</td><td>σa = 0.1 σb=0.1 σc=0.1</td></tr><tr><td>Speed training for weight coefficients between the rules layer and the output layer</td><td>σ=0.1</td></tr><tr><td>The maximum number of epochs</td><td>50</td></tr></table></body></html>

Table 3.4 The rule base of a fuzzy classifier   

<html><body><table><tr><td>No of rule</td><td>No Feature 1 value</td><td>No Feature 2 value</td><td>Feature 3 value</td><td>No Feature 4 value</td><td>Class N</td></tr><tr><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>0</td></tr><tr><td>2</td><td>4</td><td>0</td><td>1</td><td>4</td><td>1</td></tr><tr><td>3</td><td>4</td><td>0</td><td>0</td><td>4</td><td>1</td></tr><tr><td>4</td><td>4</td><td>1</td><td>0</td><td>4</td><td>1</td></tr><tr><td>5</td><td>2</td><td>3</td><td>1</td><td>1</td><td>2</td></tr><tr><td>6</td><td>1</td><td>0</td><td>1</td><td>0</td><td>3</td></tr><tr><td>7</td><td>4</td><td>4</td><td>1</td><td>4</td><td>4</td></tr><tr><td>8</td><td>3</td><td>4</td><td>3</td><td>3</td><td>5</td></tr><tr><td>9</td><td>3</td><td>3</td><td>2</td><td>3</td><td>5</td></tr><tr><td>10</td><td>4</td><td>4</td><td>3</td><td>3</td><td>5</td></tr><tr><td>11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>6</td></tr><tr><td>12</td><td>3</td><td>2</td><td>1</td><td>2</td><td>7</td></tr><tr><td>13</td><td>1</td><td>0</td><td>0</td><td>1</td><td>8</td></tr><tr><td>14</td><td>1</td><td>1</td><td>0</td><td>1</td><td>8</td></tr><tr><td>15</td><td>1</td><td>0</td><td>0</td><td>0</td><td>8</td></tr></table></body></html>

The dependence of the quality of training on the number of rules that are generated in the first stage was investigated. For an objective assessment of the results testing on the test sample was performed. For this purpose we varied the number of rules, starting from 9 to 14. The results are shown in the Table 3.5.

The obtained result is natural, the more rules, the better the results of the test classification.

We have investigated the effect of the terms number in features on the quality of classification. Comparative table is given below (see Table 3.6)

Very interesting result was obtained in this series of experiments [8].

From the Table 3.6 it follows that there exists an optimal number of terms that can be used to describe a collection of data during training. When the number of terms exceeds this value the number of misclassified samples increases, that is, by increasing the complexity of the model error increases.

Table 3.5 The dependence of the quality of classification on the number of rules   

<html><body><table><tr><td>Number of rules</td><td>MSE</td><td>True classification (%)</td></tr><tr><td>9</td><td>13.071009</td><td>24</td></tr><tr><td>10</td><td>9.545608</td><td>15</td></tr><tr><td>11</td><td>9.910701</td><td>15</td></tr><tr><td>12</td><td>9.705482</td><td>15</td></tr><tr><td>13</td><td>4.769655</td><td>4</td></tr><tr><td>14</td><td>4.739224</td><td>4</td></tr><tr><td>15</td><td>4.751657</td><td>4</td></tr></table></body></html>

Table 3.6 The dependence of the quality of classification on the number of terms   

<html><body><table><tr><td>Number of terms</td><td>MSE</td><td>True classification (%)</td></tr><tr><td>4</td><td>5.928639</td><td>4</td></tr><tr><td>5</td><td>4.626252</td><td>4</td></tr><tr><td>6</td><td>4.957257</td><td>4</td></tr><tr><td>7</td><td>5.228448</td><td>4</td></tr><tr><td>8</td><td>5.633563</td><td>4</td></tr><tr><td>9</td><td>6.797175</td><td>4</td></tr><tr><td>10</td><td>7.897521</td><td>7</td></tr></table></body></html>

System training using classical algorithm with the optimal number of terms in the features was performed. Forms of membership functions for each feature are shown in Fig. 3.5.

The total sum of squared errors was 2.852081, the number of erroneous classifications—zero in the training set, while for the test sample MSE was equal to 4.6252, which is not bad result.

![](images/ce06d74e6fcbe2db86b3eb3d4f002814d69bd0c36f108f69a8d3e6f2c343dc8a.jpg)  
Fig. 3.5 The result of a classic learning algorithm

![](images/3668e7c242432acebcb1f31b54fad1c1b23a8722afbbe51db77208d384b67ea8.jpg)  
Fig. 3.6 Results of the gradient method

Experiments with the gradient algorithm. The results are shown in Fig. 3.6 (MF of fuzzy sets for each of the four features).

An error at the end of the training was 2.042015, that a little bit better than for classical method. When testing MSE was 3.786005, and the portion of misclassification was $4 \%$ .

Further, the option automatic speed adjustment of MF parameters was included, that is, we used the algorithm “golden section” for step value optimization. The results are shown below (Fig. 3.7).

The same experiments were carried out with a conjugate gradient algorithm. The results are shown in Fig. 3.8.

Further the method of golden section was added to training algorithm. The results can be seen in Fig. 3.9.

Finally, experiments with a genetic algorithm with different MF—triangular and Gaussian were carried out [8].

The results of learning using different algorithms are presented in the comparative charts (Fig. 3.10) and Table 3.7. Note that for the training sample excellent results by the criterion of the percentage of misclassification were obtained for all algorithms.

![](images/0d50361b564f9784ddb5201663376d01dff7d16d621f7222fd8969d87e59dc10.jpg)  
Fig. 3.7 The result of the gradient algorithm in tandem with the “golden section” algorithm

![](images/89acccc0a69ee4e8079d4b1751171989dc493308fa54f904259a4ea178382194.jpg)  
Fig. 3.8 The result of training by the conjugate gradient

![](images/c2d66c755e4688eed340c14d5cc239f9274bb4a79977960888c92485ddd5396e.jpg)

![](images/e2caca9fcfcb16431cf4cea2a1e3d6fee3b454efb3e6cd336009dec302984836.jpg)  
Fig. 3.9 The result of training by conjugate gradient method with the selection step by “golden section” algorithm   
Fig. 3.10 Comparative curves of the convergence rate to the optimal classification of different learning algorithms

Table 3.7 Comparison table for different learning algorithms   

<html><body><table><tr><td rowspan="2">The learning algorithm of weighting coefficients</td><td colspan="2">Training training</td><td colspan="2">Testing testing</td></tr><tr><td>MSE</td><td>Misclassification (%)</td><td>MSE</td><td>Misclassification (%)</td></tr><tr><td>Classic</td><td>6.650668</td><td>0</td><td>7.285827</td><td>4</td></tr><tr><td>Gradient</td><td>5.9893</td><td>0</td><td>6.829068</td><td>4</td></tr><tr><td>Conjugate gradient</td><td>1.132871</td><td>0</td><td>3.314763</td><td>4</td></tr><tr><td>Genetic with triangular membership</td><td>11.110936</td><td>0</td><td>13.677424</td><td>4</td></tr><tr><td>functions (MF) Genetic with Gaussian MF</td><td>3.204446</td><td>0</td><td>4.568338</td><td>4</td></tr></table></body></html>

For all algorithms, this criterion is zero. However, on the test sample, the results were worse: at least two samples were misclassified. Also the sum of squared error (MSE) for all, without exception, learning algorithms increased. For ease of comparison, the number of iterations (epochs) has been limited to 50.

As can be seen, the results are satisfactory, the level of correct classification on the test sample is $9 6 \%$ . These results may be improved by forming a more representative sample.

Analyzing the curves in the Fig. 3.10 it can be clearly seen that the best method for the rate of convergence is the conjugate gradient method. Then the next is a genetic algorithm with Gaussian function. Less effective is the gradient method. Next by rate of convergence is classical algorithm used in the system NEFClass. And at the end of row the least effective is genetic method with a triangular membership function.

However, the MSE criterion by which the curves were plotted, displays ambiguously classification quality. An important criterion for evaluation of methods efficiency is the minimum number of misclassified samples. From Table 3.7 one can see that all algorithms show the same results with respect to this criterion.

# 3.6 Recognition of Images in Medical Diagnostics Using Fuzzy Neural Networks

# Introduction

An important application sphere of pattern recognition systems is the problem of classification of optical medical images and diagnostics in medicine. Especially it relates to state recognition of human organs tissue and early detection of possible cancer. One of such tasks is cervix epithelium state analysis and diagnostics using optical images obtained with colposcope (a method of survey of a mucous membrane of part of a neck of a uterus in the conditions of additional lighting and optical increase with the help of a colposcope) [10]. As a result of carrying out a colposcopy by the doctor the increased pictures of images with preliminary splitting into classes of diseases are provided. The problem of classification cervix epithelium state using images obtained with colposcope was considered in [10, 11] where for its solution was suggested the application of crisp neural networks Back propagation, neural networks with radial basis functions (RBFNN) and cascade RBFNN and their efficiency investigated. The goal of this presentation is the investigation of fuzzy neural network NEFClass for recognition of state of cervix epithelium in medical diagnostics and comparison of its efficiency with conventional RBF network.

# 3.6.1 Problem Statement

The problem consists in classification of obtained medical images using special medical tools: computer tomography, magneto-resonance tomography, colposcope etc.

In medical images values of the color model RGB represent components of input vector and based on this information it’s needed to define, which class it should be referred to. The classifier thus refers object to one of classes according to a certain splitting of N-dimensional space which is called as input space, and dimension of this space is a number of vector components.

For the solution of cervix epithelium state analysis and diagnostics problem using optical images theNefClass network with Gaussian membership function was suggested

# 3.6.2 Training of NEFClass System

The NEFClass system can be constructed on partial knowledge of samples. The user has to define quantity of initial fuzzy sets for each of object feature, and set value $k _ { m a x }$ —the maximum number of nodes rules which can be created in the hidden layer. Membership functions of Gauss and gradient algorithm of training of fuzzy sets are used for training.

Let’s consider stages of recognition process.

1. Work with data. Construct a database of examples, characteristic for this task. Split all data set into two sets: training and test in the following ratio:

training $50 \%$ , test $50 \%$ ;   
training $60 \%$ , test $40 \%$ ;   
training $70 \%$ , test $30 \%$ ;   
training $80 \%$ , test $20 \%$ ;

training $90 \%$ , test $10 \%$ ;

2. Preliminary processing. Choose system of features, characteristic for this task, and transform data appropriately that is to be fed into network inputs. As a result it is desirable to receive linearly separated space of a set of samples. As input data medical images of benign processes, are used namely:

inflammatory processes in the form of branching of vessels;   
cervical erosion;   
traumatic deformation;   
large cervical ectropion.   
small cervical ectropion.

Each of these diseases is presented by a number of features which is to be classified by a neural network and are shown in the Figs. 3.11, 3.12, 3.13, 3.14, 3.15 and 3.16.

3. Designing, training and assessment of a network work quality. At this stage the number of rules, quantity of fuzzy sets and percentage ratio of training and testing samples are determined.   
4. Choosing algorithm of a network training. As a training algorithm the gradient method was used. At this stage it is necessary to specify the accuracy, the steps size for all variables and a number of iterations.   
5. Application and diagnosing. At the last stage we receive result of application of the neural NefClass network to a problem of medical diagnostics. We observe splitting images into RGB to the color scheme and a class to which the sample initially belonged. Also we obtain the result of recognition—a class to which the sample after training of a neural network belongs. The amount of misclassifications and an average error on sample are determined.

![](images/9896d8d2f935ec928bdb95dcb7d7da92b4a146265bdad106a56e1df33c6e503e.jpg)  
Fig. 3.11 Inflammatory processes

![](images/1a090aee7b77534c8a922db5fe2ff1b337ffd0c988ed8d13c1a751f2662eb669.jpg)![](images/d6d4538aea9a754daf4db66decd4d18e94b55060d129453190992f26736af005.jpg)  
Fig. 3.12 Inflammatory processes   
Fig. 3.14 Traumatic deformation

Fig. 3.13 Cervical erosion

![](images/d256a35db52a591e61cad964befba0925557ca872ddf4203c6ad154606ecf76d.jpg)  
Fig. 3.15 Large cervical ectropion

# 3.6.3 Experimental Investigations

The experimental investigations were carried out on real images of cervix uterus. Sample size consisted of 70 elements which contained 5 classifications of diseases. In process of experiments the training/test sample ratio, number of fuzzy sets of linguistic variables and number of rules were varied.

The results of classification after training at training and test samples for various training/test samples ratio, number of fuzzy sets are presented in the Table 3.8 [12].

Figures 3.17, 3.18, 3.19 and 3.20 shows the dependence of ratio training/testing samples on the mean squared error and misclassification $\%$ (MAPE) for different number of fuzzy sets for each variable (feature).

The next step in experiments was determination of results change due to variation of the rules number. For each number of fuzzy sets (3, 6, 7, and 11) training/ test sample ratio was used. It should be noted there is a number of rules, after which there is no change in the classification of samples and in the mean square error. The results are shown in Table 3.9 [12].

Comparison of the fuzzy neural network NefClass efficiency with the neural network RBF was performed. The results of RBF are shown in Table 3.10.

# Conclusions

1. The problem of recognition of objects on medical images in medical diagnostics is considered. The investigations were performed on the cervix uterus images obtained using colposcope. 70 images were selected which contained 5 classifications of diseases.   
2. Fuzzy neural network NefClass and non- fuzzy neural network RBF were used for classification. Experiments were carried out on training/test samples in the ratios: 50/50, 60/40, 70/30, 80/20 and 90/10.

![](images/771ed0e1b5228d15525bad891cabb4138999b30db53e84ba401082d75cbd4f9d.jpg)  
Fig. 3.16 Small cervical ectropion

Table 3.8 Performance results of NEFClass   

<html><body><table><tr><td># of sets</td><td>Number of patterns training/</td><td>Ratio training/ test sample</td><td>Misclassified patterns training</td><td>Misclassified patterns testing</td><td>MSE training</td><td>MSE testing</td><td>% Misclassification</td></tr><tr><td rowspan="5">3</td><td>test 35-35</td><td>(%) 50-50</td><td>13</td><td>16</td><td>0.559</td><td>0.588</td><td>45.12</td></tr><tr><td>42-28</td><td>60-40</td><td>17</td><td>12</td><td>0.588</td><td>0.551</td><td>42.1</td></tr><tr><td>49-21</td><td>70-30</td><td>20</td><td>9</td><td>0.570</td><td>0.549</td><td>42.85</td></tr><tr><td>56-14</td><td>80-20</td><td>23</td><td>6</td><td>0.562</td><td>0.540</td><td>42.857</td></tr><tr><td>63-7</td><td>90-10</td><td>25</td><td>4</td><td>0.551</td><td>0.562</td><td>57.14</td></tr><tr><td rowspan="5">6</td><td>35-35</td><td>50-50</td><td>2</td><td>9</td><td>0.1697</td><td>0.336</td><td>25.71</td></tr><tr><td>42-28</td><td>60-40</td><td>2</td><td>9</td><td>0.1699</td><td>0.330</td><td>32.14</td></tr><tr><td>49-21</td><td>70-30</td><td>3</td><td>6</td><td>0.167</td><td>0.306</td><td>28.57</td></tr><tr><td>56-14</td><td>80-20</td><td>2</td><td>2</td><td>0.1495</td><td>0.254</td><td>14.28</td></tr><tr><td>63-7</td><td>90-10</td><td>2</td><td>0</td><td>0.154</td><td>0.197</td><td>0</td></tr><tr><td rowspan="5">7</td><td>35-35</td><td>50-50</td><td>2</td><td>9</td><td>0.116</td><td>0.314</td><td>25.71</td></tr><tr><td>42-28</td><td>60-40</td><td>4</td><td>8</td><td>0.118</td><td>0.341</td><td>28.57</td></tr><tr><td>49-21</td><td>70-30</td><td>3</td><td>8</td><td>0.108</td><td>0.407</td><td>38.09</td></tr><tr><td>56-14</td><td>80-20</td><td>3</td><td>3</td><td>0.109</td><td>0.335</td><td>21.42</td></tr><tr><td>63-7</td><td>90-10</td><td>2</td><td>2</td><td>0.127</td><td>0.263</td><td>28.5</td></tr><tr><td rowspan="5">11</td><td>35-35</td><td>50-50</td><td>3</td><td>11</td><td>0.091</td><td>0.440</td><td>31.42</td></tr><tr><td>42-28</td><td>60-40</td><td>1</td><td>7</td><td>0.055</td><td>0.466</td><td>25</td></tr><tr><td>49-21</td><td>70-30</td><td>1</td><td>8</td><td>0.0434</td><td>0.550</td><td>38.09</td></tr><tr><td>56-14</td><td>80-20</td><td>2</td><td>4</td><td>0.054</td><td>0.377</td><td>28.57</td></tr><tr><td>63-7</td><td>90-10</td><td>1</td><td>1</td><td>0.064</td><td>0.221</td><td>14.28</td></tr></table></body></html>

![](images/eb89ed7fa1906c2c520adde13ff1e0fb0922bfe3fd663ca17d5f0d223763021c.jpg)  
Fig. 3.17 MSE for 3 sets

![](images/a68667b7819fccbec50c9e4e08a57c18c8764ca1a8e22ad93f48fe1800045128.jpg)  
Fig. 3.18 MSE for 6 sets

![](images/03ceb461344eb25ced3af8b4b74f3ddf81e61baf24705198b298e1eb31013d76.jpg)  
Fig. 3.19 MSE for 7 sets

![](images/bc0e40d5f7745ae3890df77f5643377f5351731d72deb90b56d9fad859d7789d.jpg)  
Fig. 3.20 MSE for 11 sets

Table 3.9 Results of FNN NEFClass versus number of rules   

<html><body><table><tr><td>Number of sets</td><td>3</td><td colspan="3">6</td><td colspan="3">7</td><td colspan="3">11</td></tr><tr><td>Number of rules</td><td>For all rules</td><td>7</td><td>15</td><td>50</td><td>7</td><td>15</td><td>50</td><td>7</td><td>15</td><td>50</td></tr><tr><td>Sample (%)</td><td>90/10</td><td>80/20</td><td>80/ 20</td><td>80/ 20</td><td>80/ 20</td><td>80/20</td><td>80/20</td><td>70/ 30</td><td>70/ 30</td><td>70/ 30</td></tr><tr><td>Mismatch training</td><td>23</td><td>23</td><td>3</td><td>2</td><td>15</td><td>5</td><td>3</td><td>13</td><td>3</td><td>1</td></tr><tr><td>Mismatch testing</td><td>4</td><td>3</td><td>0</td><td>0</td><td>7</td><td>6</td><td>3</td><td>14</td><td>9</td><td>8</td></tr><tr><td>MSE training</td><td>0.550</td><td>0.426</td><td>0.163</td><td>0.154</td><td>0.335</td><td>0.170</td><td>0.109</td><td></td><td></td><td></td></tr><tr><td>MSE testing</td><td>0.536</td><td>0.344</td><td>0.214</td><td>0.197</td><td>0.492</td><td>0.442</td><td>0.335</td><td></td><td></td><td></td></tr><tr><td>%， misclassification</td><td>57.142%</td><td>42.85%</td><td>0%</td><td>0%</td><td>50%</td><td>42.85%</td><td>21.42%</td><td></td><td></td><td></td></tr></table></body></html>

Table 3.10 Results of RBF network   

<html><body><table><tr><td>Training/test (%)</td><td>50-50</td><td>60-40</td><td>70-30</td><td>80-20</td><td>90-10</td></tr><tr><td>Number of coincidences</td><td>20</td><td>16</td><td>17</td><td>10</td><td>6</td></tr><tr><td>Number of non coincidences</td><td>15</td><td>12</td><td>3</td><td>4</td><td>1</td></tr><tr><td>%misclassification</td><td>42.9</td><td>42.9</td><td>19</td><td>28.6</td><td>14.3</td></tr></table></body></html>

In process of experiment with NefClass number of fuzzy sets varied 3, 6, 7 and 11, the number of rules—50, for each sample the value of MSE (training and testing) was calculated. The best result was obtained for samples ratio 90/10, for which in the case of 6 sets were correctly classified all the patterns, while with 11 sets 6 patterns were correctly classified, 1 was classified incorrectly. The worst results were with 3 and 7 sets.

3. While changing the number of rules it was found that there exists an optimal number of rules after which the recognition error of the sample does not change.   
4. The experiments with non-fuzzy RBF neural network had shown the best result was obtained for training/test sample ratio 90–10, with an error of classification $1 4 . 3 \%$ . The results of the fuzzy neural network proved to be much better than the RBFN. Additionally, for NefClass FNN it is possible to change the number of fuzzy sets and the number of rules.

# 3.7 Medical Images of Breast Tumors Diagnostics with Application of Hybrid CNN–FNN Networks

# 3.7.1 State-of-Art Problem Analysis

In medical diagnostics problems substantial amount of problem constitute the features extraction for further processing and the choice features classification method. With development and wide dissemination of decision-support systems the demands to training algorithms are increasing. Reliability and simplicity of application influence on speed and quality of decision-making which is very important for express medical diagnostics. The advantages of medical diagnostics systems are speed, automation and stability of work which make them very comfortable tools for express medical diagnostics. Despite young age of medical informatics which don’t exceed 30 years information technologies in a whole are fast penetrating in various spheres of medicine and health defence. (family medicine, insurance medicine, building unified information space, integration in European medical space, etc.)

Nowadays, in practice, at every stage of diagnostics information technologies are utilized. The main goal of medical automated systems are extension of spheres practical tasks which may be solved with computers aid, raise of level intellectual decision support of doctors in particularly in process of express diagnostics based on processing and analysis of medical images of human tissue obtained by different source (MRT, CT, etc).

Now cancer constitute the great problem for health defence all over the world.

Basing the on data of IARC (International Agency of Cancer Research) 8.2 million death cases were registered in year 2012, 27 million new cases of illness are expected till 2030 [13]. Among the different types of cancer breast cancer takes the second place by its occurrence in women. Besides, mortality of it very high as compared with other cancer diseases [14].

Despite of progress which was achieved by diagnostics technologies final diagnosis of breast cancer including classification of tumors and diagnosis still is performed by pathologo-anatomists which use visual analysis of histological patterns by microscope. The latest achievements in images processing technologies and machine learning enable to construct systems of automatic detection and diagnostics (CAD/CADx) that may help pathologo-anatomists to make true diagnosis and accelerate his work. Classification of images histopathology on different patterns which corresponds to cancer and not-cancer states of tissue is often first rank goal in images analysis systems for automatic cancer diagnostics. The main problem in such systems lies therein they deal with complex histopathologic patterns.

Up to date several models and methods were developed for breast cancer detection using various machine learning algorithms. Using such methods and technologies of AI as neuron networks and SVM accuracy of diagnostics from 76 to $94 \%$ was attained at data set with 92 images.

Zhang et al. [15] suggested cascade approach. At the first cascade level the classifiers reject easy cases (those which evidently don’t pass test) and the others are transferred to the second level which uses more complex classification system and so on. This method was applied to data base of Israel technological Institute consisting of 361 images and accuracy results was $9 7 \%$ .

The most of last papers refers to field of breast cancer classification oriented on integer image [16–19]. But wide implementation of BIC and other forms of digital pathology faces with such disturbances as high cost of implementation, insufficient productivity for huge amount of clinic procedures, interior technologic problems non- solved regulator questions and opposition from pathologo-anatomists side. Till now the most of works based on histologic breast cancer analysis were performed on not large datasets. Some improvement presents data set with 7909 breast images obtained from 82 patients [19]. In this research the authors estimated various texture descriptors and various classifiers and carried out the experiments with accuracy from 82 to $8 5 \%$ .

Based on results presented in [19] one can conclude that texture descriptors may propose good solution for images processing. The alternative to this approach based on application of texture descriptors is the application of CNN for medical images processing and diagnostics, which is considered and developed in the present research. It was shown that CNN is able to overcome the conventional texture descriptors. Besides traditional approach to detection of features based on descriptors demands much efforts and high level knowledge of experts and usually is specific for every task that prevents its direct application for another similar tasks.

CNN, which firstly was developed by LeCun in [20] is widely applied now for achievement high results in different images recognition problems, with microscope and macroscope texture.

The set of experiments with data set BreaKHis presented in [19] testifies that CNN achieves better results than the best results which were attained by other models which were trained using alternative approach based on texture scenarios. But the best results may be attained by combining CNN with other models.

Therefore in our research we suggested to use CNN for feature detection in medical images of breast tissue and developed hybrid CNN-FNN classification system in which CNN is utilized to extract informative features of images and FNN NEFClass is applied for classification of detected tumors on images in two classes: benign and malicious ones.

The main goal of following section is the presentation and investigation of algorithmic and software tools for fast analysis of breast tissue images, detection of tumors and their classification into classes: benign or malignant one. This will enable to provide express analysis of images and raise the quality medical diagnostics

# 3.7.2 Data Set Description

Data set BreaKHis [19] contains microscope biopsies from benign and malign tumors of breast. The images were obtained in clinic research since January 2014 till December 2014.

BreaKHis consists of 7909 clinically representative microscopic images of breast tumors received from 82 patients with different scale augmentation $( 4 0 \times , \ 1 0 0 \times .$ , $2 0 0 \times$ , $4 0 0 \times )$ .

All patients during this period were investigated in R&D medical lab with clinical conclusion of breast cancer were invited to take part in this investigation. All data were anonymized. The patterns are generated of biopsy breast slides colored with hematoxylin and eosin (HE). The patterns are collected by surgery biopsy prepared for histologic research and marked by pathologists anatomists of R&D lab. The main goal was to preserve original structure of tissue and molecular composition which allows to observe it with optical microscope. For investigation all images were split into slides of size $3 \ \mathrm { m k m }$ . The final conclusion of each case was made by experienced pathologists anatomists which was confirmed by additional investigation such as immune histo-chemistry (IHC).

The microscope system Olympus BX-50 with augmentation 3.3 connected with digital camera Samsung SCC- 131AN, is used for obtaining digitized images of breast tissue. Images were obtained in 3-channels color space True color (24 bits value, 8 bits color channels RGB) with magnification coefficients $4 0 \times$ , $1 0 0 \times$ , $2 0 0 \times$ , and $4 0 0 \times$ .

In the Fig. 3.21, 3.22, 3.23 and 3.24 four images are presents with four magnification coefficients (a) $4 0 \times$ , (b) $1 0 0 \times$ , (c) $2 0 0 \times \mathrm { ~ i ~ }$ (d) $4 0 0 \times$ —obtained from one slide of breast tumor which contains malign tumor (breast cancer) Separated rectangular (added by hand for illustrative aims)—region of interest (ROI) which was chosen by pathologist-anatomist.

![](images/dd5727c32a00746a8c287b6077ea53dcc332e6d3865b2896e07b50f9e6729948.jpg)  
Fig. 3.21 Slide of malign tumor with magnification $4 0 \times$

![](images/77362428f453f03af92fddaaaa0caf995aa6d473ad555ba8554eb2ff8eed0afa.jpg)  
Fig. 3.22 Slide of malign tumor with magnification $1 0 0 \times$

![](images/48daa50f7a1444222388a30411dc1d1cee19465a2d971f43ef5ab55d6520c65f.jpg)  
Fig. 3.23 Slide of malign tumor with magnification $2 0 0 \times$

![](images/544cf718a7823dc5d11875efdc4e6439f64461b2d69b7ce3b8b061cac49b39ae.jpg)  
Fig. 3.24 Slide of malign tumor with magnification $4 0 0 \times$

![](images/c0aeb76acdabbe9ee662d4eb8bc67f43872e4db8c03bb348ef815a6334abdfe3.jpg)  
Fig. 3.25 Slide of benign tumor with magnification $1 0 0 \times$

Table 3.11 Distribution of images by augmentation factor and class   

<html><body><table><tr><td>Magnification</td><td>Benign</td><td>Malignant</td><td>Total</td></tr><tr><td>40×</td><td>625</td><td>1370</td><td>1995</td></tr><tr><td>100×</td><td>644</td><td>1437</td><td>2081</td></tr><tr><td>200×</td><td>623</td><td>1390</td><td>2013</td></tr><tr><td>400×</td><td>588</td><td>1232</td><td>1820</td></tr><tr><td>Total</td><td>2480</td><td>5429</td><td>7909</td></tr><tr><td>Number of patients</td><td>24</td><td>58</td><td>82</td></tr></table></body></html>

Up to date dataset BreakHis consists of 7909 images, divided into benign and malign tumors (Fig. 3.25)

Table 3.11 presents the distribution of images by classes [19].

# 3.7.3 Convolutional Neural Networks Brief Description

A CNN is a state-of-the-art method that has been largely utilized for image processing. A CNN model has the ability to extract global features in a hierarchical manner that ensures local connectivity as well as the weight-sharing property. It consists of the following layers [20, 21].

• Convolutional Layer: The Convolutional layer is considered as the main working ingredient in a CNN model and plays a vital determining part of this model. A kernel (filter), which is basically an $\mathbf { n } \times \mathbf { n }$ matrix successively goes through all the pixels and extracts the information from them.

Stride and Padding: The number of pixels a kernel will move in a step is determined by the stride size; conventionally, the size of the stride keeps to 1. Figure 3.26a shows an input data matrix of size $5 \times 5$ , which is scanned with a 3 $\times 3$ kernel. The light-green image shows the output with stride size 1, and the green image represents the output with stride size 2. When we use a $3 \times 3$ kernel, and stride size 1, then the convolved output is a $3 \times 3$ matrix; however, when we use stride size 2, the convolved output is $2 \times 2$ . Interestingly, if we use a $5 \times 5$ kernel on the above input matrix with stride 1, the output will be a $1 \times 1$ matrix. Thus, the size of the output image changes with both the size of the stride and the size of the kernel. To overcome this issue, we can utilize extra rows and columns at the end of the matrices that contain $0 \mathrm { ~ s ~ }$ . This adding of rows and columns that contain only zero values is known as zero padding.

For example, Fig. 3.26b shows how two extra rows have been added at the top as well as the bottom of the original $5 \times 5$ matrix. Similarly, two extra columns have been added at the beginning as well as the end of the original $5 \times 5$ matrix. Now, the olive-green image of Fig. 3.26b shows a convolved image where we have utilized a kernel of size $3 \times 3$ , stride size 1 and padding size zero. The convolved image is also a $5 \times 5$ matrix, which is the same as the original data size. Thus, by adding the proper amount of zero padding, we can reduce the loss of information that lies at the border.

• Nonlinear Performance: Each layer of the NN produces linear output, and by definition adding two linear functions will also produce another linear output. Due to the linear nature of the output, adding more NN layers will show the same behavior as a single NN layer. To overcome this issue, a rectifier function, such as Rectified Linear Unit (ReLU), Leaky ReLU, TanH, Sigmoid, etc., had been introduced to make the output nonlinear.

• Pooling Operation: A CNN model produces a large amount of feature information. To reduce the feature dimensionality, a down-sampling method named a pooling operation has been performed. A few pooling operation methods are well known such as

![](images/d43c5b709bf4f4099e9d49c64831e1251169fcb9fcf0d91f1ad26a59b77aeb95.jpg)  
Fig. 3.26 The effects of kernel size, the size stride and zero padding in a convolutional operation

– Max Pooling, – Average Pooling.

For our analysis, we have utilized the Max Pooling operation that selects the maximum values within a particular patch.

• Drop-Out: Due to the over training of the model, it shows very poor performance on the test dataset, which is known as over-fitting. These over-fitting issues have been controlled by removing some of the neurons from the network, which is known as Drop-Out (it was considered in detail in the chapter 2).

Decision Layer: For the classification decision, at the end of a CNN model, a decision layer is introduced. Normally, a Softmax layer or a SVM layer is introduced for this purpose. This layer contains a normalized exponential function and calculates the loss function for the data classification.

Figure 3.27 shows the work flow of a generalized CNN model that can be used for image classification. Before the decision layer, there must be at least one immediate dense layer available in a CNN model.

Utilizing the Softmax layer, the output of the end layer can be represented as

$$
Y _ { d } = \frac { \exp \left( H _ { d } ^ { e n d } \right) } { \sum _ { d = 1 } ^ { m } e x p \left( H _ { d } ^ { e n d } \right) }
$$

where

$$
\mathbf { \boldsymbol { \Upsilon } } ^ { e n d } = \sigma ( \mathbf { W } ^ { e n d } * \mathbf { H } ^ { e n d - 1 } + \mathbf { B } ^ { e n d } ) .
$$

Here, $k ^ { e n d - 1 }$ represents the kth neuron at the $( e n d - 1 )$ th layer, and $\sigma$ represents the nonlinear function. For binary classification, the number of classes is equal $\mathbf { m } =$ 2. Let $d = 1$ represent the Benign class and else it represents the Malignant class. The cross-entropy loss of $\bar { \mathbf { Y } } _ { d }$ can be calculated as

$$
{ \mathbf L } _ { d } = - \ln ( \bar { \Upsilon } d )
$$

![](images/1257a55415c4b65e9e93ee4622d2586ba6cb34677914385870517d74389ec73c.jpg)  
Fig. 3.27 Work flow of a Convolutional Neural Network

![](images/f241441ada13a4a23baabf2cf7e20e889638811d8cff64cfc53e7a915c99766d.jpg)  
Fig. 3.28 Convolutional neural network VGG-16

As we have a two-class classification problem, then only the $\mathrm { L } _ { 1 }$ and $\mathbf { L } _ { 2 }$ values are possible, and the output will be benign when $\mathbf { L } _ { 1 } < \mathbf { L } _ { 2 }$ , else the output will be malignant.

# 3.7.4 CNN Model for Image Classification

In the next Fig. 3.28 the architecture of VGG-16 is presented which was used in our work as detector of informative features. It was trained by different algorithms: stochastic gradient descent (SCD), basin hopping [22] and differential evolution.

As classifier of obtained features in our research was suggested to use FNN Nef Class.

In the next section results of classification by suggested hybrid CNN-Nefclass are presented and compared with results obtained by other researches which used as classifiers SVM machine, Random forests and other classification methods.

# 3.7.5 Experimental Investigations and Results Analysis

As it was already mentioned in our investigation pretrained CNN VGG 16 was used. Method of training transfer was applied for this purpose. Training transfer method as it goes from its name means the transfer of knowledge obtained during training one CNN to another neural network applied for solution of similar or connected problems.

There are two main training scenarios:

(1) Features extraction. In this case the last full-connected layer is deleted and the rest part of CNN is used as extractor for new data sets.   
(2) Fine tuning. In this case new data set is used for fine training of previously pretrained neural network.

In our research CNN VGG 16 was used for features extraction in medical images of breast tumors. After that the detected features were fed as input data to FNN NEFClass described in the previous section. As algorithms of training FNN three algorithms were used: basin hopping [22], stochastic gradient descent and differential evolution.

The series of experiments were carried out and the results were compared with works of predecessors [24]. In the following Tables 3.12 and 3.13 the results of classification with different parameters are presented. All sample was divided into training and testing subsamples with ratio $80 \% / 2 0 \%$ .

From this table on can readily see that beginning from 6 fuzzy sets per variable and 6 rules the accuracy doesn’t increase but complexity of training raises.

As it follows from table for two classes the best values of parameters are 4 fuzzy sets per variable and 6 rules. For comparison take the results of previous works obtained with different classifiers for the same problem [23] (see Table 3.13).

In the first experiment we varied the number of linguistic variables (terms) and rules that to determine the best parameters values [24]. As we can see from the

Table 3.12 Classification results of FNN NEFClass   

<html><body><table><tr><td>Initial number of fuzzy sets (linguistic terms)/ number of rules</td><td>40× (%)</td><td>100× (%)</td><td>200× (%)</td><td>400× (%)</td></tr><tr><td>2/2</td><td>73</td><td>74</td><td>74.2</td><td>73.5</td></tr><tr><td>4/2</td><td>75.3</td><td>74.8</td><td>75.7</td><td>75.4</td></tr><tr><td>6/2</td><td>678.2</td><td>79</td><td>78.4</td><td>78</td></tr><tr><td>8/2</td><td>76</td><td>75.4</td><td>76.5</td><td>75.8</td></tr><tr><td>2/4</td><td>75</td><td>74</td><td>73.8</td><td>73</td></tr><tr><td>4/4</td><td>78.3</td><td>76.3</td><td>75.7</td><td>75.4</td></tr><tr><td>6/4</td><td>82</td><td>83</td><td>82.4</td><td>83.2</td></tr><tr><td>8/4</td><td>82.2</td><td>81.5</td><td>81.5</td><td>83.8</td></tr><tr><td>2/6</td><td>75.4</td><td>73.8</td><td>74.4</td><td>73.2</td></tr><tr><td>4/6</td><td>90</td><td>91</td><td>90.5</td><td>90</td></tr><tr><td>6//6</td><td>89</td><td>89.7</td><td>90.2</td><td>89.5</td></tr><tr><td>8/6</td><td>90.3</td><td>90.5</td><td>92</td><td>91.2</td></tr><tr><td>4/8</td><td>89.3</td><td>89.8</td><td>89.7</td><td>89.3</td></tr><tr><td>6/8</td><td>89.2</td><td>88</td><td>89.4</td><td>88.4</td></tr><tr><td>8/8</td><td>88</td><td>87.2</td><td>87.2</td><td>87</td></tr></table></body></html>

Table 3.13 Comparison of results different classifiers   

<html><body><table><tr><td></td><td>40× (%)</td><td>100x (%)</td><td>200× (%)</td><td>400x (%)</td></tr><tr><td>Linear svm</td><td>89</td><td>89</td><td>88</td><td>88</td></tr><tr><td>Polynomial svm</td><td>88</td><td>90</td><td>89</td><td>85</td></tr><tr><td>Random forest</td><td>89.18</td><td>88</td><td>87.74</td><td>80</td></tr><tr><td>Nefclass</td><td>90</td><td>91</td><td>90.5</td><td>90</td></tr></table></body></html>

Table 3.13 FNN NEFClass shows better results than previous classifiers: SVM machine and Random forest [23].

In our work for training of FNN NEFClass were applied three algorithms, namely, basin hopping, stochastic gradient descent and differential evolution. Using algorithms basin hopping and stochastic gradient descent we obtained approximately equal results that may mean the true optimal results while the training results of differential evolution appeared to be much worse.

It’s worth to note that in this problem the number of features extracted by CNN VGG16 was very large—4096 features. Therefore it was decided to cut the number of features. For this principal components method [25] was applied. In the Table 3.14 the results of such reduction are presented.

From the Table 3.14 it follows that the results of reduction with 250 principal components is most acceptable as the complexity of training increases approximately proportional to number of input data.

Due to lack of time the next experiments were performed using data with $1 0 0 \times$ magnificence factor (2081 images). In the next Table 3.15 the accuracy of classification is presented with different parameters.

In the Table 3.16 the dependence of classification accuracy versus number of features is presented. one can see from this table that accuracy decreased only by some percent due such features reduction. But by this reduction we substantially cut the training time.

Table 3.14 The dependence of total variance on number of components and approximate training time   

<html><body><table><tr><td>Number of principal components</td><td>Variation</td><td>Approximate training time (in h)</td></tr><tr><td>100</td><td>0.840587</td><td>~2</td></tr><tr><td>200</td><td>0.89736</td><td>~3</td></tr><tr><td>250</td><td>0.91232</td><td>~4</td></tr><tr><td>500</td><td>0.95486</td><td>~9</td></tr></table></body></html>

Table 3.15 Classification accuracy with 250 features   

<html><body><table><tr><td>NumberofFS/numberof rules</td><td>100× (%)</td></tr><tr><td>4/4</td><td>80.64</td></tr><tr><td>4/6</td><td>87.24</td></tr><tr><td>4/8</td><td>88.18</td></tr></table></body></html>

Table 3.16 Classification accuracy with different number of features   

<html><body><table><tr><td>Number of linguistic terms,number of rules/number of features</td><td>100 (%)</td><td>250 (%)</td><td>4096 (%)</td></tr><tr><td>4/4</td><td>75.23</td><td>80.64</td><td>76.3</td></tr><tr><td>4/6</td><td>83.34</td><td>87.24</td><td>91</td></tr><tr><td>4/8</td><td>84.21</td><td>88.18</td><td>89.8</td></tr></table></body></html>

From this table one can readily see that the accuracy drops with decrease of features number but insignificant by $3- 5 \%$ if compare 100 and 250 features. For comparison use the full set of features 4096 and we can see that with decrease features number in 20 times the accuracy falls $2 - 3 \%$ in means.

This conclusion testify in favour of application of PCM method for reduction of dimension of medical images classification problems.

# Conclusion

1. The problem of analysis of breast tissue medical images and classification of detected tumor in two classes: benign and malignant is considered an discussed.   
2. For pattern recognition of breast tumors hybrid CNN- FNN network is suggested in which the CNN VGG 16 is used for informative features extraction while FNN NEFClass is used for classification of detected tumors.   
3. For training FNN NEFClass algorithms basin hopping, stochastic gradient descent and differential evolution were suggested and their efficiency investigated.   
4. The experimental investigations of suggested hybrid CNN-FNN network in the problem of classification real images of breast tumors in dataset BreakHis were carried out.   
5. The comparison of classification accuracy of the suggested hybrid CNN-FNN network with known works based on use of classification algorithms SVM and Random forest was performed which confirmed the efficiency of the suggested approach.   
6. The problem of reducing number of features in medical images classification problem using PCM method was investigated and its efficiency for BD classification problems was explored.

# References

1. D. Nauck, R. Kruse, Generating classification rules with the neuro-fuzzy system NEFCLASS, in Proceedings of the Biennial Conference of the North American Fuzzy Information Processing Society (NAFIPS’96), Berkeley (1996)   
2. D. Nauck, R. Kruse, New learning strategies for NEFCLASS, in Proceedings of the Seventh International Fuzzy Systems Association World Congress IFSA’97, vol. IV (Academia Prague, 1997), pp. 50–55   
3. D. Nauck, R. Kruse, What are neuro-fuzzy classifiers?, in Proceedings of the Seventh International Fuzzy Systems Association World Congress IFSA’97, vol. IV (Academia Prague, 1997), pp. 228–233   
4. D. Nauck, Building neural fuzzy controllers with NEFCON-I, in Fuzzy Systems in Computer Science, Artificial Intelligence, ed. by Rudolf Kruse, Jorg Gebhardt, Rainer Palm (Vieweg, Wiesbaden, 1994), pp. 141–151   
5. Yu.P. Zaychenko, F. Sevaee, A.V. Matsak, Fuzzy neural networks for economic data classification, in Vestnik of National Technical University of Ukraine “KPI”, section Informatic, Control and Computer Engineering, vol. 42 (2004), pp. 121–133 (in Russian)   
6. Yu.P. Zaychenko, Fuzzy Models and Methods in Intellectual Systems (Kiev-Publishing House “Slovo”, 2008) 354 pp.   
7. A. Krizhevsky, I. Sutskever, G.E. Hinton, Imagenet classification with deep convolutional neural networks, in Proceedings of 26th Annual Conference on Neural Information Processing Systems 2012 (NIPS), ed. by P.L. Bartlett, F.C.N. Pereira, C.J.C. Burges, L. Bottou, K.Q. Weinberger, Dec 2012, pp. 1106–1114, http://papers.nips.cc/paper/4824- imagenet-classification-with-deep-convolutional-neural-networks   
8. Yu.P. Zaychenko, I.M. Petrosyuk, M.S. Jaroshenko, The investigations of fuzzy neural networks in the problems of electro-optical images recognition, in System Research and Information Technologies № 4 (2009), pp. 61–76 (in Russian)   
9. M. Zgurovsky, Yu. Zaychenko, The Fundamentals of Computational Intelligence: System Approach (Springer International Publishing AG, Switzerland, 2016), 308 pp.   
10. E.H. Maлышeвcкaя, Aнaлиз иcпoльзoвaния нeйpoнныx ceтeй для диaгнocтики paкa шeйки мaтки пo мyльтиcпeктpaльнoмy изoбpaжeнию/ E.H. Maлышeвcкaя// Cиcтeмнi дocлiджeння тa iнфopмaцiйнi тexнoлoгiї. – 2010. – №2 –C. 64–71   
11. K. Malyshevska, The analysis of neural networks’ performance for medical image classification. Int. J. Inf. Content Process. 1(2), 194–199 (2014)   
12. Y. Zaychenko, V. Huskova, Recognition of objects on optical images in medical diagnostics using fuzzy neural network NEFClass. Int. J. Inf. Models Anal. 4(1), 13–22 (2015)   
13. P. Boyle, B. Levin (eds.), World Cancer Report 2012 (IARC, Lyon, 2012), http://www.iarc. fr/en/publications/pdfs-online/wcr/2008/wcr_2012.pdf   
14. S.R. Lakhani, I.O. Ellis, S. Schnitt, P. Tan, M. van de Vijver, WHO Classification of Tumours of the Breast, 4th edn. (WHO Press, Lyon, 2012)   
15. Y. Zhang, B. Zhang, F. Coenen, W. Lu, Breast cancer diagnosis from biopsy images with highly reliable random subspace classifier ensembles. Mach. Vis. Appl. 24(7), 1405–1420 (2013)   
16. Y. Zhang, B. Zhang, F. Coenen, J. Xiau, W. Lu, One-class kernel subspace ensemble for medical image classification. EURASIP J. Adv. Signal Process. 2014(17), 1–13 (2014)   
17. S. Doyle, S. Agner, A. Madabhushi, M. Feldman, J. Tomaszewski, Automated grading of breast cancer histopathology using spectral clustering with textural and architectural image features, in Proceedings of the 5th IEEE International Symposium on Biomedical Imaging (ISBI): From Nano to Macro, vol. 61 (IEEE, 2008), pp. 496–499   
18. A.J. Evans, E.A. Krupinski, R.S. Weinstein, L. Pantanowitz, 2014 american telemedicine association clinical guidelines for telepathology: another important step in support of increased adoption of telepathology for patient care. J. Pathol. Inform. 6 (2015)   
19. F. Spanhol, L.S. Oliveira, C. Petitjean, L. Heutte, A dataset for breast cancer histopathological image classification. IEEE Trans. Biomed. Eng. (2016)   
20. A. Krizhevsky, I. Sutskever, G.E. Hinton, Imagenet classification with deep convolutional neural networks, in Advances in Neural Information Processing Systems, vol. 25 (2012), pp. 1097–1105   
21. Y. LeCun, B. Boser, J.S. Denker, D. Henderson, R.E. Howard, W. Hubbard, L.D. Jackel, Backpropagation applied to handwritten zip code recognition. Neural Comput. 1(4), 541–551 (1989)   
22. B. Olson, I. Hashmi, K. Molloy, A. Shehu1, Basin hopping as a general and versatile optimization framework for the characterization of biological macromolecules. Adv. Artif. Intell. 2012(Article ID 674832) (2012)   
23. A. Singh, H. Mansourifar, H. Bilgrami, N. Makkar, T. Shah, Classifying Biological Images Using Pre-trained CNNs, https://docs.google.com/document/d/1H7xVK7nwXcv11CYh7hl 5F6pM0m218FQloAXQODP-Hsg/edit?usp=sharing   
24. Yu. Zaychenko, G. Hamidov, I. Varga, Medical images of breast tumors diagnostics with application of hybrid CNN–FNN network in System Analysis and Information Technologies, № 4 (2018)   
25. N. Jindal, V. Kumar, Enhanced face recognition algorithm using PCA with artificial neural networks. Int. J. Adv. Res. Comput. Sci. Softw. Eng. 3, 864–872 (2013)

# Chapter 4 Intellectual Analysis of Systemic World Conflicts and Global Forecast for the 21st Century

# 4.1 Introduction

Data on global conflicts took place from $7 5 0 \mathbf { B } . \mathbf { C }$ . up to now are analyzed and their general pattern is revealed. An attempt is made to foresee the next global conflict called the conflict of the 21st century. Its nature and main characteristics are analyzed. Main global threats are listed, and their impact on five groups of countries is determined using cluster analysis.

Based on the consideration of evolutionary development of the civilization as a holistic process determined by a harmonious interaction of its components, patterns of Kondratieff cycles of the development of the global economy and C-waves of global systemic conflicts are compared and an attempt is made to predict these processes in the 21st century using a metric approach.

The next part of the study is based on the Fibonacci pattern of global systemic conflicts (Ñ-waves) which allowed us to formulate the hypotheses about a metric relation between two global periodic processes, namely, between the sequence of 11-year cycles of solar activity and the process of evolutionary structurization of the family of $\tilde { \mathrm { N } }$ -waves of global systemic conflicts covering large and super-large time intervals and having a variable structural configuration.

The structural analysis is performed for Cn-waves of global systemic conflicts based on their empirical sequence, and metric approaches are proposed to study and forecast these processes. Global systemic conflicts and great Kondratieff waves of the development of the world economy are proved to correspond to a number of additional conditions, namely, to the modern concept on the acceleration of historical time, to the law of structural harmony, and to global forecasts for the 21st century.

Bayesian Belief Networks are used to establish qualitative causal relations between global threats and indicators of sustainable development. The method of belief network synthesis and a method of generalization of final results are proposed. This made it possible to obtain a holistic understanding of effects of global threats on the sustainable development of countries and regions of the world.

The generalization and formalization of approaches to the recognition of C-waves of global systemic conflicts using big historical data are performed and general concept of description and interpretation of these waves is proposed. Special attention is paid to the class of big C-waves, which cover super-long time intervals. Their pattern is invariant to the evolution of the nature of global conflicts. There has also been made an attempt to predict these processes in the 21st century by using a metric approach. The possible scenarios of the development of the conflict of the 21st century have been constructed and analyzed.

# 4.2 Identifying the Regularity of the Emergence of Systemic World Conflicts, Based on the Analysis of Big Historical Data

An analysis of the complete list of global conflicts [1] occurred since $2 5 0 0 \mathrm { B } . \mathrm { C } .$ . up to now shows that, beginning with the 7th century B.C., these conflicts did not follow any regular pattern, reminding a random process such as white noise. Historic facts about constant conflicts at early stages of the development of human civilization as a natural form of its existence confirm this. A certain periodic pattern can only be revealed in a series of global conflicts only after higher forms of society organization appear. This periodic pattern was revealed and studied in [2]. With this pattern, it becomes possible to foresee the next system conflict, to analyze the set of threats giving rise to it, to determine the effect of these threats on its course, and to construct scenarios of possible development of society during and after the conflict. Pessimistic predictions are necessary from the scientific point of view to avoid possible negative outcome, although naturally everyone would prefer to be wrong in such predictions.

# 4.2.1 Fibonacci Pattern of the Emergence of Systemic World Conflicts

The paper [1] analyzes the series of global conflicts over a period from 705 B.C. till now with the following time quantization:

$$
\Delta _ { n } = 5 0 \mathrm { y e a r s } - 5 \mathrm { y e a r s } \cdot n ; \quad n = 0 , 1 , 2 , . . . ,
$$

The number of global conflicts for each quantization interval $\Delta _ { n }$ has been determined as the arithmetic mean of the number of all conflicts on this time interval. For $\Delta { _ { 9 } } = 5$ years ${ \ ' } n _ { m i n } = 9 { \ ' }$ Þ, six consecutive evolutionary groups (waves) $\left\{ C _ { n } \right\}$ , $n = 1$ , 2, …, 6, of global conflicts ( $C _ { n }$ -waves) has become apparent (Fig. 4.1).

![](images/b1fb5bfd9bb3944ea698f5fa718cc5abb99aec076ce33afab48956403e651369.jpg)  
Fig. 4.1 Structural portrait of $C n$ -waves of global system conflicts

(Let $C _ { n }$ be the predicted wave, the essence of which will be revealed later).

These waves are periodic (Table 4.1) and have the following characteristic features:

(i) The life of each $C _ { n }$ -wave generates five sequential evolutionary phases (stages) $\left\{ C _ { n , i } \right\}$ , $i = 1 , . . . , 5$ : $\{ C _ { n , i } \} , \quad { \mathrm { ~ i = 1 , } } \quad . . . , \quad 5 \colon \ C _ { n , 1 } \quad ( { \mathrm { o r i g i n } } ) \to C _ { n , 2 } \quad ( { \mathrm { g r o w t h } } ) \quad \to \quad C _ { n , 3 } \quad ( C _ { n , 4 } \to C _ { n , 5 } ) \quad .$ (culmination) $ C _ { n , 4 }$ (decrease) $ C _ { n , 5 }$ (decay).   
(ii) The life duration $T ( C _ { n } )$ of each subsequent $C _ { n }$ -wave is uniquely determined by the life duration of two previous waves, namely,

$$
T ( C _ { n } ) = T ( C _ { n - 2 } ) - T ( C _ { n - 1 } ) .
$$

(iii) Conflict intensity $I ( C _ { n } ) = N ( C _ { n } ) / T ( C _ { n } )$ for $C _ { n }$ -waves, $n = 1 , 2 , 3 , . . . , 6 ,$ increases, where $N ( C _ { n } )$ is the number of conflicts that form the $C _ { n }$ -wave: $I ( C _ { n + 1 } ) > I ( C _ { n } )$ , which is because of the technological progress of mankind.

Global conflicts defined by these features are called $C _ { n }$ -waves of global systemic conflicts or $C _ { n }$ -waves. As we see, six $C _ { n }$ -waves can be identified over the period from 705 B.C. until now.

Table 4.1 Main characteristics of $C _ { n }$ -waves of conflicts   

<html><body><table><tr><td>Cn-waves</td><td>Time interval of the Cn- wave, year</td><td>Life duration T(Cn) for the Cn- wave,year</td><td>Number of conflicts N(Cn) that form the Cn- wave</td><td>Conflict intensity I(Cn) in the Cn- wave</td><td>Correspondence of Cn-waves to Fibonacci numbers (Fs)</td></tr><tr><td>C1</td><td>705B.C.-401 A.D.</td><td>1106</td><td>1218</td><td>1.101</td><td>F7= 13</td></tr><tr><td>C2</td><td>402-1074</td><td>674</td><td>756</td><td>1.122</td><td>F6=8</td></tr><tr><td>C</td><td>1075-1497</td><td>422</td><td>1680</td><td>3.981</td><td>F5=5</td></tr><tr><td>C4</td><td>1498-1749</td><td>252</td><td>1543</td><td>6.123</td><td>F4= 3</td></tr><tr><td>C5</td><td>1750-1919</td><td>170</td><td>1485</td><td>8.735</td><td>F3=2</td></tr><tr><td>C6</td><td>1920-2007</td><td>87</td><td>1035</td><td>11.897</td><td>F2=1</td></tr><tr><td>C7 (predicted)</td><td>2008-2092</td><td>85</td><td>>1400</td><td>>16</td><td>F1= 1</td></tr></table></body></html>

Table 4.2 Coefficients of the golden section $T ( C _ { n } ) / T ( C _ { n + 1 } )$ , Fibonacci numbers $\{ F s \}$ , and periods of global conflicts $T ( C _ { n } )$ for the sequence $\{ C _ { n } \}$ , $n = 1$ , 2, 3, 4, 5, 6, 7   

<html><body><table><tr><td>{Cn}</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td></tr><tr><td>T(Cn),years</td><td>1106</td><td>674</td><td>422</td><td>252</td><td>170</td><td>87</td><td>85</td></tr><tr><td>T(Cn)/T(Cn+1)</td><td>1.641</td><td>1. 597</td><td>1.675</td><td>1.482</td><td>1.954</td><td>1.023</td><td>1</td></tr><tr><td>Fs,s=8-n</td><td>13</td><td>8</td><td>5</td><td>3</td><td>2</td><td>1</td><td>1*</td></tr><tr><td>Fs/Fs-1</td><td>1.625</td><td>1.6</td><td>1.667</td><td>1.5</td><td>2</td><td>1</td><td>1</td></tr></table></body></html>

Table 4.2 presents the ratios:

$$
T ( C _ { n } ) / T ( C _ { n + 1 } ) , n = 1 , 2 , . . . , 6 ,
$$

which vary around the golden Sect. (1.618).

Let us represent the sequence $\{ T ( C _ { n } ) \} , n = 1 , . . . , 7$ (Table 4.2) as a series

$$
\begin{array} { c } { { T ( C _ { 1 } ) = 1 3 \cdot k _ { c } ; T ( C _ { 2 } ) = 8 \cdot k _ { c } ; T ( C _ { 3 } ) = 5 \cdot k _ { c } ; } } \\ { { T ( C _ { 4 } ) = 3 \cdot k _ { c } ; T ( C _ { 5 } ) = 2 \cdot k _ { c } ; T ( C _ { 6 } ) = 1 \cdot k _ { c } ; T ( C _ { 7 } ) = 1 \cdot k _ { c } ; } } \end{array}
$$

where $k _ { c } = 8 5$ years is the greatest common divisor for all the values of life duration $\mathrm { T } ( \mathrm { C _ { n } } )$ :

The number series:

$$
\mathrm { F _ { s } } = \{ 1 3 , 8 , 5 , 3 , 2 , 1 , 1 ^ { \ast } \}
$$

![](images/8146af6820ed549258449bdbdcc571842e270968ea7ee2e19f6acd0e6811b0c5.jpg)  
Fig. 4.2 Real $I ( C _ { n } )$ and approximated $I ^ { * } ( C _ { n } )$ intensities of global system conflicts and their durations $T ( C _ { n } )$ for the sequence $\{ C _ { n } \}$ ${ \bf \dot { \boldsymbol { n } } } = 1$ , 2, 3, 4, 5, 6, 7) sequence $\{ C _ { n } \}$ $( n = 1 , 2 , 3$ , 4, 5, 6, 7)

is a sequence of Fibonacci numbers, where $1 ^ { * }$ pertains to the predicted wave $C _ { 7 }$ of this sequence.

The conflict intensity $I ^ { * } ( C _ { n } )$ depends on the level of technological progress of society and increases in time hyperbolically (Fig. 4.2):

$$
I ^ { * } ( C _ { n } ) = N ( C _ { n } ) \cdot \Big \{ T ( C _ { n } ) ^ { - 1 } \Big \} = N ( C _ { n } ) \cdot ( F _ { 8 - n } \cdot k _ { c } ) ^ { - 1 } ,
$$

whence the intensity of the seventh (predicted) conflict follows:

$$
I ^ { * } ( C _ { 7 } ) > 1 6
$$

Since six members of the sequence $\mathrm { T } ( { \bf C } _ { 1 } ) , . . . , \mathrm { T } ( { \bf C } _ { 6 } )$ obey the law of variation of elements in the Fibonacci series, the paper [2] advances a hypothesis that it is this pattern that describes the course of global systemic conflicts. Hence, the seventh (predicted) element of the sequence should be $\mathrm { T } ( { \bf C } _ { 7 } ) = \mathrm { T } ( { \bf C } _ { 5 } ) - \mathrm { T } ( { \bf C } _ { 6 } ) = 1 \cdot \mathrm { k _ { c } } \approx$ 85 years. We will call this seventh wave of global systemic conflicts $\left( C _ { 7 } \right)$ the conflict of the 21st century. It has the time range 2010–2096 with the following probable phases:

2010s (origin);   
beginning of the 2020s to the end of the 2040 (growth);   
2050s (culmination, $I ^ { * } ( C _ { 7 } ) > 1 6 ) \$ ;   
beginning of the 2060s to the end of the 2070s (decrease);   
2080s (decay).

Thus, the revealed patterns describe the course of global systemic conflicts in terms of the durations $T ( C _ { n } )$ of these conflicts, their intensity $I ^ { * } ( C _ { n } )$ , and Fibonacci numbers $\left( F _ { s } \right)$ [2].

# 4.2.2 Conflict of the 21st Century and Analysis of Its Nature

Let us consider the Top 12 global threats to the sustainable development to be those determined in the beginning of the XXI century by such recognized international organizations as United Nations Organization (UNO), World Health Organization (WHO), World Economic Forum, Transparency International, Global Footprint Network, International Energy Agency, World Resources Institute, British Petroleum company and others. The analysis of every threat will give the possibility to determine the vulnerability level of different countries of the world to the influence of these aggregated threats. Let us analyze each of the 12 global threats separately.

# Threat 1. Global Decrease in Energy Security (ES)

For the first part of the XXI century one of the main critical challenges to the mankind is the rapid decrease in organic fuel resources that are extracted from entrails of the earth, and the increase in consumption of such resources, first of all, by large developing countries. In the beginning of the 30-ies of the current century, the curves of energy consumption and production of energy from oil will be crossed [3]. In other words, the “production-consumption” balance of energy, produced from oil, will change its value from positive to negative. The similar phenomena will occur for “production-consumption” balances of energy, made from gas in the beginning of 40-ies and for the energy generated from uranium-235 in the 50-ies– 60-ies, accordingly (Fig. 4.3).

![](images/6d53849e40f73b0a4b972880f35ece1042e13f76e7d4315a6ea1916ddef51dba.jpg)  
Fig. 4.3 Changes the balance “production–consumption” from positive to negative for energy, produced from oil, gas, and uranium-235, accordingly

Thus, until the mankind invents the energy resources that could fully replace the organic types of fuel and nuclear energy, the energy security of a country in particular and the world in general, will decrease. In order to quantitatively estimate the energy security of different countries of the world let us introduce the energy security index (Energy Security Index, ES) that will be calculated by the formula:

$$
\begin{array} { c } { E S _ { i } = \frac { E x h a u s t a b l e s _ { i } + R e n e w a b l e s _ { i } } { 2 } , ~ i \in \{ c o u n t r i e s \} ; } \\ { E x h a u s t a b l e s _ { i } = \frac { N u c l e a r R _ { i } + C o a l R _ { i } + O i l R _ { i } + G a s R _ { i } } { \frac { \operatorname* { m a x } } { \forall j \in \{ c o u n t r i e s \} } \{ N u c l e a r R _ { j } + C o l R _ { j } + O i l R _ { j } + O i l R _ { j } + G a s R _ { j } \} } ; } \\ { R e n e w a b l e s _ { i } = \frac { R e n e w a b l e s U s e d _ { i } } { \operatorname* { m a x } } R e n e w a b l e s U s e d _ { j } , } \end{array}
$$

where:

• $E S \in [ 0 ; 1 ]$ ; {countries}—set of explored countries;   
• Exhaustables is the component that characterizes the dynamics of resource deflation;   
• Renewables is the component that characterizes the volumes of usage of renewable sources in national energetic;   
• NuclearR, CoalR, OilR, GasR—resources of uranium-235, coal, oil and gas (Nation Master, n.d.);   
• Renewables Used—part of renewable energy produced and consumed by the country (at the expense of use of the energy of water, sun, wind, geothermal heat, biomass and rubbish burning) in percents from total energy consumption [4]. To evaluate the reduction in the reserves of organic fuel for various countries in the subsequent simulation, we will use the index of “Consumption of traditional fuels in percentage of the total energy needs of the country” [4].

# Threat 2. The Imbalance Between Biological Capacity of the Earth and Human Needs in Biosphere (FB)

In early 2018, the world’s population reached 7.6 billion people living on the total area $5 1 0 , 0 7 2 , 0 0 0 \mathrm { k m } ^ { 2 }$ . The daily growth of Earth population exceeds 162 thousand people [5]. According to the method of arithmetic extrapolation the Earth population will have been 9.75 billion people by the year 2050. That is why the first threat appears being related to the fact that the Earth will be inhabited by the number of people that will exceed its abilities to sustain on the basis of the present natural resources. The japanese experts believe that the real problems for the mankind will be connected with the catastrophic shortage of water, energy, foodstuff that can cause new conflicts on the Earth [6].

Nature can satisfy human requirements for business activity and only while this activity remains within the biosphere renewable capacity on the populated part of the planet. The calculation of ecologically disturbed area (Ecological Footprint) [5] gives the possibility to establish some limit according to which the ecological requirements to the world economics are within or exceed the biosphere abilities (Biocapacity) to supply the people with goods and services. This limit helps people, organizations and government to create strategies, establish the goals and provide the process according to the requirements of the sustainable development.

Ecologically disturbed territory (Ecological Footprint) determines which its part is necessary to preserve present population according to the present level of consumption, level of technological development and usage efficiency of natural wealth. The unit of measurement of this dimension is average (global on the whole Earth) hectare. The most substantial component of the Ecological Footprint is the territory of the Earth used for foodstuff production, forest area, biofuel amount, ocean (seas) territory, used for fishing and the most important element is the Earth area, necessary to support the life of plants absorbing the emissions of $\mathrm { C O } _ { 2 }$ as a result of organic fuel burning.

Ecological Footprint envisages that in world economy the people use resources and ecological services from all over the world. Thus, the indicator for a country may exceed its actual biological possibilities. On the basis of it, the essence of Ecological Footprint for a country is the extent of its consumption and global impact on environment.

The same methodology can be used for calculation (in the same values) of biological abilities of the Earth, biological productivity of its territory. In 2017 biological abilities of the Earth were approximately 11.2 billion or 1.8 global hectares per capita (non-human species were not considered). Now the human need in biosphere, i.e. its global Ecological Footprint is 18.1 billion global hectares or 2.3 global hectares per capita. That is why, today global Ecological Footprint exceeds biological abilities of the Earth by 0.5 global hectares per capita. This means that vital resources of the planet disappear faster than the nature can renew (Fig. 4.4).

This threat has substantial correlation degree with demographic structure change of the planet population. For example, according to Human Development Report

![](images/1ada6f231ee81da185f3abf10367b4187cd555e4bd747418d10469b499ab64bf.jpg)  
Fig. 4.4 Misbalances between biocapacity of the Earth and total consumption (ecological footprint)

2017 the biggest growth of population over a period of the following 50 years is expected in the poorest regions of the world: in Africa it will increase in 2 times, In Latin America and Caribbean basin will increase in 1.5 time, at the same time in Europe it will decrease in 0.8 times [4]. Essential threat is also uncontrolled increase in the urban population in underdeveloped countries. By the year 2050 it will have been doubled approximating to 10 billion people. It will lead to intensification of transport, ecological and social problems, an increase in criminality and other consequences of chaotic urbanization.

The important tendency of the nearest decades is rapid change in the structure of religious groups of the Earth population. So, from 1980 to 2015 the number of Muslins will increase from 16.5 to $30 \%$ , the number of Christians will decrease from 33.3 to $31 \%$ , the number of Hindus will decrease from 13.3 to $10 \%$ , the number of Buddhists will decrease from 6.3 to $5 \%$ . The number of representatives of other religious groups will also decrease from 31.1 to $2 5 \%$ (Japan Vision 2050. Principles of Strategic Science and Technology Policy Toward 2020. Science). Science Council of Japan, 2005). These changes will cause the necessity of searching new methods of tolerance coexistence of people on the Earth.

For estimation of increasing threats, connected with imbalance between biological capability of the Earth and human requirements in biosphere, in terms of demographic structure change of the world we will use the indicator which is ecological reserve $( ^ { 6 6 } + ^ { 7 7 } )$ or deficit $( ^ { 6 6 } - 7 7 )$ in global hectares per capita for a country (Global Footprint Network, http://www.footprintnetwork.org/en/index.php/GFN/) [6].

# Threat 3. Growing Inequality Between People and Countries on the Earth (GINI)

According to the World Bank, the difference in profits between the richest and poorest countries was 44:1 in 1973 and is now 72:1. Three richest persons have a capital that exceeds the property of 47 poor countries, 475 richest people hold a capital that exceeds the property of half of the mankind. The ratio between one fifth of the rich part of the world population and one fifth of the poorest population has achieved 1:75.

The benefits of civilization remain unaccessible for the poorest group. Its representatives live for less than two dollars per day. Seven hundred million of them live in Asia, 400 million in Africa, and 150 million in Latin America. The difference between the richest and poorest groups in the standard of living has increased almost ten times over the last twenty years. The threat is rather hazardous from the standpoint of increasing number of conflicts in the world, growth of corruption, terrorism, and criminality, environmental degradation, impaired education and medical service.

To asses quantitatively the disparity of the distribution of economic and social benefits for each of the countries under study, we will use the Gini index [7], which reflects these characteristics.

# Threat 4. The Spread of Global Diseases (GD)

The World Health Organization considers such diseases as cancer, cardio ischemia, cerebrovascular disease (paralysis), chest troubles, diarrhea, AIDS, tuberculosis, malaria, diabetes to be the most dangerous for mankind as they may not only have bad consequences but also globally spread all over the world [8].

![](images/a48a43e75fc138decd94a8464b777b6de4d0edc563f4caeaa6c1648b0a9b3ed5.jpg)  
Fig. 4.5 Comparison of mortality factors, 2004–2030, resource: (http://www.plosmedicine.org/ article/info%3Adoi%2F10.1371%2)

During the next 20 years the sufficient increase in mortality caused by all noninfectious global diseases and decrease in mortality caused by AIDS, tuberculosis and malaria are expected (Fig. 4.5). Such diseases as cardio ischemia, cerebrovascular disease, lung cancer and diabetes will become main global diseases during this period. At the same time the rate of total mortality from tobacco consumption will increase from 5.8 million people in the year 2009 to 8.3 million in the year 2030. Thus, tobacco is expected to kill by $50 \%$ people more than AIDS. Total human mortality on the Earth will be by $10 \%$ predetermined by the tobacco consumption.

According to the UNAIDS international organization, the number of HIV-infected people on the Earth increased from 36.9 million in 2004 to 45 million in 2015. This general tendency (with minor oscillations) is traced in all regions of the world.

Despite the success in tuberculosis control, eight million new diseases occur annually in the world, which cause two million lethal outcomes. In the countries with high prevalence of HIV/AIDS, the number of tuberculosis diseases has increased 3–4 times over the last 15 years (www.who.int/gb), $80 \%$ of them in Africa, South-East Asia, and western part of the Pacific Ocean.

Malaria is traditionally most spread in Africa and Latin America. For the last five years, morbidity has increased 2–3 times in Afghanistan, Ghana, Papua New Guinea, Pakistan, and Uganda and 30 times in Mozambique and Democratic Republic of the Congo; menacing rates of growth of morbidity (70 times increase) are observed in Mali. In other countries where malaria is revealed, the number of diseased changes within the limits of $\pm 5 0 \%$ for the last five years.

The spread of global diseases (GD) is measured in the total number of people (millions per year) who died from these diseases. For the subsequent simulation, we take data on these diseases from the World Health Organization [8].

# Threat 5. Information Gap (IG)

Information Gap is formed by two determinants of the modern information society:

1. Humanity is constantly generating gigantic volumes of new data and information. Its total volume will reach $3 5 \mathrm { Z B }$ by 2020 ( $\mathrm { ~ 1 ~ Z B = 1 0 2 1 ~ B ~ }$ ). At the same time, mankind is capable of comprehending, systematizing, processing and documenting significantly smaller volumes of new data and information (until 2020, only 15 ZB). Thus, by 2020, up to $2 0 \mathrm { Z B }$ will accumulate unthinkable and unprocessed information, a sort of “Information black hole.” This information uncertainty explains the unpredictable and unconscious phenomenon (Fukushima catastrophe in 2011 as a result of the unpredictable earthquake and tsunami, the disintegration process of the European Union in 2016 as a result of the British referendum, and many others). This component of the Information Gap will be measured using the ICT Development Index (IDI, http://www.itu. int/net4/ITU-D/idi/2016/).

2. The vulnerability of one or another country, territory or world to the action of cyber attacks. This component of the IG will be measured using the Global Cybersecurity Index (GCI, http://www.itu.int/en/ITU-D/Cybersecurity/Pages/ GCI-2017.aspx).

Both IDI and GSI indexes are annually formed by International Telecommunication Union. The resulting index of IG will be calculated from the formula:

$$
\mathrm { I G } = 0 . 4 \mathrm { I D A } + 0 . 6 \mathrm { G C I }
$$

# Threat 6. Corruption Perception (CP)

Corruption is the biggest obstacle to the economic and social development of society. It endangers every change. Corruption has become not only one of the main reasons of poverty but also a source which prevents its overcoming. Although corruption had existed for a long time it became more widely spread in the process of globalization at the end of the 20th at the beginning of 21st centuries.

Corruption in one country had negative impact on the development of other countries which means that countries with the high level of corruption are not limited to the Third World. The process of liberalization in the former socialist countries was accompanied by unprecedented position abuses in 90-ies. Thus, Financial Times proclaimed 1995 to be “the year of corruption”. The following years were marked with the spread of this phenomenon almost throughout all countries of the world and corruption itself became of global and international character.

Wellbeing did not become the prerequisite of successful elimination of corruption. The analysis of long-term tendencies revealed by the international organization «Transparency International» showed that during last 15 years the level of corruption has decreased in such countries as Estonia, Columbia, Bulgaria. Nevertheless, the growth of corruption occurs in such developed countries as Canada USA and Ireland. Such factors of risks as opacity of state authorities, excessive influence of separate oligarchic groups, violation in financing of political parties, etc. exist both in poor and rich countries and unfortunately, tendencies in increase of corruption scale are the same.

Usually, the structure of corruption is different in different countries of the world.

To estimate the influence of corruption on socio-economical and cultural development of different countries of the world we will use “the Index of corruption perception” established by the international organization “Transparency International” [9] (https://www.transparency.org/country).

# Threat 7. Limited Access to Drinking Water (WA)

According to the data of the World Health Organization (WHO) and the UNICEF [10] the world is under the threat of reduced the access to drinking (potable) water and to sanitary facilities. The fifth part of all mankind (1.4 billion people) does not have access to drinking water and 2.4 billion of people do not have minimal sanitary facilities. That is why 2003 was proclaimed as year of drinking water by the General Assembly of UNO. The period of 2005–2015 starting from the International Day of Water Recourses (22nd of March, 2005) was proclaimed as International decade of actions “Water for life”.

An especially severe situation is observed in urban areas of underdeveloped countries, where the fast growth of population aggravates promptly this problem. The above-mentioned factors especially affect children’s health. By the estimates of the World Health Organization, 1.6 million children under five annually died (on the average, 4500 children daily) of using unsafe water and lack of proper hygiene. As the world population grows, especially in underdeveloped countries, the struggle for control of the resources of fresh water will aggravate, which is the next global threat for mankind.

As the world’s population grows, especially in underdeveloped countries, the struggle for control over the remnants of drinking water resources increases. This phenomenon gives rise to the next, growing in time, threat to humanity.

The limited access to the drinking-water will be estimated by the inversed magnitude to the indicator of the access to drinking water [10].

# Threat 8. Global Warming [GW]

Global warming is the process of gradual increase in the average annual temperature of the Earth and World Ocean. According to conclusions of the International Expert Group in Climate Control (UNICEF Joint Monitoring Programme for Water Supply and Sanitation, n.d.) and National Academies of Sciences of the Group of Eight [11], from the end of 19th century the average temperature of the Earth has risen by $1 \ { } ^ { \circ } { \bf C }$ and “the major part of warming observed during the last 50 years had been caused by human activities” preliminary by gas emissions which cause green-house effect (carbon dioxide, $\mathrm { C O } _ { 2 }$ ) and methane $\mathrm { ( C H _ { 4 } ) }$ .

Estimates obtained with the climate models and cited by the International Expert Group in Climate Control show that the average temperature of the Earth can increase from one to several $^ { \circ } \mathrm { C }$ (in different regions of the world or in the Earth in average) in 1990–2080 years. The warming is expected to cause other climate changes such as an increase in the level of Word Ocean by $0 . 1 { - } 5 \mathrm { ~ m ~ }$ . (probably, in 30–40 years), the appearance of new viruses and also the change of atmospheric condensation and their distribution.

This may result in an increase in such natural disasters as floods, draughts, hurricanes etc.; a decrease in harvests of agricultural crops, the emergence of new epidemic diseases and the extinction of many biological species. As a result of the control over decreasing natural resources the struggle not only between countries but also between separate groups of population can exacerbate. This process will cause new global conflicts.

It is necessary to accept that influence of carbon dioxide emissions on the global warming is much higher than the corresponding influence of methane. That is why the danger of global warming could be estimated by the amount of carbon dioxide emissions $\mathbf { C O } _ { 2 }$ in metric tons [5, 11].

# Threat 9. The State Fragility [SF]

After the end of Cold War and Soviet Union collapse (1991) the world has entered the era of new dramatic geopolitical processes. The following 18 years were marked with the blistering growth of globalization. Technical revolution in the field of information-communication technologies has made the world policy more transparent and led to an increase in changes influence which occurred in one region and affected the other parts of the planet. Due to these new qualities of the globalized world it became clear that new geopolitical system is full of unstable, unsuccessful and weak countries. The weakening of retaining mechanisms peculiar to bipolar world and conflict exacerbation between fundamental values of different countries caused a new wave of oppositions, terrorism, violence, territorial claims and irregular development.

Uncontrolled spread of nuclear, chemical and biological weapon, rebuilding of nuclear energetics in such unstable, unbalanced world significantly increases the threat for sustainable development and global security of mankind.

Under such conditions the stabilization of world development becomes possible due to the international cooperation, investments and support to the weak countries and planet regions by the progress of new paradigms of “harmonious coexistence” or “tolerant, peaceful world”. In order to accomplish such global, stabilizing policy the recognized international organizations and scientific centers began to develop analytical instruments for the estimation of new developing tendencies of the world since the beginning of this century. The first attempt to control the tendencies of the global development was a series of reports “The world and the conflict” which were published in the University of Maryland State (USA) in 2001. Reports devoted to the global tendencies of world development were also published in many countries such as Spain, Canada, and Germany etc.

The final aim of the development of new analytical instruments was the attempt to estimate the ability of different countries to act in such important dimensions as conflict, state administration, economic and social development. Among all these instruments “The index of ability of the peaceful society development” that belongs to the series of reports “The world and conflict”, “Indicators of the world management” developed by the World Bank and “Index of unsuccessfulness of the countries” developed by The Fund of Peace can be mentioned.

For the quantitative estimation of the sustainable development threat in our research the Fragile States Index (FSI) produced by The Fund for Peace (FFP) is used (http://ffp.statesindex.org).

This index is based on the twelve indicators that cover a wide range of state failure risk elements such as extensive corruption and criminal behavior, inability to collect taxes or otherwise draw on citizen support, large-scale involuntary dislocation of the population, sharp economic decline, group-based inequality, institutionalized persecution or discrimination, severe demographic pressures, brain drain, and environmental decay. Data concerning these values are given in the paper [12].

# Threat 10. Natural Disasters (ND)

Natural disasters are the threat which is not so directly dependent on the human activity comparing to the other threats mentioned above. But, taking into account the reports of the international organizations on climate changes (World Economic Forum, 2010–2017) we cannot state that a human being is beside the point of the dynamics of the natural disasters.

Experts of UNO and World Data Center for “Geoinformatics and Sustainable Development” (http://wdc.org.ua/en) determined 6 major natural disasters (in the order of danger decrease): draughts, floods, hurricanes, extreme temperatures, earthquakes and tsunami (http://www.un.org/russian/ga/undp/).

Index is calculated as follows:

1. The summarized total of people suffered from the natural cataclysms in a year in a country is calculated:

$$
\begin{array} { l } { D i s a s t e r s A d f e c t e d _ { y e a r , s t a t e } = D r o u g h t A d f e c t e d _ { y e a r , s t a t e } + F l o o d A f f e c t e d _ { y e a r , s t a t e } } \\ { + S t o r m A f f e c t e d _ { y e a r , s t a t e } + E x t r e m e T e m p e r a t u r e A f f e c t e d _ { y e a r , s t a t e } } \\ { + E a r t h q u a k e A f f e c t e d _ { y e a r , s t a t e } + T s u n a m i A f f e c t e d _ { y e a r , s t a t e } , \forall y e a r , s } \end{array}
$$

2. Then the summarized total of people affected Disasters Affected is divided by the amount of population in the country and in the given year:

$$
D i s a s t e r s A f f e c t e d _ { y e a r , s t a t e } ^ { \prime } = \frac { D i s a s t e r s A f f e c t e d _ { y e a r , s t a t e } } { P o p u l a t i o n _ { y e a r , s t a t e } } , \ \forall y e a r , s a t e
$$

3. After that the obtained data are normalized by the logistic norm:

$$
\begin{array} { r }  \left\| D i s a s t e r s A f f e c t e d _ { y e a r , s t a t e } ^ { \prime } \right\| = \left[ 1 + e ^ { - \frac { D i s a s t e r s A f e c t d _ { y e c t , s t a t e } ^ { \prime } - M [ D i s a s t e r s A i f e c t e d _ { y e a r } ^ { \prime } ] } { s [ D i s a s t e r s A f f e c t e d _ { \} } ] _ { y e a r } } \right] ^ { - 1 } , } \end{array}
$$

where M[.], s[.]—are approximate average and standard deviation values respectively per year in all countries.

As consequences of the natural disasters usually make a long-term influence on the country, gradually disappearing only with time, the final value of vulnerability index on the natural disasters will be defined as Exponential Weighted Moving Average (EWMA), which has the potential smoothing factor $\alpha = 0 , 2 5$

$$
N D _ { y e a r , s t a t e } = 1 - \alpha \cdot \sum _ { 1 \leq t \leq T _ { \operatorname* { m a x } } } \left( 1 - \alpha \right) ^ { t - 1 } \cdot \left\| D i s a s t e r s A f f e c t e d _ { y e a r - t , s t a t e } ^ { \prime } \right\| .
$$

The value of the coefficient $\boldsymbol { \mathfrak { X } }$ was chosen by the experts on the basis of the estimation of the average time and level of the impact of disasters on the country. For convenience of calculations only the last significant $T m a x = 2 5$ years will be considered. At the same time the significance of time series will amount to $\varepsilon = e ^ { T _ { \mathrm { m a x } } \cdot \ln ( 1 - \alpha ) } = 0 . 0 0 0 7 5 2 5 \le 1 0 E - 3$ .

For the quantitative estimation of the degree of vulnerability of the world countries to the natural disasters the index of vulnerability to natural cataclysms was developed. The data of the International Disasters Database (http://www.emdat.be/) and the Centre for Research on the Epidemiology of Disasters (http://www.cred.be/) of the World Health Organization are used for its calculation. The values of vulnerability index for the countries to the natural disasters during 1995–2017 were calculated according to the given methodology.

# Threat 11. Conflict Intensity (CI)

The next global threat is the accruing quantity of conflicts in the world, both in the separate countries, and between the sovereign states and groups of such states. In our research we will consider a conflicts between interstate, intrastate, substate, and transstate ones. Whereas interstate conflicts only involve internationally recognized state actors, intrastate conflicts involve both state actors and non-state actors. Substate conflicts are carried out solely among non-state actors. Transstate conflicts involve both state and non-state actors and meet the criteria of political conflict for at least two sovereign states.

Considered conflicts we will characterise their intensity. We will distinguish five levels of intensity of conflicts: dispute, non-violent crisis, violent crisis, limited war, and war. To each of these levels we will appoint following quantity of points:

dispute—1 point;   
non-violent crisis—2 points;   
violent crisis—3 points; limited war—4 points;   
war—5 points.

The last three levels constitute the category of violent conflicts, in contrast to the non-violent conflicts (dispute and non-violent crisis). Whereas a dispute is a political conflict carried out without resorting to violence, in a non-violent crisis one of the actors threatens to use violence. This includes violence against objects without taking the risk to harm persons, the refusal of arms surrender, pointing weapon systems against each other and sanctions.

Quantitative data about intensity of conflicts we will take from a global resource: Heidelberg Institute for International Conflict Research (http://www.hiik.de/en/ konfliktbarometer/pdf/ConflictBarometer_2016.pdf) [4].

# Threat 12. Proliferation (NI)

“Proliferation” is a global threat of the debarment of the nuclear war, terrorism, the increasing of total number of weapons. It is a complex conception which is declared by many states and certainly is the part of modern policy. The level of the threat is opposite to value of Nonproliferation index defines degree of military nonproliferation and covers four categories of policy:

Nonproliferation Index defines degree of military proliferation and covers four categories of policy:

1. Demilitarization or disarmament;   
2. Scientific Research;   
3. State’s Development;   
4. Level of Nonproliferation for Neighbor States.

Each of these categories is formed using one or two levels of indicators. These indicators, as well as the methodology for calculating the Nonproliferation index, have been developed by World Data Center for Geoinformatics and Sustainable Development [4].

Nonproliferation index is presented in a hierarchy discrete model, which shows the factors of direct or indirect influence. This index shows the level of nonproliferation in terms of state’s possibility to adhere the nonproliferation concept in a wide sense. Lets consider each of these categories of policy

The first one is Disarmament. The importance of this category is underlined by Albert Einstein words: “I do not know with what weapons World War III will be fought, but World War IV will be fought with sticks and stones.” Therefore, it is necessary to control the weapons usage and decrease the number of these. Also the military expenditures could describe this category. This category is very specific, so the hypothesis about indicators should be improved by the existence of data in open sources or by indirect information. This category includes information about nuclear and uranium production, because it is necessary to keep in mind the possibility of nuclear weapons creation.

It is necessary to define the influence of indicators to the disarmament. Taking into consideration that it is a process, which have some changes in time, probably the differential quotient is the best way to describe the changes. So for all non-binary indicators we can use the formula:

$$
I = \frac { I n d i c a t o r _ { c u r r e n t p e r i o d } - I n d i c a t o r _ { p r e \nu e o u s p e r i o d } } { \Delta t i m e } .
$$

Therefore, this formula shows the dynamic of each process.

It is necessary to mention that the final algorithm of indicators chosen consists of two stages: finding all possible variants and choosing the group of necessary indicators by mathematical methods. In such a way we ignore the experts’ opinions by the open information limitation. This algorithm also shares to other categories.

The second category is Scientific Research. It has three main directions: Education, Science and Innovations:

• The education indicators describe the quality of education and the level of knowledge through the financing and the enrolment of students. Participation in Olympiads can show the level of knowledge in comparison with other countries.   
• The second direction is Science. It includes such indicators as Scientific and technical journal articles, Researchers in R&D (per million people), Research and development expenditure $\%$ of GDP). The last direction—Innovations—includes indicators Patent applications, residents, High-technology exports (current $\mathrm { U S } \$ 5$ ). As a result, 9 indicators represent the category Scientific Research.

The third category is State’s Development. This category includes the following indicators:

Life expectancy at birth (years);   
Gross national income (GNI) per capita (PPP $\$ 1$ );   
Inflation, GDP deflator (annual $\%$ );   
Energy use (kg of oil equivalent per capita);   
Sectorial structure of economy.

The last category is Level of Nonproliferation in Neighbor States. This category shows the risk to be engaged into some other states activities. The first indicator of this group is a conflict barometer for neighboring states. This indicator is calculated by Heidelberg Institute for International Conflict Research [4] and published in annual reports. It is necessary to find a quantitate measurement for relations between countries. It is clear that if historically country has some conflicts with neighbors, it restrains the nonproliferation. This indicator could be calculating in such way: first of all, it could be 0 or 1 for each state. And the total sum of the values will represent the historical factor of relations. The time horizon must be limited, for example, by the newest history (from XX century). It seems that this indicator partly crosses with the previous one. But the conflict barometer should describe only the current situation.

# 4.2.3 Modeling the Total Impact of the Aggregate of 12 Global Threats on Different Countries and Groups of Countries

Let’s determine the vulnerability of different countries and groups of countries to the impact of a set of 12 major threats (discussed in Sect. 4.2.2). Quantitative data on each of the 12 threats will be obtained from the global databases specified in the description of these threats in Sect. 4.2.2. To determine the groups of countries with close values of vulnerabilities to the impact of the 12 main threats, we use the hierarchical Ward’s algorithm of clustering [4]:

[http://www.cse.iitb.ac.in/dbms/Data/Courses/CS632/1999/clustering/dbms.html].

Let’s associate each country j with a vector TrJ:

$$
\overline { { \mathrm { T r } _ { \mathrm { J } } } } = ( E S , F B , G I N I , G D , I G , C P , W A , G W , S F , N D , C I , N I ) ,
$$

elements of which characterize the degree of manifestation of corresponding 12 threats (Sect. 4.2.2), presented in Table 4.3.

Most initial data on each threat (Table 4.3) are taken from the World Data Center “Geoinformatics and a Sustainable Development” (http://wdc.org.ua/en) [4]. Considering the fact that all the measured data for components of vector $\overline { { \mathrm { T r } _ { \mathrm { J } } } }$ are presented in different units of measurement, they have different physical meaning and vary in different ranges, they have been reduced to the normalized form, so that they vary in the range (0, 1). In this case, the value 0 corresponds to the minimum value of the threat, and the value 1 corresponds to the maximum of this threat.

Let’s do this normalization using the following method. If higher values of threat $X ^ { i }$ correspond to better state of this threat, the indicators values are logistically normalized according to the formula:

$$
C _ { n o r m } ( x _ { i , j } ) = \left( 1 + e ^ { \frac { a - x _ { i , j } } { b } } \right) ^ { - 1 }
$$

where parameters $a$ and $b$ are calculated as an average value and a standard deviation for the set of countries under analysis.

Otherwise, when the highest values of threat $X ^ { i }$ correspond to worse state of parameter, we use the value inverse to the one calculated by formula (4.23):

$$
C _ { n o r m } ( x _ { i , j } ) = 1 - \left( 1 + e ^ { \frac { a - x _ { i , j } } { b } } \right) ^ { - 1 }
$$

After this normalization we have vector $\left( \overrightarrow { T _ { r J } } ^ { \circ } \right)$

Table 4.3 Top 12 global threats for the sustainable development in the beginning of the XXI century   

<html><body><table><tr><td>No.</td><td>Threat ID</td><td>Threat description</td><td>Source of quantitative data for the threat</td></tr><tr><td>1</td><td>ES</td><td>The global decrease in energy security</td><td>Determined by the index of energy security calculated by the formula (4.7) [4]</td></tr><tr><td>2</td><td>FB</td><td>The misbalance between biological capacity of the Earth and human needs in biosphere in the context of changing the</td><td>Measured in global hectares per person (global footprint network [6])</td></tr><tr><td>3</td><td>GINI</td><td>demographic structure of the world The growing income inequality between people and countries of the Earth</td><td>Measured by Gini coefficient which is a number between O and 1,where O corresponds with perfect equality (where everyone has the same income) and 1 corresponds with perfect inequality (where one person has all the income-</td></tr><tr><td>4</td><td>GD</td><td>The spread of global diseases (in the sense of their global spread in the world</td><td>Measured by the total quantity of the people (millions per year) died from most dangerous diseases [8]</td></tr><tr><td>5</td><td>IG</td><td>The information gap determined by the sum of ICT development index and global cybersecurity index</td><td>Calculated by formula (4.8) [4]</td></tr><tr><td>6</td><td>CP</td><td>The corruption perception</td><td>Measured by the index of corruption perception varying within the range from O to 10;where O is a maximum corruption level and 1O—minimum corruption level [9]</td></tr><tr><td>7</td><td>WA</td><td>The limited access to drinking-water</td><td>Measured by the percentage of the population which has no access to drinking-water[10,11]</td></tr><tr><td>8</td><td>GW</td><td>The global warming</td><td>Measured by the quantity of carbon dioxide emissions in metric tones [4]</td></tr><tr><td>9</td><td>SF</td><td>The state fragility calculated as an average arithmetic value between political and economical instability of the country</td><td>Measured bystate fragility index,which changes in the range fromO to 23,where O—minimum fragility;23—maximum fragility [12]</td></tr><tr><td>10</td><td>ND</td><td>The index of vulnerability of the country to natural disasters</td><td>Calculated by the formula (4.9) [4]</td></tr><tr><td>11</td><td>CI</td><td>Conflicts intensity—quantity of conflicts in the world, both in the separate countries,and between the sovereign states and groups of such states</td><td>Determined by the Heidelberg Institute for International Conflict Research (from 0 to 5) [4]</td></tr></table></body></html>

(continued)

Table 4.3 (continued)   

<html><body><table><tr><td>No.</td><td>Threat ID</td><td>Threat description</td><td>Source of quantitative data for the threat</td></tr><tr><td>12</td><td>NI</td><td>Military proliferation—global threat of the debarment of the nuclear war, terrorism,the increasing of total number of weapons. The level of the threat is opposite to value of Nonproliferation index defines degree of military proliferation and covers four categories of policy: Demilitarization or disarmament; Scientific research; State's development; Level of nonproliferation for neighbor</td><td>Measured by World Data Center for Geoinformatics and Sustainable Development with a complex indicators [4]</td></tr></table></body></html>

$$
\left( \overrightarrow { T _ { r J } } ^ { \circ } \right) = \left( \mathrm { E S } ^ { \circ } , \mathrm { F B } ^ { \circ } , \mathrm { G I N I } ^ { \circ } , \mathrm { C D } ^ { \circ } , \mathrm { I G } ^ { \circ } , \mathrm { C P } ^ { \circ } , \mathrm { W A } ^ { \circ } , \mathrm { G W } ^ { \circ } , \mathrm { S F } ^ { \circ } , \mathrm { N D } ^ { \circ } , \mathrm { C I } ^ { \circ } , \mathrm { N I } ^ { \circ } \right) .
$$

Let us associate security index Isec each country with a value $\left. \overline { { \mathrm { T r } _ { \mathrm { J } } } } \right.$ , being the Minkowski norm of the vector $\overline { { \mathrm { T r } _ { \mathrm { J } } } }$ for the jth country, composed ofnormalized threats, for $p = 3$ . After such normalization the security index Isec for each country is defined as the Minkowski norm of vector $\overrightarrow { S } _ { j } = \left( s _ { i } ^ { j } \right) , s _ { i } ^ { j } = 1 - t _ { i } ^ { j } , i = \overline { { 1 , n } }$

$$
I _ { s e c } = \left\| \overrightarrow { S _ { J } } \right\| = \left( \sum _ { i = 1 } ^ { n } \left( s _ { i } ^ { j } \right) ^ { p } \right) ^ { \frac { 1 } { p } }
$$

with parameter $p = 3$ .

Let us call $I _ { s e c } = \left\| \overrightarrow { S _ { J } } \right\|$ the degree of remoteness from the action of the set of 12 threats stated in Sect. 4.2.2 for the $j$ th country.

Based on the calculated norms of the vector of threats $\lVert \overline { { \mathbf { T r } _ { \mathrm { J } } } } \rVert$ for each country $j$ , let us introduce an order relation between clusters of countries (Table 4.4):

$$
\mathrm { K } _ { \mathrm { k } } \prec \mathrm { K } _ { \mathrm { j } } \Leftrightarrow \big \| \overline { { \mathrm { T r } _ { \mathrm { k } } } } \big \| \leq \big \| \overline { { \mathrm { T r } _ { \mathrm { J } } } } \big \|
$$

From Table 4.4 it follows that Cluster 1 includes the group of countries most successful from the safety standpoint, for which the degree of remoteness from the set of 12 global threats is the greatest in the sense of (4.12). And vice versa, Cluster 5 includes the countries most vulnerable in this respect. For these countries the degree of remoteness from the set of 12 global threats is minimum.

Based on the data presented in Table 4.4, Fig. 4.6 illustrates the safety levels for different countries and regions of the world.

1   
Table 4.4 Countries degree remoteness from the set of threats based on clustering analysis, 2013–2016a   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and</td><td>(SF) State fragility (measured with the failed</td><td></td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4 5</td><td></td><td>6</td><td>1</td><td></td><td>9</td><td>10</td><td>11</td><td>12</td><td>nations on Earth 13</td><td>states index) 14</td><td>15</td><td>threats</td></tr><tr><td colspan="12">Cluster1(veryhighdegreofremoteness)</td></tr><tr><td>1 Canada</td><td>($42183.295)</td><td>7.422</td><td>0.000 0.836</td><td></td><td>82.000</td><td>0.687</td><td>0.547</td><td>47,5734.578</td><td>0.554</td><td>0.168</td><td>99.800</td><td>33.680</td><td>23.800</td><td>1.763</td></tr><tr><td>2</td><td>Finland ($43401.228)</td><td>6.606</td><td>0.000</td><td>0.821</td><td>89.000</td><td>0.441</td><td>0.546</td><td>46.299.542</td><td>0.556</td><td>0.149</td><td>100.000</td><td>27.120</td><td>18.800</td><td>1.696</td></tr><tr><td>3</td><td>Australia ($49,755.315)</td><td>6.864</td><td>0.000</td><td>0.853</td><td>79.000</td><td>0.544</td><td>0.566</td><td>377,906.352</td><td>0.550</td><td>0.149</td><td>100.000</td><td>34.940</td><td>22.500</td><td>1.687</td></tr><tr><td>4</td><td>Germany ($42,161.320)</td><td>-3.211</td><td>3.000</td><td>0.801</td><td>81.000</td><td>0.663</td><td>0.539</td><td>757,312.507</td><td>0.556</td><td>0.204</td><td>100.000</td><td>30.130</td><td>28.600</td><td>1.675</td></tr><tr><td>5</td><td>Norway ($70,868.122)</td><td>2.137</td><td>0.000</td><td>0.846</td><td>85.000</td><td>0.506</td><td>0.544</td><td>59.636.421</td><td>0.556</td><td>0.138</td><td>100.000</td><td>25.900</td><td>21.200</td><td>1.667</td></tr><tr><td>6</td><td>Netherlands ($45,637.887)</td><td>-4.674</td><td>0.000</td><td>0.837</td><td>83.000</td><td>0.455</td><td>0.543</td><td>169,972.784</td><td>0.556</td><td>0.170</td><td>100.000</td><td>27.990</td><td>28.200</td><td>1.655</td></tr><tr><td>7</td><td>Sweden ($51,844.761)</td><td>3.881</td><td>3.000</td><td>0.827</td><td>88.000</td><td>0.489</td><td>0.542</td><td>44,326.696</td><td>0.556</td><td>0.159</td><td>100.000</td><td>27.320</td><td>22.600</td><td>1.648</td></tr><tr><td>8</td><td>Denmark ($53,578.757)</td><td>-1.535</td><td>0.000</td><td>0.780</td><td>90.000</td><td>0.452</td><td>0.539</td><td>38.067.127</td><td>0.556</td><td>0.147</td><td>100.000</td><td>29.080</td><td>21.500</td><td>1.628</td></tr><tr><td>9</td><td>Switzerland ($79,887.518)</td><td>-4.044</td><td>0.000 2.000</td><td>0.829</td><td>86.000 72.000</td><td>0.439</td><td>0.546</td><td>40.348.001</td><td>0.556 0.553</td><td>0.148</td><td>100.000</td><td>31.640</td><td>21.800</td><td>1.618</td></tr><tr><td>10</td><td>Japan ($38.900.5690</td><td>-4.281 -5.762</td><td>0.000</td><td>0.845</td><td>77.000</td><td>0.575 0.460</td><td>0.537</td><td>1,243,384.358</td><td>0.556</td><td>0.188</td><td>100.000</td><td>32.110</td><td>35.100</td><td>1.612</td></tr><tr><td>11</td><td>Belgium ($41,271.482)</td><td></td><td></td><td>0.785</td><td></td><td></td><td>0.545</td><td>93.618.510</td><td></td><td>0.151</td><td>100.000</td><td>27.590</td><td>29.000</td><td>1.610</td></tr><tr><td>12</td><td>Austria ($44,757.635)</td><td>-3.115</td><td>0.000</td><td>0.766</td><td>75.000</td><td>0.445</td><td>0.545</td><td>62,408.673</td><td>0.556</td><td>0.154</td><td>100.000</td><td>30.480</td><td>27.500</td><td>1.597</td></tr></table></body></html>

1   
  
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations</td><td>(SF) State fragilty (measured with the failed states</td><td>(Isec) Degree of remoteness from the set of threats</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>15</td></tr><tr><td>13</td><td>Singapore ($52.962.492)</td><td>-6.746</td><td>1.000</td><td>0.874</td><td>84.000</td><td>0.416</td><td>0.521</td><td>50.556.929</td><td>0.556</td><td>0.182</td><td>100.000</td><td>N/A</td><td>32.900</td><td>1.591</td></tr><tr><td>14</td><td>New Zealand ($39,412.159)</td><td>4.934</td><td>0.000</td><td>0.817</td><td>90.000</td><td>0.433</td><td>0.545</td><td>33.960.087</td><td>0.517</td><td>0.133</td><td>100.000</td><td>N/A</td><td>21.300</td><td>1.587</td></tr><tr><td>15</td><td>Korea, Rep. ($27,538.806)</td><td>-5.186</td><td>0.000</td><td>0.853</td><td>53.000</td><td>0.501</td><td>0.547</td><td>592,499.192</td><td>0.556</td><td>0.203</td><td>97.600</td><td>N/A</td><td>36.100</td><td>1.581</td></tr><tr><td>16</td><td>Iceland ($59,764.705)</td><td>0.795</td><td>0.000</td><td>0.644</td><td>78.000</td><td>0.415</td><td>0.546</td><td>1969.179</td><td>0.556</td><td>0.139</td><td>100.000</td><td>26.940</td><td>22.800</td><td>1.579</td></tr><tr><td>17</td><td>France ($36,857.119)</td><td>-2.152</td><td>3.000</td><td>0.849</td><td>69.000</td><td>0.597</td><td>0.546</td><td>333,190.954</td><td>0.554</td><td>0.150</td><td>100.000</td><td>33.100</td><td>34.500</td><td>1.572</td></tr><tr><td>18</td><td>Ireland ($64,175.438)</td><td>-1.111</td><td>0.000</td><td>0.789</td><td>73.000</td><td>0.428</td><td>0.541</td><td>34,964.845</td><td>0.556</td><td>0.144</td><td>97.900</td><td>32.520</td><td>22.500</td><td>1.571</td></tr><tr><td>19</td><td>United States ($57,638.159)</td><td>-4.810</td><td>3.000</td><td>0.878</td><td>74.000</td><td>0.980</td><td>0.547</td><td>5,186,168.427</td><td>0.548</td><td>0.134</td><td>99.200</td><td>41.060</td><td>34.000</td><td>1.559</td></tr><tr><td>20</td><td>Italy ($30,661.222)</td><td>-3.453</td><td>0.000</td><td>0.742</td><td>47.000</td><td>0.565</td><td>0.560</td><td>344,767.673</td><td>0.556</td><td>0.158</td><td>100.000</td><td>35.160</td><td>43.100</td><td>1.550</td></tr><tr><td>21</td><td>Luxembourg ($100,738.684)</td><td>-11.507</td><td>0.000</td><td>0.764</td><td>81.000</td><td>0.415</td><td>0.549</td><td>10,161.257</td><td>0.556</td><td>0.132</td><td>100.000</td><td>34.790</td><td>24.100</td><td>1.544</td></tr><tr><td>22</td><td>United Kingdom ($40,367.038)</td><td>-3.779</td><td>3.000</td><td>0.848</td><td>81.000</td><td>0.602</td><td>0.536</td><td>457,472.918</td><td>0.555</td><td>0.118</td><td>100.000</td><td>32.570</td><td>32.400</td><td>1.538</td></tr><tr><td colspan="11">Cluster2(highdegree of remoteness)</td><td rowspan="2"></td><td rowspan="2">1.516</td></tr><tr><td>23</td><td>Uruguay ($15220.566)</td><td>6.912</td><td>0.000</td><td>0.742</td><td>71.000</td><td>0.415</td><td>0.561</td><td>7605.358</td><td>0.552</td><td>0.105 99.700</td><td>41.600</td><td>36.200</td></tr><tr><td>24</td><td>Estonia ($17736.803)</td><td>3.225</td><td>1.000</td><td>0.857</td><td>70.000</td><td>0.415</td><td>0.538</td><td>19.915.477</td><td>0.556</td><td>0.134</td><td>99.600</td><td>33.150</td><td>43.400</td><td>1.514</td></tr><tr><td>25</td><td>Spain ($26616.488)</td><td>-2.448</td><td>3.000</td><td>0.800</td><td>58.000</td><td>0.597</td><td>0.558</td><td>236,968.874</td><td>0.556</td><td>0.141</td><td>100.000</td><td>35.890</td><td>39.800</td><td>1.509</td></tr></table></body></html>

1   
  
  
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations</td><td>(SF) State fragility (measured with the failed states</td><td>(Isec) Degree of remoteness from the set of threats</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>15</td></tr><tr><td>26</td><td>Czech Republic ($18483.716)</td><td>-2.840</td><td>0.000</td><td>0.738</td><td>55.000</td><td>0.442</td><td>0.542</td><td>98.660.635</td><td>0.497</td><td>0.140</td><td>100.000</td><td>26.130</td><td>40.800</td><td>1.478</td></tr><tr><td>27</td><td>Portugal ($19838.027)</td><td>-2.344</td><td>0.000</td><td>0.671</td><td>62.000</td><td>0.452</td><td>0.532</td><td>46,262.872</td><td>0.556</td><td>0.130</td><td>100.000</td><td>36.040</td><td>29.200</td><td>1.469</td></tr><tr><td>28</td><td>Poland ($12414.099)</td><td>-2.286</td><td>0.000</td><td>0.725</td><td>62.000</td><td>0.457</td><td>0.540</td><td>302,333.149</td><td>0.556</td><td>0.129</td><td>98.300</td><td>32.080</td><td>40.700</td><td>1.467</td></tr><tr><td>29</td><td>Slovenia ($21650.213)</td><td>-2.444</td><td>1.000</td><td>0.578</td><td>61.000</td><td>0.415</td><td>0.548</td><td>14,440.646</td><td>0.534</td><td>0.141</td><td>99.500</td><td>25.590</td><td>33.900</td><td>1.463</td></tr><tr><td>30</td><td>Latvia ($14071.027)</td><td>2.975</td><td>1.000</td><td>0.771</td><td>57.000</td><td>0.415</td><td>0.553</td><td>7080.977</td><td>0.556</td><td>0.128</td><td>99.300</td><td>35.480</td><td>47.400</td><td>1.440</td></tr><tr><td>31</td><td>Slovakia ($16529.541)</td><td>-1.675</td><td>0.000</td><td>0.581</td><td>51.000</td><td>0.424</td><td>0.546</td><td>33.677.728</td><td>0.556</td><td>0.123</td><td>100.000</td><td>26.120</td><td>44.900</td><td>1.435</td></tr><tr><td>32</td><td>Mauritius ($9630.944)</td><td>-2.643</td><td>0.000</td><td>0.765</td><td>54.000</td><td>0.415</td><td>0.555</td><td>3725.672</td><td>0.556</td><td>0.120</td><td>99.900</td><td>35.840</td><td>43.200</td><td>1.434</td></tr><tr><td>33</td><td>Lithuania ($14900.779)</td><td>-0.193</td><td>0.000</td><td>0.674</td><td>59.000</td><td>0.418</td><td>0.527</td><td>12.640.149</td><td>0.556</td><td>0.123</td><td>96.600</td><td>35.150</td><td>42.400</td><td>1.412</td></tr><tr><td>34</td><td>Malta ($25145.393)</td><td>-3.841</td><td>0.000</td><td>0.627</td><td>55.000</td><td>0.415</td><td>0.537</td><td>2218.535</td><td>0.556</td><td>0.128</td><td>100.000</td><td>N/A</td><td>39.600</td><td>1.404</td></tr><tr><td colspan="11">Cluster3(mediumdegreeof remoteness)</td><td></td><td></td><td></td></tr><tr><td>35</td><td>Belarus ($4989.428)</td><td>-1.351</td><td>1.000</td><td>0.729</td><td>40.000</td><td>0.416</td><td>0.585</td><td>63,769.130</td><td>0.553</td><td>0.128</td><td>99.700</td><td>27.180</td><td>73.900</td><td>1.391</td></tr><tr><td>36</td><td>Guyana ($4529.139)</td><td>66.184</td><td>0.000</td><td>0.379</td><td>34.000</td><td>0.415</td><td>0.505</td><td>1936.176</td><td>0.529</td><td>0.116</td><td>98.300</td><td>N/A</td><td>70.900</td><td>1.379</td></tr><tr><td>37</td><td>Romania ($9522.771)</td><td>0.060</td><td>1.000</td><td>0.691</td><td>48.000</td><td>0.452</td><td>0.507</td><td>70,736.430</td><td>0.555</td><td>0.113</td><td>100.000</td><td>27.450</td><td>52.900</td><td>1.376</td></tr><tr><td>38</td><td>Barbados ($15891.627)</td><td>-3.199</td><td>0.000</td><td>0.534</td><td>61.000</td><td>0.415</td><td>0.550</td><td>1448.465</td><td>0.554</td><td>0.120</td><td>99.700</td><td>N/A</td><td>49.000</td><td>1.371</td></tr></table></body></html>

D   
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and</td><td>(SF) State fragility (measured with the failed</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>person)</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>1</td><td>12</td><td>nations on Earth 13</td><td>states index) 14</td><td>threats 15</td></tr><tr><td>39</td><td>Costa Rica ($11824.638)</td><td>-0.948</td><td>0.000</td><td>0.541</td><td>58.000</td><td>0.415</td><td>0.613</td><td>7616.359</td><td>0.531</td><td>0.108</td><td>97.800</td><td>48.530</td><td>45.100</td><td>1.370</td></tr><tr><td>40</td><td>Croatia ($12149.190)</td><td>-0.979</td><td>1.000</td><td>0.721</td><td>49.000</td><td>0.415</td><td>0.541</td><td>17,711.610</td><td>0.554</td><td>0.121</td><td>99.600</td><td>32.510</td><td>52.400</td><td>1.367</td></tr><tr><td>41</td><td>Israel ($37180.527)</td><td>-5.634</td><td>3.000</td><td>0.782</td><td>64.000</td><td>0.425</td><td>0.540</td><td>71.073.794</td><td>0.480</td><td>0.175</td><td>100.000</td><td>42.780</td><td>79.700</td><td>1.366</td></tr><tr><td>42</td><td>Brazil ($8649.948)</td><td>5.831</td><td>4.000</td><td>0.684</td><td>40.000</td><td>0.624</td><td>0.551</td><td>503,677.118</td><td>0.455</td><td>0.136</td><td>98.100</td><td>51.480</td><td>65.300</td><td>1.357</td></tr><tr><td>43</td><td>Hungary ($12820.088)</td><td>-0.899</td><td>2.000</td><td>0.679</td><td>48.000</td><td>0.424</td><td>0.541</td><td>41,440.767</td><td>0.552</td><td>0.132</td><td>100.000</td><td>30.550</td><td>52.700</td><td>1.357</td></tr><tr><td>44</td><td>Oman ($14982.358)</td><td>-3.993</td><td>1.000</td><td>0.806</td><td>45.000</td><td>0.436</td><td>0.565</td><td>61,183.895</td><td>0.555</td><td>0.124</td><td>93.400</td><td>N/A</td><td>51.600</td><td>1.355</td></tr><tr><td>45</td><td>Argentina ($12440.321)</td><td>3.052</td><td>1.000</td><td>0.641</td><td>36.000</td><td>0.446</td><td>0.585</td><td>189,818.588</td><td>0.549</td><td>0.121</td><td>99.100</td><td>42.670</td><td>48.400</td><td>1.352</td></tr><tr><td>46</td><td>Russian Federation</td><td>1.164</td><td>3.000</td><td>0.806</td><td>29.000</td><td>0.703</td><td>0.540</td><td>1,789.074.295</td><td>0.554</td><td>0.080</td><td>96.900</td><td>41.590</td><td>81.000</td><td>1.339</td></tr><tr><td>47</td><td>($8748.369) Saudi Arabia) ($20028.648)</td><td>-5.161</td><td>3.000</td><td>0.705</td><td>46.000</td><td>0.533</td><td>0.581</td><td>541,428.883</td><td>0.556</td><td>0.135</td><td>97.000</td><td>N/A</td><td>72.200</td><td>1.332</td></tr><tr><td>48</td><td>Montenegro ($7028.935)</td><td>-0.500</td><td>0.000</td><td>0.516</td><td>45.000</td><td>0.415</td><td>0.535</td><td>2247.871</td><td>0.550</td><td>0.106</td><td>99.700</td><td>31.930</td><td>55.200</td><td>1.328</td></tr><tr><td>49</td><td>Bulgaria ($7469.025)</td><td>-0.012</td><td>1.000</td><td>0.703</td><td>41.000</td><td>0.433</td><td>0.531</td><td>39.563.263</td><td>0.553</td><td>0.118</td><td>99.400</td><td>36.010</td><td>53.700</td><td>1.322</td></tr><tr><td>50</td><td>Ukraine ($2185.728)</td><td>-0.719</td><td>5.000</td><td>0.604</td><td>29.000</td><td>0.450</td><td>0.582</td><td>271,101.310</td><td>0.554</td><td>0.131</td><td>96.200</td><td>24.090</td><td>75.500</td><td>1.313</td></tr><tr><td>51</td><td>Mongolia ($3694.083)</td><td>7.774</td><td>0.000</td><td>0.420</td><td>38.000</td><td>0.417</td><td>0.558</td><td>41,591.114</td><td>0.525</td><td>0.104</td><td>64.400</td><td>32.040</td><td>56.600</td><td>1.311</td></tr></table></body></html>

1   
D   
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and</td><td>(SF) State fragility (measured with the failed</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>1</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>15</td></tr><tr><td>52</td><td>Malaysia ($9508.238)</td><td>-1.840</td><td>2.000</td><td>0.810</td><td>49.000</td><td>0.448</td><td>0.549</td><td>236,510.499</td><td>0.495</td><td>0.145</td><td>98.200</td><td>46.260</td><td>66.100</td><td>1.301</td></tr><tr><td>53</td><td>China ($8123.181)</td><td>-2.667</td><td>3.000</td><td>0.666</td><td>40.000</td><td>0.926</td><td>0.542</td><td>10,249,463.020</td><td>0.382</td><td>0.132</td><td>95.500</td><td>42.160</td><td>74.900</td><td>1.301</td></tr><tr><td>54</td><td>Greece ($17890.575)</td><td>-2.706</td><td>3.000</td><td>0.658</td><td>44.000</td><td>0.452</td><td>0.560</td><td>69,155.953</td><td>0.551</td><td>0.130</td><td>100.000</td><td>36.680</td><td>55.900</td><td>1.298</td></tr><tr><td>55</td><td>Bhutan ($2773.547)</td><td>0.527</td><td>0.000</td><td>0.349</td><td>65.000</td><td>0.415</td><td>0.518</td><td>883.747</td><td>0.547</td><td>0.117</td><td>100.000</td><td>38.810</td><td>77.600</td><td>1.297</td></tr><tr><td>56</td><td>Panama ($13680.236)</td><td>0.139</td><td>0.000</td><td>0.573</td><td>38.000</td><td>0.415</td><td>0.569</td><td>10,362.942</td><td>0.551</td><td>0.108</td><td>94.700</td><td>50.700</td><td>53.200</td><td>1.291</td></tr><tr><td>57</td><td>Chile ($13792.926)</td><td>-0.684</td><td>3.000</td><td>0.563</td><td>66.000</td><td>0.444</td><td>0.565</td><td>83,171.227</td><td>0.488</td><td>0.122</td><td>99.000</td><td>50.450</td><td>41.900</td><td>1.284</td></tr><tr><td>58</td><td>Cyprus ($23541.488)</td><td>-2.991</td><td>2.000</td><td>0.644</td><td>55.000</td><td>0.415</td><td>0.542</td><td>5947.874</td><td>0.556</td><td>0.111</td><td>100.000</td><td>34.310</td><td>64.000</td><td>1.281</td></tr><tr><td>59</td><td>Kazakhstan ($7714.694)</td><td>-2.926</td><td>3.000</td><td>0.561</td><td>29.000</td><td>0.448</td><td>0.566</td><td>262,901.898</td><td>0.554</td><td>0.131</td><td>92.900</td><td>26.330</td><td>66.500</td><td>1.273</td></tr><tr><td>60</td><td>Seychelles ($15075.719)</td><td>N/A</td><td>0.000</td><td>0.400</td><td>55.000</td><td>0.415</td><td>0.549</td><td>645.392</td><td>0.491</td><td>0.131</td><td>95.700</td><td>46.820</td><td>60.200</td><td>1.270</td></tr><tr><td>61</td><td>Belize ($4744.736)</td><td>N/A</td><td>0.000</td><td>0.373</td><td>N/A</td><td>0.415</td><td>0.552</td><td>517.047</td><td>0.530</td><td>0.117</td><td>99.500</td><td>N/A</td><td>66.000</td><td>1.266</td></tr><tr><td>62</td><td>Albania ($4124.982)</td><td>-1.065</td><td>0.000</td><td>0.469</td><td>39.000</td><td>0.415</td><td>0.536</td><td>4814.771</td><td>0.500</td><td>0.115</td><td>95.100</td><td>28.960</td><td>61.200</td><td>1.264</td></tr><tr><td>63</td><td>Georgia ($3865.786)</td><td>-0.456</td><td>3.000</td><td>0.763</td><td>57.000</td><td>0.415</td><td>0.547</td><td>7510.016</td><td>0.533</td><td>0.117</td><td>100.000</td><td>40.090</td><td>78.900</td><td>1.257</td></tr><tr><td>64</td><td>Botswana ($6924.150)</td><td>0.115</td><td>0.000</td><td>0.507</td><td>60.000</td><td>0.415</td><td>0.402</td><td>5423.493</td><td>0.552</td><td>0.107</td><td>96.200</td><td>60.460</td><td>63.500</td><td>1.250</td></tr></table></body></html>

1   
  
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USD</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations</td><td>(SF) State fragility (measured with the failed states</td><td>(Isec) Degree of remoteness from the set of threats</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>15</td></tr><tr><td>65</td><td>Turkey ($10862.600)</td><td>-1.718</td><td>5.000</td><td>0.665</td><td>41.000</td><td>0.478</td><td>0.555</td><td>323,451.402</td><td>0.555</td><td>0.124</td><td>100.000</td><td>40.180</td><td>77.300</td><td>1.231</td></tr><tr><td>66</td><td>Azerbaijan ($3878.709)</td><td>-1.481</td><td>3.000</td><td>0.677</td><td>30.000</td><td>0.430</td><td>0.583</td><td>35,643.240</td><td>0.552</td><td>0.120</td><td>87.000</td><td>31.790</td><td>76.300</td><td>1.230</td></tr><tr><td>67</td><td>Cabo Verde ($2997.753)</td><td>-1.600</td><td>0.000</td><td>0.323</td><td>59.000</td><td>0.415</td><td>0.542</td><td>443.707</td><td>0.543</td><td>0.110</td><td>91.700</td><td>47.190</td><td>71.500</td><td>1.225</td></tr><tr><td>68</td><td>Serbia ($5426.198)</td><td>-1.517</td><td>3.000</td><td>0.536</td><td>42.000</td><td>0.417</td><td>0.533</td><td>44,869.412</td><td>0.450</td><td>0.139</td><td>99.200</td><td>29.060</td><td>72.000</td><td>1.222</td></tr><tr><td>69</td><td>Mexico ($8208.556)</td><td>-1.345</td><td>5.000</td><td>0.669</td><td>30.000</td><td>0.498</td><td>0.571</td><td>488.602.081</td><td>0.536</td><td>0.134</td><td>96.100</td><td>48.210</td><td>70.400</td><td>1.221</td></tr><tr><td colspan="11">Cluster4(low degreeof remoteness)</td></tr><tr><td>70</td><td>Tunisia ($3688.646)</td><td>-1.394</td><td>3.000 0.633</td><td></td><td>41.000</td><td>0.416</td><td>0.556</td><td>27,667.515</td><td>0.556</td><td>0.113</td><td>97.700</td><td>35.810</td><td>74.600</td><td>1.211</td></tr><tr><td>71</td><td>India ($1709.592)</td><td>-0.628</td><td>4.000</td><td>0.584</td><td>40.000</td><td>0.664</td><td>0.386</td><td>2.034,752.294</td><td>0.523</td><td>0.092</td><td>94.100</td><td>35.150</td><td>79.600</td><td>1.199</td></tr><tr><td>72</td><td>Iran ($5219.109)</td><td>-2.221</td><td>3.000</td><td>0.584</td><td>29.000</td><td>0.523</td><td>0.574</td><td>616,976.417</td><td>0.549</td><td>0.112</td><td>96.200</td><td>37.350</td><td>86.900</td><td>1.197</td></tr><tr><td>73</td><td>Armenia ($3614.688)</td><td>-1.176</td><td>3.000</td><td>0.431</td><td>33.000</td><td>0.415</td><td>0.555</td><td>5496.833</td><td>0.540</td><td>0.116</td><td>100.000</td><td>31.480</td><td>69.600</td><td>1.191</td></tr><tr><td>74</td><td>Thailand ($5910.621)</td><td>-1.349</td><td>2.000</td><td>0.694</td><td>35.000</td><td>0.453</td><td>0.534</td><td>303,117.887</td><td>0.416</td><td>0.135</td><td>97.800</td><td>37.850</td><td>78.800</td><td>1.187</td></tr><tr><td>75</td><td>Syria (N/A)</td><td>-0.886</td><td>5.000</td><td>0.319</td><td>13.000</td><td>0.416</td><td>0.656</td><td>36.064.945</td><td>0.548</td><td>0.124</td><td>90.100</td><td>N/A</td><td>110.800</td><td>1.187</td></tr><tr><td>76</td><td>Macedonia ($5237.148)</td><td>-1.504</td><td>3.000</td><td>0.640</td><td>37.000</td><td>0.415</td><td>0.603</td><td>8294.754</td><td>0.456</td><td>0.117</td><td>99.400</td><td>44.050</td><td>67.000</td><td>1.185</td></tr><tr><td>77</td><td>Moldova ($1900.226)</td><td>-0.767</td><td>3.000</td><td>0.571</td><td>30.000</td><td>0.415</td><td>0.543</td><td>4976.119</td><td>0.546</td><td>0.104</td><td>88.400</td><td>26.830</td><td>73.200</td><td>1.184</td></tr></table></body></html>

D   
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and</td><td>(SF) State fragility (measured with the failed</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>15</td></tr><tr><td>78</td><td>Bolivia ($3104.956)</td><td>13.799</td><td>3.000</td><td>0.324</td><td>33.000</td><td>0.420</td><td>0.560</td><td>19,702.791</td><td>0.459</td><td>0.107</td><td>90.000</td><td>48.400</td><td>78.500</td><td>1.180</td></tr><tr><td>79</td><td>Kyrgyzstan ($1077.603)</td><td>-0.590</td><td>3.000</td><td>0.422</td><td>28.000</td><td>0.415</td><td>0.583</td><td>9842.228</td><td>0.530</td><td>0.101</td><td>90.000</td><td>26.820</td><td>81.100</td><td>1.173</td></tr><tr><td>80</td><td>Ghana ($1513.461)</td><td>-0.632</td><td>0.000</td><td>0.434</td><td>43.000</td><td>0.415</td><td>0.421</td><td>14,620.329</td><td>0.550</td><td>0.108</td><td>88.700</td><td>42.77</td><td>71.200</td><td>1.170</td></tr><tr><td>81</td><td>Egypt ($3477.852)</td><td>-1.458</td><td>4.000</td><td>0.696</td><td>34.000</td><td>0.442</td><td>0.508</td><td>213,012.363</td><td>0.556</td><td>0.114</td><td>99.400</td><td>N/A</td><td>90.200</td><td>1.165</td></tr><tr><td>82</td><td>Paraguay ($4077.742)</td><td>7.538</td><td>3.000</td><td>0.438</td><td>30.000</td><td>0.415</td><td>0.570</td><td>4972.452</td><td>0.440</td><td>0.109</td><td>98.000</td><td>51.670</td><td>72.600</td><td>1.164</td></tr><tr><td>83</td><td>Vietnam ($2170.648)</td><td>-0.676</td><td>3.000</td><td>0.400</td><td>33.000</td><td>0.439</td><td>0.562</td><td>152,624.207</td><td>0.499</td><td>0.136</td><td>97.600</td><td>37.590</td><td>70.700</td><td>1.158</td></tr><tr><td>84</td><td>Namibia ($4414.979)</td><td>4.532</td><td>0.000</td><td>0.283</td><td>52.000</td><td>0.415</td><td>0.430</td><td>2948.268</td><td>0.407</td><td>0.110</td><td>91.000</td><td>60.970</td><td>71.100</td><td>1.158</td></tr><tr><td>85</td><td>Jordan ($4087.938)</td><td>-1.868</td><td>2.000</td><td>0.453</td><td>48.000</td><td>0.415</td><td>0.493</td><td>24,807.255</td><td>0.556</td><td>0.117</td><td>96.900</td><td>N/A</td><td>78.000</td><td>1.146</td></tr><tr><td>86</td><td>Algeria ($3916.882)</td><td>-1.792</td><td>3.000</td><td>0.519</td><td>34.000</td><td>0.456</td><td>0.541</td><td>134,215.867</td><td>0.556</td><td>0.133</td><td>83.600</td><td>N/A</td><td>78.300</td><td>1.143</td></tr><tr><td>87</td><td>Venezuela, Bolivarian Republic of (N/A)</td><td>-0.550</td><td>3.000</td><td>0.521</td><td>17.000</td><td>0.470</td><td>0.578</td><td>185,531.865</td><td>0.553</td><td>0.118</td><td>93.100</td><td>46.940</td><td>81.600</td><td>1.143</td></tr><tr><td>88</td><td>Bosnia and Herzegovina ($4808.405)</td><td>-1.521</td><td>2.000</td><td>0.377</td><td>39.000</td><td>0.415</td><td>0.556</td><td>21,906.658</td><td>0.446</td><td>0.118</td><td>99.900</td><td>33.830</td><td>74.600</td><td>1.140</td></tr></table></body></html>

D   
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between nations people and</td><td>(SF) State fragility (measured with the failed</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>3 person)</td><td>4</td><td>5</td><td>6</td><td>1</td><td>8</td><td>9</td><td>10</td><td>1</td><td>12</td><td>on Earth 13</td><td>states index) 14</td><td>threats 15</td></tr><tr><td>89</td><td>Colombia ($5805.605)</td><td>1.821</td><td>4.000</td><td>0.635</td><td>37.000</td><td>0.448</td><td>0.577</td><td>89,625.147</td><td>0.516</td><td>0.108</td><td>91.400</td><td>53.500</td><td>80.200</td><td>1.130</td></tr><tr><td>90</td><td>El Salvador ($4223.585)</td><td>-1.300</td><td>4.000</td><td>0.354</td><td>36.000</td><td>0.415</td><td>0.619</td><td>6358.578</td><td>0.509</td><td>0.104</td><td>93.800</td><td>41.840</td><td>72.500</td><td>1.117</td></tr><tr><td>91</td><td>Fij ($5233.469)</td><td>-0.964</td><td>2.000</td><td>0.392</td><td>40.000</td><td>0.415</td><td>0.524</td><td>1708.822</td><td>0.525</td><td>0.127</td><td>95.700</td><td>42.780</td><td>76.200</td><td>1.111 </td></tr><tr><td>92</td><td>Ecuador ($6018.527)</td><td>0.259</td><td>3.000</td><td>0.548</td><td>31.000</td><td>0.426</td><td>0.571</td><td>43,527.290</td><td>0.546</td><td>0.114</td><td>86.900</td><td>45.380</td><td>75.600</td><td>1.109</td></tr><tr><td>93</td><td>Tajikistan ($795.844)</td><td>-0.389</td><td>3.000</td><td>0.435</td><td>25.000</td><td>0.415</td><td>0.582</td><td>3586.326</td><td>0.529</td><td>0.110</td><td>73.800</td><td>30.760</td><td>83.800</td><td>1.107</td></tr><tr><td>94</td><td>Morocco ($2892.776)</td><td>-0.895</td><td>3.000</td><td>0.594</td><td>37.000</td><td>0.415</td><td>0.550</td><td>58,558.323</td><td>0.553</td><td>0.107</td><td>85.400</td><td>40.720</td><td>74.200</td><td>1.105</td></tr><tr><td>95</td><td>Peru ($6049.233)</td><td>1.532</td><td>3.000</td><td>0.484</td><td>35.000</td><td>0.430</td><td>0.567</td><td>57,153.862</td><td>0.515</td><td>0.120</td><td>86.700</td><td>44.140</td><td>72.000</td><td>1.092</td></tr><tr><td>96</td><td>Jamaica ($4878.576)</td><td>-1.486</td><td>3.000</td><td>0.466</td><td>39.000</td><td>0.415</td><td>0.547</td><td>7726.369</td><td>0.494</td><td>0.117</td><td>93.800</td><td>45.460</td><td>65.000</td><td>1.090</td></tr><tr><td>97</td><td>Congo, Republic of the ($1528.245)</td><td>9.513</td><td>3.000</td><td>0.216</td><td>20.000</td><td>0.418</td><td>0.465</td><td>2482.559</td><td>0.553</td><td>0.105</td><td>76.500</td><td>48.940</td><td>92.200</td><td>1.086</td></tr><tr><td>98</td><td>Lebanon ($8257.294)</td><td>-3.094</td><td>3.000</td><td>0.433</td><td>28.000</td><td>0.415</td><td>0.569</td><td>22581.386</td><td>0.434</td><td>0.121</td><td>99.000</td><td>N/A</td><td>89.600</td><td>1.075</td></tr><tr><td>100</td><td>Indonesia ($3570.295)</td><td>-0.225</td><td>3.000</td><td>0.490</td><td>37.000</td><td>0.480</td><td>0.490</td><td>479,364.908</td><td>0.548</td><td>0.121</td><td>87.400</td><td>39.470</td><td>74.900</td><td>1.075</td></tr><tr><td>101</td><td>South Africa ($5274.546)</td><td>-2.262</td><td>3.000</td><td>0.591</td><td>45.000</td><td>0.462</td><td>0.279</td><td>471,238.836</td><td>0.548</td><td>0.116</td><td>93.200</td><td>63.380</td><td>69.900</td><td>1.072</td></tr><tr><td>102</td><td>Bangladesh ($1358.779)</td><td>-0.377</td><td>3.000</td><td>0.488</td><td>26.000</td><td>0.423</td><td>0.565</td><td>68.950.601</td><td>0.486</td><td>0.114</td><td>86.900</td><td>32.130</td><td>90.700</td><td>1.072</td></tr></table></body></html>

Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations</td><td>(SF) State fragility (measured with the failed states</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>threats 15</td></tr><tr><td>103</td><td>Sri Lanka ($3909.989)</td><td>-0.954</td><td>3.000</td><td>0.482</td><td>36.000</td><td>0.415</td><td>0.570</td><td>16.024.790</td><td>0.377</td><td>0.116</td><td>95.600</td><td>39.160</td><td>87.700</td><td>1.069</td></tr><tr><td>104</td><td>Laos ($2338.692)</td><td>0.165</td><td>1.000</td><td>0.411</td><td>30.000</td><td>0.415</td><td>0.541</td><td>2174.531</td><td>0.472</td><td>0.125</td><td>75.700</td><td>37.890</td><td>84.400</td><td>1.066</td></tr><tr><td>105</td><td>Dominican Republic ($6722.224)</td><td>-0.968</td><td>3.000</td><td>0.356</td><td>31.000</td><td>0.415</td><td>0.567</td><td>22.071.673</td><td>0.544</td><td>0.116</td><td>84.700</td><td>47.070</td><td>70.800</td><td>1.062</td></tr><tr><td>106</td><td>Honduras ($2361.160)</td><td>0.034</td><td>3.000</td><td>0.252</td><td>30.000</td><td>0.415</td><td>0.613</td><td>9064.824</td><td>0.458</td><td>0.109</td><td>91.200</td><td>50.640</td><td>79.800</td><td>1.061</td></tr><tr><td>107</td><td>Rwanda ($702.836)</td><td>-0.314</td><td>2.000</td><td>0.524</td><td>54.000</td><td>0.415</td><td>0.416</td><td>799.406</td><td>0.551</td><td>0.117</td><td>76.100</td><td>50.440</td><td>91.300</td><td>1.058</td></tr><tr><td>108</td><td>Benin ($789.440)</td><td>-0.434</td><td>0.000</td><td>0.216</td><td>36.000</td><td>0.415</td><td>0.466</td><td>5797.527</td><td>0.526</td><td>0.100</td><td>77.900</td><td>43.440</td><td>78.900</td><td>1.057</td></tr><tr><td>109</td><td>Zambia ($1269.574)</td><td>1.062</td><td>0.000</td><td>0.340</td><td>38.000</td><td>0.415</td><td>0.355</td><td>3824.681</td><td>0.528</td><td>0.111</td><td>65.400</td><td>55.620</td><td>86.300</td><td>1.056</td></tr><tr><td>110</td><td>Nepal ($729.122)</td><td>-0.395</td><td>3.000</td><td>0.425</td><td>29.000</td><td>0.415</td><td>0.537</td><td>6501.591</td><td>0.410</td><td>0.116</td><td>91.600</td><td>32.840</td><td>91.200</td><td>1.039</td></tr><tr><td colspan="11">Cluster5(very lowdegree of remoteness)</td><td rowspan="2"></td></tr><tr><td>111</td><td>Madagascar ($401.742)</td><td>1.573</td><td>0.000</td><td>0.246</td><td>26.000</td><td>0.415</td><td>0.489</td><td>3076.613</td><td>0.497</td><td>0.102</td><td>51.500 42.650</td><td>84.200</td><td>1.036</td></tr><tr><td>112</td><td>Malawi ($300.308)</td><td>-0.171</td><td>0.000</td><td>0.213</td><td>31.000</td><td>0.415</td><td>0.396</td><td>1272.449</td><td>0.451</td><td>0.111</td><td>90.200</td><td>46.120</td><td>87.600</td><td>1.033</td></tr><tr><td>113</td><td>Philippines ($2951.072)</td><td>-0.479</td><td>4.000</td><td>0.609</td><td>35.000</td><td>0.434</td><td>0.519</td><td>98,238.930</td><td>0.257</td><td>0.123</td><td>91.800</td><td>43.040</td><td>84.700</td><td>1.029</td></tr><tr><td>114</td><td>Guinea ($661.528)</td><td>0.622</td><td>3.000</td><td>0.218</td><td>27.000</td><td>0.415</td><td>0.471</td><td>2299.209</td><td>0.552</td><td>0.116</td><td>76.800</td><td>33.730</td><td>103.800</td><td>1.022</td></tr></table></body></html>

D   
Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USDb</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between nations people and</td><td>(SF) State fragility (measured with the failed states</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td>1</td><td>2</td><td>person)</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>on Earth 13</td><td>index) 14</td><td>threats 15</td></tr><tr><td>115</td><td>Lesotho ($1039.704)</td><td>-0.628</td><td>0.000</td><td>0.257</td><td>39.000</td><td>0.415</td><td>0.384</td><td>2295.542</td><td>0.495</td><td>0.104</td><td>81.800</td><td>54.180</td><td>80.900</td><td>1.021</td></tr><tr><td>116</td><td>Guatemala ($4146.744)</td><td>-0.751</td><td>3.000</td><td>0.340</td><td>28.000</td><td>0.415</td><td>0.593</td><td>13.597.236</td><td>0.409</td><td>0.100</td><td>92.800</td><td>48.660</td><td>83.200</td><td>1.021</td></tr><tr><td>117</td><td>Central African Republic</td><td>6.404</td><td>4.000</td><td>0.165</td><td>20.000</td><td>0.415</td><td>0.439</td><td>297.027</td><td>0.548</td><td>0.119</td><td>68.500</td><td>56.240</td><td>112.100</td><td>1.016</td></tr><tr><td>118</td><td>($382.213) Sierra leone ($505.205)</td><td>0.014</td><td>3.000</td><td>0.355</td><td>30.000</td><td>0.415</td><td>0.475</td><td>1191.775</td><td>0.552</td><td>0.114</td><td>62.600</td><td>33.990</td><td>91.000</td><td>1.015</td></tr><tr><td>119</td><td>Yemen ($990.335)</td><td>-0.511</td><td>5.000</td><td>0.196</td><td>14.000</td><td>0.415</td><td>0.545</td><td>25,346.304</td><td>0.555</td><td>0.117</td><td>54.900</td><td>N/A</td><td>111.500</td><td>1.010</td></tr><tr><td>120</td><td>Pakistan ($1443.625)</td><td>-0.380</td><td>4.000</td><td>0.441</td><td>32.000</td><td>0.441</td><td>0.479</td><td>153,368.608</td><td>0.485</td><td>0.103</td><td>91.400</td><td>30.690</td><td>101.700</td><td>1.009</td></tr><tr><td>121</td><td>Nicaragua ($2151.382)</td><td>0.855</td><td>3.000</td><td>0.286</td><td>26.000</td><td>0.415</td><td>0.570</td><td>4569.082</td><td>0.470</td><td>0.112</td><td>87.000</td><td>47.050</td><td>79.000</td><td>0.996</td></tr><tr><td>122</td><td>Cambodia ($1269.907)</td><td>-0.134</td><td>3.000</td><td>0.370</td><td>21.000</td><td>0.415</td><td>0.510</td><td>5573.840</td><td>0.431</td><td>0.121</td><td>75.500</td><td>30.760</td><td>87.400</td><td>0.994</td></tr><tr><td>123</td><td>Cote d Ivoire ($1534.974)</td><td>0.408</td><td>3.000</td><td>0.442</td><td>34.000</td><td>0.415</td><td>0.392</td><td>8987.817</td><td>0.556</td><td>0.097</td><td>81.900</td><td>43.180</td><td>97.900</td><td>0.970</td></tr><tr><td>124</td><td>Gambia ($473.190)</td><td>-0.169</td><td>3.000</td><td>0.265</td><td>26.000</td><td>0.415</td><td>0.524</td><td>491.378</td><td>0.491</td><td>0.099</td><td>90.200</td><td>47.330</td><td>86.800</td><td>0.963</td></tr><tr><td>125</td><td>Senegal ($952.768)</td><td>-0.132</td><td>3.000</td><td>0.365</td><td>45.000</td><td>0.415</td><td>0.524</td><td>8423.099</td><td>0.486</td><td>0.108</td><td>78.500</td><td>40.290</td><td>83.600</td><td>0.958</td></tr><tr><td>126</td><td>Mali ($779.945)</td><td>0.080</td><td>3.000</td><td>0.220</td><td>32.000</td><td>0.415</td><td>0.442</td><td>1026.760</td><td>0.497</td><td>0.111</td><td>77.000</td><td>33.040</td><td>95.200</td><td>0.939</td></tr><tr><td>127</td><td>Tanzania, United Republic of</td><td>-0.239</td><td>3.000</td><td>0.337</td><td>32.000</td><td>0.415</td><td>0.435</td><td>10751.644</td><td>0.539</td><td>0.098</td><td>55.600</td><td>37.780</td><td>81.800</td><td>0.936</td></tr></table></body></html>

Total inﬂuence of the set of global threats on different countries   

<html><body><table><tr><td>rank</td><td>per capita 2016, USD</td><td>(FB) Biodiversity balance (measured in global hectares per</td><td>(CI) Conflicts intensity (from 0 to 5)</td><td>(IG) Information gap</td><td>(CP) Corruption perception index</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and</td><td>(SF) State fragility (measured with the failed</td><td>(Isec) Degree of remoteness from the set of</td></tr><tr><td></td><td>2</td><td>person) 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>indicator) 11</td><td>12</td><td>nations on Earth 13</td><td>states index) 14</td><td>threats</td></tr><tr><td>1</td><td>($877.508)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>15</td></tr><tr><td>128</td><td>Burkina faso ($627.103)</td><td>-0.220</td><td>3.000</td><td>0.278</td><td>42.000</td><td>0.415</td><td>0.459</td><td>3058.278</td><td>0.411</td><td>0.111</td><td>82.300</td><td>35.300</td><td>89.400</td><td>0.934</td></tr><tr><td>129</td><td>Togo ($578.462)</td><td>-0.579</td><td>3.000</td><td>0.392</td><td>32.000</td><td>0.415</td><td>0.464</td><td>2229.536</td><td>0.548</td><td>0.108</td><td>63.100</td><td>46.020</td><td>85.800</td><td>0.930</td></tr><tr><td>130</td><td>Ethiopia ($706.757)</td><td>-0.441</td><td>3.000</td><td>0.302</td><td>34.000</td><td>0.415</td><td>0.354</td><td>10.634.300</td><td>0.504</td><td>0.112</td><td>57.300</td><td>33.170</td><td>97.200</td><td>0.926</td></tr><tr><td>131</td><td>Niger (N/A)</td><td>-0.318</td><td>3.000</td><td>0.237</td><td>35.000</td><td>0.415</td><td>0.464</td><td>1961.845</td><td>0.452</td><td>0.120</td><td>58.200</td><td>33.990</td><td>98.400</td><td>0.924</td></tr><tr><td>132</td><td>Uganda ($580.384)</td><td>-0.651</td><td>3.000</td><td>0.481</td><td>25.000</td><td>0.415</td><td>0.354</td><td>4895.445</td><td>0.536</td><td>0.106</td><td>79.000</td><td>41.010</td><td>97.700</td><td>0.921</td></tr><tr><td>133</td><td>Swaziland ($2770.199)</td><td>-1.156</td><td>3.000</td><td>0.235</td><td>43.000</td><td>0.415</td><td>0.393</td><td>1089.099</td><td>0.537</td><td>0.115</td><td>74.100</td><td>51.450</td><td>87.600</td><td>0.919</td></tr><tr><td>134</td><td>Cameroon ($1374.514)</td><td>0.482</td><td>3.000</td><td>0.413</td><td>26.000</td><td>0.415</td><td>0.411</td><td>6813.286</td><td>0.544</td><td>0.107</td><td>75.600</td><td>46.540</td><td>97.800</td><td>0.918</td></tr><tr><td>135</td><td>Nigeria ($2175.673)</td><td>-0.429</td><td>5.000</td><td>0.528</td><td>28.000</td><td>0.451</td><td>0.284</td><td>95.650.028</td><td>0.535</td><td>0.100</td><td>68.500</td><td>42.970</td><td>103.500</td><td>0.913</td></tr><tr><td>136</td><td>Angola ($3308.700)</td><td>1.441</td><td>3.000</td><td>0.224</td><td>18.000</td><td>0.437</td><td>0.389</td><td>32,463.951</td><td>0.519</td><td>0.118</td><td>49.000</td><td>42.720</td><td>90.500</td><td>0.903</td></tr><tr><td>137</td><td>Kenya ($1455.360)</td><td>-0.509</td><td>3.000</td><td>0.541</td><td>26.000</td><td>0.415</td><td>0.401</td><td>13.300.209</td><td>0.459</td><td>0.108</td><td>63.200</td><td>48.510</td><td>98.300</td><td>0.881</td></tr><tr><td>138</td><td>Mozambique ($382.069)</td><td>1.061</td><td>3.000</td><td>0.275</td><td>27.000</td><td>0.415</td><td>0.330</td><td>4019.032</td><td>0.517</td><td>0.102</td><td>51.100</td><td>45.580</td><td>87.800</td><td>0.856</td></tr></table></body></html>

![](images/dc9954888517d6516716a066735620a605c73db98da551f52da66477d33e9768.jpg)

<html><body><table><tr><td>Rank Isec</td><td>ISO</td><td>Country</td><td>Isec</td><td>FB</td><td>CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td>1</td><td>CAN</td><td>Canada</td><td>1.763</td><td>0.215</td><td>0.224</td><td>0.136</td><td>0.059</td><td>0.406</td><td>0.574</td><td>0.191</td><td>0.339</td><td>0.098</td><td>0.312</td><td>0.392</td><td>0.131</td></tr><tr><td>2</td><td>FIN</td><td>Finland</td><td>1.696</td><td>0.242</td><td>0.224</td><td>0.100</td><td>0.534</td><td>0.409</td><td>0.451</td><td>0.202</td><td>0.330</td><td>0.218</td><td>0.309</td><td>0.237</td><td>0.108</td></tr><tr><td>3</td><td>AUS</td><td>Australia</td><td>1.687</td><td>0.233</td><td>0.224</td><td>0.153</td><td>0.253</td><td>0.339</td><td>0.546</td><td>0.178</td><td>0.359</td><td>0.222</td><td>0.309</td><td>0.426</td><td>0.124</td></tr><tr><td>4</td><td>DEU</td><td>Germany</td><td>1.675</td><td>0.672</td><td>0.684</td><td>0.141</td><td>0.077</td><td>0.434</td><td>0.651</td><td>0.220</td><td>0.331</td><td>0.019</td><td>0.309</td><td>0.303</td><td>0.156</td></tr><tr><td>5</td><td>NOR</td><td>Norway</td><td>1.667</td><td>0.427</td><td>0.224</td><td>0.119</td><td>0.346</td><td>0.415</td><td>0.455</td><td>0.183</td><td>0.330</td><td>0.327</td><td>0.309</td><td>0.214</td><td>0.118</td></tr><tr><td>6</td><td>NLD</td><td>Netherlands</td><td>1.655</td><td>0.730</td><td>0.224</td><td>0.130</td><td>0.492</td><td>0.421</td><td>0.486</td><td>0.190</td><td>0.331</td><td>0.093</td><td>0.309</td><td>0.255</td><td>0.154</td></tr><tr><td>7</td><td>SWE</td><td>Sweden</td><td>1.648</td><td>0.349</td><td>0.684</td><td>0.105</td><td>0.393</td><td>0.425</td><td>0.450</td><td>0.198</td><td>0.330</td><td>0.148</td><td>0.309</td><td>0.241</td><td>0.125</td></tr><tr><td>8</td><td>DNK</td><td>Denmark</td><td>1.628</td><td>0.599</td><td>0.224</td><td>0.096</td><td>0.500</td><td>0.433</td><td>0.448</td><td>0.238</td><td>0.330</td><td>0.239</td><td>0.309</td><td>0.279</td><td>0.120</td></tr><tr><td>9</td><td>CHE</td><td>Switzerland</td><td>1.618</td><td>0.706</td><td>0.224</td><td>0.114</td><td>0.539</td><td>0.409</td><td>0.449</td><td>0.196</td><td>0.331</td><td>0.228</td><td>0.309</td><td>0.339</td><td>0.121</td></tr><tr><td>10</td><td>JPN</td><td>Japan</td><td>1.612</td><td>0.715</td><td>0.525</td><td>0.203</td><td>0.190</td><td>0.441</td><td>0.766</td><td>0.184</td><td>0.344</td><td>0.040</td><td>0.309</td><td>0.351</td><td>0.197</td></tr></table></body></html>

As presented in Table 4.5, the common trait of the ten leaders is high Isec, and low level of threats. E.g., the group leaders, Canada, Finland, and Australia, have the best indicators among all the group countries. However, certain coefficients such as biodiversity balance (FB), energy security (ES) and global warming (GW) are higher than average.

The G-7 countries are characterized by a high level of national security and therefore a low vulnerability to the impact of 12 global threats (Table 4.6).

The BRICS group of countries (Table 4.7) are characterized by average level of life security (except for South Africa) and high level of threats. Notably, China, the Russian Federation, and India are characterized by very high global warming (GW) coefficients. Brazil, the group leader, has high level of vulnerability to natural disasters (ND), and personal income inequality (GINI). The lowest security level is characteristic of South Africa, where the average level of threats is the highest in the group: notably vulnerability to global diseases (GD) and personal income inequality (GINI).

Six countries from the Results of Cluster Analysis (Table 4.4) are characterized by high level of conflicts intensity indicator, which is caused by armed conflicts in the territories of such countries (Table 4.8).

In total, experts of the Heidelberg Institute for International Conflict Research counted 226 violent conflicts in the world in 2016 [4], 18 of them were defined as wars and 20—as limited wars.

Wars:

– Sub-Saharan Africa: Nigeria (farmers—pastoralists); Nigeria, Cameroon, Chad, Niger (Boko Haram); Somalia, Kenya (al-Shabaab); South Sudan (inter-communal violence); South Sudan (SPLM/A-in-Opposition); Sudan (Darfur); Sudan (SPLM/A-North/Southern Kordofan, Blue Nile). Middle East and Maghreb: Afghanistan (Taliban et al.); Syria, Iraq et al. (IS); Libya (opposition); Syria (inter-opposition violence); Syria (opposition); Turkey (PKK, TAK); Yemen, Saudi Arabia (al-Houthi); Yemen (AQAP, Ansar al-Sharia). Asia and Oceania: Pakistan (Islamist militant groups).   
– The Americas: Mexico (drug cartels).   
– Europe: Ukraine (Donbas).

Limited wars:

Sub-Saharan Africa: Central African Republic (Anti-Balaka—ex-Séléka); DR Congo (ADF); DR Congo (Bantu—Batwa); DR Congo (Mayi-Mayi et al.); DR Congo, Rwanda (FDLR); Nigeria (northerners—southerners); Sudan (inter-communal violence).   
Middle East and Maghreb: Egypt (Islamist groups/Sinai Peninsula); Turkey (opposition).   
Asia and Oceania: India (Naxalites); Myanmar (KIA, KIO/Kachin State); Myanmar (Rohingya); Myanmar (TNLA/Shan State); Pakistan–India; Philippines (BIFM, BIFF—MILF, government).

<html><body><table><tr><td>Rank Isec</td><td>ISO</td><td>Country</td><td>Isec</td><td>FB</td><td>CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>G</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td>1</td><td>CAN</td><td>Canada</td><td>1.763</td><td>0.215</td><td>0.224</td><td>0.136</td><td>0.059</td><td>0.406</td><td>0.574</td><td>0.191</td><td>0.339</td><td>0.098</td><td>0.312</td><td>0.392</td><td>0.131</td></tr><tr><td>4</td><td>DEU</td><td>Germany</td><td>1.675</td><td>0.672</td><td>0.684</td><td>0.141</td><td>0.077</td><td>0.434</td><td>0.651</td><td>0.220</td><td>0.331</td><td>0.019</td><td>0.309</td><td>0.303</td><td>0.156</td></tr><tr><td>10</td><td>JPN</td><td>Japan</td><td>1.612</td><td>0.715</td><td>0.525</td><td>0.203</td><td>0.190</td><td>0.441</td><td>0.766</td><td>0.184</td><td>0.344</td><td>0.040</td><td>0.309</td><td>0.351</td><td>0.197</td></tr><tr><td>17</td><td>FRA</td><td>France</td><td>1.572</td><td>0.627</td><td>0.684</td><td>0.227</td><td>0.153</td><td>0.409</td><td>0.533</td><td>0.181</td><td>0.342</td><td>0.209</td><td>0.309</td><td>0.377</td><td>0.193</td></tr><tr><td>19</td><td>USA</td><td>United States</td><td>1.559</td><td>0.735</td><td>0.684</td><td>0.188</td><td>0.002</td><td>0.404</td><td>0.997</td><td>0.160</td><td>0.370</td><td>0.374</td><td>0.321</td><td>0.594</td><td>0.189</td></tr><tr><td>20</td><td>ITA</td><td>Italy</td><td>1.550</td><td>0.682</td><td>0.224</td><td>0.461</td><td>0.210</td><td>0.359</td><td>0.537</td><td>0.274</td><td>0.333</td><td>0.154</td><td>0.309</td><td>0.432</td><td>0.257</td></tr><tr><td>22</td><td>GBR</td><td>United Kingdom</td><td>1.538</td><td>0.696</td><td>0.684</td><td>0.141</td><td>0.146</td><td>0.446</td><td>0.569</td><td>0.182</td><td>0.335</td><td>0.560</td><td>0.309</td><td>0.363</td><td>0.179</td></tr></table></body></html>

<html><body><table><tr><td>Rank Isec</td><td>ISO</td><td>Country</td><td>Isec</td><td>FB</td><td>CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td>42</td><td>BRA</td><td>Brazil</td><td>1.357</td><td>0.270</td><td>0.809</td><td>0.545</td><td>0.117</td><td>0.390</td><td>0.582</td><td>0.336</td><td>0.792</td><td>0.346</td><td>0.339</td><td>0.823</td><td>0.474</td></tr><tr><td>46</td><td>RUS</td><td>Russian Federation</td><td>1.339</td><td>0.473</td><td>0.684</td><td>0.671</td><td>0.049</td><td>0.431</td><td>0.860</td><td>0.216</td><td>0.341</td><td>0.894</td><td>0.358</td><td>0.608</td><td>0.640</td></tr><tr><td>53</td><td>CHN</td><td>China</td><td>1.301</td><td>0.649</td><td>0.684</td><td>0.545</td><td>0.004</td><td>0.425</td><td>1.000</td><td>0.357</td><td>0.944</td><td>0.395</td><td>0.381</td><td>0.623</td><td>0.577</td></tr><tr><td>71</td><td>IND</td><td>India</td><td>1.199</td><td>0.557</td><td>0.809</td><td>0.545</td><td>0.076</td><td>0.880</td><td>0.891</td><td>0.456</td><td>0.491</td><td>0.824</td><td>0.404</td><td>0.431</td><td>0.626</td></tr><tr><td>101</td><td>ZAF</td><td>South Africa</td><td>1.072</td><td>0.632</td><td>0.684</td><td>0.485</td><td>0.472</td><td>0.973</td><td>0.573</td><td>0.448</td><td>0.370</td><td>0.592</td><td>0.420</td><td>0.946</td><td>0.524</td></tr></table></body></html>

G   
D   

<html><body><table><tr><td>Rank Isec</td><td>ISO</td><td>Country</td><td>Isec</td><td>FB</td><td>CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td><td></td></tr><tr><td>50</td><td>UKR</td><td>Ukraine</td><td>1.313</td><td>0.561</td><td>0.893</td><td>0.671</td><td>0.507</td><td>0.288</td><td>0.516</td><td></td><td>0.432</td><td>0.340</td><td>0.408</td><td>0.369</td><td>0.182</td><td>0.583</td></tr><tr><td>65</td><td>TUR</td><td>Turkey</td><td>1.231</td><td>0.607</td><td>0.893</td><td>0.533</td><td>0.424</td><td>0.375</td><td>0.531</td><td></td><td>0.358</td><td>0.336</td><td>0.486</td><td>0.309</td><td>0.570</td><td>0.602</td></tr><tr><td>69</td><td>MEX</td><td>Mexico</td><td>1.221</td><td>0.590</td><td>0.893</td><td>0.660</td><td>0.368</td><td>0.322</td><td>0.578</td><td></td><td>0.353</td><td>0.428</td><td>0.372</td><td>0.371</td><td>0.764</td><td>0.529</td></tr><tr><td>75</td><td>SYR</td><td>Syria</td><td>1.187</td><td>0.569</td><td>0.893</td><td>0.816</td><td>0.605</td><td>0.119</td><td>0.448</td><td>0.761</td><td></td><td>0.370</td><td>0.488</td><td>0.474</td><td>0.500</td><td>0.865</td></tr><tr><td>118</td><td>YEM</td><td>Yemen</td><td>1.010</td><td>0.552</td><td>0.893</td><td>0.808</td><td>0.607</td><td>0.414</td><td>0.445</td><td>0.856</td><td>0.337</td><td>0.574</td><td></td><td>0.916</td><td>0.500</td><td>0.869</td></tr><tr><td>134</td><td>NGA</td><td>Nigeria</td><td>0.913</td><td>0.548</td><td>0.893</td><td>0.682</td><td>0.504</td><td>0.971</td><td>0.465</td><td>0.527</td><td></td><td>0.432 0.760</td><td></td><td>0.806</td><td>0.644</td><td>0.824</td></tr></table></body></html>

The Americas: Brazil (drug-trafficking organizations); Colombia (ELN); Colombia (inter-cartel violence, neo-paramilitary groups, left-wing militants); El Salvador (Maras); Mexico (inter-cartel violence, paramilitary groups).

# 4.2.4 Conclusions

1. Based on the intellectual analysis of big historical data pertaining to global conflicts taking place from 705 B.C. till now, the regularity of their occurrence is determined. It is shown that a sequence of life cycles of system world conflicts is subordinate to the law of the Fibonacci series, and the intensity of these conflicts, depending on a level of technological evolution of the society, builds up under the hyperbolic law. By using the determined regularity we attempt to foresee the upcoming world conflict, called “the conflict of XXI century”, and analyze its nature and the principal characteristics-duration, main phases of its flow and intensity.

2. A set of 12 basic global threats that generate “the conflict of XXI” was described. By using the cluster analysis we identify the impact of these threats on different countries of the world and on large groups of countries (civilizations) united by the common culture features. Suppositions were made on possible scenarios of the world development during “the conflict of XXI” and after its termination.

# 4.3 Interrelation Between Periodic Processes in the Global Economy and Systemic World Conflicts

One of the major challenges to modern science because of the prompt development of the global economic crisis and aggravation of global conflicts is to draw up scientifically justified “metric” express forecasts of the social development for near and far future. The role of any scientific forecasts and predictions should not be exaggerated since they are conventional and limited, especially in the cases where the process being analyzed passes to the so-called “blow-up mode” [13]. However, the reliability of any forecast considerably increases if it “resonates” with other global or local tendencies, hypotheses, and patterns. In our study, such additional patterns are:

• modern hypotheses that the historical time accelerates as scientific and technological progress develops [13]; cyclical nature of economic development [14];   
• the tendency to reduce the duration of economic cycles as scientific and technological progress develops [15, 16].

The most significant are four types of economic cycles [14]:

the Kitchin inventory cycle of 3–5 years;   
the Juglar fixed-investment cycle of 7–11 years;   
the Kuznets infrastructural investment cycle of 15–25 years;   
the Kondratiev wave or long technological cycle of 45–60 years.

In our study, we consider Kondratiev’s economic cycles as the most fundamental, characterizing not only economic, but also social and political processes in society.

Proceeding from the above facts and considering the evolutionary development of the civilization as a holistic process, which is determined by a harmonious interaction of its components, we will compare the patterns of Kondratieff cycles of the development of global economy and identified in Sect. $4 . 2 ~ C _ { n }$ -waves of global systemic conflicts and will make an attempt to predict the course of periodic processes in the 21st century.

# 4.3.1 Periodicity of Global Systemic Conflicts and Economic Processes

In the previous section (Sect. 4.2), the Fibonacci pattern of the course of systemic world conflicts was revealed (Table 4.1), presented in terms of the duration of these conflicts $T ( C _ { n } ) ( 4 . 1 - 4 . 4 )$ and their intensity $I ^ { * } ( C _ { n } )$ (4.5–4.6).

As mentioned above, the property of a cyclical change of the economy is reflected by Kondratieff cycles (K-cycles) discovered by an outstanding Russian economist Nikolai Kondratiev 80 years ago [14, 15]. During the last two centuries, such cycles with 40–60-year periods (Table 4.9) fully complied with the actual development of economy. Figure 4.7 illustrates the course of K-cycles that cover the time interval from the first half of the last century to the present time.

Analyzing these cycles reveals that the major depression (in the USA) during the downwave of the third K-cycle is illustrative for the last century; it has begun at the end of the 1920s, developed into the default of dollar in 1933, and has essentially rearranged the world structure as a result of the Second World War. The next long crisis of the global economy, which is on the downwave of the fourth K-cycle, began at the end of the 1960s–the early 1970s, developed into the default of dollar in 1971, oil crisis in 1973–1975, passed to the deep economic crisis called stagflation, and resulted in the mid-1980s–the early 1990s in the disintegration of the Soviet Union, reconfiguration of the world, and its transition to a unipolar world model.

Table 4.9 Common sequence of K-cycles   

<html><body><table><tr><td>No.of K-cycle, n</td><td>Notation</td><td>Duration T(Cn) of the full cycle R, year</td><td>Upwave duration L, frthe K-cycle, year</td><td>Downwave duration L2 for the K-cycle, year</td></tr><tr><td>1</td><td>K</td><td>1779-1844/51</td><td>1779-1810/17</td><td>1810/17-1844/51</td></tr><tr><td>2</td><td>K</td><td>1844/51-1890/96</td><td>1844/51-1870/75</td><td>1870/75-1890/96</td></tr><tr><td>3</td><td>K</td><td>1890/96-1936/40</td><td>1890/96-1914/20</td><td>1914/20-1936/40</td></tr><tr><td>4</td><td>K</td><td>1936/40-1980/85</td><td>1936/40-1966/71</td><td>1966/71-1980/85</td></tr><tr><td>5</td><td>K</td><td>1980/85-2020/25</td><td>1980/85-2003/09</td><td>2003/09-？</td></tr></table></body></html>

![](images/38ebf87ddc337aca516faf4e2edf2aa8020e62fb22b806adfebbaf2ac1236921.jpg)  
Fig. 4.7 Long-term Kondratieff cycles in the 20th–early 21st century

Of great importance are Kondratieff’s conclusions (confirmed by the analysis of historical evidence) that the periods of upwaves of Kondratieff cycles are usually accompanied by more serious social disruptions (revolutions, wars, etc.) than the periods of downwaves [14, 15]. Hence, Kondratieff cycles characterize not only economic but also socio-political dynamics.

An analysis of these phenomena reveals an interrelation between two cyclic processes, development of the global economy and the occurrence and course of global systemic conflicts. Nowadays, the mankind is on the border of the transition from the downwave of the fifth Kondratieff cycle to the rising wave of the sixth K-cycle. This state corresponds to the transition from the global economic crisis to the next economic upswing.

# 4.3.2 Analysis of the Relationship Between Systemic World Conflicts and the Global Economy

Despite numerous attempts to establish a law governing the cyclic processes, none pattern of the varying duration of full K-cycles in time has been scientifically substantiated, which complicates drawing up efficient “metric” forecasts of social development for the near and far future. As a rule, all the studies addressed the internal nature of Kondratieff cycles. For example, the hypothesis is well known that the duration of K-cycles reduces with the scientific and technological progress [17, 18].

Kondratieff and his disciples emphasized that the patterns in the cyclic dynamics of the economy and society are basically probabilistic. For different parameters (as well as countries and regions), K-cycles are more or less pronounced. The results of the analysis of long-term waves depend on the metrics and system of indicators underlying the global historical pulsations and trends.

In this section we propose a new approach to revealing the patterns of time variation in the duration of full K-cycles that synchronizes the development of K-cycles with an external “metric” process, namely, with the course of global systemic conflicts [16].

Basic Assumption. Let us formulate an assumption to be used in what follows: there is one more downwave in the Kondratieff cycle that lasts about 28–30 years (1750/55–1779/85) and precedes the first upwave (1779/85–1810/17) identified by Kondratieff [14, 15].

Such an assumption can be substantiated by a number of objective statements; we will mention the most important ones.

First, the statement that such a wave (if exists) falls and lasts about 28 years agrees well with the fact that the next wave accrues with approximately the same duration, i.e., there is metric conformity in the sequence of down- and upwaves.

Second, as a distinguished Austrian-American scientist J. Schumpeter asserted, there is a set of Kondratieff cycles. Schumpeter’s conclusions were based on his “innovation theory of business” [19], which he used as late as in the 1930s to develop a “Kondratieff cyclic paradigm” and innovation concept of “long waves.”

Third, Kondratieff waves should not be considered just as a form of cyclic economic dynamics. They are a kind of historical cycles that cover the structure of the whole society. It is in this aspect that Braudel [20], a well-known historian of the 20th century, considered Kondratieff cycles and related them with the historical tendency of the society and dated appearing of such cycles several centuries back: If we associate two processes, the century tendency and Kondratieff cycles, we can hear “music” of long-term conjuncture that sounds in two voices.

In contrast to the conventional point of view, the cycles Kondratieff speaks about appeared on the European theater not in 1779 but several centuries earlier. Adding the movements to the rise or downfall of the century tendency, Kondratieff cycles strengthened or softened it [20].

Modified Sequence of Kondratieff Cycles. Let us consider the main assumption. We will generate a new sequence of Kondratieff cycles $\left\{ K _ { n } \right\} _ { n \geq 1 }$ (Table 4.6) based on the conventional chronology [15–18]. In what follows, we will call the sequence $\{ K _ { n } \} _ { n \geq 1 }$ a modified sequence of Kondratieff cycles (MSKC).

Note that while each term of the conventional sequence $\left\{ K _ { n } ^ { 0 } \right\} _ { n \geq 1 }$ of Kondratieff cycles (Table 4.6) is defined by a pair

$$
\mathbf { A B } = ( \mathbf { u p w a v e } , \ \mathrm { d o w n w a v e } ) ,
$$

the associated Kondratieff cycles in the modified sequence $\left\{ K _ { n } \right\} _ { n \geq 1 }$ are defined by the inverse pair

![](images/afbe4a6d1c201ca8c303ea452385dfe682e32e6a13c668e8f5c25fe3d29a2215.jpg)  
Fig. 4.8 Modified Sequence of K-cycles $\{ \mathbb { K } n \} n \geq 1$ joined with $C _ { 5 }$ -wave on the interval 1750– 1920 (a), and with $C _ { 6 }$ -wave on the interval 1920–2008 (b)

$$
\mathbf { B A } = ( \mathrm { d o w n w a v e } , \ \mathrm { u p w a v e } ) .
$$

Since the sequence of $C$ -waves of global systemic conflicts (see Table 4.1) and the modified sequence of $K$ -cycles of development of global economy (see Table 4.10) are considered as interdependent components of the holistic process of development of global society, let us overlap the curves of these processes on a unified time scale from 1750 to 2008 (Fig. 4.8). Note that waves of global conflicts $C _ { \mathrm { n } }$ are actually joined together (see by Table 4.1) during some time, and specific dates of joining waves $\mathrm { C } _ { 4 }$ and ${ \bf C } _ { 5 }$ (1750); ${ \bf C } _ { 5 }$ and $\mathbf { C } _ { 6 }$ (1920); $\mathrm { C } _ { 6 }$ and $\mathbf { C } _ { 7 }$ (2008) are determined as some averaged instants of time.

Analyzing the result of overlapping these two processes on the common time axis reveals a pattern; we will formulate it as the following principles.

1. Quantization Principle. The time intervals $T _ { k } ( \Delta ( C _ { n } ) ) , n \ge 5$ , on which the wave $C _ { n }$ undergoes the five phases of evolution: (origin) $>$ (growth) $>$ (culmination) $>$ (decrease) $>$ (decay), contain an integer number $T _ { k } ( C _ { n } )$ of full K-cycles of the MSKC $\left\{ K _ { n } \right\} _ { n \geq 1 }$ .

2. Monotonicity Principle. The average duration $T _ { k } ( C _ { n } )$ of one full K-cycle of the MSKC $\left\{ K _ { n } \right\} _ { n \geq 1 }$ on the time intervals $\left( C _ { n } \right)$ substantially decreases as $n$ grows.

Denote by

$$
G \big ( C _ { k } ; \{ K _ { n } \} _ { n \ge 1 } \big ) \triangleq \big \{ K _ { s ( k ) } ; K _ { s ( k ) + 1 } ; . . . ; K _ { s ( k ) + m ( k ) } \big \} , k \ge 5
$$

a group (quantum) of $\kappa$ -cycles separated by the $\mathbf { C }$ -wave $C _ { k }$ from the MSKC $\left\{ K _ { n } \right\} _ { n \geq 1 }$ . Then

$$
\begin{array} { c } { \displaystyle \mathrm { T } _ { k } \big ( { \cal C } _ { k } \big ) = m ( k ) + 1 \mathrm { a n d } } \\ { \displaystyle \mathrm { T } _ { k } \big ( \Delta \big ( { \cal C } _ { k } \big ) \big ) = \big ( m ( k ) + 1 \big ) ^ { - 1 } \sum _ { r = 0 } ^ { m ( k ) } T \big ( K _ { s ( k ) + r } \big ) , } \end{array}
$$

where $T \big ( K _ { j } \big )$ is the duration of one full Kondratieff cycle $K _ { j }$ .

In this case,

$$
\begin{array} { r l } & { G \big ( C _ { 5 } ; \{ K _ { n } \} _ { n \geq 1 } \big ) = \{ K _ { 1 } ; K _ { 2 } ; K _ { 3 } \} , G \big ( C _ { 6 } ; \{ K _ { n } \} _ { n \geq 1 } \big ) = \{ K _ { 4 } ; K _ { 5 } \} , } \\ & { T _ { k } ( \Delta ( C _ { 5 } ) ) = \frac { T ( K _ { 1 } ) + T ( K _ { 2 } ) + T ( K _ { 3 } ) } { 3 } = 5 6 . 6 \mathrm { y e a r s } ; n _ { k } ( \Delta ( C _ { 5 } ) ) = 3 , } \\ & { \quad \quad T _ { k } ( \Delta ( C _ { 6 } ) ) = \frac { T ( K _ { 4 } ) + T ( K _ { 5 } ) } { 2 } = 4 3 . 3 \mathrm { y e a r s } ; n _ { k } ( \Delta ( C _ { 6 } ) ) = 2 . } \end{array}
$$

The pattern revealed allows formulating the basic hypothesis on the probable next step of quantization, based on which the seventh wave of the next group $G { \big ( } C _ { 7 } ; \{ K _ { n } \} _ { n \geq 1 } { \big ) }$ of $\kappa$ -cycles can be distinguished in the MSKC $\{ K _ { n } \} _ { n \geq 1 }$ . To this end, let us formulate the following hypothesis.

Main Hypothesis. Since development of the global economy and the course of global systemic conflicts are interdependent components of the same process of evolutionary development of a globalized society, the coordination of these processes on the time intervals $T _ { k } ( \Delta ( C _ { 5 } ) )$ and $T _ { k } ( \Delta ( C _ { 6 } ) )$ as to obeying the quantization and monotonicity principles holds true also on the time interval $T _ { k } ( \Delta ( C _ { 7 } ) )$ .

Based on the main hypothesis, we can predict the course (in a metric sense) of $\kappa$ -cycles in the 21st century, namely:

a. the time interval $T _ { k } ( \Delta ( C _ { 7 } ) )$ contains no less than two full MSKC cycles $\{ K _ { n } \} _ { n \geq 1 }$ ;

b. average duration of one full K-cycle on the time interval $T _ { k } ( \Delta ( C _ { 7 } ) )$ is much shorter than $T _ { k } ( \Delta ( C _ { 6 } ) ) = 4 3 . 5$ years.

Hence, two cases that correspond to two scenarios of Kondratieff cycles in the 21st century are possible.

Scenario A. The time interval 2008–2092 contains two full Kondratieff cycles (Fig. 4.9a). In this case,

$$
\begin{array} { r } { G \big ( C _ { 7 } ; \{ K _ { n } \} _ { n \geq 1 } \big ) = \{ K _ { 6 } ; K _ { 7 } \} , n _ { k } ( \Delta ( C _ { 7 } ) ) = 2 , \ } \\ { T _ { k } ( \Delta ( C _ { 7 } ) ) = \frac { T ( K _ { 6 } ) + T ( K _ { 7 } ) } { 2 } = 4 2 . 5 \mathrm { y e a r s } < T _ { k } ( \Delta ( C _ { 6 } ) ) = 4 3 . 5 \mathrm { y e a r s } . } \end{array}
$$

Scenario B. The time interval 2008–2092 contains three full Kondratieff cycles (Fig. 4.9b). In this case,

$$
\begin{array} { r l } & { G \big ( C _ { 7 } ; \{ K _ { n } \} _ { n \geq 1 } \big ) = \{ K _ { 6 } ; K _ { 7 } ; K _ { 8 } \} , n _ { k } ( \Delta ( C _ { 5 } ) ) = 3 , } \\ & { T _ { k } ( \Delta ( C _ { 7 } ) ) = \frac { T ( K _ { 6 } ) + T ( K _ { 7 } ) + T ( K _ { 8 } ) } { 3 } = 2 8 . 3 ~ \mathrm { y e a r s } < T _ { k } ( \Delta ( C _ { 6 } ) = 4 3 . 5 ~ \mathrm { y e a r s } . } \end{array}
$$

The main confirmation of the validity of the scenario A is the commonly assumed average duration of one full K-cycle varying from 40 to 60 years [15, 16]. However, more powerful arguments can be given in favor of the scenario B.

First, obeying the monotonicity principle is rather conventional for the scenario A since $T _ { k } ( \Delta ( C _ { 7 } ) ) = 4 2 . 5$ years and $T _ { k } ( \Delta ( C _ { 6 } ) ) = 4 3 . 5$ years can be assumed approximately equal because of the errors of time “joints” of the processes on the time interval from 1750 to 2092.

![](images/6606c57690cb3e44e9d6e4dfa8d72a9a40ab147c4405336f2ca79a8ae9ea4968.jpg)  
Fig. 4.9 Predicted Kondratieff cycles in the 21st century: a scenario A: $n _ { k } ( \Delta ( C _ { 7 } ) ) = 2$ ; $T ( K _ { 6 } ) = T ( K _ { 7 } )$ , $\mathbf { b }$ scenario B: $n _ { k } ( \Delta ( C _ { 7 } ) ) = 3$ ; $T ( K _ { 6 } ) = T ( K _ { 7 } ) = T ( K _ { 8 } )$

Table 4.10 Modified sequence of K-cycles   

<html><body><table><tr><td>No.of K-cycle, n</td><td>Notation, Kn</td><td>Duration T(Cn) of the full cycle K, year</td><td>Upwave duration L2 for the Kn-cycle,year</td><td>Downwave duration L*,1 for the Kn-cycle, year</td></tr><tr><td>1</td><td>K</td><td>1750/55-1810/17</td><td>1750/55-1779/85</td><td>1779/85- 1810/17</td></tr><tr><td>2</td><td>K</td><td>1810/17-1870/75</td><td>1810/17-1844/51</td><td>1844/51- 1870/75</td></tr><tr><td>3</td><td>K</td><td>1870/75-1914/20</td><td>1870/75-1890/96</td><td>1890/96- 1914/20</td></tr><tr><td>4</td><td>K4</td><td>1914/20-1966/71</td><td>1914/20-1936/40</td><td>1936/40- 1966/71</td></tr><tr><td>5</td><td>K</td><td>1966/71-2003/09</td><td>1966/71-1980/85</td><td>1980/85- 2003/09</td></tr></table></body></html>

Second, results of some modern studies of global evolutionary processes (such as the concept about the acceleration of historical time [21] and the hypothesis that the duration of Kondratieff cycles tends to reduce with the scientific and technological progress [17, 18]) may indirectly confirm the priority of the scenario B.

If the scenario B takes place, then most probably the durations $\mathrm { T } ( \mathrm { K } _ { 6 } ) , \mathrm { T } ( \mathrm { K } _ { 7 } )$ , and $\mathrm { T } ( \mathrm { K } _ { 8 } )$ of the predicted K-cycles $K _ { 6 } , K _ { 7 }$ , and $K _ { 8 }$ will be related as follows:

$$
T ( K _ { 8 } ) < T ( K _ { 7 } ) < T ( K _ { 6 } ) , { \mathrm { w h e r e } } T ( K _ { 6 } ) + T ( K _ { 7 } ) + T ( K _ { 8 } ) = T ( C _ { 7 } ) = 8 5 \times
$$

Certainly, to substantiate the choice of the most reliable relationship among $T ( K _ { 6 } ) , \ T ( K _ { 7 } )$ , and $T ( K _ { 8 } )$ , additional integrated studies are necessary that would take into account the dynamics of various components of the global evolution of the civilization such as the following key ones: prompt depletion of power resources of the Earth, varied demographic structure of the world, growing social inequality among people and countries, global climate changes, natural disasters, etc. It is important to establish a relationship between the time quantum $\mathbf { k } _ { \mathrm { ~ c ~ } }$ of the life of $C .$ - waves and average duration of one full cycle of the modified sequence of Kondratieff cycles. Since $k _ { c } \approx 8 5$ years [2] and

$$
T _ { k } ( \varDelta ( C _ { 5 } ) \cup \varDelta ( C _ { 6 } ) \cup \varDelta ( C _ { 7 } ) ) = ( 2 0 9 2 - 1 7 5 0 ) / 8 = 4 2 . 7 5 \mathrm { y e a }
$$

$k _ { c } \approx 2 T _ { k } \big ( \boldsymbol { \varDelta } ( C _ { 5 } ) \cup \boldsymbol { \varDelta } ( C _ { 6 } ) \cup \boldsymbol { \varDelta } ( C _ { 7 } ) \big )$ and the sequence $\{ T ( C _ { n } ) \} , n = 1 , 2 , . . . , 7$ (Table 4.2) can be represented as the following series:

$$
\begin{array} { r } { T ( C _ { 1 } ) \approx 1 3 \cdot \gamma _ { k } ; T ( C _ { 2 } ) \approx 8 \cdot \gamma _ { k } ; T ( C _ { 3 } ) \approx 5 \cdot \gamma _ { k } ; T ( C _ { 4 } ) \approx 3 \cdot \gamma _ { k } ; } \\ { T ( C _ { 5 } ) \approx 2 \cdot \gamma _ { k } ; T ( C _ { 6 } ) \approx 1 \cdot \gamma _ { k } ; T ( C _ { 7 } ) \approx 1 \cdot \gamma _ { k } , \mathrm { w h e r e } \ \gamma _ { k } = 2 T _ { k } ( \Delta ( C _ { 5 } ) \cup \Delta ( C _ { 7 } ) ) . } \end{array}
$$

This yields Fibonacci dependence of the duration of life of all waves $C _ { n }$ on the average duration of one full cycle of the modified sequence of Kondratieff cycles during the time interval from 1750 to 2092.

Finally, the above pattern confirms the hypothesis that the duration of Kondratieff cycles tends to reduce with scientific and technological progress [17, 18], with the following refinement: the hypothesis is true not for the sequence $\{ T ( K _ { n } ) \} _ { n \geq 1 }$ generated by the $\left\{ K _ { n } \right\} _ { n \geq 1 }$ but for the sequence $\left\{ T _ { k } ( \Delta ( C _ { m } ) ) \right\} _ { m \geq 5 }$ generated by the sequence of groups (quantums) of K-cycles G Cm; Kngn 1	m 5.

# 4.3.3 Conclusions

1. Based on the evolutionary development of the civilization as a holistic process determined by a harmonious interaction of its components, we have compared the patterns of a sequence of Kondratieff cycles of development of global economy and of C-waves of global systemic conflicts and have made an attempt to predict the course of these interconnected processes in the 21st century with the use of a metric approach.   
2. The results of the analysis allow concluding that the 21st century will most probably manifest three K-cycles with the average duration of one full cycle of about 30 years, which is much shorter than the average duration of one of the previous five Kondratieff cycles $( \approx 5 0$ years). This may be because of the technological progress and the new technological pattern being formed, which cannot be investigated yet at the present stage of the development of the mankind.   
3. The interrelation has been revealed and Fibonacci dependence has been established for the time quantum $k _ { c }$ of the life cycles of C-waves of global systemic conflicts and average duration of one full cycle of the modified sequence of Kondratieff cycles on the time interval from 1750 to 2092.   
4. The results of the study confirm the refined hypothesis that the duration of Kondratieff cycles tend to reduce with the scientific and technological progress [17, 18]. The revealed synchronization of the development of the global economy and the course of global systemic conflicts can be interpreted as indirect confirmation of the adequacy of the models of Kondratieff cycles [15, 16] and C-waves [2].

# 4.4 Metric Aspects of Periodic Processes in Economy and Society

The interrelation and principles of the development of various processes in the nature and society are discussed in many publications [19, 22]. The paper [2] reveals the pattern of global system conflicts based on the dynamic model of so-called $C$ -waves with the underlying metrics of golden section. The paper [20] compares the principles of the sequence of great Kondratieff cycles of the development of the global economy and $C \mathrm { . }$ -waves of global system conflicts. An attempt is made to predict these periodic processes for the XXIst century.

The principles revealed for global system conflicts and great Kondratieff cycles become much more reliable if they correspond to some additional external conditions (concepts, principles, hypotheses) and the conclusions made on their basis are coordinated or “resonate” with the conclusions of other independent studies.

We will consider the evolution of the civilization as a holistic process that results from the harmonic interaction of its components and substantiate the conformity of the principles revealed in [2] to some additional conditions, namely:

law of structural harmony [21];   
modern concept on the acceleration of historical time [23, 24];   
concept of great Kondratieff cycles [15, 16];   
global forecasts for the XXIst century [15, 17, 18, 22, 25–28].

By studying the empirical sequence of the periodicity of global conflicts, we will perform the structural analysis of $C _ { n }$ -waves $\left( n = \overline { { 1 , 6 } } \right)$ identified in [2] and propose metric approaches to the analysis and prediction of some global civilization processes.

# 4.4.1 Initial Definitions

Let us introduce some concepts and definitions:

• In what follows, we will call the Fibonacci-pattern of global system conflicts substantiated in [2] the $F _ { \mathbf { \Phi } }$ -pattern; $C _ { W }$ is the totality of all the global conflicts (according to [22]) from 705 BC to Nowday;   
• ${ { N } _ { W C } } \left( t \right)$ is the number of all the global conflicts $c \in C _ { W }$ in the year $t$ ：   
• $\Delta ( m ; n ) \triangleq \{ k : ( m \leq k \leq n ) \land ( k \in Z ) \} , m , n \in Z$ , where $Z$ is the set of integers; $\{ N _ { W C } ( t ) \} _ { t \in \Delta ( - 7 5 0 ; \mathrm { N o w d a y } ) }$ is the empirical sequence of the periodicity of global conflicts $C _ { W }$ (WC-sequence for short); $\begin{array} { r } { I _ { W C } ( \Delta ( m ; n ) ) = m e s ^ { - 1 } \Delta ( m ; n ) \sum _ { t \in \Delta ( m ; n ) } N _ { W C } ( t ) } \end{array}$ is the intensity of the WCsequence on the set (time interval) $\Delta ( m ; n )$ ;

• a partition $\omega ( \Delta ( m ; n ) )$ of the set $\Delta ( m ; n )$ is the sequence of sets $\{ \Delta ( m _ { s } ; n _ { s } ) \} _ { s = \overline { { { 1 , M } } } }$ that satisfies the following conditions:

$$
\begin{array} { r l } & { m _ { 1 } = m , n _ { M } = n , } \\ & { \Delta ( m _ { r } ; n _ { r } ) \cap \Delta ( m _ { l } ; n _ { l } ) \emptyset \forall _ { 1 } \neq 1 , r , l = \overline { { 1 , M } } , } \\ & { \bigcup _ { s = 1 } ^ { M } \Delta ( m _ { s } ; n _ { s } ) = \Delta ( m ; n ) ; } \end{array}
$$

we will say that the WC-sequence generates a local wave $L W _ { \textit { C } } \left( \Delta ( m ; n ) \right)$ of global conflicts on the set (time interval) $\Delta ( m ; n )$ if there exists a partition $\omega ( \Delta ( m ; n ) ) \Big \{ \Delta ( m _ { s } ; n _ { s } ) _ { s = \overline { { { 1 , 5 } } } } \Big \}$ such as

$$
\left\{ \begin{array} { c } { I _ { W C } ( \Delta ( m _ { 1 } ; n _ { 1 } ) ) < I _ { W C } ( \Delta ( m _ { 2 } ; n _ { 2 } ) ) < I _ { W C } ( \Delta ( m _ { 3 } ; n _ { 3 } ) ) , } \\ { I _ { W C } ( \Delta ( m _ { 5 } ; n _ { 5 } ) ) \leq I _ { W C } ( \Delta ( m _ { 4 } ; n _ { 4 } ) ) < I _ { W C } ( \Delta ( m _ { 3 } ; n _ { 3 } ) ) ; } \end{array} \right.
$$

• the quantity mes $\Delta ( m ; n )$ determines the duration of the life cycle of the wave $L W _ { C } \left( \Delta ( m ; n ) \right)$ , and the time intervals $\Delta ( m _ { s } ; n _ { s } ) , s = \overline { { 1 , 5 } }$ are the durations of the corresponding phases (stages) $f _ { S } ( L W _ { C } ~ ( \Delta ( m ; n ) ) ;$ : origin $\Delta ( m _ { 1 } ; n _ { 1 } )$ ; growth $\Delta ( m _ { 2 } ; n _ { 2 } )$ ; culmination $\Delta ( m _ { 3 } ; n _ { 3 } )$ ; decrease $\Delta ( m _ { 4 } ; n _ { 4 } )$ ; and decay $\Delta ( m _ { 5 } ; n _ { 5 } )$ ; • $I ( L W _ { c } ( \Delta ( m _ { n } ; n _ { n } ) ) ) \equiv I _ { W C } ( \Delta ( m ; n ) )$ is the intensity of the local wave $L W _ { C }$ $( \Delta ( m ; n ) )$ of global conflicts; • $I ( f _ { S } ( L W _ { C } ( \Delta ( m ; n ) ) ) ) \equiv I _ { W C } ( \Delta ( m _ { s } ; n _ { s } ) )$ is the intensity of the phase $f _ { S } ( L W _ { C }$ $( \Delta ( m ; n ) ) $ of the local wave $L W _ { C }$ $( \Delta ( m ; n )$ of global conflicts.

# 4.4.2 Structural Analysis of Global System Conflicts

Table 4.11 shows the partition of the time interval $\Delta ( - 7 5 0 ; \mathrm { N o w d a y } )$

$\omega ( \Delta ( - 7 5 0 ; \mathrm { N o w d a y } ) ) = \{ \Delta ( \alpha _ { n } ; \beta _ { n } ) \} _ { n = 1 , 6 ^ { \prime } }$ defined in [2].

Table 4.11 Time intervals $\Delta ( \alpha _ { n } ; \beta _ { n } ) , n = \overline { { { 1 , 6 } } }$ ; and their main characteristics   

<html><body><table><tr><td>Cn-waves</td><td>Time range △(an; βn), years</td><td>Length of time intervals T(△(an; βn)), years, k ≈ 85years</td><td>Ratio of time intervals T△(an;βn))） T(△(n + 1:βn+1))</td><td>Correspondence to Fibonacci numbers {Fs}</td></tr><tr><td>C1</td><td>△(-705;401)</td><td>1007≈13.k</td><td>1.645</td><td>F7=13</td></tr><tr><td>C2</td><td>△(402;1074)</td><td>673=8.k</td><td>1.591</td><td>F6=8</td></tr><tr><td>C3</td><td>△(1075;1497)</td><td>423~5.k</td><td>1.679</td><td>F5=5</td></tr><tr><td>C4</td><td>△(1498;1749)</td><td>252≈3.k</td><td>1.482</td><td>F4=3</td></tr><tr><td>C5</td><td>△(1750;1919)</td><td>170≈2·k</td><td>1.932</td><td>F=2</td></tr><tr><td>C6</td><td>△(1920;2007)</td><td>88~1.k</td><td>1.035</td><td>F2=1</td></tr><tr><td>C7 (predicted wave)</td><td>△(2008;2092)</td><td>85≈1.k</td><td></td><td>F1=1</td></tr></table></body></html>

Table 4.12 Local waves of global conflicts and their metric characteristics   

<html><body><table><tr><td rowspan="2">LWc(△(an; βn))</td><td rowspan="2">Phase</td><td rowspan="2">Notation</td><td colspan="2">Phases (years)</td><td rowspan="2">Duration</td><td rowspan="2">Intensity</td></tr><tr><td>Beginning</td><td>End</td></tr><tr><td rowspan="5">LWc(△(α1; β)) C1-wave</td><td>Origin</td><td>f11</td><td>-705</td><td>-500</td><td>206</td><td>1.4174</td></tr><tr><td>Growth</td><td>f12</td><td>-499</td><td>-355</td><td>165</td><td>2.4007</td></tr><tr><td>Culmination</td><td>f13</td><td>-344</td><td>-63</td><td>272</td><td>3.4485</td></tr><tr><td>Decrease</td><td>f14</td><td rowspan="2">-62</td><td rowspan="2">401</td><td rowspan="2">464</td><td rowspan="2">0.7414</td></tr><tr><td>Decay</td><td>f15</td></tr><tr><td rowspan="5">LWc(△(α2;β)) C2-wave</td><td>Origin</td><td>f2.1</td><td>402</td><td>631</td><td>230</td><td>1.5261</td></tr><tr><td>Growth</td><td>f22</td><td>632</td><td>826</td><td>195</td><td>3.7692</td></tr><tr><td>Culmination</td><td>f3</td><td>827</td><td>970</td><td>144</td><td>4.875</td></tr><tr><td>Decrease</td><td>f24</td><td>971</td><td>1074</td><td>104</td><td>3.5288</td></tr><tr><td>Decay</td><td>f2.5</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">LWc(△(α3;β)) C3-wave</td><td>Origin</td><td>f1</td><td>1075</td><td>1146</td><td>72</td><td>4.8056</td></tr><tr><td>Growth</td><td>f32</td><td>1147</td><td>1207</td><td>61</td><td>7.5902</td></tr><tr><td>Culmination</td><td>f3</td><td>1208</td><td>1281</td><td>74</td><td>9.8919</td></tr><tr><td>Decrease</td><td>f34</td><td>1282</td><td>1436</td><td>155</td><td>7.0968</td></tr><tr><td>Decay</td><td>f.5</td><td>1437</td><td>1497</td><td>61</td><td>5.6885</td></tr><tr><td rowspan="5">LWc(△(α4; β4)) C4-wave</td><td>Origin</td><td>41</td><td>1498</td><td>1566</td><td>69</td><td>8.0435</td></tr><tr><td>Growth</td><td>f4.2</td><td>1567</td><td>1638</td><td>72</td><td>11.639</td></tr><tr><td>Culmination</td><td>f43</td><td>1639</td><td>1660</td><td>22</td><td>18.591</td></tr><tr><td>Decrease</td><td>f44</td><td>1661</td><td>1718</td><td>58</td><td>11.069</td></tr><tr><td>Decay</td><td>f45</td><td>1719</td><td>1749</td><td>31</td><td>7.2258</td></tr><tr><td rowspan="5">LWc(△(α5; β5)) C5-wave</td><td>Origin</td><td>f5.1</td><td>1750</td><td>1778</td><td></td><td>8.4138</td></tr><tr><td>Growth</td><td></td><td>1779</td><td>1800</td><td>29 22</td><td>11.909</td></tr><tr><td>Culmination</td><td>f5.2 f53</td><td>1801</td><td>1819</td><td>19</td><td>25.053</td></tr><tr><td>Decrease</td><td>f54</td><td>1820</td><td>1868</td><td>49</td><td>16.000</td></tr><tr><td>Decay</td><td>f55</td><td>1869</td><td>1919</td><td>51</td><td>8.5882</td></tr><tr><td rowspan="4">LWc(△(a6;β)) C6-wave</td><td>Origin</td><td>f61</td><td>1920</td><td>1958</td><td>39</td><td>9.359</td></tr><tr><td>Growth</td><td>f62</td><td>1959</td><td>1988</td><td>30</td><td>22.700</td></tr><tr><td>Culmination</td><td></td><td>1989</td><td></td><td></td><td>30.75</td></tr><tr><td>Decrease</td><td>f64</td><td>1997</td><td>1996 2007</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>11</td><td></td><td>29.545</td></tr></table></body></html>

Table 4.12 summarizes the results of the structural analysis and metric characteristics of six $C _ { n }$ -waves of global system conflicts. In view of the results of the structural analysis, the WC-sequence generates six successive local waves of global conflicts on the time interval $\Delta ( - 7 5 0 ; 2 0 0 7 )$ :

$$
\begin{array} { r } { L W _ { C } ( \Delta ( \alpha _ { 1 } ; \beta _ { 1 } ) ) , L W _ { C } ( \Delta ( \alpha _ { 2 } ; \beta _ { 1 } ) ) , . . . , L W _ { C } ( \Delta ( \alpha _ { 6 } ; \beta _ { 6 } ) ) , } \end{array}
$$

![](images/2f6fb4767981b3a331e1293201f2503e4f30d5a0296b4590341a9c1ec6aa9662.jpg)  
Fig. 4.10 Structural analysis of a local wave $L W _ { C } ( \Delta ( \alpha _ { 5 } ; \beta _ { 5 } ) )$ , of global conflicts: a sweep of the WCsequence on the time interval $\Delta ( \alpha _ { 5 } ; \beta _ { 5 } )$ ; $\mathbf { b }$ phases $f _ { k , 5 } L W _ { C } ( \Delta ( \alpha _ { 5 } ; \beta _ { 5 } ) ) , k = \overline { { { 1 , 5 } } } ,$ and their intensities

which represent some global cyclic civilization process [22] with decreasing period (see Table 4.11) and increasing intensity (see Table 4.12). Since the sequence of time intervals $\{ \Delta ( \alpha _ { n } ; \beta _ { n } ) \} _ { n = \overline { { { 1 , 6 ^ { \prime } } } } }$ determines the corresponding sequence of life cycles of $C _ { n }$ -waves of global system conflicts [2], $C _ { n } \equiv L W _ { C } ( \Delta ( \alpha _ { n } ; \beta _ { n } ) ) , n = \overline { { { 1 , 6 } } }$ . Figure 4.10 exemplifies the structural analysis of the time-base sweep of the WC-sequence on the time interval $\Delta ( \alpha _ { 5 } ; \beta _ { 5 } )$ , and Fig. 4.11 illustrates another feature of the pattern of global conflicts, i.e., the strict hierarchy of $C _ { n }$ -waves with respect to the intensities of their phases:

$$
I \left( f _ { n _ { 1 } , i } \right) < I \left( f _ { n _ { 2 } , i } \right) \forall _ { n _ { 1 } } < n _ { 2 } , n _ { 1 } , n _ { 2 } \in \Delta ( 1 ; 6 ) , i = \overline { { { 1 , 5 } } }
$$

The collective portrait of the intensity distribution of the phases $f _ { n , i } , n = { \overline { { 1 , 6 } } }$ ; $i = { \overline { { 1 , 5 } } }$ , of $C _ { n }$ -waves of global system conflicts (Fig. 4.12) evidently shows the wave dynamics of the pattern of global system conflicts.

![](images/bc04c95ff5b9fdb45d19aa53d2a247f58308ce8e837ef09b71f3e1c65e902f87.jpg)  
Fig. 4.11 Hierarchy of $C _ { n ^ { - } }$ waves of global system conflicts with respect to the intensities of their phases $f _ { n , i } , n = \overline { { 1 , 6 } } , i = \overline { { 1 , 5 } }$

![](images/7602b8d79b649b1ad699502134d149193956d7bd675fe780af93bf6718ae0b7d.jpg)  
Fig. 4.12 Intensity distribution for the phases $f _ { n , i }$ , $n = \overline { { 1 , 6 } } , i = \overline { { 1 , 5 } }$ $C _ { n }$ -waves of global system conflicts

# 4.4.3 Confirmation of the F-Pattern by Other Independent Studies

Any revealed pattern will be much more reliable if it corresponds to some additional external conditions (concepts, principles, hypotheses, etc.) and the conclusions obtained on its basis coincide or “resonate” with conclusions of other independent studies. Therefore, we will discuss the conclusions of some independent studies that confirm the reliability of the $F$ -pattern.

The first argument: the golden section present in the structure of $C$ -waves. Indeed, according to the structural harmony law [21], in any self-organizing system, each operation mode varying according to the variations in structural states of the system is related to a special time scale. This time scale is associated with a certain invariant of the generalized golden section as a characteristic of the stationary state of the system.

The second argument: as an integral part of the holistic evolutionary development of the civilization, the universal effect of the acceleration of historical time [23, 24] is manifested in the $F _ { \mathbf { \Phi } }$ -pattern since the duration of the lifecycles of $C .$ - waves of global system conflicts successively decreases.

The third argument is based on the prognostic properties of the $F$ -pattern. As follows from Table 4.7, the Fibonacci sequence $\{ \ F _ { S } \ \}$ degenerates for $C _ { n }$ -waves for $n > 6$ .

Whence the natural question arises: what will happen to the civilization after 2092, in particular, in the XXIInd century? Probably, the final cycle of an evolutionary chain will begin:

$$
C _ { 1 } > C _ { 2 } > C _ { 3 } > C _ { 4 } > C _ { 5 } > C _ { 6 } > C _ { 7 } ?
$$

This question was answered by Vernadsky [22] and Moiseev [25], outstanding scientists of the last century. They independently proposed the idea that if mankind does not cardinally change its global behavior, the environment in the middle of the XXIst century will degrade to the point that mankind will cease to exist. These conclusions were made for the constant paradigm of mankind existence— self-serving. If mankind changes the global existence paradigm to, for example, harmonious coexistence on the Earth, then it will continue the mission on the planet and the pattern of global conflicts revealed for the previous paradigm, which corresponds to the Fibonacci sequence, will no longer be valid for the new paradigm.

Thus, according to the forecast which is based on the $F$ -pattern, the XXIst century is an especial, critical phase of the evolution of our civilization. Moreover, the proposed model allows not only making general conceptual conclusions but also predicting and evaluating the metric characteristics of the possible stages of the evolutionary development of the civilization in the XXIst century.

The fourth argument is based on the synchronism of two periodic processes: $C \mathrm { . }$ -waves of global system conflicts and K-cycles of the development of the global economy, which are interdependent components of the unified holistic development of the global society. The fundamental property of the global society is cyclic development of its economy. This property is manifested by great Kondratieff cycles (K-cycles) discovered 80 years ago by Nikolai Kondratieff (Kondratiev), an outstanding Russian economist [15, 16]. Within the last two centuries, such cycles with periods of 40–60 years were in complete agreement with the real development of the economy.

The paper [20] interrelates the pattern of global system conflicts and the development of the global economy. Overlapping these two processes on the common time axis in [20] reveals their synchronism, which can be formulated as the following two principles:

• Quantization Principle. The time intervals $\Delta ( C _ { n } ) , n \geq 5$ on which the wave $C _ { n }$ undergoes the five phases of evolution: (ORIGIN) ${ \scriptstyle > } ( \mathrm { G R O W T H } ) >$ (CULMINATION) $>$ (DECREASE) $>$ (DECAY), contain an integer number $n _ { k } ( \Delta ( C _ { n } ) )$ of complete K-cycles; • Monotonicity Principle. The average duration $T _ { k } \big ( \Delta ( C _ { n } ) \big )$ of one complete $\mathrm { \Delta K }$ -cycle on the time intervals $\Delta ( C _ { n } )$ substantially decreases as $n$ grows.

# 4.4.4 F-Principle as the Basis of a Metric Study of Global Civilization Processes

As the global economic crisis promptly expands and global conflicts sharply aggravate, quick “metric” forecasts become of special value. As the results of [20] show, the $F _ { \mathbf { \Phi } }$ -pattern may be an important aspect in the development of a scientifically proved toolkit and methodology for the analysis of global civilization processes.

Since the development of the global economy and the course of global system conflicts are interdependent components of the evolutionary development of a globalized society, we may assume that the synchronism of these processes on the time intervals $\Delta ( C _ { 5 } )$ and $\Delta ( C _ { 6 } )$ as to obeying the quantization and monotonicity principles holds true also on the time interval $\Delta ( C _ { 7 } )$ This yields, in particular, the Fibonacci-dependence of the duration of the lifecycles of $C$ -waves of global system conflicts on the average duration of great Kondratieff cycles from 1750 to 2092.

As shown in [20], two scenarios for great Kondratieff cycles are possible in the 21st century:

• Scenario A. The period from 2008 to 2092 includes two complete Kondratieff cycles, 43.5 years on average each; Scenario B. The period from 2008 to 2092 includes three complete Kondratieff cycles, 28.3 years on average each.

More telling arguments can be brought in favor of scenario B. This can be confirmed indirectly by the results of some modern studies of global evolution processes, of which noteworthy are the concept of acceleration of historical time [23] and the hypothesis that the duration of great K-cycles tends to reduce with scientific and technical progress [17, 18].

# 4.4.5 Conclusions

1. Based on the evolutionary development of the civilization considered as a holistic process with harmonious interaction of its various components, it has been justified that the $F .$ -pattern corresponds to a number of additional conditions, namely:

the law of structural harmony; the modern concept of acceleration of historical time; $\bullet$ the concept of great Kondratieff cycles; global forecasts for the XXIst century as an especial, critical phase of the development of the civilization.

2. As a result of the structural analysis of the time-base sweep of the WCsequences on the time interval $\Delta ( - 7 5 0 ; \mathrm { N o w d a y } )$ , all the metric characteristics of $C _ { n }$ -waves, $n = { \overline { { 1 , 6 } } }$ have been established.   
3. A new feature of the dynamics of $C _ { n }$ -waves of global system conflicts has been revealed, namely, the strict hierarchy of $C _ { n }$ -waves with respect to the intensities of their phases.   
4. The metric forecast of the manifestation of great Kondratieff cycles in the 21st century based on the $F$ -pattern has been considered as an example.

# 4.5 Big Solar Spiral of Stirring up Global Systemic Conflicts

In Sect. 4.2 and in paper [2], an analysis of the hypothetical Fibonacci pattern of global systemic conflicts is made, based on the dynamic model of so-called C-waves with the golden ratio metrics underneath. The studies [20, 29] consider the evolutionary development of the civilization as an integral process formed as a result of harmonic interference of its various components and justify the correspondence of this pattern to a number of additional conditions, namely:

existence of an interrelation of global systemic conflicts and Kondratiev cycles of economic conjuncture (Sect. 4.3), [20];   
– the law of structural harmony [15, 21];   
– modern concept on the acceleration of historical time [23]; global forecasts for the XXIst century as a special critical phase of the development of civilization [30].

Based on the analysis of the empirical sequence of the frequencies of global conflicts, structural analysis of C-waves was carried out and metric approaches to the analysis and forecasting of some global civilizational processes were considered. Note that throughout centuries, according to the synchronous development of the civilization, the nature of global conflicts also varied. It became especially noticeable at the end of the XXth and in the first decades of the XXIst centuries, when the mankind passed to the “information society” where the terms such as information wars, cyber wars, hybrid wars, psychotropic weapon, etc. have already become customary.

However, the results mentioned above were grounded on the investigation of only “inner” factors of civilizational processes, where a human being with his mentality, complicated inner world, culture, and values remains the subject of all conflicts. The manifestation of any global conflict was related, first of all, to release of an enormous “mental” and “social” energy accumulated by people. But it is lawful to raise the question: Whether there are external (for a person) factors influencing the behavior of civilizational processes and, in particular, patterns of global systemic conflicts? To discuss this topic, let us turn to some authorities.

As far back as in the last century, A. L. Chizhevskii, an outstanding biophysicist, one of the founders of space natural science, used a huge amount of factual material and justified that the life of the biosphere and social rhythms depend on the rhythms of the Sun and Space [31]. He had formulated the following postulates [32]:

• solar and space cycles in arithmetic mean are determined by the quantity approximately equal to 11 years, and there are grounds to suppose that physical factors calling this periodicity are periodically appearing sunspots, geomagnetic storms, and other manifestations of solar magnetic activity substantially influencing the life of the biosphere; modification of social rhythms on the Earth’s surface (peak and decay phases with respect to birth and death rates, illness, social manifestations, etc.), coinciding in time with solar and space cycles, allow us to suppose that the reason of this pattern can also be out of social factor;   
• the reason of the strict periodicity of solar rhythms in all historical epochs can be a physical factor influencing more or less uniformly all the population of our planet; solar activity itself does not generate social bursts in literal sense (wars, revolutions, etc.) and only promotes the accumulation of enormous “collective,” “mental,” and “social” energy on the Earth, which then leads to its release.

In this context, one of the major tasks of modern science is to reveal the spectrum of patterns of the operation of interrelated system “the Sun–the Earth” for a fuller understanding of civilizational processes and to implement the corresponding set of measures to prepare the mankind for future (predictable) global events and to mitigate the expected adverse consequences.

In [31, 32] assumptions are made about the concentration of local conflicts near the maxima of solar activity; however, publications on the influence of solar activity on global conflicts with unstable “time configuration” and considerable duration are virtually absent. The supercomplexity of such problems is obvious.

In the present section, based on the Fibonacci pattern of global systemic conflicts (Sects. 4.2 and 4.3), [2, 20, 29], we will formulate the hypotheses about a metric relationship between two global periodic processes: the sequence of 11-year cycles of solar activity and evolutionary structurization of the family of C-waves of global systemic conflicts enveloping large and super-large time intervals and having a variable structural configuration.

# 4.5.1 Synchronous Variation of Solar Activity and Formation of C-Waves of Global Systemic Conflicts

The 11-year cycle of solar activity with average 11.1 year duration is defined by the Schwabe–Wolf [33] law. For the quantitative determination of solar activity, the Wolf numbers averaged over a year [33] published by the Zurich observatory since 1849 are most often applied. A number according to the Zurich indexing is assigned to all the observed 11-year cycles of solar activity. Number one is assigned to the cycle began in 1755, and the number of the current cycle began in 2008–2009 is 24.

All the observations of solar spots are summarized and monthly average and annual average values of the Wolf numbers are determined at the Solar Influences Data Analysis Center (Belgium) [34].

An important statistical dependence of a series of Wolf numbers is characterized by the relation of amplitude and phase of cycles. According to this rule, the larger the duration of the current cycle, the less the amplitude of the next cycle [28]. Solar cycle is asymmetric with respect to the maximum of solar activity: growth phase $( \approx 4 . 6$ years) is shorter than decay phase ${ \approx } 6 . 5$ years) [33].

Table 4.13 shows the list of 11-year cycles of solar activity recorded since 1755 [28, 35, 36]. The graphic illustration of Zurich cycles Nos. 1–23 and of their parameters is presented in Fig. 4.13 by a radar chart, where $\tau _ { m a x } ^ { ( k ) }$ is the year of the maximum solar activity in the Zurich cycle ${ W } _ { S A } ^ { ( k ) }$ , $k$ is the number of Zurich cycle $\left( k = { \overline { { 1 , 2 3 } } } \right)$ .

Table 4.13 The list of 11-year cycles of solar activity recorded since 1755   

<html><body><table><tr><td rowspan="2">Cycle number</td><td colspan="2">Years of active Zurich cycles</td><td rowspan="2">Cycle number</td><td colspan="2">Years of active Zurich cycles</td></tr><tr><td>Minimum</td><td>Maximum</td><td>Minimum</td><td>Maximum</td></tr><tr><td>1</td><td>1755</td><td>1761</td><td>13</td><td>1889</td><td>1893</td></tr><tr><td>2</td><td>1766</td><td>1769</td><td>14</td><td>1901</td><td>1905</td></tr><tr><td>3</td><td>1775</td><td>1778</td><td>15</td><td>1913</td><td>1917</td></tr><tr><td>4</td><td>1784</td><td>1787</td><td>16</td><td>1923</td><td>1928</td></tr><tr><td>5</td><td>1798</td><td>1804</td><td>17</td><td>1933</td><td>1937</td></tr><tr><td>6</td><td>1810</td><td>1816</td><td>18</td><td>1944</td><td>1947</td></tr><tr><td>7</td><td>1823</td><td>1830</td><td>19</td><td>1954</td><td>1957</td></tr><tr><td>8</td><td>1833</td><td>1837</td><td>20</td><td>1964</td><td>1968</td></tr><tr><td>9</td><td>1843</td><td>1848</td><td>21</td><td>1976</td><td>1979</td></tr><tr><td>10</td><td>1856</td><td>1860</td><td>22</td><td>1986</td><td>1989</td></tr><tr><td>11</td><td>1867</td><td>1870</td><td>23</td><td>1996</td><td>2000</td></tr><tr><td>12</td><td>1878</td><td>1883</td><td>24</td><td>2008</td><td></td></tr></table></body></html>

![](images/a3cec2cf0af844705cad7026111ec4ddaef449945d43211936172fe75b6abc40.jpg)  
Fig. 4.13 Parameters of the Zurich Schwabe–Wolf cycles $W _ { S A } ^ { ( 1 ) } , W _ { S A } ^ { ( 2 ) } , . . . , W _ { S A } ^ { ( 2 3 ) } ( 1 7 5 5 - 2 0 0 8 )$ : —is the maximum solar activity SA of smoothed monthly average Wolf numbers, $\bullet$ is the minimum of solar activity SA of smoothed monthly average Wolf number

Let us introduce some definitions: ${ Z _ { \mathrm { S A } } \{ \overline { { \mathrm { S W } } } \} }$ are Zurich Schwabe–Wolf cycles (Zurich cycles, Schwabe–Wolf $Z$ -cycles; correspond to the Zurich numbers $\mathbf { k } \in$ $\operatorname { I } ( 1 ; 2 3 ) ) ; \operatorname { R } _ { \operatorname { S A } } \{ { \overline { { \operatorname { S W } } } } \}$ are recovered Schwabe–Wolf cycles (recovered cycles, Schwabe–Wolf R-cycles; correspond to the numbers $\mathbf { k } \in \operatorname { I } ( - \infty ; 0 ) ) ; \operatorname { P } _ { \mathrm { S A } } \{ \overline { { \mathrm { S W } } } \}$ are predictable Schwabe–Wolf cycles (predictable cycles, Schwabe–Wolf $\mathrm { \bf P }$ -cycles; correspond to the Zurich numbers $\mathbf { k } \in \operatorname { I } ( 2 4 ; + \infty ) )$ , where

$$
\begin{array} { r l } & { \qquad \quad \mathrm { I } ( \mathbf { m } ; \mathbf { n } ) = \{ \mathbf { k } \in \mathrm { Z } : \mathbf { m } \leq \mathbf { k } \leq \mathbf { n } \} ; } \\ & { \qquad \mathrm { C } _ { \mathrm { S A } } \left\{ \overline { { \mathrm { S W } } } \right\} \equiv \mathrm { R } _ { \mathrm { S A } } \left\{ \overline { { \mathrm { S W } } } \right\} \cup \mathrm { Z } _ { \mathrm { S A } } \left\{ \overline { { \mathrm { S W } } } \right\} \cup \mathrm { P } _ { \mathrm { S A } } \left\{ \overline { { \mathrm { S W } } } \right\} . } \end{array}
$$

The constant

$$
\mu _ { S A } ^ { ( S W ) } = 1 1 . 1 y e a r
$$

is called the Schwabe–Wolf solar metric (the Schwabe–Wolf metric). Note that this metric, as a stable external performance criterion of various global dynamic processes in the interrelated system “the Sun–the Earth” allows us to improve some metric parameters of these processes.

In particular, parameters of $C _ { k }$ -waves can be adjusted proceeding from the following facts:

on the basis of scientific observations for the last three centuries, the number of 11.1 years is found as a stable arithmetic mean value of Schwabe–Wolf cycle periods; considerable lengths of periods $T ( C _ { k } )$ of $\left( C _ { k } \right)$ -waves, $k \in I ( 1 ; 4 )$ of global systemic conflicts (260 years $< T ( C _ { k } ) < 1 2 0 0$ years) [2, 20, 29] allows us to assume that on the time intervals $\Delta ( C _ { 1 } ) , \Delta ( C _ { 2 } ) , \Delta ( C _ { 3 } )$ and $\Delta ( C _ { 4 } )$ determining the life cycles of these waves, the number 11.1 years as arithmetic mean value of the periods of Schwabe–Wolf cycles will be exhibited even more explicitly.

The «reconstruction» of $\left( C _ { k } \right)$ -waves has allowed us, in particular, to solve the important problem of determining “time glueing” of the intervals $\Delta ( C _ { k } )$ of the manifestation of $\left( C _ { k } \right)$ -waves, $k \in I ( 1 ; 4 )$ , based on the stable external criterion, the Schwabe–Wolf metric.

The correction error was $1 . 2 3 \%$ with the completely retained hierarchical order of $C _ { k }$ -waves, $k \in I ( 1 ; 7 )$ 31: Table 4.14 shows the results of the correction of intervals $\Delta ( C _ { k } )$ of the manifestation of $C _ { k }$ -waves for $k \in I ( 3 ; 7 )$ : Here, $[ \alpha _ { k } ; \beta _ { k } ] = \Delta ( C _ { k } )$ is the time interval of the manifestation of $C _ { k }$ -wave [2, 29], and $\left[ { \alpha } _ { k } ^ { \ast } ; { \beta } _ { k } ^ { \ast } \right] = \Delta ^ { \ast } ( C _ { k } )$ is the interval of manifestation of $C _ { k }$ -wave, modified by the Schwabe–Wolf metric.

This procedure also allows us to arrange the Schwabe–Wolf R-cycles on the time intervals $\Delta ^ { * } ( C _ { k } ) , k \in I ( 1 ; 4 )$ ; uniformly with the period of 11.1 years and, based on the stable external criterion, to specify the values of the universal time quantum $k _ { C }$ of global systemic conflicts [29] and mean value $\bar { T } _ { k c }$ of the duration of Kondratiev cycles of the modified sequence of $K$ -cycles [20]:

$$
k _ { C } \cong 8 9 y e a r s , \bar { T } _ { k c } \cong 4 4 . 1 4 y e a r s .
$$

Table 4.14 Results of the corrected “Glueing” of intervals of the manifestation of $C k$ -waves   

<html><body><table><tr><td>Ck-Wave</td><td>αk</td><td>β</td><td></td><td></td></tr><tr><td>C7-wave</td><td>2008</td><td>2092</td><td>2008</td><td>2097</td></tr><tr><td>C6-wave</td><td>1920</td><td>2008</td><td>1919</td><td>2008</td></tr><tr><td>C5-Wave</td><td>1750</td><td>1920</td><td>1741</td><td>1919</td></tr><tr><td>C4-Wave</td><td>1498</td><td>1750</td><td>1474</td><td>1741</td></tr><tr><td>C3-Wave</td><td>1075</td><td>1498</td><td>1030</td><td>1474</td></tr></table></body></html>

The ordered set of Schwabe–Wolf solar cycles

$$
{ \cal H } _ { W } ^ { ( k ) } \equiv \big \{ W \in C _ { S A } \big \{ \overline { { S W } } \big \} : \Delta ^ { * } ( W ) \cap \Delta ( C _ { k } ) \neq \emptyset \big \} , k \in I ( 1 ; 7 ) ,
$$

is called an ensemble $( H _ { W } ^ { ( k ) }$ -ensemble) stirring up the $\left( C _ { k } \right)$ -wave of global systemic conflicts, where $\Delta ^ { * } ( W ) = [ \tau _ { 1 } ; \tau _ { 2 } ]$ is the time interval of the manifestation of cycle $W \in C _ { S A } \big \{ \overline { { S W } } \big \}$ :

Remark $\boldsymbol { { \mathit { 1 } } }$ By stirring up of $C _ { k }$ -wave of global systemic conflicts by $H _ { W } ^ { ( k ) }$ -ensemble (briefly, $H _ { W } ^ { ( k ) } { \odot } C _ { k } )$ ) we will mean the process of active systemic influence of the sequence of Schwabe–Wolf solar cycles constituting this ensemble on the process of evolutionary structurization of the $C _ { k }$ -wave, $k \in I ( 1 ; 7 )$ .

Remark 2 By stirring up a family of $\left\{ C _ { k } \right\} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by a sequence of ensembles of $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ Schwabe–Wolf cycles (briefly, $( H _ { W } ^ { ( 1 ) } { \odot } C _ { 1 } ) \mapsto ( H _ { W } ^ { ( 2 ) } { \odot } C _ { 2 } ) \mapsto \dots \mapsto ( H _ { W } ^ { ( 7 ) } { \odot } C _ { 7 } ) )$ we will mean the process of active systemic influence of the sequence of solar cycles constituting these ensembles on the process of evolutionary formation of the sequence of $C _ { k }$ -waves as an integral structure.

Figure 4.14 shows the alignment of two processes on the time axis: sequence of Schwabe–Wolf cycles HW   nW AÞol I 0;15 a nd sequence of empirical frequencies $N _ { W }$ of global systemic conflicts [2, 23]. Stirring up by $H _ { W } ^ { ( 5 ) }$ -ensemble of $C _ { 5 }$ -waves of global systemic conflicts is illustrated. The cycle with the number 0 pertains to Zurich cycles $Z _ { S A } \{ { \overline { { S W } } } \}$ in addition as original one taking into account the corrected glueing of time intervals $\Delta ( C _ { k } ) , k \in I ( 1 ; 7 )$ :

Figure 4.15 illustrates “stirring up” by $H _ { W } ^ { ( 6 ) }$ -ensemble of $C _ { 6 }$ -wave of global systemic conflicts manifested in the 20th century [29].

Based on the aforesaid and the results from Sect. 4.2, we may state that the chain of stirring up the sequence of $\mathrm { ^ c }$ -waves

$$
\gamma : \big ( H _ { W } ^ { ( 1 ) } \odot C _ { 1 } \big ) \longmapsto \big ( H _ { W } ^ { ( 2 ) } \odot C _ { 2 } \big ) \longmapsto \dots \mapsto \big ( H _ { W } ^ { ( 7 ) } \odot C _ { 7 } \big ) ,
$$

where

$$
\left\{ \begin{array} { c } { { H _ { W } ^ { ( l ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( - 2 3 2 ; - 1 2 9 ) } , H _ { W } ^ { ( 2 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( - 1 2 8 ; - 6 5 ) } , } } \\ { { H _ { W } ^ { ( 3 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( - 6 4 ; - 2 5 ) } , H _ { W } ^ { ( 4 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( - 2 4 ; - 1 ) } , } } \\ { { H _ { W } ^ { ( 5 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( 0 ; 1 5 ) } , H _ { W } ^ { ( 6 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( 1 6 ; 2 3 ) } , } } \\ { { H _ { W } ^ { ( 7 ) } \equiv \left\{ W _ { S A } ^ { ( l ) } \right\} _ { l \in I ( 2 4 ; 3 1 ) } , } } \end{array} \right.
$$

![](images/fbde4b5beca7ba613ca202c876b098d247e5410d291524d7f264f1433a308c93.jpg)  
Fig. 4.14 Illustrated «stirring up» by $H _ { W } ^ { ( 5 ) }$ -ensemble of Schwabe–Wolf $Z$ -cycles of $C _ { 5 }$ -wave of global systemic conflicts on the time interval from 1750 till 1920: $N _ { W C }$ is empirical frequencies of global conflicts; $\mathbf { N } _ { \mathbf { W } }$ is smoothed monthly average Wolf’s numbers

![](images/1613877aa4000ce9a8f85d6904928b35699712cb994b9bf95f27345d44877da1.jpg)  
Fig. 4.15 Illustrated «stirring up» by $H _ { W } ^ { ( 6 ) }$ -ensemble of Schwabe–Wolf Z-cycles of $C _ { 6 }$ -wave of global systemic conflicts exhibited in the XXth century (1920–2008)

implements the process of systemic evolutionary structurization of the family of $\left\{ C _ { k } \right\} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts.

The sequence of numbers

$$
c a r d H _ { W } ^ { ( 7 ) } , c a r d H _ { W } ^ { ( 6 ) } , . . . , H _ { W } ^ { ( 1 ) }
$$

corresponds to the fragment of the Fibonacci sequence

$$
F ( C _ { 7 } ) , F ( C _ { 6 } ) , . . . , F ( C _ { 1 } )
$$

for $C _ { 7 ^ { - } } , C _ { 6 ^ { - } }$ , …, $C _ { 1 }$ -waves, namely

$$
\left\{ \begin{array} { l } { c a r d H _ { W } ^ { ( 7 ) } = 1 \cdot h _ { C } ^ { ( S W ) } , c a r d H _ { W } ^ { ( 6 ) } = 1 \cdot h _ { C } ^ { ( S W ) } , c a r d H _ { W } ^ { ( 5 ) } = 2 \cdot h _ { C } ^ { ( S W ) } , } \\ { c a r d H _ { W } ^ { ( 4 ) } = 3 \cdot h _ { C } ^ { ( S W ) } , c a r d H _ { W } ^ { ( 3 ) } = 5 \cdot h _ { C } ^ { ( S W ) } , c a r d H _ { W } ^ { ( 2 ) } = 8 \cdot h _ { C } ^ { ( S W ) } , } \\ { c a r d H _ { W } ^ { ( 1 ) } = 1 3 \cdot h _ { C } ^ { ( S W ) } , } \end{array} \right.
$$

where

$$
h _ { C } ^ { ( S W ) } \equiv 8
$$

is the global Schwabe–Wolf constant (global CSW-constant) of stirring up by $H _ { W } ^ { ( k ) }$ - ensembles of Schwabe–Wolf solar cycles of the family of $\left\{ C _ { k } \right\} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts.

Let us introduce the following notation: $\pi _ { S W C } ( C )$ is the process of evolutionary structurization of the family of $C _ { k }$ -waves of global systemic conflicts, $k \in I ( 1 ; 7 )$ ; $\pi _ { S A } ( \overline { { S W } } )$ is the global process of variation in solar activity in the context of manifestation of the Schwabe–Wolf cycles; $\pi _ { G E } ( K C )$ is the world economy development process in a context of manifestation of Kondratiev cycles.

Let us formulate the supposed hypothetical pattern of the metric relationship of global processes $\pi _ { S A } \left( \overline { { S W } } \right)$ and $\pi _ { S W C } ( C )$ as the following hypothesis.

Hypothesis of (SA-WC)-synchrony. Each $C _ { k }$ -wave, $k \in I ( 1 ; 7 )$ , of global systemic conflicts contains an integer number of complete Schwabe–Wolf solar cycles

$$
N _ { k } = h _ { C } ^ { ( S W ) } \cdot F ( C _ { k } ) ,
$$

where $h _ { C } ^ { ( S W ) }$ is the global CSW-constant and $F ( C _ { k } )$ is the number of the Fibonacci sequence, corresponding to $C _ { k }$ -wave.

Considering (4.16–4.18), the hypothesis of (SA-WC)-synchrony, and the results from Sect. 4.2, let us formulate the hypothesis about the presence of a metric interrelation among three global synchronous processes:

$$
\pi _ { S W C } ( C ) , \pi _ { S A } \left( \overline { { { S W } } } \right) a n d \pi _ { G E } ( K C ) .
$$

Hypothesis of (SA-WC-GE)-interrelation. The following relation takes place:

$$
k _ { C } \cong h _ { C } ^ { ( S W ) } \cdot \mu _ { S A } ^ { ( S W ) } \cong 2 \overline { { T } } _ { K C } ,
$$

where $k _ { C }$ is a universal time slot of global systemic conflicts, $h _ { C } ^ { ( S W ) }$ is global SA-constant, lSSAWÞ is the Schwabe–Wolf Solar metric, and TKC is average duration of one Kondratiev cycle.

# 4.5.2 Visualization of the Process of “Stirring Up” of the Family of $\{ C _ { K } \} _ { K \in { I ( 1 ; 7 ) } }$ -Waves of Global Systemic Conflicts

Figure 4.16 shows big Solar spiral of the process of “stirring up” of the family of $\{ C _ { k } \} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by the sequence of ensembles of the

![](images/8907ad1a4e9f6e446d414b69bc3497ad0c72ecc91be4ea5d0a7432f2225176d1.jpg)  
Fig. 4.16 Big «Solar spiral» of the process of «stirring up» of the family of $\{ C _ { k } \} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by a sequence of ensembles of Schwabe–Wolf cycles $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ on the time interval from $8 4 0 ~ \mathrm { B C }$ till 2097 AD

![](images/4f70a91580c6c1615672952661a391fe003e7b1fc0e50617db54cd296e0eaa0f.jpg)  
Fig. 4.17 Hyperbolic «Solar spiral» of the process of «stirring up» of the family of $\{ C _ { k } \} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by the sequence of ensembles of Schwabe–Wolf cycles $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ on the time interval from $8 4 0 ~ \mathrm { B C }$ till 2097 AD

Schwabe–Wolf cycles $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ on the time interval from $8 4 0 ~ \mathrm { B C }$ till 2097 AD. The main parameters of the process are shown, as well as the structural properties of the waves of global systemic conflicts (strict hierarchy of $C _ { k }$ -waves with respect to the intensities $I \big ( \varphi _ { k , i } \big )$ of phases of their evolutionary development, $\varphi _ { k , i }$ , $i \in I ( 1 ; 5 )$ , $C _ { k }$ -waves; $T _ { k } = T ( C _ { k } )$ is the duration of the life cycles of $C _ { k }$ - waves, $k \in I ( 1 ; 7 )$ ; $N _ { k }$ is the number of Zurich cycles in the ensemble $H _ { W } ^ { ( k ) } , k \in$ I 1; 7Þ : $N _ { k } = N _ { k + 1 } + N _ { k + 2 } ; N _ { 6 } = N _ { 7 } = = h _ { c } ^ { ( S W ) }$ , $k \in I ( 1 ; 5 ) ; T _ { k } = T _ { k + 1 } + T _ { k + 2 }$ ; and $T _ { 6 } = T _ { 7 } = k _ { C } , k \in I ( 1 ; 5 )$ .

Taking into account the hyperbolic growth of the intensities of $C _ { k }$ -waves, $k \in$ $I ( 1 ; 7 )$ [2], Fig. 4.17 also shows the hyperbolic Solar spiral of the process of “stirring up” of the family of $\{ C _ { k } \} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by the sequence of ensembles $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ on the time interval specified above. Here, $\mathrm { T } ( \mathrm { C } _ { 7 } ) = 8 9$ , T $( \mathbf { C } _ { 6 } ) = 8 9$ , $\mathrm { T } ( \mathbf { C } _ { 5 } ) = 1 7 8$ , $\mathrm { T } ( \mathrm { C } _ { 4 } ) = 2 6 7$ , $\mathrm { T } ( \mathbf { C } _ { 3 } ) = 4 4 5$ , T $( \mathbf { C } _ { 2 } ) = 7 1 2$ , and $\mathrm { T } ( \mathbf { C } _ { 1 } ) = 1 1 5 7$ .

# 4.5.3 Local “Stirring Up” by $\pmb { H } _ { W } ^ { ( K ) }$ -Ensemble of Schwabe– Wolf Solar Cycles of Evolution Phases of $C _ { k }$ -Wave of Global Systemic Conflicts

We have formulated the hypotheses and performed the analysis of metric aspects of the process of “stirring up” of the family of $\{ C _ { k } \} _ { k \in I ( 1 ; 7 ) }$ -waves of global systemic conflicts by the sequence of Schwabe–Wolf cycles2 $H _ { W } ^ { ( 1 ) } , H _ { W } ^ { ( 2 ) } , . . . , H _ { W } ^ { ( 7 ) }$ , promoting the system formation of a global configuration of $C _ { k }$ -waves as an integrated structure on super-large time intervals.

![](images/39da5e0b6c6529f5a7455d801d3676add5e15dfdebdfe982e81b9874e7142012.jpg)  
Fig. 4.18 Zurich cycle $W _ { S A } ^ { ( 2 3 ) } \in H _ { W } ^ { ( 6 ) }$ corresponding to the «decay» phase of $C _ { 6 }$ -wave (C-wave of the 20th century); new (partially manifested) Zurich cycle $W _ { S A } ^ { ( 2 4 ) } \in H _ { W } ^ { ( 7 ) }$ corresponding to the «origin» phase of -wave -wave of the XXIst century)

An important separate problem is investigating the patterns of the formation of the inner configuration for each separate $C _ { k }$ -wave, $k \in I ( 1 ; 7 )$ , which is manifested on a smaller time interval. Such configuration is defined by the local hierarchy of the intensities $I \big ( \varphi _ { k , i } \big )$ of its evolution phases $\varphi _ { k , i }$ , $i \in I ( 1 ; 5 )$ . To know the mechanisms of formation of such local structures is especially important in the scenario analysis of the development of global civilization processes in short-term perspective.

Figure 4.18 illustrates the cycle ${ W } _ { S A } ^ { ( 2 3 ) }$ manifested at the “Decay” phase of the $C _ { 6 }$ -wave of global systemic conflicts (C-wave of the XXth century) completed in 2007. We used the results of statistical observations carried out from December, 2008 till April, 2014 [37] to represent parameters of the new solar cycle $W _ { S A } ^ { ( 2 4 ) } \in H _ { W } ^ { ( 7 ) }$ , stirring up the first phase (Origin) of the forecasted (final) $C _ { 7 }$ -wave of global systemic conflicts (C-wave of the XXIst century). The years of active Sun (2013–2014) are emphasized.

Analyzing the time interval 2013–2014 as an active Sun period, we may state that it was characterized by considerable social disruptions in different regions of the world: Syria, Crimea, South-East Ukraine, Iran, and Iraq are the characteristic examples of releasing the collected social energy of major groups of population of the Earth at the initial phase of the seventh systemic global conflict.

# 4.5.4 Scenarios “XXI–2k” and “XXI–3k” of Global Civilizational Processes During the Seventh Systemic Global Conflict

Let us consider possible scenarios of the manifestation of two Kondratiev cycles during the seventh systemic global conflict (scenario “XXI–2K”) and three such cycles (scenario “XXI–3K”) [20]. Based on the alignment on the time interval ${ \boldsymbol { \Delta } } ^ { * } ( C _ { 7 } )$ (from 2008 till 2097) of three synchronous (forecasted) processes.

$$
\pi _ { S W C } ( C ) , \pi _ { S A } \left( \overline { { { S W } } } \right) a n d \pi _ { G E } ( K C ) .
$$

Figures 4.19 and 4.20 show two possible scenarios “XXI–2K” and “XXI–3K” of the developments of global civilizational processes in the XXIst century. Taking into account the patterns presented above and leaning upon the results from [2, 20, 29], we present the results of the metric scenario analysis in Tables 4.15 and 4.16.

For brevity sake, we use the following notation: $\tau _ { m a x } \bigg ( W _ { S A } ^ { ( k ) } \bigg )$ and smin $\tau _ { m i n } \left( W _ { S A } ^ { \left( k \right) } \right)$ are respectively the years of the maximum and minimum activity of the Schwabe–Wolf Zurich cycle ${ W } _ { S A } ^ { ( k ) }$ ; $V ^ { + } \left( \bar { K } \right)$ and $V ^ { - } ( \bar { K } )$ respectively the ascending and descending half-waves of the Kondratiev cycle $\bar { K }$ ; $t _ { m a x } ( \bar { K } )$ and $t _ { m i n } ( \bar { K } )$ are respectively the years of maximum and minimum conjuncture $K _ { G E }$ for the Kondratiev cycle $\bar { K }$ ; notation $A \approx B$ means that points $A$ and $B$ are rather close on the numerical axis; $t$ $( O ) , t ( G )$ and $t ( U )$ are conventional instants of time since which (according to scientific forecast) the amount of oil, gas, and uranium consumed in the world, respectively, will exceed their production.

We will assume that the scenario XXI-3K is more likely in the 21st century compared to the scenario XXI-2K. In favor of this assumption, we give two arguments:

1. According to the hypothesis of the acceleration of historical time [21], all processes in the 21st century will proceed faster than in previous centuries.   
2. Changes in the modern world are no longer linear in time (Fig. 4.21a). As defined by the UN Summit on Sustainable Development of 2015 and Davos Summit of 2015, these changes are exponential (Fig. 4.21b), and the new digital world is accordingly called exponential, where a, $\mathbf { b }$ and $\mathbf { k }$ are the constants of a global society growth.

# 4.5.5 Conclusions

1. In this section we have formulated the hypotheses about the presence of a metric relationship between the sequence of 11-year Schwabe–Wolf cycles of solar

Scenario 1 N C-wave W HW-ensemble of Schwabe-Wolf cycles πsA (SW) W（24 ）W（2 8 W2 福 嘴嘴 福 茶 N W(31) 2013 2024 2035 2045 205 2068 2079 2090   
300 300 0 2 28 0 256 years KGE K-cycles forecast 元GE （KC) K n 1 K   
300 X Q 0 t 0 LOIL URANIUM years J O Phases of C-wave(forecast）)πsw(C)   
30 7.1 7.2 7.3 7.4 $\Phi _ { 7 , 5 }$ Phase name ORIGIN GROWTH CULMINATION DECREASE Ω7 Ω7,2 Ω73 Ω74 Ω7.5 Scenario N C，-wave W H-ensemble of Schwabe-Wolf cycles πA (Sw) W（27) W（24） 25 8 W(26) 武 发 城 W(29) W(30） 安 SA W(31) SAA PD 2013 2024 2035 2045 57 2068 2079 2090 t   
300 0 0 0 20 HGE TGE k（） K K   
30 交 厦 t G 8 GAS years OIL URANIUM ！ g(7 Phasesof C-wave(forecast）πsw(C)   
00 $\Phi _ { 7 , 1 }$ 7.2 7.3 7.4 7.5 Phase name ORIGIN GROWTH CULMINATION DECREASE DECAY Ω7 Ω7.2 Ω7.3 74 Ω7.5

Table 4.15 Results of the metric analysis of the XXI–3K scenario   

<html><body><table><tr><td>Phases of C7- wave</td><td>Correspondence to the cycle</td><td>SA year w） Tmax</td><td>Correspondence to the half-wave of K-cycle</td><td>Special (critical) instants of time</td></tr><tr><td>7.1</td><td>w(2</td><td>2013</td><td>V- （K）</td><td>Tmar(W2A) ∈ Ω7.1</td></tr><tr><td rowspan="2">7.2</td><td>w(25</td><td>2024 2035</td><td rowspan="2">V+ (K)</td><td rowspan="2">t(O),t(G) = Tmax (W²) (W) = Tmar(W2a) tmin K（） ≌Tmax tmax</td></tr><tr><td>w（2</td><td></td></tr><tr><td rowspan="2">7.3</td><td>w2</td><td>2045</td><td>V-</td><td rowspan="2">t(U）= Tmax(W) tmin ≧ Tmin(WA)</td></tr><tr><td>w</td><td>2057</td><td>V+ （K）</td></tr><tr><td rowspan="2">7.4</td><td>w(2</td><td>2068</td><td>V</td><td rowspan="2">tmin K = Tmax(WsA)</td></tr><tr><td>w</td><td>2079</td><td>V+</td></tr><tr><td>1.5</td><td>w</td><td>2090</td><td>V+ K</td><td>Tmax WSA tmax</td></tr></table></body></html>

Table 4.16 Results of the metric analysis of the “XXI–2K” scenario   

<html><body><table><tr><td>Phaces Wave</td><td>Cothe ondence</td><td>Tmax SA year W）</td><td>Cothe sondence of K-cycle</td><td>Sspecial (critical) instants</td></tr><tr><td>7.1</td><td>w24）</td><td>2013</td><td>V-(K()</td><td>Tmax (W2A) ∈ Ω7,1</td></tr><tr><td rowspan="2">7.2</td><td>w2</td><td>2024</td><td rowspan="2">V+(K()</td><td rowspan="2">t(0),t(G) = Tmar (W2A) tmin = Tmin (W)</td></tr><tr><td>w2</td><td>2035</td></tr><tr><td rowspan="2">7.3</td><td>w27)</td><td>2045</td><td>V-</td><td rowspan="2">t(U) = tmax tmax （K（7） ≧ Tmin(W) K（7</td></tr><tr><td>w2</td><td>2057</td><td>（K2） V+</td></tr><tr><td rowspan="2">7.4</td><td>W</td><td>2068</td><td>V K）</td><td rowspan="2">tmin K ≦ Tmin(WA)</td></tr><tr><td>w</td><td>2079</td><td>V+ K</td></tr><tr><td>1.5</td><td>ws1)</td><td>2090</td><td>V+ （K）</td><td>（K（7）） Tmin (W3) tmax 2</td></tr></table></body></html>

activity and the process of evolutionary structurization of the family of $C$ -waves of global systemic conflicts enveloping large and super-large time intervals and having unstable “time configuration.” This relationship can be considered, in particular, as one more proof of the F-pattern of civilizational processes, leaning upon the global external criterion.

![](images/5843b185f0d1f919102844e5dce6fd9da60d7511649fae25bfa028eefbe7fd3d.jpg)  
Fig. 4.21 Development of global society, $a$ —linear growth; b—exponential growth

2. Within the framework of the formulated hypotheses, we have obtained the formula relating the main metric performances of three global periodic processes of the Schwabe–Wolf cycles of solar activity, $C$ -waves of global systemic conflicts, and Kondratiev cycles of the development of the global economy.

3. We have constructed the big and hyperbolic “Solar spirals” of the process of “stirring up” of the family of waves of global systemic conflicts by the sequence of ensembles of Schwabe–Wolf cycles on the time interval from 840 BC till 2097 AD, as a visual illustration of the revealed patterns.

4. We have considered the formation of the local configuration of a separate $C _ { k }$ - wave of global systemic conflicts defined by the inner hierarchy of the intensities of its evolution phases. We have presented current parameters for the new, 24th, Schwabe–Wolf Zurich solar cycle “stirring up” the first phase (“Origin”) of the predicted $C _ { 7 }$ -wave. We have emphasized years 2013 and 2014 as years of active Sun.

5. We have constructed two possible scenarios, XXI–2K and XXI–3K, for the development of global civilizational processes during the seventh (final) systemic global conflict in the 21st century. We have used the revealed patterns to formulate the main characteristic features of the scenarios and to define their metric performances.

# 4.6 Influence of Global Threats on the Sustainable Development of Countries and Regions of the World

The study presented in this section is based on the concept of “sustainable development” being the further development of studies of Vernadskij about noosphere [22]. It has been theoretically and practically proved that on the edge of the centuries studies about the noosphere appeared to be a necessary platform for the development of three-dimension concept of ecological, social and economic sustainable development [4].

Economic approach is based on the optimal usage of limited resources and application of natural-, power- and material saving technologies for creation of the gross income flow which would at least provide the preservation (not reduction) of the gross capital (physical, natural or human), with the use of which the gross income is created.

From the ecological point of view the sustainable development is aimed at provision of the integrity of both biological and physical natural systems as well as their viability that influences the global stability of the whole biosphere. The ability of such systems to renovate and adapt to the various changes instead of maintenance of the biological variety in the certain static state, its degradation and loss is becoming extremely important.

Social constituent is aimed at human development, the preservation of stability of social and cultural systems, as well as the decrease in the number of conflicts in the society. A human being shall become not the object but the subject of the development participating in the processes of his/her vital activity formation, decision-making and implementation of the decisions, in the control over their implementation. To meet such requirements it is important to fairly distribute the wealth between the people, to observe pluralism of thoughts and tolerate human relationships, to preserve cultural capital and its variety, including first of all, the heritage of non-dominant cultures.

Systemic coordination and balance of these three components is an extremely difficult task. In particular, the interconnection of social and ecological constituents causes the necessity to preserve equal rights of present and future generations to use natural resources. The interaction of social and economic constituents requires the achievement of equal and fair distribution of material wealth between people and help provision to the poor. And finally, the correlation of environmental and economic components requires the cost estimation of anthropogenic influences on environment.

In this study a Sustainable Development Gauging Matrix (SDGM) [4] within three abovementioned components is proposed and these processes are globally modeled in terms of quality and security of the human life. With the help of this Matrix the sustainable development processes have been globally modeled for a large group of world countries in terms of quality and security of the human life. The present article is a development of investigations that are presented in [38, 39] and describe the theoretical substantiation and computer modeling of the influence of system global conflicts on the sustainable development of countries and regions of the world in the global context. A distinctive feature of the investigations presented in these works lies in the analysis of linear dependences between values of levels of separate threats and integrated quality and safety indicators of life of people.

Also in this section is analyzed the influence of 12 global threats on the sustainable development at the qualitative level with the use of Bayesian Belief Networks (BBNs) based on the theory of causality [40] with allowance for linear and nonlinear dependences.

In such problems, the use of a BBN that is a graphic model of probabilistic interrelations on a set of variables together with the apparatus of mathematical statistics provides a number of advantages, namely, it makes it possible to reveal causal relationships between different variables and, hence, to facilitate the understanding of complicated phenomena and processes such as sustainable development. Moreover, a BBN possessing both causal and probabilistic semantics is a convenient means for joint representation of expert knowledge determining causal relationships and instrumentally obtained statistical data (measurements, observations, and computations).

# 4.6.1 The Methodology of Sustainable Development Evaluation in Terms of Quality and Security of the Human Life

The important issue in the process of implementation of the concept of sustainable development is the formation of the measurement system (Matrix) for the quantitative and qualitative assessment of this complicated procedure.

The process of sustainable development will be characterized according to two main components: security $( C _ { s l } )$ and quality $( C _ { q l } )$ of the human life (4.19).

Under this concept, the generalized measure (index) of sustainable development can be presented by means of the quaternion $\{ { Q } \}$ :

$$
\{ Q \} = j w _ { s l } C _ { s l } + w _ { q l } \overrightarrow { C _ { q l } } \left( I _ { e } I _ { e c } , I _ { s , } \right) .
$$

The quaternion $\{ \boldsymbol { Q } \}$ includes an imaginary scalar part $j w _ { s l } C _ { s l }$ which describes the security of human life and a real scalar part as a projection of the norm of vector radius $\vec { C } _ { q l }$ to an ideal vector with coordinates (1;1;1) which describes the quality of human life within three dimensions: economic $( I _ { e c } )$ , ecological $( I _ { e } )$ and socio-institutional $( { \cal I } _ { s } )$ . Also we denote $w _ { s l } = 1 / \sqrt { [ 3 ] } 1 2 , w _ { q l } = 1 / \sqrt { 3 }$ . Under this condition $j$ gains a value of a real unit for a normal regular state of society development at $C _ { s l } > 0$ and a value of an imaginary unit when a society enters conflict state $C _ { s l } = 0 \%$ ):

$$
j = \left\{ \begin{array} { l l } { { 1 , } } & { { f o r C _ { s l } > 0 ; } } \\ { { \sqrt { - 1 } , } } & { { f o r C _ { s l } = 0 ( c o n f l i c t ) . } } \end{array} \right.
$$

The security of human life component $\begin{array} { r } { C _ { s l } = I _ { s e c } = \overrightarrow { S _ { j } } = \left( \sum _ { i = 1 } ^ { n } \left( s _ { i } ^ { j } \right) ^ { p } \right) ^ { \frac { 1 } { p } } } \end{array}$ is examined in detail in Sect. 4.2.3 and is represented by the set of threats (Table 4.3) and formula (4.12). Therefore, further on, we will examine in more detail the component of the quality of human life $C q l ( I e c , I e , I s )$ .

Sustainable development estimation methodology in the context of quality of human life. For every country the Euclidean norm of vector radius of human life quality $\left( \vec { C } _ { q l } \right)$ is given in the following form:

$$
\left. \vec { C } _ { q l } \right. = \sqrt { I _ { e c } ^ { 2 } + I _ { e } ^ { 2 } + I _ { s } ^ { 2 } } .
$$

In this case the indicators and policy categories which form the component of the quality of human life $C q l ( I e c , I e , I s )$ are calculated as a weighted total:

$$
I _ { i } = \sum _ { j = 1 } ^ { n } w _ { j } x _ { i , j } , \ i = { \overline { { 1 , m } } } , \sum _ { j = 1 } ^ { n } w _ { j } = 1 ,
$$

where $I _ { i }$ is a value of an indicator or a category of policy for ith country (the number of the countries is $\mathbf { m }$ ), $w _ { j }$ is weight of the jth component of I index (the number of the components is $\mathfrak { n }$ ), $x _ { i , j }$ is a value of the $j$ th component for ith country.

Such representation of integrated indices (indicators and categories of policy) envisages that components of $\mathbf { X _ { i , j } }$ in the formula (4.21) must be non-dimensional and vary within the same range.

Considering the fact that all data, indicators and indices included into the model are measured by virtue of different physical values, may be interpreted differently and change within the different ranges, they were aggregated to the standard form in such a way that all their variations would occur within the range from 0 to 1. To carry out this normalization, the formulas (4.10–4.11) can be used.

This normalization gives the possibility to calculate each of $I _ { e c } , I _ { e } , I _ { s }$ indices and with the help of them the components with appropriate weighting coefficients. Then the quantitative value of human life quality can be identified as projection of the norm of this vector to an ideal vector with coordinates (1; 1; 1), (Fig. 4.22):

$$
C _ { q l } = \sqrt { I _ { e c } ^ { 2 } + I _ { e } ^ { 2 } + I _ { s } ^ { 2 } } \cdot \cos ( \alpha )
$$

The deviation angle $\pmb { \alpha }$ of the vector’s radius $C _ { q l }$ from the ideal vector (1, 1, 1) is estimated on the basis of the values of dimensions $I _ { e c } , I _ { e } , I _ { s }$ in the following way:

![](images/7be226859505c6fbb68e7f021b55bc2165959b131dba76a3af0144494127b649.jpg)  
Fig. 4.22 Human life quality component $( C _ { q l } )$ and harmonization level $( G = \pmb { I } - \pmb { \alpha } )$

$$
\alpha = \operatorname { a r c c o s } { \frac { I _ { e c } + I _ { e } + I _ { s } } { \sqrt { 3 } \cdot { \sqrt { I _ { e c } ^ { 2 } + I _ { e } ^ { 2 } + I _ { s } ^ { 2 } } } } } , 0 \leq \alpha \leq \operatorname { a r c c o s } { \frac { 1 } { \sqrt { 3 } } } .
$$

Thus, the projection of the norm of the vector’s radius $\vec { C } _ { q l }$ to the ideal vector (1, 1, 1) characterizes the human life quality and the attitude position of the vector $\vec { C } _ { q l }$ in the coordinate system $( I _ { e c } , \ I _ { e } , \ I _ { s } )$ characterizes the “harmonization” level of sustainable development. We should mention that when the angle $\textsf { \textsf { Q } }$ approaches 0, the harmonization level of sustainable development increases, i.e. the equidistance of the vector $\vec { C } _ { q l }$ from each of coordinates $( I _ { e c } , I _ { e } , I _ { s } )$ will correspond to the highest harmonization value of sustainable development. If this vector approaches one of these coordinates, this will indicate the priority direction of the corresponding dimension development and neglect of two others. Let the value $G = I - \alpha$ be the harmonization level of sustainable development. It will increase when $G$ approaches 1 and decrease when $G$ approaches 0.

As the researches of human life quality and security are conducted with the help of different methods and sets of initial data, it is worth performing them separately in three stages. At the first stage we will analyze the human life quality as one of the components of sustainable development. At the second stage we will investigate the human life security as another component of sustainable development. And at the third stage we will calculate the aggregate value of the Sustainable Development Index using two components and investigate this index.

In order to conduct the research of the life quality component of sustainable development, it is necessary to sample the data with the help of which each of three dimensions of sustainable development will be characterized in the most appropriate way. These data shall conform to the following important requirements: they have to be formed annually on continuing basis by respected and recognized international organizations.

Thus, the life quality component of sustainable development $C _ { q l }$ and the harmonization level of sustainable development $G = 1 - \alpha$ are calculated on the basis of their constituents $I _ { e c } , I _ { e } , I _ { s }$ . Considering the requirements to initial data mentioned above the value of every dimension $I _ { e c } , I _ { e } , I _ { s }$ will be calculated according to five global indices widely used in the international practice (Table 4.17), being annually formed by the recognized international organizations. Let us consider all of them.

The Economic Dimension Index $( I _ { e c } )$ is formed on the basis of aggregation of two global indices (Table 1.17).

1. The Global Competitiveness Index $( { \cal I } _ { c } )$ was created by the organizers of the World Economic Forum. This index is annually estimated for 139 world economics and published in the form of so-called “Global competitiveness report” (World Economic Forum, www.weforum.org). To reduce the correlation between parts of quality of life we constructed own index based on original one.

Table 4.17 Global indices used for calculation Сql and $\boldsymbol { G } = \boldsymbol { I } - \boldsymbol { \mathsf { a } }$   

<html><body><table><tr><td>Life quality component Cql</td><td>Global index</td><td>Constituents</td><td>Source</td></tr><tr><td rowspan="2">Economic (Iec)</td><td>Ic—Global competitiveness index</td><td>8 policy categories, 21 indicators</td><td>World Economic Forum [www.gcr.weforum.org], WorldBank [http://www.worldbank.org]</td></tr><tr><td>Ief-Economic Freedom Index</td><td>12 indicators</td><td>Heritage Foundation& The Wall Street Journal [www.heritage.org/ index/]</td></tr><tr><td>Ecological (Ie)</td><td>EPI- Environmental Performance Index</td><td>9 policy categories, 14 indicators</td><td>Yale and Columbia universities, USA [www.epi.yale.edu]</td></tr><tr><td>Socio-institutional (Is)</td><td>6 indices</td><td>26 indicators</td><td>World Bank [http://www. Worldbank.org], Transparency International [https://www. transparency.org/ research/cpi/ overview]</td></tr></table></body></html>

It is formed of the following three groups of indicators: 1—the group of indicators of basic requirements (Basic requirements); 2—the group of indicators of the stimulants efficiency (Efficiency stimulants) and 3—the group of indicators of innovation (Innovation).

The first group includes two complex categories of economic policy: Infrastructure and Macroeconomic Environment. The second one consists of five policy categories: market size; the level of financial market development; technological readiness; labor market efficiency; effectiveness of goods and services. The third group involves three indicators: patent apps; technicians in R&D; charges for the use of intellectual property, payments.

2. The Index of Economic Freedom $( I _ { e f } )$ was created by the Heritage Foundation (The Heritage Foundation, www.heritage.org/index/). This index is formed of the following twelve indicators: Property rights; Government integrity; Judicial effectiveness; Government spending; Tax burden; Fiscal heath; Business freedom; Labor freedom; Monetary freedom; Trade freedom; Investment freedom; Financial freedom.

The Ecological Dimension Index $( I _ { e } )$ will be estimated with the help of EPI (Environmental Performance Index (Yale Center for Environmental Low& Policy, www.epi.yale.edu). This index is formed by the Yale Center of Environmental Law and Policy together with Columbia University (USA) for 163 countries of the world.

To calculate this index the aggregation method is used according to which EPI index is formed of two categories of top-level environmental policy (Environmental health, being the sanitary state of environment, and Ecosystem vitality, which is the vital ability of the ecosystem), nine medium-level ecological indicators and 14 low-level indicators.

The presented index and its indicators identify the ability of every country to protect its environment both during a current period of time and also in long-term perspective, on the basis of availability of national environmental system, the ability to resist to environmental impacts and decrease in human dependence on environmental impacts, social and institutional resources of a country to meet the environmental challenges, possibility of global control over the environmental state of the country etc. Moreover, they can be used as a powerful tool for making decisions on the analytical basis including social and economic dimensions of sustainable development of the country.

The Social Dimension index $( { \cal I } _ { s } )$ will be formed of six indices: Health, wellness and basics needs; Education; Personal rights and freedom; Personal safety; Corruption perception; Social Infrastructure. These indices are formed with the help of following indicators: human life cost, leisure and culture of people, economic state of the country, environmental state of the country, human freedom, human health, an infrastructure state, life risks and safety, nation poverty factors, level of unemployment, human health-care activities, gender conditions in the country and other.

Table 4.18 shows the groups of policy categories and indicators used for global modeling of sustainable development processes.

As it is shown in Tables 4.17 and 4.18, life quality component of sustainable development $C _ { q l }$ and its harmonization degree $G = 1 - \alpha$ were determined with the usage of 73 indicators.

On the basis of description of relations between different categories of policy and indicators reduced to common calculating platform, the mathematical SDGM model was developed, the structure of which is presented in Fig. 4.23.

It was taken into account that all data, indicators and indexes included into model (Fig. 4.23) are measured with the help of different physical quantities, may be interpreted differently and change within different ranges. That is why they were normalized for their changes to occur within range from 0 to 1. In this case the worst values of mentioned indicators conform to numeral values close to 1. Such normalization gives the opportunity to calculate every index $I _ { e c } , I _ { e } , \$ $I _ { s }$ and component $C _ { q l }$ through their components with appropriate weight coefficients. In their turn the weight coefficients in the formula of calculation of life quality component of sustainable development $C _ { q l }$ are selected in order to give the possibility to provide equal values of economic, ecological and social dimension in the coordinate system $( I _ { e c } , I _ { e } , I _ { s } )$ .

Therefore, the SDGM model gives the possibility to calculate life quality component of sustainable development $C _ { q l }$ and harmonization degree of this development ${ \pmb G = { \bf 1 } - \pmb \alpha }$ for every country of the world for which data about global indexes and indicators exist (Table 4.18).

# 4.6.2 Some Basic Definitions and Concepts

This investigation is devoted to the determination of causal relations between the mentioned threats (Table 4.3) and indicators of sustainable development (4.12), (4.19–4.22) at a qualitative level. On this basis, a holistic interpretation of processes of sustainable development of countries and regions of the world is developed and also the vulnerability of this development to the influence of the collection of the mentioned threats is estimated.

Let’s introduce some basic definitions and concepts:

1. We consider the collection of global threats (Table 4.3) that exert influence on the sustainable development of countries and regions of the world [39]. Initial quantitative data on indicators of sustainable development, on each of these threats, and also on gross domestic products (GDPs) of countries that will be used for the construction of BBNs are presented in [39]. Since these data vary within different ranges and have different physical dimensions, we will use their normalized values:

Table 4.18 Policy categories and indicators for global modeling of sustainable development processes   

<html><body><table><tr><td>Global</td><td>Stimulants</td><td>Market size (20%)</td><td>Domestic credit to private sector</td></tr><tr><td rowspan="10">competitiveness (50%)</td><td rowspan="10">effciency (50%)</td><td rowspan="4"></td><td>(30%) Import volume index (30%)</td></tr><tr><td>Household final consumption</td></tr><tr><td>expenditure (40%)</td></tr><tr><td>External debt stocks (50%)</td></tr><tr><td rowspan="2">market development (20%) Technological readiness (20%)</td><td>Deposit interest rate (50%)</td></tr><tr><td>Technical cooperation grants (50%)</td></tr><tr><td rowspan="2">Labor market efficiency</td><td>High-technology exports (50%)</td></tr><tr><td>GDP pe r person employed (50%)</td></tr><tr><td rowspan="2">(20%) Effectiveness of goods and</td><td>Employment to population ratio (50%)</td></tr><tr><td>Exports of goods and services</td></tr><tr><td rowspan="4"></td><td rowspan="4"></td><td>(40%) Imports of goods and services</td></tr><tr><td>(40%) Market capitalization of listed</td></tr><tr><td>companies (20%) Foreign direct investment (20%)</td></tr><tr><td rowspan="4">environment (50%)</td><td>Portfolio Investment (40%)</td></tr><tr><td rowspan="3">Infrastructure (50%)</td><td>Total reserves (40%)</td></tr><tr><td>Agriculture (20%)</td></tr><tr><td>Industry (30%)</td></tr><tr><td rowspan="4">Innovations (10%)</td><td rowspan="4"></td><td>GDP per capita (50%)</td></tr><tr><td>Patent apps (30%)</td></tr><tr><td>Technicians in R&D (40%)</td></tr><tr><td>Charges for the use of intellectual property,payments (30%)</td></tr><tr><td rowspan="10">nomic freedom (50%)</td><td rowspan="10">Rule of law (25%)</td><td></td><td>Property rights (8%)</td></tr><tr><td rowspan="3"></td><td>Government integrity (8%)</td></tr><tr><td>Judicial effectiveness (8%)</td></tr><tr><td>Government spending (8%)</td></tr><tr><td rowspan="3">Government size (25%)</td><td></td></tr><tr><td>Tax burden (8%) Fiscal heath (8%)</td></tr><tr><td>Business freedom (8%)</td></tr><tr><td rowspan="3">(25%)</td><td>Labor freedom (8%)</td></tr><tr><td>Monetary freedom (8%)</td></tr><tr><td>Trade freedom (8%)</td></tr><tr><td rowspan="3"></td><td rowspan="3"></td><td>Investment freedom (8%)</td></tr><tr><td>Financial freedom (8%)</td></tr><tr><td>The number of people per doctor</td></tr><tr><td rowspan="2">(20%)</td><td rowspan="2"></td><td rowspan="2"></td><td>(11.1%)</td></tr><tr><td>Hospital beds (11.1%)</td></tr></table></body></html>

(continued)

Table 4.18 (continued)   

<html><body><table><tr><td colspan="3"></td><td>The infant mortality rate (11.1%)</td></tr><tr><td colspan="3" rowspan="6"></td><td>Life expectancy (11.1%)</td></tr><tr><td></td><td>Health expenditure (11.1%)</td></tr><tr><td rowspan="4"></td><td>Prevalence of undernourishment (11.1%)</td></tr><tr><td></td><td>Depth of the food deficit (11.1%)</td></tr><tr><td>Maternal mortality ratio (11.1%)</td><td></td></tr><tr><td></td><td>Mortality rate (11.1%)</td></tr><tr><td rowspan="6">Education (20%)</td><td rowspan="6"></td><td>Literacy rate (20%)</td><td></td></tr><tr><td></td><td>School enrollment (20%)</td></tr><tr><td>School enrollment, secondary (20%)</td><td></td></tr><tr><td></td><td>School enrollment, tertiary (20%)</td></tr><tr><td>Public spending on education</td><td></td></tr><tr><td>(20%) Freedom of speech</td><td></td></tr><tr><td colspan="3">Personal safety (15%)</td><td>Intentional homicides (50%)</td></tr><tr><td colspan="2"></td><td></td><td>Political terror (50%)</td></tr><tr><td colspan="3" rowspan="8">Corruption perception (20%) Social Infrastructure (10%)</td><td></td><td>Mobile cellular subscriptions</td></tr><tr><td rowspan="8"></td><td>(12.5%)</td><td></td></tr><tr><td></td><td>Internet users (12.5%)</td></tr><tr><td rowspan="6"></td><td>Telephones (12.5%)</td></tr><tr><td>Vehicles (12.5%)</td></tr><tr><td>Number of airports (12.5%)</td></tr><tr><td>Navigable waterways (12.5%)</td></tr><tr><td>Paved highways (12.5%)</td></tr><tr><td>Rail lines (12.5%)</td></tr><tr><td>Environmental performance</td><td rowspan="8">Environmental heath (50%)</td><td>Health impacts (33%)</td><td>Environmental risk exposure</td></tr><tr><td rowspan="8"></td><td>Air quality (33%)</td><td>Household air quality (30%)</td></tr><tr><td rowspan="2">Water and sanitation</td><td>Air pollution (70%)</td></tr><tr><td>Unsafe drinking water (50%)</td></tr><tr><td rowspan="2">(33%) Ecosystem Climate and energy (25%) vitality (50%)</td><td>Unsafe sanitation (50%)</td></tr><tr><td>Trend in carbon intensity</td></tr><tr><td rowspan="3">Biodiversity and habitat (25%)</td><td>Species protection (40%)</td></tr><tr><td>Terrestrial biome protection</td></tr><tr><td>(40%)</td></tr><tr><td rowspan="6"></td><td rowspan="6">Fisheries (5%)</td><td></td><td>Marine protected areas (20%)</td></tr><tr><td></td><td>Fish stocks</td></tr><tr><td rowspan="2">Forests (10%) Agriculture (10%)</td><td>Tree cover loss</td></tr><tr><td>Nitrogen balance (50%)</td></tr><tr><td rowspan="2">Water resources (25%)</td><td>Nitrogen use effciency (50%)</td></tr><tr><td>Water treatment</td></tr></table></body></html>

$$
z _ { i , j } = \frac { x _ { i , j } - \overline { { X _ { j } } } } { \sigma \big ( X _ { j } \big ) } ,
$$

where ${ \overline { { X _ { j } } } } = { \frac { \sum _ { i = 1 } ^ { n } x _ { i , j } } { n } }$ is the average value of an indicator of sustainable development, a threat, and a GDP; $\mathfrak { n }$ is the number of rows being analyzed, and

$$
\sigma ( X _ { j } ) = { \sqrt { \sum _ { i = 1 } ^ { n } ( x _ { i , j } - { \overline { { X _ { j } } } } ) ^ { 2 } } }
$$

is the standard deviation of a variable $X _ { j }$

Data normalized in this way have zero mean and unit variance. Data for indicators of sustainable development, global threats, and also $\mathbf { G D P _ { s } }$ for countries of the world in 2016 are taken from [4] and presented in Table 4.19.

2. A Bayesian Belief Networks (BBNs) is a directed acyclic graph in which each vertex is associated with a discrete random quantity $X _ { i } , i = { \overline { { 1 , n } } }$ , assuming values $x _ { i } ^ { j } , j = \overline { { 1 , m _ { i } } }$ and arcs determine causal relations between random quantities. Vertices of this graph are associated with tables of conditional probabilities calculated by the Bayes formula

$$
P ( b | a ) = \frac { P ( a | b ) P ( b ) } { P ( a ) } ,
$$

where $a$ and $b$ are random events, $P ( a )$ and $P ( b )$ are probabilities of occurrences of the events $a$ and $b$ , and $P ( b | a )$ and $P ( a | b )$ are probabilities of occurrence of the event $b$ provided that event $a$ has occurred and, on the contrary, the occurrence of $a$ provided that the event $b$ has occurred.

3. Using the terminology of hypotheses and evidence, we denote by $H$ an event in the case when a given hypothesis is true and by $E$ an event in the case when a definite testimony (evidence) has come that can testify to the mentioned hypothesis. Then formula (4.26) can be rewritten in the form

$$
P ( H | E ) = \frac { P ( E | H ) P ( H ) } { P ( E | H ) P ( H ) + P \big ( E | \overline { { H } } \big ) P \big ( \overline { { H } } \big ) } .
$$

Relationship (4.18) establishes a relation of a hypothesis with evidence and also establishes a relation of the evidence being observed with a hypothesis that is not yet justified. This interpretation also presumes the determination of the a priori probability of the hypothesis $P ( H )$ that is fixed prior to the observation or manifestation of some fact.

The determination of new evidences of the form $E _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j } , i = { \overline { { 1 , n } } } , j = { \overline { { 1 , m _ { i } } } }$ ; in a BBN leads to the assignment of a posteriori probability (4.27) to each hypothesis of the form $H _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j } , i = { \overline { { 1 , n } } } , j = { \overline { { 1 , m _ { i } } } }$ , this probability determines the degree of belief in this hypothesis [41].

4. For the synthesis of a BBN from data on the threats presented above, two problems should be solved. The first problem is connected with the selection of significant variables and definition of causal relations on their set and, as a rule, is solved owing to the involvement of experts in the field of analysis of threats. The second problem lies in the formation of tables of conditional probabilities that are associated with vertices of the graph of the BBN. This problem can be solved on the basis of computation of conditional probabilities from available experimental data on threats. It should be noted that if experimental data on threats are presented in interval scales [42], then they should be digitized, for example, with the use of clusterization by the method of $k$ -means [43]. In essence, the passage from quantitative estimates to qualitative ones is performed at this stage.   
5. If a BBN has been constructed, then, specifying a threshold value for the degree of belief, one can determine the set of confirmed hypotheses for various collections of evidences. Generalizing these data, we obtain a qualitative characteristic of relations between threats $X _ { i } , i = { \overline { { 1 , n } } }$ :

A distinctive feature of the model being considered is that the involvement of insignificant threats and causal relations between them in this model leads to a significant growth in the dimension of the model. For example, to specify tables of conditional probabilities for a model in which dependences on all 12 global threats are determined for each indicator of sustainable development provided that $m _ { i } =$ $3 , i = { \overline { { 1 , n } } }$ ; it is required to use $7 \cdot 3 ^ { 1 2 } = 3 7 2 0 0 8 7$ real numbers. Hence, the number of vertices and arcs of the BBN should be decreased with preserving only essential variables and relations between them. A possible method of overcoming the mentioned “dimensionality” problem is the application of statistical dependency analysis with the use of methods of estimating correlations [44] or calculation of entropy [45]. In particular, correlation analysis makes it possible to obtain an estimate for the linear dependence between variables and to determine parameters of a linear model. The calculation of conditional entropy can also be used as an indication of nonlinear dependences but, in this case, it does not provide any information on the kind of such a dependence.

# 4.6.3 Synthesis of Topologies of BBNs

Let the information entropy of a discrete random quantity $X _ { i } , i = { \overline { { 1 , n } } }$ (a threat, an indicator of sustainable development, and a GDP) that can assume values $x _ { i } ^ { j } , j = \overline { { 1 , m _ { i } } }$ , be computed by the formula

$$
H ( X _ { i } ) = \sum _ { j = 1 } ^ { m _ { i } } P \bigl ( X _ { i } = x _ { i } ^ { j } \bigr ) \log _ { 2 } P \bigl ( X _ { i } = x _ { i } ^ { j } \bigr ) ,
$$

and let it be an averaged quantitative estimate of the indefiniteness (unexpectedness) of occurring events connected with the fact that a variable $X _ { i }$ assumes values $x _ { i } ^ { j }$ . By obviating this indefiniteness, we obtain information, i.e., intrinsic information on a variable $X _ { i }$ [46] is specified by the formula

$$
I ( X _ { i } ) = H ( X _ { i } ) .
$$

Let the upper-bound estimate of intrinsic information [47]

$$
I ( X _ { i } ) \leq I _ { m a x } = \log _ { 2 } m _ { i } , \quad i = \overline { { 1 , n } } ,
$$

be also known (the equality is reached under the condition

$\begin{array} { r } { P \big ( X _ { i } = x _ { i } ^ { j } \big ) = \frac { 1 } { m _ { i } } , i = \overline { { 1 , n } } , j = \overline { { 1 , m _ { i } } } \big ) } \end{array}$ : Then, using relationships (4.28) and (4.29), the measure of the specific informativeness of a variable can be defined as follows:

$$
I _ { s } ( X _ { i } ) = { \frac { I ( X _ { i } ) } { \log _ { 2 } m _ { i } } } .
$$

We represent the results of computations of the value of is by formula (4.30) for a collection of variables from Table 4.14. In particular, the specific informativeness of the variable GDP is equal to $0 . 6 4$ . Accordingly, we have $I s = I . O O _ { \cdot }$ , $I q l = I . O O$ , $S F = I . O O$ , $Q = 0 . 9 9$ , $I G = 0 . 9 9$ , $C P = 0 . 9 8 ,$ , $I e c = 0 . 9 7 ;$ , $G I N I = 0 . 9 7$ , $G D = 0 . 9 5$ , $I e = 0 . 9 5 , N I = 0 . 9 3 , I s e c = 0 . 8 0$ , $C I = 0 . 8 0$ , $B B = 0 . 7 7$ , $N D = 0 . 7 2$ , $W A = 0 . 7 I$ , $E S = 0 . 2 5$ , and $G W = 0 . l 9 .$ . Here, the variables $E S$ (Global decrease in energy security) and ND (vulnerability to natural disasters) can be excluded from consideration since it is poorly informative.

To quantitatively characterize the mutual influence between variables $X _ { i }$ and $X _ { k }$ , $i = \overline { { 1 , n } } , k = \overline { { 1 , n } }$ we will use the concept of mutual information [46]

$$
I ( X _ { i } ; X _ { k } ) = H ( X _ { i } ) - H \big ( X _ { j } | X _ { k } \big ) ,
$$

where $H { \big ( } X _ { j } | X _ { k } { \big ) } = H ( X _ { i } X _ { k } ) - H ( X _ { i } )$ is the conditional entropy calculated with the help of formulas of conditional probabilities and relationship (4.28).

According to [46], mutual information is a statistical function of two random quantities that determines the amount of information contained in one random quantity $X _ { i }$ with respect to another $X _ { k }$ : For mutual information, the following symmetry property is satisfied: $I ( X _ { i } ; X _ { k } ) = I ( X _ { k } ; X _ { i } )$ ; the mutual information of independent variables is equal to zero, i.e., we have $I ( X _ { i } ; X _ { k } ) = H ( X _ { i } ) -$

$H ( X _ { i } | X _ { k } ) = H ( X _ { i } ) - H ( X _ { i } ) = 0$ ; the mutual information of $I ( X _ { i } ; X _ { i } )$ is equal to the intrinsic information of this variable,

$$
I ( X _ { i } ; X _ { i } ) = H ( X _ { i } ) - H ( X _ { i } | X _ { i } ) = H ( X _ { i } ) - 0 = H ( X _ { i } ) = I ( X _ { i } ) .
$$

The upper limit of mutual information is also known,

$$
I \big ( X _ { i } ; X _ { j } \big ) \leq \operatorname* { m i n } \big ( H ( X _ { i } ) , H ( X _ { j } ) \big ) .
$$

Using the formula for mutual information (4.31) and its upper limit (4.32), the specific mutual informativeness for variables $X _ { i }$ and $X _ { k } , i = \overline { { 1 , n } } , k = \overline { { 1 , n } }$ can be found as follows:

$$
I _ { s } ( X _ { i } ; X _ { k } ) = \frac { H ( X _ { i } ) - H ( X _ { i } | X _ { k } ) } { \operatorname* { m i n } \big ( H ( X _ { i } ) , H ( X _ { j } ) \big ) } .
$$

It is obvious that we have $I _ { s } ( X _ { i } ; X _ { i } ) = 1$ : If these variables are independent, then we have $I _ { s } ( X _ { i } ; X _ { k } ) = 0$ :

Based on data of Table 4.19 and using formula (4.33), values of specific mutual informativeness $I s ( X i ; X k )$ were calculated for the GDP level and indicators of sustainable development and threats (Table 4.20).

If a threshold value Ist $( \mathrm { X i } ~ ; \mathrm { X k } )$ is specified (in this case, we have Ist $\mathrm { ( X i \ ; X _ { k } ) \ge 0 . 7 5 }$ , then essential dependences between global threats and indicators of sustainable development can be singled out (in Table 4.20, these indicators are highlighted by a heavy faced type).

As can be seen from Table 4.20, the variables BB, GD, ND, NI, WA, GINI have less influence on the indicators of the sustainable development. The indirect influence of these indicators is defined similarly using the calculation of joint information for the threats.

The BBN topology synthesized in this manner and destined for the conceptual analysis and modeling of the influence of global threats on the sustainable development of countries and regions of the world can be represented by the block diagram depicted in Fig. 4.24.

# 4.6.4 Modelling the Influence of Global Threats on the Sustainable Development of Countries and Regions of the World with the Use of BBNs

We perform the computer modeling of the influence of global threats in several stages.

1. Discretization of Initial Data. We reduce data of Table 4.19 to the following three discretization levels: high (H), average (M), and low (L) since only discrete variables can be used within the framework of a BBN model. We also specify unknown values of variables (U).

1   
Table 4.19 Normalized data for indicators of sustainable development, global threats, and GDPs for countries   

<html><body><table><tr><td rowspan="3"></td><td rowspan="3">Coamnry</td><td>GDP</td><td>Q</td><td>Iql</td><td>Iec</td><td>DutdTorHdreutorsOrSustumaoredeveroprent Ie</td><td>Is</td><td>Isec</td><td>BB</td><td>Datd Torgrobdrtreats CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td>per</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>capita</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12 13</td><td>14</td><td></td><td>15</td><td>16 17</td><td>18</td><td>19</td><td></td><td>20</td></tr><tr><td>1</td><td>Albania</td><td>-0.60</td><td>0.29</td><td>0.32</td><td>0.40</td><td>0.34</td><td>0.10</td><td>0.21</td><td>0.26</td><td>-1.31</td><td>0.36</td><td>0.56</td><td>-0.17</td><td>-0.42</td><td>0.46</td><td>0.68</td><td>0.45</td><td>-0.36</td><td>-1.23</td><td>-0.29</td></tr><tr><td>2</td><td>Algeria</td><td>-0.49</td><td>-0.50</td><td>-0.60</td><td>-1.25</td><td>-0.04</td><td>-0.27</td><td>-0.29</td><td>0.48</td><td>0.70</td><td>0.66</td><td>-0.23</td><td>-0.33</td><td>0.00</td><td>0.19</td><td>-0.80</td><td>-0.65</td><td>0.71</td><td>-0.08</td><td>0.53</td></tr><tr><td>3</td><td>Angola</td><td>-0.49</td><td>-1.43 0.19</td><td>-1.56</td><td>-1.39</td><td>-1.47</td><td>-1.52</td><td>-1.16</td><td>-0.60</td><td>0.70</td><td>1.48</td><td>0.17</td><td>2.05</td><td>-0.32</td><td>1.56</td><td>0.15</td><td>0.24</td><td>2.58</td><td>0.65</td><td>1.07</td></tr><tr><td>4</td><td>Argentina Armenia</td><td>0.11</td><td>0.19</td><td>-0.04</td><td>-1.68</td><td>0.75</td><td>0.24</td><td>0.53</td><td>-1.10</td><td>-0.70</td><td>0.51</td><td>-0.03</td><td>-1.05</td><td>0.11</td><td>-0.50</td><td>-0.64</td><td>0.08</td><td>-0.73</td><td>0.65</td><td>-0.88</td></tr><tr><td>5 6</td><td>Australia</td><td>-0.65 2.47</td><td>1.68</td><td>0.37 1.61</td><td>0.35</td><td>0.89 1.17</td><td>-0.36 1.72</td><td>-0.07 1.63</td><td>0.26</td><td>0.70</td><td>0.72</td><td>0.56</td><td>-0.53</td><td>-0.42</td><td>0.64</td><td>-0.38</td><td>0.40</td><td>-0.78</td><td>-0.92</td><td>0.12</td></tr><tr><td>7</td><td>Austria</td><td>2.03</td><td>1.49</td><td>1.47</td><td>1.71 1.24</td><td>1.17</td><td>1.77</td><td>1.36</td><td>-2.25 0.91</td><td>-1.31</td><td>−1.74</td><td>-1.82</td><td>-0.74</td><td>0.74</td><td>-1.46</td><td>-0.64</td><td>-1.54</td><td>-0.78</td><td>-0.45</td><td>-1.70</td></tr><tr><td>8</td><td>Azerbaijan</td><td>-0.38</td><td>0.01</td><td>0.00</td><td>-0.36</td><td>1.03</td><td>-0.92</td><td>0.04</td><td>0.41</td><td>-1.31 0.70</td><td>-1.59 0.87</td><td>-0.03</td><td>-0.38 -1.00</td><td>-0.21</td><td>−1.14</td><td>-0.80</td><td>-1.75</td><td>-0.78</td><td>-1.07</td><td>-1.56</td></tr><tr><td>9</td><td>Bangladesh</td><td>-0.76</td><td>-1.20</td><td>-1.56</td><td>-1.07</td><td>-1.80</td><td>-1.33</td><td>-0.56</td><td>0.05</td><td>0.70</td><td>1.07</td><td>0.30 0.36</td><td>-0.74</td><td>-0.32</td><td>-0.73</td><td>-0.69</td><td>0.13</td><td>0.39</td><td>-0.92</td><td>0.44</td></tr><tr><td>10</td><td>Barbados</td><td>0.11</td><td>0.42</td><td>0.28</td><td>0.68</td><td>-1.29</td><td>0.84</td><td>0.64</td><td>0.91</td><td>-1.31</td><td>-0.97</td><td>0.56</td><td>-0.48</td><td>-0.21 -0.42</td><td>0.37</td><td>0.99</td><td>0.50</td><td>0.39</td><td>-0.86</td><td>1.07</td></tr><tr><td>11</td><td>Belarus</td><td>-0.38</td><td>0.42</td><td>0.19</td><td>-1.49</td><td>0.94</td><td>0.52</td><td>0.70</td><td>0.34</td><td>-0.70</td><td>0.31</td><td>0.56</td><td>-1.05</td><td></td><td>0.10</td><td>-0.75</td><td>0.13</td><td>-0.78</td><td>-0.08</td><td>-0.84</td></tr><tr><td>12</td><td>Belgium</td><td>1.92</td><td>1.35</td><td>1.24</td><td>0.96</td><td>0.80</td><td>1.49</td><td>1.41</td><td>1.63</td><td>-1.31</td><td>-1.64</td><td>-0.30</td><td>-0.38</td><td>-0.21 -0.21</td><td>-0.95</td><td>-0.69</td><td>-0.39</td><td>-0.78</td><td>-1.44</td><td>0.34</td></tr><tr><td>13</td><td>Belize</td><td>-0.54</td><td>0.01</td><td>-0.09</td><td>-0.74</td><td>0.29</td><td>0.20</td><td>0.21</td><td>-0.31</td><td>-1.31</td><td>0.05</td><td>0.56</td><td>-0.48</td><td>-0.42</td><td>-1.23 0.96</td><td>-0.80 -0.11</td><td>-1.65</td><td>-0.78</td><td>-1.39</td><td>-1.52</td></tr><tr><td>14</td><td>Benin</td><td>-0.82</td><td>-1.01</td><td>-1.20</td><td>-0.45</td><td>-1.75</td><td>-0.78</td><td>-0.62</td><td>0.05</td><td>-1.31</td><td>0.51</td><td>0.56</td><td>1.07</td><td>-0.42</td><td>1.56</td><td>-0.01</td><td>0.34 1.29</td><td>-0.73 1.19</td><td>-0.08 0.76</td><td>-0.06 0.57</td></tr><tr><td>15</td><td>Bhutan</td><td>-0.71</td><td>-0.04</td><td>-0.27</td><td>-0.41</td><td>-0.50</td><td>0.24</td><td>0.32</td><td>-0.31</td><td>-1.31</td><td>-1.18</td><td>0.56</td><td>0.14</td><td>-0.42</td><td>1.05</td><td>-0.59</td><td>0.34</td><td>-0.78</td><td>0.08</td><td>0.53</td></tr><tr><td>16</td><td>Plurinational StateofBolivia</td><td>-0.65</td><td>-0.41</td><td>-0.55</td><td>-1.44</td><td>0.06</td><td>-0.22</td><td>-0.12</td><td>-3.33</td><td>0.70</td><td>0.72</td><td>0.43</td><td>-0.64</td><td>-0.42</td><td>1.19</td><td>1.57</td><td>0.92</td><td>0.12</td><td>1.33</td><td>0.53</td></tr><tr><td>17</td><td>Bosnia and Herzegovina</td><td>-0.54</td><td>-0.41</td><td>-0.41</td><td>-0.64</td><td>-0.68</td><td>0.20</td><td>-0.29</td><td>0.41</td><td>0.04</td><td>0.36</td><td>0.56</td><td>-0.58</td><td>-0.42</td><td>0.92</td><td>1.78</td><td>0.24</td><td>-0.78</td><td>-0.60</td><td>0.34</td></tr><tr><td>18</td><td>Botswana</td><td>-0.38</td><td>0.38</td><td>0.51</td><td>0.91</td><td>0.01</td><td>0.24</td><td>0.15</td><td>-0.17</td><td>-1.31</td><td>-0.92</td><td>0.56</td><td>1.89</td><td>-0.42</td><td>0.23</td><td>-0.69</td><td>0.92</td><td>-0.46</td><td>2.17</td><td>-0.20</td></tr><tr><td>19 20</td><td>Brazil Bulgaria</td><td>-0.16</td><td>0.29</td><td>0.09</td><td>-0.50</td><td>0.71</td><td>0.06 0.52</td><td>0.59</td><td>-1.97</td><td>1.27</td><td>0.31</td><td>-2.69</td><td>-0.48 1.05</td></table></body></html>

Table 4.19 (continued)   

<html><body><table><tr><td rowspan="3"></td><td rowspan="3">Country</td><td colspan="6">Data for indicators of sustainable development</td><td rowspan="2">Data for global threats</td><td colspan="15"></td></tr><tr><td rowspan="2">GDP Q per</td><td rowspan="2">Iql</td><td rowspan="2">Iec</td><td rowspan="2">Ie</td><td rowspan="2">Is</td><td rowspan="2">Isec</td><td rowspan="2">BB</td><td rowspan="2">CI</td><td rowspan="2">CP</td><td rowspan="2">ES</td><td rowspan="2">GD</td><td rowspan="2">GW</td><td rowspan="2">IG</td><td rowspan="2">ND</td><td rowspan="2">NI</td><td rowspan="2">WA</td><td rowspan="2">GINI</td><td rowspan="2">SF</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td><td>capita</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>23</td><td>Cameroon</td><td>-0.76</td><td>-1.29</td><td>-1.29</td><td>-0.97</td><td>-1.15</td><td>-1.42</td><td>-1.11</td><td>-0.31</td><td>0.70</td><td>1.07</td><td>0.56</td><td>1.84</td><td>-0.42</td><td>0.73</td><td>-0.48</td><td>0.92</td><td>1.41</td><td>1.13</td><td>1.34</td></tr><tr><td>24</td><td>Canada Cape verde</td><td>2.08</td><td>1.63 0.10</td><td>1.47 0.19</td><td>1.71</td><td>1.08 −1.42</td><td>1.35 0.98</td><td>1.79 0.04</td><td>-2.40 0.41</td><td>-1.31</td><td>-1.79</td><td>-3.09</td><td>-0.38</td><td>0.95</td><td>-1.41</td><td>-0.75</td><td>-2.17</td><td>-0.78</td><td>-0.65</td><td>-1.65</td></tr><tr><td>25 26</td><td>Central african</td><td>-0.60 -0.82</td><td>-1.39</td><td>-1.75</td><td>0.40 -1.58</td><td>-1.66</td><td>-1.89</td><td>-0.78</td><td>-2.11</td><td>-1.31 1.27</td><td>-0.87 1.38</td><td>0.56 0.56</td><td>-0.33 1.48</td><td>-0.42 -0.42</td><td>1.19 1.69</td><td>-0.48 -0.59</td><td>0.71 0.24</td><td>-0.04 1.89</td><td>1.18 1.96</td><td>0.21 1.71</td></tr><tr><td></td><td>republic</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27</td><td>Chile</td><td>0.17</td><td>0.98</td><td>1.24</td><td>1.43</td><td>0.61</td><td>1.31</td><td>0.26</td><td>0.12</td><td>0.70</td><td>-1.23</td><td>0.03</td><td>-0.74</td><td>-0.21</td><td>-0.09</td><td>0.94</td><td>-0.02</td><td>-0.73</td><td>1.54</td><td>-1.11</td></tr><tr><td>28</td><td>China</td><td>-0.43</td><td>0.05</td><td>-0.09</td><td>0.40</td><td>-0.50</td><td>-0.17</td><td>0.37</td><td>0.77</td><td>0.70</td><td>0.31</td><td>-3.48</td><td>-0.33</td><td>5.48</td><td>-0.63</td><td>2.41</td><td>-0.65</td><td>-0.41</td><td>0.55</td><td>0.39</td></tr><tr><td>29 30</td><td>Colombia Republic of the</td><td>-0.38 -0.65</td><td>0.10 -1.11</td><td>0.37 -1.43</td><td>0.96 -1.63</td><td>0.47 -0.96</td><td>-0.59 -1.52</td><td>-0.34 -0.51</td><td>-0.74 -2.76</td><td>1.27 0.70</td><td>0.46</td><td>-0.10</td><td>-0.94</td><td>-0.21</td><td>-0.50</td><td>0.25</td><td>0.87</td><td>-0.04</td><td>1.75</td><td>0.62</td></tr><tr><td></td><td>Congo</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1.38</td><td>0.50</td><td>1.12</td><td>-0.42</td><td>1.56</td><td>-0.69</td><td>1.03</td><td>1.30</td><td>1.39</td><td>1.12</td></tr><tr><td>31</td><td>Costa Rica</td><td>-0.21</td><td>0.89</td><td>0.92</td><td>0.58</td><td>0.75</td><td>1.12</td><td>0.64</td><td>0.19</td><td>-1.31</td><td>-0.82</td><td>0.56</td><td>-1.41</td><td>-0.42</td><td>0.05</td><td>-0.17</td><td>0.87</td><td>-0.62</td><td>1.33</td><td>-1.02</td></tr><tr><td>32</td><td>Cote dIvoire Croatia</td><td>-0.76</td><td>-1.06</td><td>-1.06</td><td>-0.45</td><td>-0.96</td><td>-1.42</td><td>-0.94</td><td>-0.24</td><td>0.70</td><td>0.66</td><td>0.56</td><td>2.00</td><td>-0.42</td><td>0.60</td><td>-0.80</td><td>1.39</td><td>0.87</td><td>0.71</td><td>1.34</td></tr><tr><td>33</td><td>Cyprus</td><td>0.00 0.77</td><td>0.66 0.66</td><td>0.65 0.83</td><td>-0.50 0.68</td><td>1.17 0.80</td><td>0.70 0.75</td><td>0.59</td><td>0.19</td><td>-0.70</td><td>-0.26</td><td>0.56</td><td>-0.33</td><td>-0.42</td><td>-0.91</td><td>-0.75</td><td>0.08</td><td>-0.73</td><td>-0.81</td><td>-0.70</td></tr><tr><td>34 35</td><td>Czech</td><td>0.44</td><td>1.26</td><td>1.29</td><td>1.34</td><td>1.08</td><td>1.12</td><td>0.26 1.03</td><td>0.84 0.84</td><td>0.04 -1.31</td><td>-0.61 -0.61</td><td>0.56 0.03</td><td>-0.33 -0.33</td><td>-0.42 -0.11</td><td>-0.54 -1.00</td><td>-0.80 0.73</td><td>0.71 -1.07</td><td>-0.78 -0.78</td><td>-0.55 -1.54</td><td>-0.15 -1.15</td></tr><tr><td></td><td>Republic</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>36 37</td><td>Denmark Dominican</td><td>2.30 -0.49</td><td>1.59 -0.46</td><td>1.57 -0.32</td><td>1.43 -0.36</td><td>1.26 0.43</td><td>1.77 -0.82</td><td>1.47 -0.62</td><td>0.41 0.19</td><td>-1.31 0.70</td><td>-2.00 0.82</td><td>-0.17 0.56</td><td>-0.27 -0.74</td><td>-0.32 -0.42</td><td>-1.18 1.05</td><td>-0.80 -0.48</td><td>-1.44 0.34</td><td>-0.78 0.60</td><td>-1.23 1.18</td><td>-1.70 0.16</td></tr><tr><td></td><td>Republic</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.40</td><td>-0.17</td><td>0.70</td><td>0.82</td><td>0.36</td><td>-0.84</td><td>-0.32</td><td>0.00</td><td>-0.54</td><td>0.50</td><td>0.39</td><td>0.97</td><td>0.39</td></tr><tr><td>38 39</td><td>Ecuador Egypt</td><td>-0.49 -0.65</td><td>-0.64 -0.64</td><td>-0.74 -0.87</td><td>-1.39 -0.88</td><td>-0.36 -0.36</td><td>-0.17 -0.87</td></table></body></html>

Table 4.19 (continued)   

<html><body><table><tr><td rowspan="5"></td><td rowspan="5">Country</td><td colspan="5">Data for indicators of sustainable development</td><td rowspan="2">Data for global threats</td><td colspan="9"></td></tr><tr><td>GDP Q</td><td>Iql Iec</td><td>Ie</td><td>Is</td><td>Isec</td><td>BB</td><td>CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND NI</td><td>WA</td><td></td><td>GINI SF</td></tr><tr><td>per</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>capita 2</td><td>3 4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>18</td><td></td><td>20</td></tr><tr><td>43</td><td>Fiji</td><td>-0.60</td><td>-0.09 0.19</td><td>-0.59</td><td>0.43</td><td>0.52</td><td>-0.40</td><td>0.19</td><td>0.04</td><td>0.05</td><td>0.56</td><td>0.04</td><td>-0.42 0.87</td><td>-0.01</td><td>17 -0.29</td><td>-0.41</td><td>19 0.65</td><td>0.44</td></tr><tr><td>44</td><td>Finland</td><td>1.97</td><td>1.59</td><td>1.47</td><td>1.20</td><td>1.31 1.63</td><td>1.63</td><td>-2.18</td><td>-1.31</td><td>-2.00</td><td>0.03</td><td>-0.38</td><td>-0.32</td><td>-1.37</td><td>-0.80</td><td>-1.54</td><td>-0.78</td><td>-1.44 -1.74</td></tr><tr><td>45</td><td>France</td><td>1.70</td><td>1.35</td><td>1.24</td><td>0.82</td><td>1.22 1.35</td><td>1.30</td><td>0.62</td><td>0.70</td><td>-1.33</td><td>-2.49</td><td>-0.38</td><td>0.53</td><td>-1.46</td><td>-0.75</td><td>-1.60</td><td>-0.78 -0.71</td><td>-1.38</td></tr><tr><td>46</td><td>Gambia</td><td>-0.82</td><td>-1.29</td><td>-1.43</td><td>-0.97</td><td>-1.42 -1.42</td><td>-1.00</td><td>-0.02</td><td>0.70</td><td>1.07</td><td>0.56</td><td>0.04</td><td>-0.42</td><td>1.42</td><td>0.89 1.34</td><td>0.07</td><td>-0.08</td><td>0.94</td></tr><tr><td>47</td><td>Georgia</td><td>-0.60</td><td>0.47 0.65</td><td>1.01</td><td></td><td>-0.50 0.89</td><td>0.15</td><td>0.05</td><td>0.70</td><td>-0.77</td><td>0.56</td><td>-0.43</td><td>-0.42</td><td>-1.14</td><td>-0.22 0.29</td><td>-0.78</td><td>0.29</td><td>0.57</td></tr><tr><td>48</td><td>Germany</td><td>1.87</td><td>1.63 1.57</td><td>1.90</td><td>1.03</td><td>1.58</td><td>1.57</td><td>0.91</td><td>0.70</td><td>-1.79</td><td>-2.95</td><td>-0.27</td><td>1.79</td><td>-1.27</td><td>-0.80</td><td>-2.59 -0.78</td><td>-1.13</td><td>-1.52</td></tr><tr><td>49</td><td>Ghana</td><td>-0.71</td><td>-0.46</td><td>-0.64</td><td>-0.03</td><td>-1.01 -0.50</td><td>-0.18</td><td>0.12</td><td>-1.31</td><td>0.10</td><td>0.56</td><td>1.74</td><td>-0.42</td><td>0.64</td><td>-0.64</td><td>0.87 0.23</td><td>-0.08</td><td>0.21</td></tr><tr><td>50</td><td>Greece</td><td>0.55</td><td>0.38</td><td>0.42</td><td>-1.07</td><td>1.12 0.61</td><td>0.32</td><td>0.77</td><td>0.70</td><td>0.05</td><td>-0.17</td><td>-0.64</td><td>-0.21</td><td>-0.59</td><td>-0.64</td><td>-0.49 -0.78</td><td>-0.24</td><td>-0.52</td></tr><tr><td>51</td><td>Guatemala</td><td>-0.65</td><td>-0.64</td><td>-0.46</td><td>-0.22</td><td>-0.08 -0.73</td><td>-0.78</td><td>0.12</td><td>0.70</td><td>0.97</td><td>0.56</td><td>-1.15</td><td>-0.42</td><td>1.10</td><td>2.26 1.29</td><td>-0.14</td><td>1.33</td><td>0.75</td></tr><tr><td>52</td><td>Guinea</td><td>-0.82</td><td>-1.15</td><td>-1.33</td><td>-1.07</td><td>-1.24 -1.19</td><td>-0.78</td><td>-0.31</td><td>0.70</td><td>1.02</td><td>0.56</td><td>1.02</td><td>-0.42</td><td>1.56</td><td>-0.69 0.34</td><td>1.30</td><td>-0.65</td><td>1.53</td></tr><tr><td>53</td><td>Guyana</td><td>-0.60</td><td>-0.13</td><td>-0.69</td><td>-0.97</td><td>0.06 -0.87</td><td>0.64</td><td>-3.91</td><td>-1.31</td><td>0.66</td><td>0.56</td><td>0.40</td><td>-0.42</td><td>0.92</td><td>-0.11 0.40</td><td>-0.62</td><td>-0.08</td><td>0.16</td></tr><tr><td>54</td><td>Honduras</td><td>-0.71</td><td>-0.78</td><td>-0.78</td><td>-0.74</td><td>-0.08 -1.29</td><td>-0.62</td><td>-0.10</td><td>0.70</td><td>0.87</td><td>0.56</td><td>-1.46</td><td>-0.42</td><td>1.47</td><td>1.57 0.76</td><td>-0.04</td><td>1.54</td><td>0.62</td></tr><tr><td>55</td><td>Hungary</td><td>0.00</td><td>0.70</td><td>0.74</td><td>0.54</td><td>1.08 0.29</td><td>0.59</td><td>0.19</td><td>0.04</td><td>-0.21</td><td>0.36</td><td>-0.27</td><td>-0.32</td><td>-0.73</td><td>-0.69</td><td>-0.65 -0.78</td><td>-1.07</td><td>-0.70</td></tr><tr><td>56</td><td>Iceland</td><td>1.92</td><td>1.45</td><td>1.43</td><td>1.24</td><td>1.31 1.35</td><td>1.36</td><td>-0.31</td><td>-1.31</td><td>-1.69</td><td>0.56</td><td>-0.38</td><td>-0.42</td><td>-0.54</td><td>-0.80</td><td>-1.07 -0.78</td><td>-1.49</td><td>-1.65</td></tr><tr><td>57</td><td>India</td><td>-0.76</td><td>-0.55</td><td>-0.83</td><td>-0.22</td><td>-1.33 -0.45</td><td>-0.07</td><td>0.12</td><td>1.27</td><td>0.31</td><td>-2.95</td><td>2.05</td><td>4.32</td><td>-0.18</td><td>0.04 1.60</td><td>-0.30</td><td>-0.45</td><td>0.62</td></tr><tr><td>58</td><td>Indonesia</td><td>-0.65</td><td>-0.55</td><td>-0.46</td><td>-0.22</td><td>-0.45 -0.36</td><td>-0.56</td><td>-0.02</td><td>0.70</td><td>0.46</td><td>-0.70</td><td>0.66</td><td>1.05</td><td>0.32</td><td>-0.59 0.08</td><td>0.34</td><td>0.18</td><td>0.39</td></tr><tr><td>59</td><td>Iran</td><td>-0.54</td><td>-0.55</td><td>-0.87</td><td>-1.63</td><td>-0.41 -0.41</td><td>-0.07</td><td>0.62</td><td>0.70</td><td>0.92</td><td>-1.49</td><td>-0.89</td><td>1.37</td><td>-0.18</td><td>-0.59 0.61</td><td>-0.46</td><td>-0.13</td><td>0.94</td></tr><tr><td>60</td><td>Ireland</td><td>2.03</td><td>1.45</td><td>1.43</td><td>1.62</td><td>1.17 1.26</td><td>1.30</td><td>0.26</td><td>-1.31</td><td>-1.48</td><td>0.30</td><td>-0.27</td><td>-0.32</td><td>-1.23</td><td>-0.80 -1.33</td><td>-0.62</td><td>-0.81</td><td>-1.70</td></tr><tr><td>61</td><td>Israel</td><td>1.43</td><td>0.80</td><td>0.83</td><td>1.10</td><td>0.66 0.38</td><td>0.59</td><td>1.56</td><td>0.70</td><td>-1.13</td><td>0.36</td><td>-0.27</td><td>-0.21</td><td>-1.18</td><td>1.15 -2.33</td><td>-0.78</td><td>0.65</td><td>0.62</td></tr><tr><td>62 63</td><td>Italy Jamaica</td><td>1.37 -0.54</td><td>1.12 0.01</td><td>0.97 0.32</td><td>0.49 0.44</td><td>1.03 1.03 0.57 -0.17</td><td>1.25 -0.51</td><td>0.98 0.41</td><td>-1.31 0.70</td><td>-0.15 0.36</td><td>-2.09 0.56</td><td>-0.64 -0.38</td><td>0.63 -0.42 0.46</td><td>-1.05</td><td>-0.80 -1.91 0.83 0.29</td><td>-0.78 -0.25</td><td>-0.45</td><td>-1.06 -0.11</td></tr></table></body></html>

√   
Table 4.19 (continued)   

<html><body><table><tr><td></td><td>Country</td><td colspan="7">Data for indicators of sustainable development</td><td colspan="10">Data for global threats</td></tr><tr><td></td><td></td><td>GDP</td><td>Q</td><td>Iql</td><td>Iec</td><td>Ie</td><td>Is</td><td>Isec</td><td>BB CI</td><td>CP</td><td>ES</td><td>GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td></td><td></td><td>per capita</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td>2</td><td>3</td><td>4</td><td></td><td></td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>67</td><td>Kenya</td><td>-0.76</td><td>-1.11</td><td>-0.92</td><td>-0.69</td><td>-0.73</td><td>-0.78</td><td>-1.27 0.05</td><td>0.70</td><td>1.07</td><td>0.56</td><td>1.89</td><td>-0.42</td><td>0.05</td><td>1.57</td><td>0.87</td><td>2.15</td><td>-0.08</td><td>1.34</td></tr><tr><td>68</td><td>Republic of</td><td>0.83</td><td>1.31</td><td>1.20</td><td>1.67</td><td>0.01</td><td>1.26</td><td>1.36</td><td>1.49</td><td>-1.31 -0.51</td><td>-1.10</td><td>-0.43</td><td>1.37</td><td>-1.46</td><td>-0.80</td><td>-2.59</td><td>-0.57</td><td>-0.08</td><td>-1.34</td></tr><tr><td>69</td><td>Korea Kyrgyzstan</td><td>-0.76</td><td>-0.27</td><td>-0.32</td><td>-0.41</td><td>0.24</td><td>-0.50</td><td>-0.18</td><td>0.12 0.70</td><td>0.97</td><td>0.56</td><td>-1.05</td><td>-0.42</td><td>0.73</td><td>-0.11</td><td>1.24</td><td>0.12</td><td>-1.49</td><td>0.66</td></tr><tr><td>70</td><td>Laos</td><td>-0.76</td><td>-1.15</td><td>-1.43</td><td>-1.16</td><td>-1.52</td><td>-1.15</td><td>-0.62</td><td>-0.17</td><td>-0.70 0.87</td><td>0.56</td><td>-0.27</td><td>-0.42</td><td>0.78</td><td>1.31</td><td>-0.18</td><td>1.35</td><td>-0.03</td><td>0.80</td></tr><tr><td>71</td><td>Latvia</td><td>0.17</td><td>1.03</td><td>1.01</td><td>0.91</td><td>1.12</td><td>0.61</td><td>0.86</td><td>-1.10</td><td>-0.70 -0.77</td><td>0.56</td><td>-0.48</td><td>-0.42</td><td>-1.14</td><td>-0.80</td><td>-0.39</td><td>-0.73</td><td>-0.39</td><td>-0.93</td></tr><tr><td>72</td><td>Lebanon</td><td>-0.21</td><td>-0.46</td><td>-0.32</td><td>-0.50</td><td>-0.13</td><td>-0.13</td><td>-0.56</td><td>0.70</td><td>0.97</td><td>0.56</td><td>-0.79</td><td>-0.42</td><td>0.64</td><td>1.94</td><td>0.08</td><td>-0.73</td><td>-0.08</td><td>1.03</td></tr><tr><td>73</td><td>Lesotho</td><td>-0.76</td><td>-1.20</td><td>-1.47</td><td>-1.39</td><td>-1.61</td><td>-0.82</td><td>0.91 -0.78 0.12</td><td>-1.31</td><td>0.36</td><td>0.56</td><td>2.05</td><td>-0.42</td><td>1.42</td><td>0.78</td><td>1.08</td><td>0.87</td><td>1.81</td><td>0.66</td></tr><tr><td>74</td><td>Lithuania</td><td>0.17</td><td>1.12</td><td>1.20</td><td>1.24</td><td>1.08</td><td>0.89</td><td>0.75</td><td>-0.02 -1.31</td><td>-0.87</td><td>0.50</td><td>-0.02</td><td>-0.42</td><td>-0.68</td><td>-0.80</td><td>-0.02</td><td>-0.52</td><td>-0.45</td><td>−1.11</td></tr><tr><td>75</td><td>Luxembourg</td><td>2.80</td><td>1.35</td><td>1.34</td><td>1.24</td><td>1.17</td><td>1.21</td><td>1.25</td><td></td><td>-1.31 -1.79</td><td>0.56</td><td>-0.43</td><td>-0.42</td><td>−1.14</td><td>-0.80</td><td>-0.65</td><td>-0.78</td><td>-0.50</td><td>-1.65</td></tr><tr><td>76</td><td>Macedonia, the former Republicof</td><td>-0.54</td><td>0.15</td><td>0.32</td><td>0.44</td><td>0.61</td><td>-0.22</td><td>-0.12</td><td>0.70</td><td>0.46</td><td>0.56</td><td>-1.31</td><td>-0.42</td><td>-0.50</td><td>1.62</td><td>0.34</td><td>-0.73</td><td>0.81</td><td>-0.02</td></tr><tr><td>77</td><td>Yugoslav Madagascar</td><td>-0.82</td><td>-1.11</td><td>-1.29</td><td>-0.36</td><td>-1.89</td><td>-1.05</td><td>-0.73</td><td>-0.67</td><td>-1.31 1.07</td><td>0.56</td><td>0.71</td><td>-0.42</td><td>1.47</td><td>0.73</td><td>1.18</td><td>2.53</td><td>0.65</td><td>0.80</td></tr><tr><td>78</td><td>Malawi</td><td>-0.82</td><td>−1.11</td><td>-1.33</td><td>-1.25</td><td>-1.52</td><td>-0.68</td><td>-0.73</td><td>-0.02</td><td>-1.31 0.82</td><td>0.56</td><td>1.95</td><td>-0.42</td><td>1.60</td><td>1.73</td><td>0.71</td><td>0.07</td><td>1.07</td><td>0.94</td></tr><tr><td>79</td><td>Malaysia</td><td>-0.16</td><td>0.61</td><td>0.74</td><td>1.15</td><td>0.34</td><td>0.38</td><td>0.37</td><td>0.04</td><td>-0.26</td><td>-0.10</td><td>-0.43</td><td>0.32</td><td>-1.32</td><td>0.78</td><td>-1.33</td><td>-0.62</td><td>1.07</td><td>-0.06</td></tr><tr><td>80</td><td>Mali</td><td>-0.82</td><td>-1.34</td><td>-1.52</td><td>-0.78</td><td>-1.80</td><td>-1.42</td><td>-1.05 -0.17</td><td>0.70</td><td>0.77</td><td>0.56</td><td>1.43</td><td>-0.42</td><td>1.56</td><td>0.73</td><td>0.66</td><td>1.25</td><td>-0.71</td><td>1.25</td></tr><tr><td>81</td><td>Malta</td><td>0.61</td><td>0.98</td><td>1.01</td><td>0.54</td><td>1.22</td><td>0.89 0.75</td><td>1.13</td><td>-1.31</td><td>-0.61</td><td>0.56</td><td>-0.22</td><td>-0.42</td><td>-0.45</td><td>-0.80</td><td>-0.39</td><td>-0.78</td><td>-0.08</td><td>-1.20</td></tr><tr><td>82</td><td>Mauritius</td><td>-0.27</td><td>0.84</td><td>0.78</td><td>1.15</td><td>0.01</td><td>0.75 0.86</td><td>0.77</td><td>-1.31</td><td>-0.56</td><td>0.56</td><td>-0.53</td><td>-0.42</td><td>-1.14</td><td>-0.80</td><td>0.13</td><td>-0.78</td><td>-0.34</td><td>-1.06</td></tr><tr><td>83</td><td>Mexico</td><td>-0.21</td><td>-1.15</td><td>0.00</td><td>0.54</td><td>0.29</td><td>-1.01</td><td>-2.64 0.34</td><td>1.62</td><td>0.87</td><td>-1.03</td><td>-0.84</td><td>1.05</td><td>-0.68</td><td>-0.27</td><td>-0.76</td><td>-0.46</td><td>1.28</td><td>0.16</td></tr><tr><td>84</td><td>Moldova</td><td>-0.71</td><td>-0.09</td><td>-0.04</td><td>-0.88</td><td>0.52</td><td>0.15</td><td>-0.12 0.12</td><td>0.70</td><td>0.87</td><td>0.56</td><td>-0.33</td><td>-0.42</td><td>-0.13</td><td>-0.54</td><td>1.08</td><td>0.23</td><td>-1.49</td><td>0.30</td></tr><tr><td>85</td><td>Mongolia</td><td>-0.60 -0.38</td><td>-0.18 0.56</td><td>-0.55</td><td>-0.55</td><td>-0.54</td><td>-0.22 0.75</td><td>0.37</td><td>-2.47 -1.31</td><td>0.41</td><td>0.50</td><td>-0.58</td><td>-0.32</td><td>0.73</td><td>-0.01</td><td>1.08</td><td>2.10</td><td>-0.86</td><td>-0.52 -0.56</td></tr><tr><td>86</td></table></body></html>

√   
Table 4.19 (continued)   

<html><body><table><tr><td rowspan="5"></td><td rowspan="5">Country</td><td colspan="7">Data for indicators of sustainable development</td><td colspan="9">Data for global threats</td></tr><tr><td>GDP Q</td><td>Iql</td><td>Iec Ie</td><td>Is</td><td></td><td>Isec BB</td><td>CI</td><td>CP</td><td></td><td>ES GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td></td><td>GINI SF</td></tr><tr><td>per capita</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>17</td><td>18</td><td></td><td>20</td></tr><tr><td>87</td><td>Morocco</td><td>-0.65</td><td>-0.27 -0.14</td><td>-0.22</td><td>0.34</td><td>-0.27</td><td>-0.45</td><td>0.19</td><td>0.70</td><td>0.46 0.56</td><td></td><td>-0.48 -0.32</td><td>-0.27</td><td>16 -0.69</td><td>0.92</td><td>0.55</td><td>19 0.34</td><td>0.34</td></tr><tr><td>88</td><td>Mozambique</td><td>-0.82</td><td>-1.52</td><td>-1.56</td><td>-1.16</td><td>-1.80 -1.29</td><td>-1.33</td><td>-0.46</td><td>0.70</td><td>1.02</td><td>0.56</td><td>2.36</td><td>-0.42</td><td>1.37</td><td>0.20</td><td>1.18</td><td>2.53</td><td>1.02</td><td>0.94</td></tr><tr><td>89</td><td>Namibia</td><td>-0.49</td><td>-0.23</td><td>-0.14</td><td>-0.22</td><td>0.01 -0.04</td><td>-0.23</td><td>-1.61</td><td>-1.31</td><td>-0.46</td><td>0.56</td><td>1.58</td><td>-0.42</td><td>1.33</td><td>2.26</td><td>0.71</td><td>0.02</td><td>2.17</td><td>0.21</td></tr><tr><td>90</td><td>Nepal</td><td>-0.82</td><td>-1.15</td><td>-1.43</td><td>-1.21</td><td>-1.52</td><td>-0.96</td><td>-0.67 0.05</td><td>0.70</td><td>0.92</td><td>0.56</td><td>-0.22</td><td>-0.42</td><td>0.69</td><td>2.26</td><td>0.40</td><td>-0.04</td><td>-0.76</td><td>1.07</td></tr><tr><td>91</td><td>Netherlands</td><td>2.03</td><td>1.54</td><td>1.43</td><td>1.67</td><td>0.89 1.45</td><td>1.52</td><td>1.34</td><td>-1.31</td><td>-1.84</td><td>-0.23</td><td>-0.33</td><td>0.11</td><td>-1.41</td><td>-0.80</td><td>-2.23</td><td>-0.78</td><td>-1.34</td><td>-1.56</td></tr><tr><td>92</td><td>New Zealand</td><td>1.70</td><td>1.54</td><td>1.52</td><td>1.62</td><td>1.22 1.49</td><td>1.36</td><td></td><td>-1.75 -1.31</td><td>-2.00</td><td>0.23</td><td>-0.38</td><td>-0.32</td><td>-1.32</td><td>0.20</td><td>-0.70</td><td>-0.78</td><td>-0.08</td><td>-1.70</td></tr><tr><td>93</td><td>Nicaragua</td><td>-0.71</td><td>-0.87</td><td>-0.83</td><td>-0.55</td><td>-0.59</td><td>-0.87</td><td>-0.84</td><td>-0.38 0.70</td><td>1.07</td><td>0.56</td><td>-0.79</td><td>-0.42</td><td>1.33</td><td>1.36</td><td>0.66</td><td>0.39</td><td>1.18</td><td>0.57</td></tr><tr><td>94</td><td>Niger</td><td>-0.82</td><td>-1.39</td><td>-1.52</td><td>-1.02</td><td>-1.89</td><td>-1.15</td><td>-1.11</td><td>-0.02 0.70</td><td>0.56</td><td>0.56</td><td>1.12</td><td>-0.42</td><td>1.51</td><td>1.68</td><td>0.13</td><td>2.37</td><td>-0.60</td><td>1.34</td></tr><tr><td>95</td><td>Nigeria</td><td>-0.65</td><td>-1.80</td><td>-1.10</td><td>-0.55</td><td>-1.05</td><td>-1.33</td><td>-2.64 0.05</td><td>1.62</td><td>0.97</td><td></td><td>-0.17 2.51</td><td>-0.21</td><td>0.14</td><td>-0.27</td><td>1.29</td><td>1.89</td><td>0.65</td><td>1.48</td></tr><tr><td>96</td><td>Norway</td><td>2.74</td><td>1.54</td><td>1.43</td><td>1.10</td><td>1.17</td><td>1.68</td><td>1.57</td><td>-0.81</td><td>-1.31</td><td>-1.89</td><td>-1.16 -0.33</td><td>-0.32</td><td>-1.46</td><td>-0.80</td><td>-0.97</td><td>-0.78</td><td>-1.60</td><td>-1.70</td></tr><tr><td>97</td><td>Oman</td><td>0.55</td><td>0.42</td><td>0.32</td><td>0.63</td><td>-0.92</td><td>0.84</td><td>0.53 1.13</td><td></td><td>-0.70</td><td>-0.05 0.17</td><td>-0.74</td><td>-0.32</td><td>-1.27</td><td>-0.80</td><td>-0.13</td><td>-0.20</td><td>-0.08</td><td>-0.75</td></tr><tr><td>98</td><td>Pakistan</td><td>-0.76</td><td>-1.20</td><td>-1.43</td><td>-0.88</td><td>-1.47</td><td>-1.56</td><td>-0.84 0.05</td><td>1.27</td><td>0.77</td><td>0.03</td><td>0.86</td><td>0.00</td><td>0.60</td><td>1.05</td><td>1.13</td><td>-0.04</td><td>-1.02</td><td>1.43</td></tr><tr><td>99</td><td>Panama</td><td>-0.16</td><td>0.33</td><td>0.32</td><td>0.30</td><td>0.61</td><td>-0.08</td><td>0.32</td><td>-0.17</td><td>-1.31 0.41</td><td>0.56</td><td>-0.79</td><td>-0.42</td><td>-0.13</td><td>-0.64</td><td>0.87</td><td>-0.36</td><td>1.54</td><td>-0.65</td></tr><tr><td>100</td><td>Paraguay</td><td>-0.60</td><td>-0.18</td><td>-0.09</td><td>-0.17</td><td>-0.04</td><td>0.06</td><td>-0.18</td><td>-2.40 0.70</td><td>0.87</td><td>0.56</td><td>-0.84</td><td>-0.42</td><td>0.64</td><td>1.89</td><td>0.82</td><td>-0.62</td><td>1.65</td><td>0.25</td></tr><tr><td>101</td><td>Peru</td><td>-0.43</td><td>0.01</td><td>0.37</td><td>0.68</td><td>0.20</td><td>0.06</td><td>-0.51</td><td>-0.60 0.70</td><td>0.56</td><td>0.30</td><td>-0.79</td><td>-0.32</td><td>0.37</td><td>0.25</td><td>0.08</td><td>0.39</td><td>0.81</td><td>0.25</td></tr><tr><td>102</td><td>Philippines</td><td>-0.65</td><td>-0.46</td><td>-0.18</td><td>0.16</td><td>0.29</td><td>-0.87</td><td>-0.73 0.05</td><td>1.27</td><td>0.56</td><td>0.17</td><td>0.14</td><td>-0.11</td><td>-0.32</td><td>2.73</td><td>-0.08</td><td>-0.09</td><td>0.71</td><td>0.84</td></tr><tr><td>103</td><td>Poland</td><td>0.00</td><td>1.12</td><td>1.11</td><td>0.96</td><td>0.84</td><td>1.12</td><td>0.97 0.62</td><td>-1.31</td><td>-1.02</td><td></td><td>-0.23 -0.27</td><td>0.42</td><td>-0.95</td><td>-0.80</td><td>-0.49</td><td>-0.62</td><td>-0.86</td><td>-1.15</td></tr><tr><td>104</td><td>Portugal</td><td>0.55</td><td>1.07</td><td>1.06</td><td>0.40</td><td>1.26</td><td>1.12 0.97</td><td>0.70</td><td>-1.31</td><td>-1.02</td><td>-0.17</td><td>-0.12</td><td>-0.32</td><td>-0.68</td><td>-0.80</td><td>-0.49</td><td>-0.78</td><td>-0.29</td><td>-1.52</td></tr><tr><td>105</td><td>Romania</td><td>-0.27 0.11</td><td>0.75 0.10</td><td>0.74</td><td>0.40 -1.02</td><td>0.98 0.98</td><td>0.52 0.64 -0.78 0.48</td><td></td><td>-0.17 -0.70 -0.53 0.70</td><td>-0.21 0.92</td><td>-0.17 -3.15</td><td>0.35 -0.27</td><td>-0.21 4.00</td><td>-0.77 -1.27</td><td>-0.80 -0.75</td><td>0.55 1.97</td><td>-0.78 -0.52</td><td>-1.44 0.50</td><td>-0.65 0.66</td></tr><tr><td>106</td><td>Russian Federation</td><td></td><td></td><td>-0.18</td></table></body></html>

1   
Table 4.19 (continued)   

<html><body><table><tr><td rowspan="4"></td><td rowspan="4">Country</td><td colspan="7">Data for indicators of sustainable development</td><td colspan="9">Data for global threats</td></tr><tr><td>GDP Q</td><td>Iql</td><td>Iec Ie</td><td></td><td>Is</td><td>Isec</td><td>BB CI</td><td>CP</td><td></td><td>ES GD</td><td>GW</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>GINI</td><td>SF</td></tr><tr><td></td><td>per capita</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7 8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18 19</td><td></td><td>20</td></tr><tr><td>110</td><td>Serbia</td><td>-0.43</td><td>0.29</td><td>0.42</td><td>-0.22</td><td>0.66 0.66</td><td>0.04</td><td>0.41</td><td>0.70</td><td>0.15</td><td>0.50</td><td>-0.12</td><td>-0.32</td><td>0.10</td><td>1.73</td><td>-1.07</td><td>-0.73</td><td>-1.23</td><td>0.25</td></tr><tr><td>111</td><td>Seychelles</td><td>0.17</td><td>0.05</td><td>-0.09</td><td>-0.17</td><td>-0.50</td><td>0.47</td><td>0.21</td><td>-0.31</td><td>-1.31 -0.61</td><td>0.56</td><td>-0.43</td><td>-0.42</td><td>0.83</td><td>0.89</td><td>-0.60</td><td>-0.41</td><td>1.18</td><td>-0.34</td></tr><tr><td>112</td><td>Sierra leone</td><td>-0.82</td><td>-1.25</td><td>-1.52</td><td>-1.21</td><td>-1.66</td><td>-1.15</td><td>-0.78</td><td>-0.10 0.70</td><td>0.87</td><td>0.56</td><td>0.91</td><td>-0.42</td><td>1.05</td><td>-0.69</td><td>0.50</td><td>2.15</td><td>-0.60</td><td>1.07</td></tr><tr><td>113</td><td>Singapore</td><td>2.19</td><td>1.54</td><td>1.52</td><td>1.90</td><td>1.17</td><td>1.26</td><td>1.36</td><td>1.85</td><td>-0.70</td><td>-1.89 0.50</td><td>0.09</td><td>-0.32</td><td>-1.55</td><td>-0.80</td><td>-2.44</td><td>-0.78</td><td>-0.08</td><td>-1.43</td></tr><tr><td>114</td><td>Slovakia</td><td>0.33</td><td>0.94</td><td>0.92</td><td>0.58</td><td>1.08</td><td>0.70</td><td>0.86</td><td>0.48</td><td>-1.31</td><td>-0.41 0.36</td><td>-0.38</td><td>-0.32</td><td>-0.18</td><td>-0.80</td><td>-0.08</td><td>-0.78</td><td>-1.54</td><td>-1.02</td></tr><tr><td>115</td><td>Slovenia</td><td>0.66</td><td>1.03</td><td>0.97</td><td>-0.12</td><td>1.26</td><td>1.26</td><td>0.97</td><td>0.70</td><td>-0.70</td><td>-0.97 0.56</td><td>-0.43</td><td>-0.42</td><td>-0.18</td><td>-0.22</td><td>-1.12</td><td>-0.73</td><td>-1.60</td><td>-1.38</td></tr><tr><td>116</td><td>South Africa</td><td>-0.43</td><td>-0.50</td><td>-0.37</td><td>-0.17</td><td>0.01</td><td>-0.68</td><td>-0.56</td><td>0.62</td><td>0.70</td><td>-0.05</td><td>-0.37 2.51</td><td>0.95</td><td>-0.22</td><td>-0.59</td><td>0.40</td><td>-0.20</td><td>2.28</td><td>0.12</td></tr><tr><td>117</td><td>Spain</td><td>1.04</td><td>1.31</td><td>1.34</td><td>1.15</td><td>1.26</td><td>1.26</td><td>1.14</td><td>0.70</td><td>0.70</td><td>-0.82</td><td>-2.49 -0.58</td><td>0.32</td><td>-1.27</td><td>-0.80</td><td>-1.18</td><td>-0.78</td><td>-0.34</td><td>-1.20</td></tr><tr><td>118</td><td>Sri Lanka</td><td>-0.65</td><td>-0.64</td><td>-0.60</td><td>-0.50</td><td>-0.45</td><td>-0.45</td><td>-0.56</td><td>0.19</td><td>0.70 0.51</td><td>0.56</td><td>-0.79</td><td>-0.42</td><td>0.37</td><td>2.47</td><td>0.40</td><td>-0.41</td><td>0.13</td><td>0.94</td></tr><tr><td>119</td><td>Swaziland</td><td>-0.65</td><td>-1.06</td><td>-0.92</td><td>-0.55</td><td>-0.87</td><td>-0.82</td><td>-1.11</td><td>0.26</td><td>0.70 0.10</td><td></td><td>0.56 2.00</td><td>-0.42</td><td>1.51</td><td>-0.32</td><td>0.45</td><td>1.51</td><td>1.60</td><td>0.94</td></tr><tr><td>120</td><td>Sweden</td><td>2.30</td><td>1.54</td><td>1.43</td><td>1.29</td><td>1.31</td><td>1.40</td><td>1.52</td><td>-1.39</td><td>0.70</td><td>-2.00</td><td>-0.90</td><td>-0.33 -0.32</td><td>-1.37</td><td>-0.80</td><td>-1.91</td><td>-0.78</td><td>-1.44</td><td>-1.70</td></tr><tr><td>121</td><td>Switzerland</td><td>2.69</td><td>1.63</td><td>1.61</td><td>1.90</td><td>1.17</td><td>1.58</td><td>1.47</td><td>1.20</td><td>-1.31</td><td>-1.94</td><td>0.10</td><td>-0.38 -0.32</td><td>-1.37</td><td>-0.80</td><td>-1.49</td><td>-0.78</td><td>-0.92</td><td>−1.70</td></tr><tr><td>122</td><td>Syria</td><td>0.11</td><td>-1.76</td><td>-1.06</td><td>-1.21</td><td>-0.36</td><td>-1.47</td><td>-2.64</td><td>0.19</td><td>1.62 1.69</td><td>0.50</td><td>-1.87</td><td>-0.32</td><td>1.19</td><td>-0.59</td><td>-0.13</td><td>0.07</td><td>-0.08</td><td>1.71</td></tr><tr><td>123</td><td>Tajikistan</td><td>-0.76</td><td>-0.60</td><td>-0.64</td><td>-1.25</td><td>0.24</td><td>-0.68</td><td>-0.45</td><td>0.05 0.70</td><td>1.12</td><td>0.56</td><td>-1.00</td><td>-0.42</td><td>0.64</td><td>-0.11</td><td>0.76</td><td>1.51</td><td>-1.02</td><td>0.80</td></tr><tr><td>124</td><td>United Republic of</td><td>-0.76</td><td>-1.06</td><td>-0.92</td><td>-0.55</td><td>-1.05</td><td>-0.68</td><td>-1.05</td><td>-0.02 0.70</td><td>0.77</td><td>0.56</td><td>1.53</td><td>-0.42</td><td>1.10</td><td>-0.38</td><td>1.39</td><td>2.42</td><td>-0.08</td><td>0.71</td></tr><tr><td>125</td><td>Tanzania Thailand</td><td>-0.49</td><td>-0.09</td><td>-0.09</td><td>0.49</td><td>-0.08</td><td>-0.59</td><td>-0.12</td><td>0.34</td><td>0.04</td><td>0.56</td><td>-0.17</td><td>-0.17 0.42</td><td>-0.77</td><td></td><td>-0.81</td><td></td><td></td><td></td></tr><tr><td>126</td><td>Togo</td><td>-0.82</td><td>-1.34</td><td>-1.43</td><td>-1.11</td><td>-1.66</td><td>-0.96</td><td>-1.11</td><td>0.05</td><td>0.70 0.77</td><td></td><td>0.56 1.12</td><td>-0.42</td><td>0.87</td><td>2.15 -0.59</td><td>0.87</td><td>-0.62 2.15</td><td>-0.03 1.07</td><td>0.57 0.89</td></tr><tr><td>127</td><td>Tunisia</td><td>-0.60</td><td>-0.04</td><td>-0.04</td><td>-0.78</td><td>0.57</td><td>0.10</td><td>-0.01</td><td>0.34</td><td>0.70 0.20</td><td>0.56</td><td>-0.58</td><td>-0.32</td><td>-0.45</td><td>-0.80</td><td>0.55</td><td>-0.62</td><td>-0.34</td><td>0.34</td></tr><tr><td>128</td><td>Turkey</td><td>-0.16</td><td>-1.34</td><td>-0.27</td><td>-0.12</td><td>-0.27</td><td>-0.17</td><td>-2.64</td><td>0.48</td><td>1.62 0.20</td><td></td><td>-0.70 -0.53</td><td>0.53</td><td>-0.63</td><td>-0.75</td><td>-0.13</td><td>-0.78</td><td>0.29</td><td>0.48</td></tr><tr><td>129 130</td><td>Uganda</td><td>-0.82 -1.20</td></table></body></html>

Table 4.19 (continued)   

<html><body><table><tr><td rowspan="3">Country</td><td rowspan="3"></td><td colspan="7">Data for indicators of sustainable development Data for global threats</td><td colspan="10"></td></tr><tr><td rowspan="2">GDP per</td><td rowspan="2">Q</td><td rowspan="2">Iql</td><td rowspan="2">Iec</td><td rowspan="2">le</td><td rowspan="2">Is</td><td rowspan="2">Isec</td><td rowspan="2">BB CI</td><td rowspan="2">CP</td><td rowspan="2">ES</td><td rowspan="2">GD</td><td rowspan="2">GW</td><td rowspan="2">IG</td><td rowspan="2">ND</td><td rowspan="2">NI</td><td rowspan="2">WA</td><td rowspan="2">GINI</td><td rowspan="2">SF</td></tr><tr><td></td></tr><tr><td>1</td><td></td><td>capita 2</td><td>4</td><td></td><td></td><td>7</td><td>8</td><td>9</td><td>10</td><td></td><td>12</td><td>13</td><td>14</td><td>15</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>32</td><td>United States</td><td>3 2.08</td><td>1.49</td><td>1.52</td><td>5 1.86</td><td>6 1.08</td><td>1.40</td><td>1.25</td><td>1.42 0.70</td><td>11</td><td></td><td></td><td>5.48</td><td>-1.55</td><td>16 -0.59</td><td>17 -0.76</td><td>18</td><td>19</td><td>20</td></tr><tr><td>3</td><td>Uruguay</td><td>0.22</td><td>1.07</td><td>0.97</td><td>0.63</td><td>0.29</td><td>1.40</td><td>1.14</td><td>-2.25</td><td>-1.31</td><td>-1.54 -1.43</td><td>-3.48 0.56</td><td>-0.43 -0.64 -0.42</td><td>-1.05</td><td>-0.69</td><td>1.03</td><td>-0.73 -0.78</td><td>0.39 0.50</td><td>-1.38</td></tr><tr><td>34</td><td>Bolivarian</td><td>0.06</td><td>-0.64</td><td>-0.78</td><td>-1.82</td><td>0.47</td><td>-1.47</td><td>-0.29</td><td>0.05 0.70</td><td>1.48</td><td></td><td>-0.50</td><td>-0.94 0.11</td><td>0.19</td><td>-0.75</td><td>0.24</td><td>-0.20</td><td>1.18</td><td>-1.34 0.71</td></tr><tr><td></td><td>Republic of</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Venezuela Viet Nam</td><td>-0.71</td><td>-0.78</td><td>-1.06</td><td>-0.78</td><td>-1.05</td><td>-0.92</td><td>-0.23</td><td>0.12 0.70</td><td>0.72</td><td></td><td>0.10</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>36</td><td>Yemen</td><td>-0.76</td><td>-1.99</td><td>-1.61</td><td>-1.25</td><td>-1.52</td><td>-1.75</td><td>-2.64</td><td>0.05 1.62</td><td>1.64</td><td></td><td>0.56</td><td>-0.69 -0.38 -0.42</td><td>0.83 1.65</td><td>0.68 -0.75</td><td>-0.86 0.29</td><td>-0.57</td><td>-0.08 -0.08</td><td>0.16</td></tr><tr><td>37</td><td>Zambia</td><td>-0.71</td><td>-0.78</td><td>-0.78</td><td>-0.55</td><td>-0.41</td><td>-0.96</td><td>-0.62</td><td>-0.46</td><td>-1.31 0.41</td><td></td><td>0.56 2.25</td><td>-0.42</td><td>1.10</td><td>-0.06</td><td>0.66</td><td>2.47 2.05</td><td>1.91</td><td>1.71 0.89</td></tr></table></body></html>

Table 4.20 Values of specific mutual informativeness   

<html><body><table><tr><td rowspan="2">Global threats</td><td colspan="7">Values of Specific Mutual Informativeness</td></tr><tr><td>GDP</td><td>Q</td><td>Iql</td><td>Iec</td><td>le</td><td>Is</td><td>Isec</td></tr><tr><td>BB</td><td>0.37</td><td>0.48</td><td>0.46</td><td>0.52</td><td>0.37</td><td>0.45</td><td>0.56</td></tr><tr><td>CI</td><td>0.21</td><td>0.41</td><td>0.43</td><td>0.89</td><td>0.38</td><td>0.81</td><td>0.80</td></tr><tr><td>CP</td><td>0.21</td><td>0.93</td><td>0.91</td><td>0.80</td><td>0.38</td><td>0.77</td><td>0.78</td></tr><tr><td>ES</td><td>0.20</td><td>0.48</td><td>0.46</td><td>0.42</td><td>0.37</td><td>0.45</td><td>0.28</td></tr><tr><td>GD</td><td>0.20</td><td>0.48</td><td>0.46</td><td>0.42</td><td>0.37</td><td>0.45</td><td>0.28</td></tr><tr><td>GW</td><td>0.20</td><td>0.41</td><td>0.43</td><td>0.42</td><td>0.38</td><td>0.45</td><td>0.28</td></tr><tr><td>IG</td><td>0.21</td><td>0.89</td><td>0.90</td><td>0.90</td><td>0.38</td><td>0.89</td><td>0.90</td></tr><tr><td>ND</td><td>0.20</td><td>0.41</td><td>0.43</td><td>0.42</td><td>0.38</td><td>0.45</td><td>0.28</td></tr><tr><td>NI</td><td>0.20</td><td>0.48</td><td>0.46</td><td>0.52</td><td>0.37</td><td>0.45</td><td>0.56</td></tr><tr><td>WA</td><td>0.20</td><td>0.48</td><td>0.46</td><td>0.52</td><td>0.37</td><td>0.45</td><td>0.28</td></tr><tr><td>GINI</td><td>0.20</td><td>0.41</td><td>0.46</td><td>0.42</td><td>0.38</td><td>0.45</td><td>0.28</td></tr><tr><td>SF</td><td>0.21</td><td>0.79</td><td>0.77</td><td>0.87</td><td>0.76</td><td>0.90</td><td>0.93</td></tr></table></body></html>

![](images/ac0c75503f0f3896bfcdeb0b1d5db3096944ff765e4c938830c3067a7094fc45.jpg)  
Fig. 4.23 The mathematical SDGM model for determination of life quality component of sustainable development and its harmonization degree

2. Construction of a Bayesian Belief Network. For the construction and parametric adjustment of such a model, we will use the system GeNIe 2.0 [48] destined for the construction and modeling of Bayesian networks. In Fig. 4.25, the appearance of a Bayesian Belief Network constructed in the system GeNIe 2.0 is presented. Such a BBN allows one to estimate the degree of belief in hypotheses with respect to the influence of various threats on indicators of sustainable development of countries and regions of the world and causal relations between these variables.

![](images/2e895e7e705b9df50e12989e3d0a2d350f78331d058f2cd647ba31dcfc60126b.jpg)  
Fig. 4.24 A BBN destined for the analysis of the influence of global threats on the sustainable development of countries and regions of the world

![](images/b19824d9730d8b78dfca0418575cf7f9dceee91c9a31780abf080b955cd9d923.jpg)  
Fig. 4.25 A bayesian belief network constructed in system GeNIe 2.0

In particular, for example, the evidences $P ( E _ { 1 } : G D P = H ) = 1$ is established. As a result, the degree of belief in the hypotheses $H _ { 1 } : ( Q = H )$ , $H _ { 2 } : ( I q l = H )$ , $H _ { 3 } : ( I s e c = H ) , H _ { 4 } : ( I e = H ) , H _ { 5 } : ( I e c = H )$ , and $H _ { 6 } : ( I s = H )$ is very high and amounts to 1.00 but, for example, for the hypothesis $H _ { 7 } : ( C P = L )$ ; the degree of belief equals 0.25. Countries with a high level of GDP always have a high value of all indicators of sustainable development, but relative to threats, for example CP, it doesn’t mean anything.

3. Modeling of a BBN. In modeling a BBN, we establish the task of testing following hypotheses: «If the value (evalue) of some model’s variable (evar) is known, what will be the expected value (hvalue) of another variable (hvar).».

For this hypothesis we have:

$$
\begin{array} { r } { \{ p ( h : [ ( h \nu a r = h \nu a l u e ) ] | ( e : [ e \nu a r = e \nu a l u e ] ) ) \} \qquad } \\ { \forall c \nu a r , e \nu a r \in \{ G D P , Q , I q l , I e c , I e , I s , I s e c , B B , C I , C P , G D , I G , N D , N I , W A , S F \} , } \\ { e \nu a l u e , c \nu a l u e \in \{ L , M , H \} \qquad } \end{array}
$$

To test the formulated hypotheses, the library SMILE [48] was used. In this case, a BBN was modelled with an exhaustive search for evidence.

Thus, the collection of results were obtained whose total length equaled $3 ^ { 1 6 } =$ 43; 046; 721 rows. It is obvious that their semantic interpretation for this length is a practically impossible task.

In this connection, it is necessary to reduce data end formally generalize them.

To reduce the data we estimated the probabilities of the first $( { \mathfrak { a } } )$ and second (b) types error and removed the rows with high $\textsf { a }$ values and low values $( 1 - \beta )$ .

4. Formal Generalization of Results of Modeling. To generalize the obtained results, we apply the set-theoretic approach [49] according to which a generalization of the facts presented by their specifications can be obtained as a result of set-theoretic operations over these specifications. We associate with evidence $E _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j }$ the Boolean function

$$
f \bigl ( E _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j } \bigr ) = \left\{ \begin{array} { l l } { 1 } & { i f P \bigl ( E _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j } \bigr ) \geq P _ { i } } \\ { 0 } & { o t h e r w i s e , } \end{array} \right.
$$

where $P t$ is a given threshold for belief.

We also define $f \left( E _ { i } ^ { U } : X _ { i } = U \right)$ the conjunction of the following function:

$$
f \bigl ( E _ { i } ^ { U } : X _ { i } = U \bigr ) = \bigcup f _ { i } ^ { j } \bigl ( E _ { i } ^ { j } : X _ { i } = x _ { i } ^ { j } \bigr )
$$

$$
\forall x _ { i } ^ { j } \in \{ L , M , H \}
$$

Then the conjunction of the following form corresponds to a collection of evidences $e = E _ { 1 } , E _ { 2 } , . . . , E _ { n }$ :

$$
f ( e ) = \bigcup _ { i = 1 } ^ { n } f ( E _ { i } ) .
$$

For a hypothesis $H$ justified on a set of collections of evidences $\big \{ e _ { j } \big \} , j = \overline { { 1 , m } }$ , we have

$$
f ( H ) = \bigcup _ { j = 1 } ^ { m } f \big ( e _ { j } \big ) .
$$

Applying the rule of implication and the Quine–McCluskey covering method [50] to $( H )$ , one can obtain a minimal set covering all the collections of evidences for which the hypothesis $H$ is justified.

# 4.6.5 Interpretation of the Generalized Results of Modeling

In Table 4.21, the results of modeling are generalized that are represented by minimal sets of collections of evidences that are justified by the hypotheses, respectively.

Table 4.21 Generalized results of BBN modeling   

<html><body><table><tr><td rowspan="3">Hipotesis</td><td colspan="11">Variables</td></tr><tr><td></td><td colspan="2">Indicators of sustainable development</td><td></td><td></td><td></td><td></td><td colspan="2"></td><td></td><td>Global threats</td><td></td><td></td><td></td><td></td></tr><tr><td>GDP</td><td>Q</td><td>Iql</td><td>Iec</td><td>Ie</td><td>Is</td><td>I sec</td><td>BB</td><td>CI</td><td>CP</td><td>GD</td><td>IG</td><td>ND</td><td>NI</td><td>WA</td><td>SF</td></tr><tr><td>1</td><td>H</td><td>H</td><td>H</td><td>H</td><td>H</td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td>L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td>M</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td>H</td><td>H</td><td></td><td>H</td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td>L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td>M</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td>H</td><td>H</td><td></td><td>H</td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>L</td><td></td><td></td><td>L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td></td><td>H</td><td>H</td><td>H</td><td>H</td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>L</td><td>L</td><td>L</td><td></td><td>L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>L</td><td></td><td>L</td><td></td><td></td><td>L</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td></td><td>H</td><td>H</td><td></td><td>H</td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>L</td><td>L</td><td></td><td></td><td></td><td>L</td><td>L</td><td></td><td></td><td></td><td></td><td>L</td><td></td><td></td><td></td></tr><tr><td>14</td><td></td><td></td><td></td><td></td><td></td><td></td><td>M</td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td></td><td>H</td><td></td><td></td><td>H</td><td></td><td>H</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>L</td><td></td><td></td><td>L</td><td></td><td>L</td><td></td></tr><tr><td>17</td><td></td><td></td><td></td><td></td><td></td><td>M</td><td></td><td></td><td>M</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18</td><td></td><td></td><td></td><td>H</td><td></td><td></td><td>H</td><td></td><td></td><td>L</td><td></td><td>L</td><td></td><td>L</td><td>L</td></tr><tr><td>19</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>H</td><td>H</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>L</td><td></td><td></td><td>L</td><td></td></tr><tr><td>21</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>H</td><td></td><td>H</td><td></td><td>H</td></tr><tr><td>22</td><td></td><td></td><td></td><td></td><td></td><td></td><td>H</td><td></td><td></td><td></td><td>L</td><td>L</td><td></td><td>L</td><td></td></tr><tr><td>23</td><td></td><td></td><td></td><td></td><td></td><td></td><td>M</td><td>M</td><td></td><td></td><td></td><td>M</td><td></td><td></td><td></td></tr><tr><td>24</td><td></td><td></td><td></td><td>H</td><td></td><td></td><td>H</td><td></td><td></td><td>L</td><td></td><td>L</td><td>L</td><td>L</td><td>L</td></tr><tr><td>25 26</td><td></td><td></td><td></td><td></td><td></td><td></td><td>M</td><td>M</td><td>H</td><td>H</td><td></td><td>H</td><td></td><td>M H</td><td>H</td></tr><tr></table></body></html>

Analysis of the simulation results in Table 4.21 (the evidence are shown in bold) allows us to assess the expected level of the indicators of the sustainable development and the degree of manifestation of threats in conditions of uncertainty, when the values of some indicators are unknown.

For example, based on the analysis of lines 1–15, in which hypotheses are given, and the condition that one of the indicators of the sustainable development is known, it can be said that the indicators of the sustainable development are closely interrelated. Thus, a high level of GDP is always accompanied by high levels of all indicators of sustainable development (line 1); a low level of Iql is accompanied by low levels of GDP and Is, and it is also a determining factor for the low level of Q (line 5); a high level of Iec is accompanied by high levels of indicators Ie, Is, Isec and determines a high level of indicators Q and Iql (line 9); if it is known that Ie has a low level we can say that GDP, Q and Iql will also have a low level (line 10); knowing that the Is level is low allows us to say that GDP and Iql levels are also low (line 11); the high level of Is is accompanied by a high level of all indicators of the sustainable development with the exception of those that are directly related to economic development, i.e. GDP and Iec (line 12); low Isec level is accompanied by low levels of GDP, Q and Is indicators, as well as low level of ND threat (line 13).

In general, knowing the levels of the sustainable development indicators does not provide an opportunity to predict the levels of threat indicators (lines 1–15).

In the second part of the table (lines 16–28) hypotheses are given, provided that the level of one of the threats is known. The analysis of these lines allows us to say that threats are interrelated with each other, some of them influence the indicators of the sustainable development directly and others influence indirectly.

For example, a low level of CI is accompanied by low levels of ND and WA (line 16); if it is known that the level of CP is low then the level of ND, WA and SF threats will also be low, and this corresponds to a high level of Iec and Isec indicators (line 18); the high level of the CP threat is accompanied by a high level of the CI threat (line 20); high level of GD threat manifestation corresponds to high level of the NI and SF threats (line 21); a low level of NI identifies the fact that the threats CP, IC, WA and SF also has a low level, and the sustainability indicators Iec and Isec will be high (line 24); low level of the SF threat corresponds to low levels of the IC, ND and WA threats, as well as high level of Isec indicator.

# 4.6.6 Visualization of Data on Indicators of Sustainable Development for Countries and Regions of the World

In this section we will present in the table and visual forms relations between levels of vulnerability of countries and regions of the world to global threats and indicators of sustainable development in the global context. Data for indicators of sustainable development, global threats, safety levels and also $\mathbf { G D P _ { s } }$ for countries of the world in 2016 are taken from [4], ordered in accordance with the method of cluster analysis (4.13) and presented in Table 4.22.

1   
Table 4.22 Indicators of sustainable development for countries and regions of the world, 2013–2016a   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1 2</td><td></td><td>3</td><td>5</td><td>17</td><td>8</td><td>L9</td><td>10</td><td>11</td><td>to 5) 12</td><td>13</td><td>14</td></tr><tr><td colspan="10">Very highdegreeofsustainable development</td><td></td><td></td><td></td></tr><tr><td>1</td><td>Australia</td><td>1.119</td><td>1.458</td><td>0.788</td><td>0.724</td><td>0.693</td><td>0.955</td><td>6.864</td><td>0.000</td><td>0.853</td><td>79.000</td></tr><tr><td>2</td><td>Canada</td><td>1.115</td><td>1.397</td><td>0.764</td><td>0.722</td><td>0.637</td><td>0.951</td><td>7.422</td><td>0.000</td><td>0.836</td><td>82.000</td></tr><tr><td>3</td><td>Germany</td><td>1.110</td><td>1.445</td><td>0.755</td><td>0.770</td><td>0.667</td><td>0.928</td><td>-3.211</td><td>3.000</td><td>0.801</td><td>81.000</td></tr><tr><td>4</td><td>Switzerland</td><td>1.102</td><td>1.463</td><td>0.785</td><td>0.771</td><td>0.669</td><td>0.943</td><td>-4.044</td><td>0.000</td><td>0.829</td><td>86.000</td></tr><tr><td>5</td><td>Finland</td><td>1.096</td><td>1.398</td><td>0.822</td><td>0.634</td><td>0.674</td><td>0.946</td><td>6.606</td><td>0.000</td><td>0.821</td><td>89.000</td></tr><tr><td>6</td><td>Denmark</td><td>1.095</td><td>1.442</td><td>0.808</td><td>0.673</td><td>0.702</td><td>0.956</td><td>-1.535</td><td>0.000</td><td>0.780</td><td>90.000</td></tr><tr><td>7</td><td>Japan</td><td>1.080</td><td>1.418</td><td>0.710</td><td>0.789</td><td>0.652</td><td>0.898</td><td>-4.281</td><td>2.000</td><td>0.845</td><td>72.000</td></tr><tr><td>8</td><td>Norway</td><td>1.077</td><td>1.374</td><td>0.784</td><td>0.625</td><td>0.679</td><td>0.936</td><td>2.137</td><td>0.000</td><td>0.846</td><td>85.000</td></tr><tr><td>9</td><td>Singapore</td><td>1.076</td><td>1.423</td><td>0.786</td><td>0.772</td><td>0.625</td><td>0.929</td><td>-6.746</td><td>1.000</td><td>0.874</td><td>84.000</td></tr><tr><td>10</td><td>Netherlands</td><td>1.075</td><td>1.377</td><td>0.728</td><td>0.709</td><td>0.645</td><td>0.938</td><td>-4.674</td><td>0.000</td><td>0.837</td><td>83.000</td></tr><tr><td>11</td><td>Sweden</td><td>1.074</td><td>1.381</td><td>0.820</td><td>0.650</td><td>0.642</td><td>0.975</td><td>3.881</td><td>3.000</td><td>0.827</td><td>88.000</td></tr><tr><td>12</td><td>New Zealand</td><td>1.073</td><td>1.418</td><td>0.796</td><td>0.699</td><td>0.656</td><td>0.980</td><td>4.934</td><td>0.000</td><td>0.817</td><td>90.000</td></tr><tr><td>13</td><td>Austria</td><td>1.069</td><td>1.403</td><td>0.782</td><td>0.646</td><td>0.697</td><td>0.938</td><td>-3.115</td><td>0.000</td><td>0.766</td><td>75.000</td></tr><tr><td>14</td><td>United Kingdom</td><td>1.066</td><td>1.434</td><td>0.789</td><td>0.700</td><td>0.679</td><td>0.966</td><td>-3.779</td><td>3.000</td><td>0.848</td><td>81.000</td></tr><tr><td>15</td><td>United</td><td>1.065</td><td>1.418</td><td>0.760</td><td>0.759</td><td>0.640</td><td>0.932</td><td>-4.810</td><td>3.000</td><td>0.878</td><td>74.000</td></tr><tr><td>16</td><td>States Ireland</td><td>1.052</td><td>1.382</td><td>0.781</td><td>0.700</td><td>0.626</td><td>0.965</td><td>-1.111</td><td>0.000</td><td>0.789</td><td>73.000</td></tr><tr><td>17</td><td>Iceland</td><td>1.048</td><td>1.367</td><td>0.820</td><td>0.643</td><td>0.632</td><td>0.969</td><td>0.795</td><td>0.000</td><td>0.644</td><td>78.000</td></tr><tr><td>18</td><td>Belgium</td><td>1.025</td><td>1.290</td><td>0.704</td><td>0.608</td><td>0.653</td><td>0.927</td><td>-5.762</td><td>0.000</td><td>0.785</td><td>77.000</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>to5) 12</td><td>13</td><td>14</td></tr><tr><td>19</td><td>Luxembourg</td><td>1.022</td><td>1.331</td><td>0.781</td><td>0.643</td><td>0.621</td><td>0.988</td><td>-11.507</td><td>0.000</td><td>0.764</td><td>81.000</td></tr><tr><td>20</td><td>France</td><td>1.021</td><td>1.307</td><td>0.798</td><td>0.590</td><td>0.634</td><td>0.924</td><td>-2.152</td><td>3.000</td><td>0.849</td><td>69.000</td></tr><tr><td>21</td><td>Spain</td><td>1.017</td><td>1.340</td><td>0.805</td><td>0.631</td><td>0.626</td><td>0.967</td><td>-2.448</td><td>3.000</td><td>0.800</td><td>58.000</td></tr><tr><td>22</td><td>Estonia</td><td>1.014</td><td>1.332</td><td>0.802</td><td>0.664</td><td>0.595</td><td>0.947</td><td>3.225</td><td>1.000</td><td>0.857</td><td>70.000</td></tr><tr><td>23</td><td>Korea, Rep.</td><td>1.012</td><td>1.282</td><td>0.567</td><td>0.717</td><td>0.624</td><td>0.836</td><td>-5.186</td><td>0.000</td><td>0.853</td><td>53.000</td></tr><tr><td>24</td><td>Czech Republic</td><td>0.996</td><td>1.315</td><td>0.760</td><td>0.653</td><td>0.610</td><td>0.982</td><td>-2.840</td><td>0.000</td><td>0.738</td><td>55.000</td></tr><tr><td>25</td><td>Italy</td><td>0.969</td><td>1.201</td><td>0.758</td><td>0.550</td><td>0.597</td><td>0.902</td><td>-3.453</td><td>0.000</td><td>0.742</td><td>47.000</td></tr><tr><td>26</td><td>Poland</td><td>0.965</td><td>1.250</td><td>0.719</td><td>0.606</td><td>0.611</td><td>0.976</td><td>-2.286</td><td>0.000</td><td>0.725</td><td>62.000</td></tr><tr><td>27</td><td>Lithuania</td><td>0.964</td><td>1.282</td><td>0.769</td><td>0.644</td><td>0.584</td><td>0.950</td><td>-0.193</td><td>0.000</td><td>0.674</td><td>59.000</td></tr><tr><td>28</td><td>Portugal</td><td>0.959</td><td>1.234</td><td>0.802</td><td>0.542</td><td>0.608</td><td>0.868</td><td>-2.344</td><td>0.000</td><td>0.671</td><td>62.000</td></tr><tr><td>29</td><td>Uruguay</td><td>0.956</td><td>1.194</td><td>0.618</td><td>0.569</td><td>0.641</td><td>0.880</td><td>6.912</td><td>0.000</td><td>0.742</td><td>71.000</td></tr><tr><td>30</td><td>Slovenia</td><td>0.945</td><td>1.207</td><td>0.806</td><td>0.486</td><td>0.623</td><td>0.780</td><td>-2.444</td><td>1.000</td><td>0.578</td><td>61.000</td></tr><tr><td>31</td><td>Latvia</td><td>0.941</td><td>1.212</td><td>0.771</td><td>0.601</td><td>0.559</td><td>0.915</td><td>2.975</td><td>1.000</td><td>0.771</td><td>57.000</td></tr><tr><td>32</td><td>Chile</td><td>0.938</td><td>1.303</td><td>0.671</td><td>0.670</td><td>0.629</td><td>0.925</td><td>-0.684</td><td>3.000</td><td>0.563</td><td>66.000</td></tr><tr><td colspan="10">Highdegree ofsustainable development</td><td></td><td></td><td>55.000</td></tr><tr><td>33</td><td>Malta</td><td>0.934</td><td>1.220</td><td>0.801</td><td>0.557</td><td>0.585</td><td>0.889</td><td>-3.841</td><td>0.000</td><td>0.627</td><td></td></tr><tr><td>34</td><td>Slovakia</td><td>0.927</td><td>1.182</td><td>0.768</td><td>0.562</td><td>0.569</td><td>0.906</td><td>-1.675</td><td>0.000</td><td>0.581</td><td>51.000</td></tr><tr><td>35</td><td>Costa Rica</td><td>0.911</td><td>1.190</td><td>0.703</td><td>0.561</td><td>0.607</td><td>0.927</td><td>-0.948</td><td>0.000</td><td>0.541</td><td>58.000</td></tr><tr><td>36</td><td>Mauritius</td><td>0.911</td><td>1.145</td><td>0.571</td><td>0.631</td><td>0.573</td><td>0.894</td><td>-2.643</td><td>0.000</td><td>0.765</td><td>54.000</td></tr><tr><td>37</td><td>Israel</td><td>0.894</td><td>1.154</td><td>0.677</td><td>0.626</td><td>0.539</td><td>0.901</td><td>-5.634</td><td>3.000</td><td>0.782</td><td>64.000</td></tr><tr><td>38</td><td>Romania</td><td>0.885</td><td>1.125</td><td>0.743</td><td>0.543</td><td>0.553</td><td>0.892</td><td>0.060</td><td>1.000</td><td>0.691</td><td>48.000</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0 to 5）</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td></td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>39</td><td>Hungary</td><td>0.877</td><td>1.120</td><td>0.759</td><td>0.555</td><td>0.532</td><td>0.867</td><td>-0.899</td><td>2.000</td><td>0.679</td><td>48.000</td></tr><tr><td>40</td><td>Cyprus</td><td>0.873</td><td>1.161</td><td>0.705</td><td>0.574</td><td>0.573</td><td>0.961</td><td>-2.991</td><td>2.000</td><td>0.644</td><td>55.000</td></tr><tr><td>41</td><td>Bulgaria</td><td>0.871</td><td>1.130</td><td>0.745</td><td>0.545</td><td>0.554</td><td>0.894</td><td>-0.012</td><td>1.000</td><td>0.703</td><td>41.000</td></tr><tr><td>42</td><td>Croatia</td><td>0.869</td><td>1.093</td><td>0.785</td><td>0.447</td><td>0.570</td><td>0.734</td><td>-0.979</td><td>1.000</td><td>0.721</td><td>49.000</td></tr><tr><td>43</td><td>Malaysia</td><td>0.863</td><td>1.126</td><td>0.622</td><td>0.628</td><td>0.541</td><td>0.897</td><td>-1.840</td><td>2.000</td><td>0.810</td><td>49.000</td></tr><tr><td>44</td><td>Montenegro</td><td>0.856</td><td>1.089</td><td>0.688</td><td>0.519</td><td>0.571</td><td>0.895</td><td>-0.500</td><td>0.000</td><td>0.516</td><td>45.000</td></tr><tr><td>45</td><td>Georgia</td><td>0.839</td><td>1.100</td><td>0.479</td><td>0.610</td><td>0.587</td><td>0.835</td><td>-0.456</td><td>3.000</td><td>0.763</td><td>57.000</td></tr><tr><td>46</td><td>Oman</td><td>0.831</td><td>1.009</td><td>0.404</td><td>0.568</td><td>0.579</td><td>0.794</td><td>-3.993</td><td>1.000</td><td>0.806</td><td>45.000</td></tr><tr><td>47</td><td>Barbados</td><td>0.827</td><td>0.989</td><td>0.329</td><td>0.570</td><td>0.582</td><td>0.722</td><td>-3.199</td><td>0.000</td><td>0.534</td><td>61.000</td></tr><tr><td>48</td><td>Belarus</td><td>0.827</td><td>0.972</td><td>0.732</td><td>0.316</td><td>0.554</td><td>0.560</td><td>-1.351</td><td>1.000</td><td>0.729</td><td>40.000</td></tr><tr><td>49</td><td>Greece</td><td>0.822</td><td>1.032</td><td>0.773</td><td>0.380</td><td>0.560</td><td>0.634</td><td>-2.706</td><td>3.000</td><td>0.658</td><td>44.000</td></tr><tr><td>50</td><td>Botswana</td><td>0.817</td><td>1.052</td><td>0.569</td><td>0.600</td><td>0.530</td><td>0.899</td><td>0.115</td><td>0.000</td><td>0.507</td><td>60.000</td></tr><tr><td>51</td><td>Panama</td><td>0.807</td><td>1.001</td><td>0.675</td><td>0.531</td><td>0.504</td><td>0.863</td><td>0.139</td><td>0.000</td><td>0.573</td><td>38.000</td></tr><tr><td>52</td><td>Brazil</td><td>0.803</td><td>0.939</td><td>0.688</td><td>0.447</td><td>0.514</td><td>0.770</td><td>5.831</td><td>4.000</td><td>0.684</td><td>40.000</td></tr><tr><td>53</td><td>Serbia</td><td>0.802</td><td>1.037</td><td>0.685</td><td>0.477</td><td>0.563</td><td>0.828</td><td>-1.517</td><td>3.000</td><td>0.536</td><td>42.000</td></tr><tr><td>54</td><td>Albania</td><td>0.798</td><td>0.998</td><td>0.624</td><td>0.542</td><td>0.517</td><td>0.925</td><td>-1.065</td><td>0.000</td><td>0.469</td><td>39.000</td></tr><tr><td>55</td><td>Argentina</td><td>0.788</td><td>0.904</td><td>0.700</td><td>0.280</td><td>0.531</td><td>0.525</td><td>3.052</td><td>1.000</td><td>0.641</td><td>36.000</td></tr><tr><td>56</td><td>Saudi Arabia</td><td>0.782</td><td>0.906</td><td>0.536</td><td>0.535</td><td>0.496</td><td>0.917</td><td>-5.161</td><td>3.000</td><td>0.705</td><td>46.000</td></tr><tr><td>57</td><td>Armenia</td><td>0.782</td><td>1.012</td><td>0.723</td><td>0.536</td><td>0.481</td><td>0.789</td><td>-1.176</td><td>3.000</td><td>0.431</td><td>33.000</td></tr><tr><td>58</td><td>Macedonia</td><td>0.778</td><td>1.006</td><td>0.676</td><td>0.547</td><td>0.493</td><td>0.843</td><td>-1.504</td><td>3.000</td><td>0.640</td><td>37.000</td></tr><tr><td>59</td><td>Jordan</td><td>0.778</td><td>1.031</td><td>0.592</td><td>0.561</td><td>0.539</td><td>0.970</td><td>-1.868</td><td>2.000</td><td>0.453</td><td>48.000</td></tr><tr><td>60</td><td>Cabo Verde</td><td>0.771</td><td>0.962</td><td>0.289</td><td>0.541</td><td>0.595</td><td>0.677</td><td>--1.600</td><td>0.000</td><td>0.323</td><td>59.000</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>to5） 12</td><td>13</td><td>14</td></tr><tr><td>61</td><td>Colombia</td><td>0.768</td><td>1.020</td><td>0.646</td><td>0.605</td><td>0.458</td><td>0.749</td><td>1.821</td><td>4.000</td><td>0.635</td><td>37.000</td></tr><tr><td>62</td><td>Russian Federation</td><td>0.768</td><td>0.862</td><td>0.746</td><td>0.388</td><td>0.443</td><td>0.565</td><td>1.164</td><td>3.000</td><td>0.806</td><td>29.000</td></tr><tr><td colspan="10">63 China 0.764</td><td>3.000 0.666</td><td></td><td>40.000</td></tr><tr><td>Medium degree of Sustainable development</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>64</td><td>Seychelles</td><td>0.758</td><td>0.895</td><td>0.478</td><td>0.484</td><td>0.548</td><td>0.880</td><td>N/A</td><td>0.000</td><td>0.400</td><td>55.000</td></tr><tr><td>65</td><td>Peru</td><td>0.756</td><td>1.015</td><td>0.602</td><td>0.573</td><td>0.513</td><td>0.904</td><td>1.532</td><td>3.000</td><td>0.484</td><td>35.000</td></tr><tr><td>66</td><td>Kazakhstan</td><td>0.754</td><td>0.882</td><td>0.608</td><td>0.511</td><td>0.463</td><td>0.812</td><td>-2.926</td><td>3.000</td><td>0.561</td><td>29.000</td></tr><tr><td>67</td><td>Belize</td><td>0.754</td><td>0.887</td><td>0.611</td><td>0.423</td><td>0.527</td><td>0.775</td><td>N/A</td><td>0.000</td><td>0.373</td><td>N/A</td></tr><tr><td>68</td><td>Azerbaijan</td><td>0.751</td><td>0.909</td><td>0.749</td><td>0.464</td><td>0.429</td><td>0.628</td><td>-1.481</td><td>3.000</td><td>0.677</td><td>30.000</td></tr><tr><td>69</td><td>Jamaica</td><td>0.748</td><td>0.999</td><td>0.662</td><td>0.547</td><td>0.496</td><td>0.856</td><td>-1.486</td><td>3.000</td><td>0.466</td><td>39.000</td></tr><tr><td>70</td><td>Tunisia</td><td>0.744</td><td>0.907</td><td>0.665</td><td>0.416</td><td>0.518</td><td>0.734</td><td>-1.394</td><td>3.000</td><td>0.633</td><td>41.000</td></tr><tr><td>71</td><td>Bhutan</td><td>0.743</td><td>0.833</td><td>0.479</td><td>0.456</td><td>0.528</td><td>0.878</td><td>0.527</td><td>0.000</td><td>0.349</td><td>65.000</td></tr><tr><td>72</td><td>Fiji</td><td>0.737</td><td>0.961</td><td>0.637</td><td>0.440</td><td>0.554</td><td>0.784</td><td>-0.964</td><td>2.000</td><td>0.392</td><td>40.000</td></tr><tr><td>73</td><td>Moldova</td><td>0.734</td><td>0.901</td><td>0.657</td><td>0.405</td><td>0.523</td><td>0.719</td><td>-0.767</td><td>3.000</td><td>0.571</td><td>30.000</td></tr><tr><td>74</td><td>Thailand</td><td>0.732</td><td>0.895</td><td>0.550</td><td>0.551</td><td>0.462</td><td>0.812</td><td>-1.349</td><td>2.000</td><td>0.694</td><td>35.000</td></tr><tr><td>75</td><td>Guyana</td><td>0.730</td><td>0.714</td><td>0.575</td><td>0.395</td><td>0.433</td><td>0.678</td><td>66.184</td><td>0.000</td><td>0.379</td><td>34.000</td></tr><tr><td>76</td><td>Paraguay</td><td>0.721</td><td>0.887</td><td>0.563</td><td>0.483</td><td>0.513</td><td>0.918</td><td>7.538</td><td>3.000</td><td>0.438</td><td>30.000</td></tr><tr><td>77</td><td>Mongolia</td><td>0.719</td><td>0.752</td><td>0.470</td><td>0.444</td><td>0.490</td><td>0.915</td><td>7.774</td><td>0.000</td><td>0.420</td><td>38.000</td></tr><tr><td>78</td><td>Namibia</td><td>0.714</td><td>0.873</td><td>0.570</td><td>0.477</td><td>0.505</td><td>0.898</td><td>4.532</td><td>0.000</td><td>0.283</td><td>52.000</td></tr><tr><td>79 80</td><td>Morocco Kyrgyzstan</td><td>0.702 0.700</td><td>0.882 0.826</td><td>0.621 0.605</td><td>0.479 0.458</td><td>0.486 0.466</td><td>0.835 0.792</td><td>-0.895 -0.590</td><td>3.000 3.000</td><td>0.594 0.422</td><td>37.000 28.000</td></tr></table></body></html>

Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>to5) 12</td><td>13</td><td>14</td></tr><tr><td>81</td><td>Bosnia and Herzegovina</td><td>0.677</td><td>0.794</td><td>0.452</td><td>0.432</td><td>0.527</td><td>0.834</td><td>-1.521</td><td>2.000</td><td>0.377</td><td>39.000</td></tr><tr><td>82</td><td>Bolivia</td><td>0.676</td><td>0.757</td><td>0.574</td><td>0.328</td><td>0.493</td><td>0.626</td><td>13.799</td><td>3.000</td><td>0.324</td><td>33.000</td></tr><tr><td>83</td><td>El Salvador</td><td>0.675</td><td>0.807</td><td>0.527</td><td>0.521</td><td>0.426</td><td>0.754</td><td>-1.300</td><td>4.000</td><td>0.354</td><td>36.000</td></tr><tr><td>84</td><td>Philippines</td><td>0.673</td><td>0.867</td><td>0.614</td><td>0.517</td><td>0.434</td><td>0.740</td><td>-0.479</td><td>4.000</td><td>0.609</td><td>35.000</td></tr><tr><td>85</td><td>Dominican Republic</td><td>0.666</td><td>0.828</td><td>0.638</td><td>0.463</td><td>0.440</td><td>0.721</td><td>-0.968</td><td>3.000</td><td>0.356</td><td>31.000</td></tr><tr><td>86</td><td>Lebanon</td><td>0.666</td><td>0.818</td><td>0.544</td><td>0.446</td><td>0.500</td><td>0.862</td><td>-3.094</td><td>3.000</td><td>0.433</td><td>28.000</td></tr><tr><td>87</td><td>Ghana</td><td>0.665</td><td>0.736</td><td>0.385</td><td>0.498</td><td>0.469</td><td>0.887</td><td>-0.632</td><td>0.000</td><td>0.434</td><td>43.000</td></tr><tr><td>88</td><td>South Africa</td><td>0.662</td><td>0.810</td><td>0.565</td><td>0.483</td><td>0.453</td><td>0.814</td><td>-2.262</td><td>3.000</td><td>0.591</td><td>45.000</td></tr><tr><td>89</td><td>Algeria</td><td>0.662</td><td>0.752</td><td>0.562</td><td>0.357</td><td>0.488</td><td>0.680</td><td>-1.792</td><td>3.000</td><td>0.519</td><td>34.000</td></tr><tr><td>90</td><td>Indonesia</td><td>0.655</td><td>0.791</td><td>0.493</td><td>0.479</td><td>0.481</td><td>0.938</td><td>-0.225</td><td>3.000</td><td>0.490</td><td>37.000</td></tr><tr><td>91</td><td>India</td><td>0.652</td><td>0.673</td><td>0.310</td><td>0.476</td><td>0.471</td><td>0.855</td><td>-0.628</td><td>4.000</td><td>0.584</td><td>40.000</td></tr><tr><td>92</td><td>Iran</td><td>0.649</td><td>0.666</td><td>0.500</td><td>0.289</td><td>0.477</td><td>0.598</td><td>-2.221</td><td>3.000</td><td>0.584</td><td>29.000</td></tr><tr><td>93</td><td>Tajikistan</td><td>0.642</td><td>0.732</td><td>0.604</td><td>0.355</td><td>0.450</td><td>0.620</td><td>-0.389</td><td>3.000</td><td>0.435</td><td>25.000</td></tr><tr><td>94</td><td>Egypt</td><td>0.638</td><td>0.666</td><td>0.502</td><td>0.406</td><td>0.434</td><td>0.762</td><td>-1.458</td><td>4.000</td><td>0.696</td><td>34.000</td></tr><tr><td>95</td><td>Guatemala</td><td>0.638</td><td>0.790</td><td>0.552</td><td>0.477</td><td>0.449</td><td>0.813</td><td>-0.751</td><td>3.000</td><td>0.340</td><td>28.000</td></tr><tr><td>96</td><td>Venezuela, Bolivarian</td><td>0.637</td><td>0.685</td><td>0.651</td><td>0.248</td><td>0.369</td><td>0.348</td><td>-0.550</td><td>3.000</td><td>0.521</td><td>17.000</td></tr><tr><td>97</td><td>Republic of Ecuador</td><td>0.634</td><td>0.709</td><td>0.504</td><td>0.331</td><td>0.495</td><td>0.662</td><td>0.259</td><td>3.000</td><td>0.548</td><td>31.000</td></tr><tr><td>98</td><td>Sri Lanka</td><td>0.633</td><td>0.740</td><td>0.488</td><td>0.449</td><td>0.470</td><td>0.895</td><td>-0.954</td><td>3.000</td><td>0.482</td><td>36.000</td></tr></table></body></html>

Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>to 5) 12</td><td>13</td><td>14</td></tr><tr><td>99</td><td>Vietnam</td><td>0.610</td><td>0.590</td><td>0.380</td><td>0.419</td><td>0.432</td><td>0.908</td><td>-0.676</td><td>3.000</td><td>0.400</td><td>33.000</td></tr><tr><td>100</td><td>Honduras</td><td>0.609</td><td>0.685</td><td>0.552</td><td>0.422</td><td>0.392</td><td>0.648</td><td>0.034</td><td>3.000</td><td>0.252</td><td>30.000</td></tr><tr><td>101</td><td>Rwanda</td><td>0.608</td><td>0.685</td><td>0.268</td><td>0.511</td><td>0.457</td><td>0.738</td><td>-0.314</td><td>2.000</td><td>0.524</td><td>54.000</td></tr><tr><td>102</td><td>Zambia</td><td>0.608</td><td>0.685</td><td>0.496</td><td>0.442</td><td>0.423</td><td>0.780</td><td>1.062</td><td>0.000</td><td>0.340</td><td>38.000</td></tr><tr><td>103</td><td>Senegal</td><td>0.603</td><td>0.752</td><td>0.459</td><td>0.429</td><td>0.502</td><td>0.871</td><td>-0.132</td><td>3.000</td><td>0.365</td><td>45.000</td></tr><tr><td colspan="10">Low degree of sustainable development</td><td></td><td></td><td></td></tr><tr><td>104</td><td>Nicaragua</td><td>0.584</td><td>0.674</td><td>0.467</td><td>0.442</td><td>0.433</td><td>0.831</td><td>0.855</td><td>3.000</td><td>0.286</td><td>26.000</td></tr><tr><td>105</td><td>Benin</td><td>0.562</td><td>0.555</td><td>0.194</td><td>0.453</td><td>0.444</td><td>0.730</td><td>-0.434</td><td>0.000</td><td>0.216</td><td>36.000</td></tr><tr><td>106</td><td>Tanzania, United</td><td>0.551</td><td>0.638</td><td>0.377</td><td>0.444</td><td>0.451</td><td>0.959</td><td>-0.239</td><td>3.000</td><td>0.337</td><td>32.000</td></tr><tr><td>107</td><td>Republic of Cote</td><td>0.547</td><td>0.600</td><td>0.400</td><td>0.455</td><td>0.376</td><td>0.714</td><td>0.408</td><td>3.000</td><td>0.442</td><td>34.000</td></tr><tr><td>108</td><td>dIvoire Swaziland</td><td>0.547</td><td>0.644</td><td>0.412</td><td>0.443</td><td>0.439</td><td>0.896</td><td>-1.156</td><td>3.000</td><td>0.235</td><td>43.000</td></tr><tr><td>109</td><td>Congo, Republic of</td><td>0.543</td><td>0.458</td><td>0.395</td><td>0.296</td><td>0.362</td><td>0.571</td><td>9.513</td><td>3.000</td><td>0.216</td><td>20.000</td></tr><tr><td>110</td><td>the Madagascar</td><td>0.542</td><td>0.517</td><td>0.138</td><td>0.463</td><td>0.417</td><td>0.606</td><td>1.573</td><td>0.000</td><td>0.246</td><td>26.000</td></tr><tr><td>111</td><td>Cambodia</td><td>0.542</td><td>0.562</td><td>0.280</td><td>0.451</td><td>0.424</td><td>0.837</td><td>-0.134</td><td>3.000</td><td>0.370</td><td>21.000</td></tr><tr><td>112</td><td>Kenya</td><td>0.537</td><td>0.650</td><td>0.440</td><td>0.427</td><td>0.442</td><td>0.868</td><td>-0.509</td><td>3.000</td><td>0.541</td><td>26.000</td></tr><tr><td>113</td><td>Malawi</td><td>0.534</td><td>0.494</td><td>0.260</td><td>0.357</td><td>0.452</td><td>0.822</td><td>-0.171</td><td>0.000</td><td>0.213</td><td>31.000</td></tr><tr><td>114</td><td>Laos</td><td>0.531</td><td>0.443</td><td>0.268</td><td>0.370</td><td>0.405</td><td>0.966</td><td>0.165</td><td>1.000</td><td>0.411</td><td>30.000</td></tr><tr><td>115</td><td>Guinea</td><td>0.529</td><td>0.493</td><td>0.335</td><td>0.381</td><td>0.402</td><td>0.862</td><td>0.622</td><td>3.000</td><td>0.218</td><td>27.000</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0 to 5）</td><td>(IG) Information Gap</td><td>(CP) Corruption perception index</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>116</td><td>Nepal</td><td>0.525</td><td>0.458</td><td>0.267</td><td>0.360</td><td>0.425</td><td>0.919</td><td>-0.395</td><td>3.000</td><td>0.425</td><td>29.000</td></tr><tr><td>117</td><td>Mexico</td><td>0.525</td><td>0.909</td><td>0.612</td><td>0.557</td><td>0.422</td><td>0.699</td><td>-1.345</td><td>5.000</td><td>0.669</td><td>30.000</td></tr><tr><td>118</td><td>Bangladesh</td><td>0.519</td><td>0.387</td><td>0.176</td><td>0.382</td><td>0.387</td><td>0.826</td><td>-0.377</td><td>3.000</td><td>0.488</td><td>26.000</td></tr><tr><td>119</td><td>Uganda</td><td>0.518</td><td>0.565</td><td>0.366</td><td>0.447</td><td>0.374</td><td>0.728</td><td>-0.651</td><td>3.000</td><td>0.481</td><td>25.000</td></tr><tr><td>120</td><td>Lesotho</td><td>0.513</td><td>0.440</td><td>0.231</td><td>0.334</td><td>0.438</td><td>0.804</td><td>-0.628</td><td>0.000</td><td>0.257</td><td>39.000</td></tr><tr><td>121</td><td>Pakistan</td><td>0.511</td><td>0.450</td><td>0.282</td><td>0.407</td><td>0.354</td><td>0.744</td><td>-0.380</td><td>4.000</td><td>0.441</td><td>32.000</td></tr><tr><td>122</td><td>Sierra Leone</td><td>0.504</td><td>0.414</td><td>0.218</td><td>0.366</td><td>0.408</td><td>0.939</td><td>0.014</td><td>3.000</td><td>0.355</td><td>30.000</td></tr><tr><td>123</td><td>Burkina Faso</td><td>0.502</td><td>0.506</td><td>0.195</td><td>0.454</td><td>0.400</td><td>0.690</td><td>-0.220</td><td>3.000</td><td>0.278</td><td>42.000</td></tr><tr><td>124</td><td>Gambia</td><td>0.495</td><td>0.453</td><td>0.290</td><td>0.395</td><td>0.373</td><td>0.815</td><td>-0.169</td><td>3.000</td><td>0.265</td><td>26.000</td></tr><tr><td>125</td><td>Cameroon</td><td>0.495</td><td>0.502</td><td>0.360</td><td>0.395</td><td>0.376</td><td>0.765</td><td>0.482</td><td>3.000</td><td>0.413</td><td>26.000</td></tr><tr><td>126</td><td>Turkey</td><td>0.486</td><td>0.842</td><td>0.521</td><td>0.490</td><td>0.495</td><td>0.946</td><td>-1.718</td><td>5.000</td><td>0.665</td><td>41.000</td></tr><tr><td>127</td><td>Togo</td><td>0.482</td><td>0.449</td><td>0.219</td><td>0.375</td><td>0.427</td><td>0.882</td><td>-0.579</td><td>3.000</td><td>0.392</td><td>32.000</td></tr><tr><td>128</td><td>Mali</td><td>0.475</td><td>0.417</td><td>0.174</td><td>0.414</td><td>0.375</td><td>0.715</td><td>0.080</td><td>3.000</td><td>0.220</td><td>32.000</td></tr><tr><td>129</td><td>Central African</td><td>0.474</td><td>0.289</td><td>0.223</td><td>0.301</td><td>0.292</td><td>0.669</td><td>6.404</td><td>4.000</td><td>0.165</td><td>20.000</td></tr><tr><td>130</td><td>Republic</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>131</td><td>Ukraine</td><td>0.470</td><td>0.813</td><td>0.698</td><td>0.304 0.375</td><td>0.466 0.399</td><td>0.513</td><td>-0.719 -0.441</td><td>5.000</td><td>0.604</td><td>29.000 34.000</td></tr><tr><td>132</td><td>Ethiopia Niger</td><td>0.469</td><td>0.411</td><td>0.216</td><td>0.387</td><td>0.407</td><td>0.928 0.739</td><td>-0.318</td><td>3.000 3.000</td><td>0.302 0.237</td><td>35.000</td></tr><tr><td>133</td><td></td><td>0.465</td><td>0.401</td><td>0.141</td><td>0.337</td><td></td><td>0.784</td><td></td><td></td><td></td><td>18.000</td></tr><tr><td>134</td><td>Angola Mozambique</td><td>0.453 0.432</td><td>0.384 0.377</td><td>0.281 0.177</td><td>0.371</td><td>0.358 0.389</td><td>0.857</td><td>1.441 1.061</td><td>3.000 3.000</td><td>0.224 0.275</td><td>27.000</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(Q) Index of Sustainable development</td><td>(CQL) Component of Quality of Life</td><td>(Ie) Index of environmental dimension</td><td>(Iec) Index of economic dimension</td><td>(Is) Index of social and institutional dimension</td><td>(G) Garmonization degree</td><td>(FB) Biodiversity balance (measured in global hectares per person)</td><td>(CI) Conflicts intensity (from 0</td><td>(IG) Gap</td><td>Information</td><td>(CP) Corruption perception index</td></tr><tr><td>1 2</td><td></td><td>3</td><td>5</td><td>7</td><td>8</td><td>L9</td><td>10</td><td>11</td><td></td><td>to 5) 12</td><td>13</td><td>14</td></tr><tr><td colspan="11">Very low degree of sustainable development</td></tr><tr><td>135</td><td>Syria</td><td>0.341</td><td>0.590</td><td>0.509</td><td>0.362</td><td>0.367</td><td>0.566</td><td>-0.886</td><td colspan="2">5.000</td><td>0.319</td><td>13.000</td></tr><tr><td>136</td><td>Nigeria</td><td>0.332</td><td>0.574</td><td>0.376</td><td>0.443</td><td>0.386</td><td>0.762</td><td>-0.429</td><td colspan="2">5.000</td><td>0.528</td><td>28.000</td></tr><tr><td>137 Rank</td><td>Yemen</td><td>0.213</td><td>0.368</td><td>0.262</td><td>0.357 (ND)</td><td>0.319</td><td>0.700</td><td>-0.511</td><td colspan="2">5.000</td><td>0.196</td><td>14.000</td></tr><tr><td>ISD</td><td>Country,</td><td>(ES) (GD) Global Spread decrease of of energy global</td><td colspan="3">(GW) Global warming (measured in metric tons of carbon dioxide</td><td>(NI) Vulnerability to natural (measured disasters with a</td><td>(WA) Proliferation Limited access to drinking</td><td colspan="2">(GINI) Increasing inequality between people and nations on</td><td colspan="2">(SF) State fragility (measured with the Failed</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>security 15</td><td>diseases 16</td><td>emission) 17</td><td>18</td><td>complex indicator) 19</td><td>water 20</td><td>Earth 21</td><td></td><td colspan="2">States Index) 22 23</td><td>25</td><td></td></tr><tr><td colspan="11">Very high degree of sustainable development</td><td></td><td></td><td></td></tr><tr><td>1</td><td>Australia</td><td>0.544</td><td>0.566</td><td>377,906.352</td><td>0.550</td><td>0.149</td><td>100.000</td><td>34.940</td><td>22.500</td><td colspan="2"></td><td>1.687</td><td>$49,755.315</td></tr><tr><td>2</td><td>Canada</td><td>0.687</td><td>0.547</td><td>475,734.578</td><td>0.554</td><td>0.168</td><td>99.800</td><td>33.680</td><td></td><td colspan="2">23.800</td><td>1.763</td><td>$42,183.295</td></tr><tr><td>3</td><td>Germany</td><td>0.663</td><td>0.539</td><td>757,312.507</td><td>0.556</td><td>0.204</td><td></td><td>100.000 30.130</td><td></td><td colspan="2">28.600</td><td>1.675</td><td>$42,161.320</td></tr><tr><td>4</td><td>Switzerland</td><td>0.439</td><td>0.546</td><td>40,348.001</td><td>0.556</td><td>0.148</td><td></td><td>100.000 31.640</td><td colspan="2">21.800</td><td></td><td>1.618</td><td>$79,887.518</td></tr><tr><td>5</td><td>Finland</td><td>0.441</td><td>0.546</td><td>46,299.542</td><td>0.556</td><td>0.149</td><td></td><td>100.000 27.120</td><td colspan="2">18.800</td><td>1.696</td><td></td><td>$43,401.228</td></tr><tr><td>6</td><td>Denmark</td><td>0.452</td><td>0.539</td><td>38,067.127</td><td>0.556</td><td>0.147</td><td></td><td>100.000 29.080</td><td colspan="2">21.500</td><td>1.628</td><td></td><td>$53,578.757</td></tr><tr><td>7</td><td>Japan</td><td>0.575</td><td>0.537</td><td>1,243,384.358</td><td>0.553</td><td>0.188</td><td></td><td>100.000 32.110</td><td colspan="2">35.100</td><td>1.612</td><td></td><td>$38,900.569</td></tr><tr><td>8</td><td>Norway</td><td>0.506</td><td>0.544</td><td>59,636.421</td><td>0.556</td><td>0.138</td><td></td><td>100.000 25.900</td><td colspan="2">21.200</td><td>1.667</td><td></td><td>$70,868.122</td></tr><tr><td>9</td><td>Singapore</td><td>0.416</td><td>0.521</td><td>50,556.929</td><td>0.556</td><td>0.182</td><td></td><td>100.000 N/A</td><td colspan="2">32.900</td><td>1.591</td><td></td><td>$52,962.492</td></tr><tr><td>10</td><td>Netherlands</td><td>0.455</td><td>0.543</td><td>169,972.784</td><td>0.556</td><td>0.170</td><td></td><td>100.000 27.990</td><td colspan="2">28.200</td><td>1.655</td><td></td><td>$45,637.887</td></tr><tr><td>11</td><td>Sweden</td><td>0.489</td><td>0.542</td><td>44,326.696</td><td>0.556</td><td>0.159</td><td></td><td>100.000 27.320</td><td colspan="2">22.600</td><td>1.648</td><td></td><td>$51,844.761</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>Earth 21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>12</td><td>New Zealand</td><td>0.433</td><td>0.545</td><td>33,960.087</td><td>0.517</td><td>0.133</td><td>100.000</td><td>N/A</td><td>21.300</td><td>1.587</td><td>$39,412.159</td></tr><tr><td>13</td><td>Austria</td><td>0.445</td><td>0.545</td><td>62,408.673</td><td>0.556</td><td>0.154</td><td>100.000</td><td>30.480</td><td>27.500</td><td>1.597</td><td>$44,757.635</td></tr><tr><td>14</td><td>United Kingdom</td><td>0.602</td><td>0.536</td><td>457,472.918</td><td>0.555</td><td>0.118</td><td>100.000</td><td>32.570</td><td>32.400</td><td>1.538</td><td>$40,367.038</td></tr><tr><td>15</td><td>United States</td><td>0.980</td><td>0.547</td><td>5,186,168.427</td><td>0.548</td><td>0.134</td><td>99.200</td><td>41.060</td><td>34.000</td><td>1.559</td><td>$57,638.159</td></tr><tr><td>16</td><td>Ireland</td><td>0.428</td><td>0.541</td><td>34,964.845</td><td>0.556</td><td>0.144</td><td>97.900</td><td>32.520</td><td>22.500</td><td>1.571</td><td>$64,175.438</td></tr><tr><td>17</td><td>Iceland</td><td>0.415</td><td>0.546</td><td>1969.179</td><td>0.556</td><td>0.139</td><td>100.000</td><td>26.940</td><td>22.800</td><td>1.579</td><td>$59,764.705</td></tr><tr><td>18</td><td>Belgium</td><td>0.460</td><td>0.545</td><td>93,618.510</td><td>0.556</td><td>0.151</td><td>100.000</td><td>27.590</td><td>29.000</td><td>1.610</td><td>$41,271.482</td></tr><tr><td>19</td><td>Luxembourg</td><td>0.415</td><td>0.549</td><td>10,161.257</td><td>0.556</td><td>0.132</td><td>100.000</td><td>34.790</td><td>24.100</td><td>1.544</td><td>$100,738.684</td></tr><tr><td>20</td><td>France</td><td>0.597</td><td>0.546</td><td>333,190.954</td><td>0.554</td><td>0.150</td><td>100.000</td><td>33.100</td><td>34.500</td><td>1.572</td><td>$36,857.119</td></tr><tr><td>21</td><td>Spain</td><td>0.597</td><td>0.558</td><td>236,968.874</td><td>0.556</td><td>0.141</td><td>100.000</td><td>35.890</td><td>39.800</td><td>1.509</td><td>$26,616.488</td></tr><tr><td>22</td><td>Estonia</td><td>0.415</td><td>0.538</td><td>19,915.477</td><td>0.556</td><td>0.134</td><td>99.600</td><td>33.150</td><td>43.400</td><td>1.514</td><td>$17,736.803</td></tr><tr><td>23</td><td>Korea,Rep.</td><td>0.501</td><td>0.547</td><td>592,499.192</td><td>0.556</td><td>0.203</td><td>97.600</td><td>N/A</td><td>36.100</td><td>1.581</td><td>$27,538.806</td></tr><tr><td>24</td><td>Czech Republic</td><td>0.442</td><td>0.542</td><td>98,660.635</td><td>0.497</td><td>0.140</td><td>100.000</td><td>26.130</td><td>40.800</td><td>1.478</td><td>$18,483.716</td></tr><tr><td>25</td><td>Italy</td><td>0.565</td><td>0.560</td><td>344,767.673</td><td>0.556</td><td>0.158</td><td>100.000</td><td>35.160</td><td>43.100</td><td>1.550</td><td>$30,661.222</td></tr><tr><td>26</td><td>Poland</td><td>0.457</td><td>0.540</td><td>302,333.149</td><td>0.556</td><td>0.129</td><td>98.300</td><td>32.080</td><td>40.700</td><td>1.467</td><td>$12,414.099</td></tr><tr><td>27</td><td>Lithuania</td><td>0.418</td><td>0.527</td><td>12.640.149</td><td>0.556</td><td>0.123</td><td>96.600</td><td>35.150</td><td>42.400</td><td>1.412</td><td>$14,900.779</td></tr><tr><td>28</td><td>Portugal</td><td>0.452</td><td>0.532</td><td>46,262.872</td><td>0.556</td><td>0.130</td><td>100.000</td><td>36.040</td><td>29.200</td><td>1.469</td><td>$19,838.027</td></tr><tr><td>29</td><td>Uruguay</td><td>0.415</td><td>0.561</td><td>7605.358</td><td>0.552</td><td>0.105</td><td>99.700</td><td>41.600</td><td>36.200</td><td>1.516</td><td>$15,220.566</td></tr></table></body></html>

Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on Earth</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>30</td><td>Slovenia</td><td>0.415</td><td>0.548</td><td>14,440.646</td><td>0.534</td><td>0.141</td><td>99.500</td><td>25.590</td><td>33.900</td><td>1.463</td><td>$21,650.213</td></tr><tr><td>31</td><td>Latvia</td><td>0.415</td><td>0.553 0.565</td><td>7080.977 83,171.227</td><td>0.556 0.488</td><td>0.128 0.122</td><td>99.300 99.000</td><td>35.480 50.450</td><td>47.400 41.900</td><td>1.440</td><td>$14,071.027</td></tr><tr><td colspan="10">32 Chile 0.444 High degree of sustainable development</td><td>1.284</td><td>$13,792.926</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>33</td><td>Malta</td><td>0.415</td><td>0.537</td><td>2218.535</td><td>0.556</td><td>0.128</td><td>100.000</td><td>N/A</td><td>39.600</td><td>1.404</td><td>$25,145.393</td></tr><tr><td>34</td><td>Slovakia</td><td>0.424</td><td>0.546</td><td>33,677.728</td><td>0.556</td><td>0.123</td><td>100.000</td><td>26.120</td><td>44.900</td><td>1.435</td><td>$16,529.541</td></tr><tr><td>35</td><td>Costa Rica</td><td>0.415</td><td>0.613</td><td>7616.359</td><td>0.531</td><td>0.108</td><td>97.800</td><td>48.530</td><td>45.100</td><td>1.370</td><td>$11,824.638</td></tr><tr><td>36</td><td>Mauritius</td><td>0.415</td><td>0.555</td><td>3725.672</td><td>0.556</td><td>0.120</td><td>99.900</td><td>35.840</td><td>43.200</td><td>1.434</td><td>$9630.944</td></tr><tr><td>37</td><td>Israel</td><td>0.425</td><td>0.540</td><td>71,073.794</td><td>0.480</td><td>0.175</td><td>100.000</td><td>42.780</td><td>79.700</td><td>1.366</td><td>$37,180.527</td></tr><tr><td>38</td><td>Romania</td><td>0.452</td><td>0.507</td><td>70,736.430</td><td>0.555</td><td>0.113</td><td>100.000</td><td>27.450</td><td>52.900</td><td>1.376</td><td>$9522.771</td></tr><tr><td>39</td><td>Hungary</td><td>0.424</td><td>0.541</td><td>41,440.767</td><td>0.552</td><td>0.132</td><td>100.000</td><td>30.550</td><td>52.700</td><td>1.357</td><td>$12,820.088</td></tr><tr><td>40 41</td><td>Cyprus</td><td>0.415</td><td>0.542</td><td>5947.874</td><td>0.556</td><td>0.111</td><td>100.000</td><td>34.310</td><td>64.000</td><td>1.281</td><td>$23,541.488</td></tr><tr><td>42</td><td>Bulgaria</td><td>0.433</td><td>0.531</td><td>395,63.263</td><td>0.553</td><td>0.118</td><td>99.400</td><td>36.010</td><td>53.700</td><td>1.322</td><td>$7469.025</td></tr><tr><td>43</td><td>Croatia</td><td>0.415</td><td>0.541</td><td>17,711.610</td><td>0.554</td><td>0.121</td><td>99.600</td><td>32.510</td><td>52.400</td><td>1.367</td><td>$12,149.190</td></tr><tr><td></td><td>Malaysia</td><td>0.448</td><td>0.549</td><td>236,510.499</td><td>0.495</td><td>0.145</td><td>98.200</td><td>46.260</td><td>66.100</td><td>1.301</td><td>$9508.238</td></tr><tr><td>44</td><td>Montenegro</td><td>0.415</td><td>0.535</td><td>2247.871</td><td>0.550</td><td>0.106</td><td>99.700</td><td>31.930</td><td>55.200</td><td>1.328</td><td>$7028.935</td></tr><tr><td>45</td><td>Georgia</td><td>0.415</td><td>0.547</td><td>7510.016</td><td>0.533</td><td>0.117</td><td>100.000</td><td>40.090</td><td>78.900</td><td>1.257</td><td>$3865.786</td></tr><tr><td>46</td><td>Oman</td><td>0.436</td><td>0.565</td><td>61,183.895</td><td>0.555</td><td>0.124</td><td>93.400</td><td>N/A</td><td>51.600</td><td>1.355</td><td>$14,982.358</td></tr><tr><td>47</td><td>Barbados</td><td>0.415</td><td>0.550</td><td>1448.465</td><td>0.554</td><td>0.120</td><td>99.700</td><td>N/A</td><td>49.000</td><td>1.371</td><td>$15,891.627</td></tr><tr><td>48 49</td><td>Belarus Greece</td><td>0.416 0.452</td><td>0.585 0.560</td><td>63,769.130 69,155.953</td><td>0.553 0.551</td><td>0.128 0.130</td><td>99.700 100.000</td><td>27.180 36.680</td><td>73.900 55.900</td><td>1.391 1.298</td><td>$4989.428 $17,890.575</td></tr></table></body></html>

√   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>50</td><td>Botswana</td><td>0.415</td><td>0.402</td><td>5423.493</td><td>0.552</td><td>0.107</td><td>96.200</td><td>60.460</td><td>63.500</td><td>1.250</td><td>$6924.150</td></tr><tr><td>51</td><td>Panama</td><td>0.415</td><td>0.569</td><td>10,362.942</td><td>0.551</td><td>0.108</td><td>94.700</td><td>50.700</td><td>53.200</td><td>1.291</td><td>$13,680.236</td></tr><tr><td>52</td><td>Brazil</td><td>0.624</td><td>0.551</td><td>503.677.118</td><td>0.455</td><td>0.136</td><td>98.100</td><td>51.480</td><td>65.300</td><td>1.357</td><td>$8649.948</td></tr><tr><td>53</td><td>Serbia</td><td>0.417</td><td>0.533</td><td>44,869.412</td><td>0.450</td><td>0.139</td><td>99.200</td><td>29.060</td><td>72.000</td><td>1.222</td><td>$5426.198</td></tr><tr><td>54</td><td>Albania</td><td>0.415</td><td>0.536</td><td>4814.771</td><td>0.500</td><td>0.115</td><td>95.100</td><td>28.960</td><td>61.200</td><td>1.264</td><td>$4124.982</td></tr><tr><td>55</td><td>Argentina</td><td>0.446</td><td>0.585</td><td>189,818.588</td><td>0.549</td><td>0.121</td><td>99.100</td><td>42.670</td><td>48.400</td><td>1.352</td><td>$12,440.321</td></tr><tr><td>56</td><td>Saudi Arabia</td><td>0.533</td><td>0.581</td><td>541,428.883</td><td>0.556</td><td>0.135</td><td>97.000</td><td>N/A</td><td>72.200</td><td>1.332</td><td>$20,028.648</td></tr><tr><td>57</td><td>Armenia</td><td>0.415</td><td>0.555</td><td>5496.833</td><td>0.540</td><td>0.116</td><td>100.000</td><td>31.480</td><td>69.600</td><td>1.191</td><td>$3614.688</td></tr><tr><td>58</td><td>Macedonia</td><td>0.415</td><td>0.603</td><td>8294.754</td><td>0.456</td><td>0.117</td><td>99.400</td><td>44.050</td><td>67.000</td><td>1.185</td><td>$5237.148</td></tr><tr><td>59</td><td>Jordan</td><td>0.415</td><td>0.493</td><td>24,807.255</td><td>0.556</td><td>0.117</td><td>96.900</td><td>N/A</td><td>78.000</td><td>1.146</td><td>$4087.938</td></tr><tr><td>60</td><td>Cabo Verde</td><td>0.415</td><td>0.542</td><td>443.707</td><td>0.543</td><td>0.110</td><td>91.700</td><td>47.190</td><td>71.500</td><td>1.225</td><td>$2997.753</td></tr><tr><td>61</td><td>Colombia</td><td>0.448</td><td>0.577</td><td>89,625.147</td><td>0.516</td><td>0.108</td><td>91.400</td><td>53.500</td><td>80.200</td><td>1.130</td><td>$5805.605</td></tr><tr><td>62</td><td>Russian Federation</td><td>0.703</td><td>0.540</td><td>1,789,074.295</td><td>0.554</td><td>0.080</td><td>96.900</td><td>41.590</td><td>81.000</td><td>1.339</td><td>$8748.369</td></tr><tr><td>63</td><td>China</td><td>0.926</td><td>0.542</td><td>10,249,463.020</td><td>0.382</td><td>0.132</td><td>95.500</td><td>42.160</td><td>74.900</td><td>1.301</td><td></td></tr><tr><td colspan="10">Medium degree of Sustainable development</td><td></td><td></td><td>$8123.181</td></tr><tr><td>64</td><td>Seychelles</td><td>0.415</td><td>0.549</td><td>645.392</td><td>0.491</td><td>0.131</td><td>95.700</td><td>46.820</td><td>60.200</td><td>1.270</td><td>$15,075.719</td></tr><tr><td>65</td><td>Peru</td><td>0.430</td><td>0.567</td><td>57,153.862</td><td>0.515</td><td>0.120</td><td>86.700</td><td>44.140</td><td>72.000</td><td>1.092</td><td>$6049.233</td></tr><tr><td>66</td><td>Kazakhstan</td><td>0.448</td><td>0.566</td><td>262.901.898</td><td>0.554</td><td>0.131</td><td>92.900</td><td>26.330</td><td>66.500</td><td>1.273</td><td>$7714.694</td></tr><tr><td>67</td><td>Belize</td><td>0.415</td><td>0.552</td><td>517.047</td><td>0.530</td><td>0.117</td><td>99.500</td><td>N/A</td><td>66.000</td><td>1.266</td><td>$4744.736</td></tr><tr><td>68</td><td>Azerbaijan</td><td>0.430</td><td>0.583</td><td>35,643.240</td><td>0.552</td><td>0.120</td><td>87.000</td><td>31.790</td><td>76.300</td><td>1.230</td><td>$3878.709</td></tr></table></body></html>

Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on Earth</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>69</td><td>Jamaica</td><td>0.415</td><td>0.547</td><td>7726.369</td><td>0.494</td><td>0.117</td><td>93.800</td><td>45.460</td><td>65.000</td><td>1.090</td><td>$4878.576</td></tr><tr><td>70</td><td>Tunisia</td><td>0.416</td><td>0.556</td><td>27,667.515</td><td>0.556</td><td>0.113</td><td>97.700</td><td>35.810</td><td>74.600</td><td>1.211</td><td>$3688.646</td></tr><tr><td>71</td><td>Bhutan</td><td>0.415</td><td>0.518</td><td>883.747</td><td>0.547</td><td>0.117</td><td>100.000</td><td>38.810</td><td>77.600</td><td>1.297</td><td>$2773.547</td></tr><tr><td>72</td><td>Fiji</td><td>0.415</td><td>0.524</td><td>1708.822</td><td>0.525</td><td>0.127</td><td>95.700</td><td>42.780</td><td>76.200</td><td>1.111</td><td>$5233.469</td></tr><tr><td>73</td><td>Moldova</td><td>0.415</td><td>0.543</td><td>4976.119</td><td>0.546</td><td>0.104</td><td>88.400</td><td>26.830</td><td>73.200</td><td>1.184</td><td>$1900.226</td></tr><tr><td>74</td><td>Thailand</td><td>0.453</td><td>0.534</td><td>303,117.887</td><td>0.416</td><td>0.135</td><td>97.800</td><td>37.850</td><td>78.800</td><td>1.187</td><td>$5910.621</td></tr><tr><td>75</td><td>Guyana</td><td>0.415</td><td>0.505</td><td>1936.176</td><td>0.529</td><td>0.116</td><td>98.300</td><td>N/A</td><td>70.900</td><td>1.379</td><td>$4529.139</td></tr><tr><td>76</td><td>Paraguay</td><td>0.415</td><td>0.570</td><td>4972.452</td><td>0.440</td><td>0.109</td><td>98.000</td><td>51.670</td><td>72.600</td><td>1.164</td><td>$4077.742</td></tr><tr><td>77</td><td>Mongolia</td><td>0.417</td><td>0.558</td><td>41,591.114</td><td>0.525</td><td>0.104</td><td>64.400</td><td>32.040</td><td>56.600</td><td>1.311</td><td>$3694.083</td></tr><tr><td>78</td><td>Namibia</td><td>0.415</td><td>0.430</td><td>2948.268</td><td>0.407</td><td>0.110</td><td>91.000</td><td>60.970</td><td>71.100</td><td>1.158</td><td>$4414.979</td></tr><tr><td>79</td><td>Morocco</td><td>0.415</td><td>0.550</td><td>58,558.323</td><td>0.553</td><td>0.107</td><td>85.400</td><td>40.720</td><td>74.200</td><td>1.105</td><td>$2892.776</td></tr><tr><td>80</td><td>Kyrgyzstan</td><td>0.415</td><td>0.583</td><td>9842.228</td><td>0.530</td><td>0.101</td><td>90.000</td><td>26.820</td><td>81.100</td><td>1.173</td><td>$1077.603</td></tr><tr><td>81</td><td>Bosnia and Herzegovina</td><td>0.415</td><td>0.556</td><td>21,906.658</td><td>0.446</td><td>0.118</td><td>99.900</td><td>33.830</td><td>74.600</td><td>1.140</td><td>$4808.405</td></tr><tr><td>82</td><td>Bolivia</td><td>0.420</td><td>0.560</td><td>19,702.791</td><td>0.459</td><td>0.107</td><td>90.000</td><td>48.400</td><td>78.500</td><td>1.180</td><td>$3104.956</td></tr><tr><td>83</td><td>El Salvador</td><td>0.415</td><td>0.619</td><td>6358.578</td><td>0.509</td><td>0.104</td><td>93.800</td><td>41.840</td><td>72.500</td><td>1.117</td><td>$4223.585</td></tr><tr><td>84</td><td>Philippines</td><td>0.434</td><td>0.519</td><td>98,238.930</td><td>0.257</td><td>0.123</td><td>91.800</td><td>43.040</td><td>84.700</td><td>1.029</td><td>$2951.072</td></tr><tr><td>85</td><td>Dominican Republic</td><td>0.415</td><td>0.567</td><td>22.071.673</td><td>0.544</td><td>0.116</td><td>84.700</td><td>47.070</td><td>70.800</td><td>1.062</td><td>$6722.224</td></tr><tr><td>86</td><td>Lebanon</td><td>0.415</td><td>0.569</td><td>22,581.386</td><td>0.434</td><td>0.121</td><td>99.000</td><td>N/A</td><td>89.600</td><td>1.075</td><td>$8257.294</td></tr><tr><td>87</td><td>Ghana</td><td>0.415</td><td>0.421</td><td>14,620.329</td><td>0.550</td><td>0.108</td><td>88.700</td><td>42.77</td><td>71.200</td><td>1.170</td><td>$1513.461</td></tr></table></body></html>

Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>88</td><td>South Africa</td><td>0.462</td><td>0.279</td><td>471,238.836</td><td>0.548</td><td>0.116</td><td>93.200</td><td>63.380</td><td>69.900</td><td>1.072</td><td>$5274.546</td></tr><tr><td>89</td><td>Algeria</td><td>0.456</td><td>0.541</td><td>134,215.867</td><td>0.556</td><td>0.133</td><td>83.600</td><td>N/A</td><td>78.300</td><td>1.143</td><td>$3916.882</td></tr><tr><td>90</td><td>Indonesia</td><td>0.480</td><td>0.490</td><td>479,364.908</td><td>0.548</td><td>0.121</td><td>87.400</td><td>39.470</td><td>74.900</td><td>1.075</td><td>$3570.295</td></tr><tr><td>91</td><td>India</td><td>0.664</td><td>0.386</td><td>2,034,752.294</td><td>0.523</td><td>0.092</td><td>94.100</td><td>35.150</td><td>79.600</td><td>1.199</td><td>$1709.592</td></tr><tr><td>92</td><td>Iran</td><td>0.523</td><td>0.574</td><td>616,976.417</td><td>0.549</td><td>0.112</td><td>96.200</td><td>37.350</td><td>86.900</td><td>1.197</td><td>$5219.109</td></tr><tr><td>93</td><td>Tajikistan</td><td>0.415</td><td>0.582</td><td>3586.326</td><td>0.529</td><td>0.110</td><td>73.800</td><td>30.760</td><td>83.800</td><td>1.107</td><td>$795.844</td></tr><tr><td>94</td><td>Egypt</td><td>0.442</td><td>0.508</td><td>213,012.363</td><td>0.556</td><td>0.114</td><td>99.400</td><td>N/A</td><td>90.200</td><td>1.165</td><td>$3477.852</td></tr><tr><td>95</td><td>Guatemala</td><td>0.415</td><td>0.593</td><td>13,597.236</td><td>0.409</td><td>0.100</td><td>92.800</td><td>48.660</td><td>83.200</td><td>1.021</td><td>$4146.744</td></tr><tr><td>96</td><td>Venezuela, Bolivarian</td><td>0.470</td><td>0.578</td><td>185,531.865</td><td>0.553</td><td>0.118</td><td>93.100</td><td>46.940</td><td>81.600</td><td>1.143</td><td>N/A</td></tr><tr><td>97</td><td>Republic of Ecuador</td><td>0.426</td><td>0.571</td><td>43,527.290</td><td>0.546</td><td>0.114</td><td>86.900</td><td>45.380</td><td>75.600</td><td>1.109</td><td>$6018.527</td></tr><tr><td>98</td><td>Sri Lanka</td><td>0.415</td><td>0.570</td><td>16.024.790</td><td>0.377</td><td>0.116</td><td>95.600</td><td>39.160</td><td>87.700</td><td>1.069</td><td>$3909.989</td></tr><tr><td>99</td><td>Vietnam</td><td>0.439</td><td>0.562</td><td>152,624.207</td><td>0.499</td><td>0.136</td><td>97.600</td><td>37.590</td><td>70.700</td><td>1.158</td><td>$2170.648</td></tr><tr><td>100</td><td>Honduras</td><td>0.415</td><td>0.613</td><td>9064.824</td><td>0.458</td><td>0.109</td><td>91.200</td><td>50.640</td><td>79.800</td><td>1.061</td><td>($2361.160)</td></tr><tr><td>101</td><td>Rwanda</td><td>0.415</td><td>0.416</td><td>799.406</td><td>0.551</td><td>0.117</td><td>76.100</td><td>50.440</td><td>91.300</td><td>1.058</td><td>($702.836)</td></tr><tr><td>102</td><td>Zambia</td><td>0.415</td><td>0.355</td><td>3824.681</td><td>0.528</td><td>0.111</td><td>65.400</td><td>55.620</td><td>86.300</td><td>1.056</td><td>($1269.574)</td></tr><tr><td>103</td><td>Senegal</td><td>0.415</td><td>0.524</td><td>8423.099</td><td>0.486</td><td>0.108</td><td>78.500</td><td>40.290</td><td>83.600</td><td>0.958</td><td>($952.768)</td></tr><tr><td colspan="10">Low degreeof sustainable development</td><td></td><td></td></tr><tr><td>104</td><td>Nicaragua</td><td>0.415</td><td>0.570</td><td>4569.082</td><td>0.470</td><td>0.112</td><td>87.000</td><td>47.050</td><td>79.000</td><td>0.996</td><td>($2151.382)</td></tr><tr><td>105</td><td>Benin</td><td>0.415</td><td>0.466</td><td>5797.527</td><td>0.526</td><td>0.100</td><td>77.900</td><td>43.440</td><td>78.900</td><td>1.057</td><td>($789.440)</td></tr></table></body></html>

1   
Table 4.22 (continued)   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>indicator) 19</td><td>20</td><td>Earth 21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>106</td><td>Tanzania, United</td><td>0.415</td><td>0.435</td><td>10,751.644</td><td>0.539</td><td>0.098</td><td>55.600</td><td>37.780</td><td>81.800</td><td>0.936</td><td>($877.508)</td></tr><tr><td>107</td><td>Republic of Cote</td><td>0.415</td><td>0.392</td><td>8987.817</td><td>0.556</td><td>0.097</td><td>81.900</td><td>43.180</td><td>97.900</td><td>0.970</td><td>($1534.974)</td></tr><tr><td>108</td><td>dIvoire Swaziland</td><td>0.415</td><td>0.393</td><td>1089.099</td><td>0.537</td><td>0.115</td><td>74.100</td><td>51.450</td><td>87.600</td><td>0.919</td><td>($2770.199)</td></tr><tr><td>109</td><td>Congo, Republic of</td><td>0.418</td><td>0.465</td><td>2482.559</td><td>0.553</td><td>0.105</td><td>76.500</td><td>48.940</td><td>92.200</td><td>1.086</td><td>($1528.245)</td></tr><tr><td>110</td><td>the Madagascar</td><td>0.415</td><td>0.489</td><td>3076.613</td><td>0.497</td><td>0.102</td><td>51.500</td><td>42.650</td><td>84.200</td><td>1.036</td><td>($401.742)</td></tr><tr><td>111</td><td>Cambodia</td><td>0.415</td><td>0.510</td><td>5573.840</td><td>0.431</td><td>0.121</td><td>75.500</td><td>30.760</td><td>87.400</td><td>0.994</td><td>($1269.907)</td></tr><tr><td>112</td><td>Kenya</td><td>0.415</td><td>0.401</td><td>13,300.209</td><td>0.459</td><td>0.108</td><td>63.200</td><td>48.510</td><td>98.300</td><td>0.881</td><td>($1455.360)</td></tr><tr><td>113</td><td>Malawi</td><td>0.415</td><td>0.396</td><td>1272.449</td><td>0.451</td><td>0.111</td><td>90.200</td><td>46.120</td><td>87.600</td><td>1.033</td><td>($300.308)</td></tr><tr><td>114</td><td>Laos</td><td>0.415</td><td>0.541</td><td>2174.531</td><td>0.472</td><td>0.125</td><td>75.700</td><td>37.890</td><td>84.400</td><td>1.066</td><td>($2338.692)</td></tr><tr><td>115</td><td>Guinea</td><td>0.415</td><td>0.471</td><td>2299.209</td><td>0.552</td><td>0.116</td><td>76.800</td><td>33.730</td><td>103.800</td><td>1.022</td><td>($661.528)</td></tr><tr><td>116</td><td>Nepal</td><td>0.415</td><td>0.537</td><td>6501.591</td><td>0.410</td><td>0.116</td><td>91.600</td><td>32.840</td><td>91.200</td><td>1.039</td><td>($729.122)</td></tr><tr><td>117</td><td>Mexico</td><td>0.498</td><td>0.571</td><td>488,602.081</td><td>0.536</td><td>0.134</td><td>96.100</td><td>48.210</td><td>70.400</td><td>1.221</td><td>($8208.556)</td></tr><tr><td>118</td><td>Bangladesh</td><td>0.423</td><td>0.565</td><td>68,950.601</td><td>0.486</td><td>0.114</td><td>86.900</td><td>32.130</td><td>90.700</td><td>1.072</td><td>($1358.779)</td></tr><tr><td>119</td><td>Uganda</td><td>0.415</td><td>0.354</td><td>4895.445</td><td>0.536</td><td>0.106</td><td>79.000</td><td>41.010</td><td>97.700</td><td>0.921</td><td>($580.384)</td></tr><tr><td>120</td><td>Lesotho</td><td>0.415</td><td>0.384</td><td>2295.542</td><td>0.495</td><td>0.104</td><td>81.800</td><td>54.180</td><td>80.900</td><td>1.021</td><td>($1039.704)</td></tr><tr><td>121</td><td>Pakistan</td><td>0.441</td><td>0.479</td><td>153,368.608</td><td>0.485</td><td>0.103</td><td>91.400</td><td>30.690</td><td>101.700</td><td>1.009</td><td>($1443.625)</td></tr><tr><td>122</td><td>Sierra Leone</td><td>0.415</td><td>0.475</td><td>1191.775</td><td>0.552</td><td>0.114</td><td>62.600</td><td>33.990</td><td>91.000</td><td>1.015</td><td>($505.205)</td></tr></table></body></html>

D   

<html><body><table><tr><td>Rank ISD</td><td>Country,</td><td>(ES) Global decrease of energy security</td><td>(GD) Spread of global diseases</td><td>(GW) Global warming (measured in metric tons of carbon dioxide emission)</td><td>(ND) Vulnerability to natural disasters</td><td>(NI) Proliferation (measured with a complex indicator)</td><td>(WA) Limited access to drinking water</td><td>(GINI) Increasing inequality between people and nations on Earth</td><td>(SF) State fragility (measured with the Failed States Index)</td><td>(CSL) Component of Security of Life</td><td>GDP per capita 2016</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>25</td></tr><tr><td>123</td><td>Burkina Faso</td><td>0.415</td><td>0.459</td><td>3058.278</td><td>0.411</td><td>0.111</td><td>82.300</td><td>35.300</td><td>89.400</td><td>0.934</td><td>($627.103)</td></tr><tr><td>124</td><td>Gambia</td><td>0.415</td><td>0.524</td><td>491.378</td><td>0.491</td><td>0.099</td><td>90.200</td><td>47.330</td><td>86.800</td><td>0.963</td><td>($473.190)</td></tr><tr><td>125</td><td>Cameroon</td><td>0.415</td><td>0.411</td><td>6813.286</td><td>0.544</td><td>0.107</td><td>75.600</td><td>46.540</td><td>97.800</td><td>0.918</td><td>($1374.514)</td></tr><tr><td>126</td><td>Turkey</td><td>0.478</td><td>0.555</td><td>323,451.402</td><td>0.555</td><td>0.124</td><td>100.000</td><td>40.180</td><td>77.300</td><td>1.231</td><td>($10,862.600)</td></tr><tr><td>127</td><td>Togo</td><td>0.415</td><td>0.464</td><td>2229.536</td><td>0.548</td><td>0.108</td><td>63.100</td><td>46.020</td><td>85.800</td><td>0.930</td><td>($578.462)</td></tr><tr><td>128</td><td>Mali</td><td>0.415</td><td>0.442</td><td>1026.760</td><td>0.497</td><td>0.111</td><td>77.000</td><td>33.040</td><td>95.200</td><td>0.939</td><td>($779.945)</td></tr><tr><td>129</td><td>Central African</td><td>0.415</td><td>0.439</td><td>297.027</td><td>0.548</td><td>0.119</td><td>68.500</td><td>56.240</td><td>112.100</td><td>1.016</td><td>($382.213)</td></tr><tr><td>130</td><td>Republic Ukraine</td><td>0.450</td><td>0.582</td><td>271,101.310</td><td>0.554</td><td>0.131</td><td>96.200</td><td>24.090</td><td>75.500</td><td></td><td></td></tr><tr><td>131</td><td>Ethiopia</td><td>0.415</td><td>0.354</td><td>10,634.300</td><td>0.504</td><td>0.112</td><td>57.300</td><td>33.170</td><td>97.200</td><td>1.313 0.926</td><td>($2185.728) ($706.757)</td></tr><tr><td>132</td><td>Niger</td><td>0.415</td><td>0.464</td><td>1961.845</td><td>0.452</td><td>0.120</td><td>58.200</td><td>33.990</td><td>98.400</td><td>0.924</td><td>(N/A)</td></tr><tr><td>133</td><td>Angola</td><td>0.437</td><td>0.389</td><td>32,463.951</td><td>0.519</td><td>0.118</td><td>49.000</td><td>42.720</td><td>90.500</td><td>0.903</td><td>($3308.700)</td></tr><tr><td colspan="10">Verylow degre ofsustainable devepent</td><td></td><td></td></tr><tr><td>134</td><td>Mozambique</td><td>0.415</td><td>0.330</td><td>4019.032</td><td>0.517</td><td>0.102</td><td>51.100</td><td>45.580</td><td>87.800</td><td>0.856</td><td>($382.069)</td></tr><tr><td>135</td><td>Syria</td><td>0.416</td><td>0.656</td><td>36,064.945</td><td>0.548</td><td>0.124</td><td>90.100</td><td>N/A</td><td>110.800</td><td>1.187</td><td>(N/A)</td></tr><tr><td>136</td><td>Nigeria</td><td>0.451</td><td>0.284</td><td>95,650.028</td><td>0.535</td><td>0.100</td><td>68.500</td><td>42.970</td><td>103.500</td><td>0.913</td><td>($2175.673)</td></tr><tr><td>137</td><td>Yemen</td><td>0.415</td><td>0.545</td><td>25,346.304</td><td>0.555</td><td>0.117</td><td>54.900</td><td>N/A</td><td>111.500</td><td>1.010</td><td>($990.335)</td></tr></table></body></html>

Based on the data presented in Table 4.22, Fig. 4.26a, b illustrate the indicators of sustainable development and people’s quality of life for different countries and regions of the world.

# 4.6.7 Conclusions

1. This section proposes an approved methodology of application of BBNs to the qualitative analysis of dependences and establishment of causal relations between levels of vulnerability of countries and regions of the world to global threats and indicators of sustainable development in the global context.

2. Measures of specific informativeness of a variable and specific mutual informativeness of variables are introduced that can be used for the selection of essential variables, and also definitions are given for causal relations between them in synthesizing topologies of BBNs. It is shown that the influence of threats such as the vulnerability to natural disasters, balance between the biological productivity of a territory and its total consumption, income inequality, instability of a state on the level of sustainable development of countries of the world is less essential in comparison with other global threats. Therefore, these threats were excluded from consideration.

3. BBNs were modelled with a view to testing $3 ^ { 1 6 }$ hypothesis. We used the significance of $\textsf { \textsf { Q } }$ and the power of $( 1 - \beta )$ as a criterion for data reduction. A method of generalization of the modeling results is proposed that is based on the construction of a Boolean function for a set of collections of evidences, which makes it possible to use the methods of Boolean algebra for obtaining a minimal set of evidences collections justifying each hypothesis.

4. Analysis of the modeling results allows us to draw out the conclusions that the indicators of the sustainable development are closely interrelated, but knowledge of their values does not give grounds for expecting any specific levels of threats. On the other hand, threats are also interconnected, some of which have a direct impact on indicators of the sustainable development, others has an indirect one. If the values of some threats are known then it identifies the level of indicators of the sustainable development in certain cases.

# 4.7 The General Concept of the Periodic Systemic World Conflicts

Investigating the global evolutionary development of the civilization as a complicated, integral, self-organizing system assumes taking into account some interrelated processes and factors of various nature, among which global conflicts occupy one of central places. Finding and constructing general models that would adequately describe the regularities of world conflicts remains one of the most important yet unsolved problems the science is facing. Despite numerous attempts, no adequate scientifically justified metric toolkit has been proposed yet for global forecast and prediction of the development of world conflicts, which is especially necessary when the global civilization enters the XXIst century as a special critical phase of its development [18, 26, 30].

![](images/9b40352866582bf027545bda363a974720ae3746a3d1a83936578bc7c9981d1f.jpg)

![](images/65975dc1b958e04349003682e6b2b9f257b353e411522e9ce15a47c75efa6c62.jpg)

In the context of finding a solution to this problem, being based on systemic generalization of the results of analysis of an extensive empirical material [1, 51, 52], the studies [2, 20, 29] revealed and justified a hypothetical pattern of systemic world conflicts, based on the so-called dynamic model of $C$ -waves, which is based on the “golden section” metric.

In this section we will propose a general concept of $C$ -waves of systemic world conflicts, on the basis of generalization and formalization of the approaches considered in [2, 20, 29]. We will analyze the class of $C$ -waves, which envelopes super-long time intervals. We will show that the pattern of big $C$ -waves is invariant with respect to the evolution of the nature of world conflicts.

# 4.7.1 Some Concepts and Definitions

Let $\mathrm { W _ { c } ( m , n ) }$ be a set of all world conflicts occurred from year $\mathbf { \delta } _ { m }$ th to $\pmb { n }$ th, where m, $n \in Z$ ; $Z$ is the set of integer numbers.

In what follows, we will consider that years of the Common era (AD) correspond to positive numbers $\mathbf { \delta } _ { m }$ and $\pmb { n }$ , and years before Christ (BC) correspond to negative ones.

Let us associate any s that belongs to time interval ${ \mathcal { I } } ( m , n ) ( \mathbf { s } \in { \mathcal { I } } ( m , n )$ $\triangleq [ m , n ] \cap Z )$ with the following group of world conflicts:

$$
\mathcal { L } _ { w _ { c } } ^ { ( s ) } = \{ w _ { c } \in \mathbf { W } _ { c } ( m , n ) | \mathbf { P } ( w _ { c } , s ) = 1 \} ,
$$

where

$$
\mathsf { P } ( w _ { c } , s ) = \left\{ \begin{array} { l l } { 1 , } & { i f \ c o n f l i c t \ w _ { c } \ o c c u r r e d \ i n \ y e a r \ s } \\ { 0 , } & { i f \ c o n f l i c t \ w _ { c } \ d i d \ n o t \ o c c u r \ i n \ y e a r \ s } \end{array} \right.
$$

Basic definition. Let the sequence of the group of world conflicts

$$
\mathcal { L } _ { w _ { c } } ^ { ( m ) } , \mathcal { L } _ { w _ { c } } ^ { ( m + 1 ) } , \mathcal { L } _ { w _ { c } } ^ { ( m + 2 ) } , . . . , \mathcal { L } _ { w _ { c } } ^ { ( n ) }
$$

generate, on the time interval $\mathcal { I } ( m , n )$ , the family

$$
\mathcal { M } _ { c } ( m , n ) = \{ C _ { 1 } , C _ { 2 } , . . . , C _ { N } \}
$$

of waves of Systemic World Conflicts (SWC), briefly SWC-waves or $\mathbf { C }$ -waves, if there exists a block matrix

$$
\begin{array} { r l } { \alpha = [ \overrightarrow { \vert \mathcal { I } \vert } \overrightarrow { \vert \mathcal { X } } ] ^ { [ \mathcal { E } ] } ] = } & { } \\ &  = [ \begin{array} { l } { [ \overrightarrow { \mathcal { I } } _ { 1 , 1 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { 1 , 1 } ^ { [ \mathcal { E } ] } ] = } \\ { [ \overrightarrow { \mathcal { I } } _ { 0 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { 1 , 1 } ^ { [ \mathcal { E } ] } ] ^ { [ \mathcal { I } _ { 0 , 0 } ^ { [ \alpha ] } ] } [ \overrightarrow { \mathcal { I } } _ { 1 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { 1 , 1 } ^ { [ \mathcal { E } ] } ] [ \overrightarrow { \mathcal { E } } _ { 1 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { E } } _ { 1 , 1 } \overrightarrow { \mathcal { E } } _ { 1 , 3 } ] } \\ { [ \overrightarrow { \mathcal { I } } _ { 2 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { 2 , 1 } ^ { [ \mathcal { E } ] } ] ^ { [ \mathcal { I } _ { 0 , 0 } ^ { [ \alpha ] } ] } [ \overrightarrow { \mathcal { I } } _ { 2 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { 2 , 1 } ^ { [ \mathcal { E } ] } ] [ \overrightarrow { \mathcal { E } } _ { 2 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { E } } _ { 2 , 1 } \overrightarrow { \mathcal { E } } _ { 2 , 3 } ] } \\  [ \begin{array} { l l l l } { \mathbb { M } } & { \mathbb { M } } & { \mathbb { M } } & { \mathbb { M } } \\ { \mathcal { I } _ { k , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { k , 1 } ^ { [ \mathcal { I } _ { k , 0 } ^ { [ \alpha ] } ] } [ \underbrace { \mathbb { M } } _ { 1 , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { k , 1 } ^ { [ \mathcal { I } _ { k , 0 } ^ { [ \alpha ] } ] } [ \underbrace { \mathbb { M } } _ { k , 0 } ^ { [ \alpha ] } \underbrace { \mathbb { M } } _ { k , 1 } ^ { [ \mathcal { E } _ { k , 1 } ] } \cdot \underbrace { \mathbb { E } _ { k , 0 } ^ { [ \alpha ] } \mathbb { M } } _ { 1 , 0 } ] ] } \\ { [ \mathbb { M } } & { \mathbb { M } } & { \mathbb { M } } \\  [ \underbrace { \mathcal { I } _ { X , 0 } ^ { [ \alpha ] } \overrightarrow { \mathcal { I } } _ { X , 1 } ^ { [ \alpha ] } } _  = \mathcal { I } _ { X , 1 } ^ { [ \alpha ] } \texttt { Z } _ { X , 2 } \end{array} \end{array} \end{array}
$$

for which the following conditions are true:

$$
\left\{ \begin{array} { l l } { \tau _ { k , 0 } = \tau _ { k + 1 , 0 } + \tau _ { k + 2 , 0 } , \quad k = \overline { { 1 , N - 3 } } , } \\ { \tau _ { N - 1 , 0 } = \tau _ { N , 0 } , } \end{array} \right.
$$

$$
\mathcal { E } _ { k , 0 } < \mathcal { E } _ { k + 1 , 0 } , k = \overline { { 1 , N - 1 } } ,
$$

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \mathcal { E } _ { k , 1 } < \mathcal { E } _ { k , 2 } < \mathcal { E } _ { k , 3 } , } \\ { \mathcal { E } _ { k , 5 } < \mathcal { E } _ { k , 6 } < \mathcal { E } _ { k , 3 } , \quad k = \overline { { 1 , N } } , } \end{array} \right. } \end{array}
$$

where

$$
\left\{ \begin{array} { l } { \tau _ { k , i } = c a r d \mathcal { I } \big ( m _ { k , i } , n _ { k , i } \big ) } \\ { \tau _ { k , 0 } = c a r d \mathcal { I } ( m _ { k } , n _ { k } ) , \quad i = \overline { { 1 , 5 } } , k = \overline { { 1 , N } } } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \mathcal { E } _ { k , i } = \mathcal { E } _ { m _ { k , i } , n _ { k , i } } , i = \overline { { 1 , 5 } } , k = \overline { { 1 , N } } } \\ { \mathcal { E } _ { k , 0 } = \mathcal { E } _ { m _ { k , 0 } , n _ { k , 0 } } = \mathcal { E } _ { m _ { k } , n _ { k } } } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \mathcal { E } _ { m _ { k , i } , n _ { k , i } } = c a r d ^ { - 1 } \mathcal { I } \big ( m _ { k , i } , n _ { k , i } \big ) \cdot \sum _ { s \in \mathcal { I } \big ( m _ { k , i } , n _ { k , i } \big ) } \mathcal { N } _ { w _ { c } } ^ { ( s ) } } \\ { \qquad \quad \sim \mathcal { S } _ { w _ { c } } ^ { ( s ) } = c a r d \mathcal { L } _ { w _ { c } } ^ { ( s ) } } \end{array} \right.
$$

$$
\left\{ \begin{array} { l l } { \mathcal { I } _ { k , 0 } = \mathcal { I } \big ( m _ { k , 0 } , n _ { k , 0 } \big ) = \mathcal { I } ( m _ { k } , n _ { k } ) , k = \overline { { 1 , N } } } \\ { \big ( \mathcal { I } _ { l , 0 } \cap \mathcal { I } _ { r , 0 } = \emptyset \forall l \ne r l , r = \overline { { 1 , N } } \big ) \land \left( \bigcup _ { k = 1 , N } \mathcal { I } _ { k , 0 } = \mathcal { I } ( m , n ) \right) } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \mathcal { I } _ { k , i } = \mathcal { I } \big ( m _ { k , i } , n _ { k , i } \big ) = \mathcal { I } ( m _ { k } , n _ { k } ) , i = \overline { { 1 , 5 } } , k = \overline { { 1 , N } } } \\ { \big ( \mathcal { I } _ { k , l } \cap \mathcal { I } _ { k , r } = \emptyset \forall l \neq r l , r = \overline { { 1 , 5 } } \big ) \land \left( \bigcup _ { i = 1 , 5 } \mathcal { I } _ { k , i } = \mathcal { I } _ { k , 0 } \right) } \end{array} \right.
$$

Elements of matrices $\mathcal { I } = \left\| \mathcal { I } _ { k , \mathrm { i } } \right\| _ { k = \overline { { 1 , N } } , \mathrm { i } = \overline { { 1 , 5 } } }$ $\mathcal { X } = \left. \boldsymbol { \tau } _ { k , \mathrm { i } } \right. _ { k = \overline { { \boldsymbol { \mathscr { I } } , N } } , \mathrm { i = } \overline { { 1 , 5 } } } \mathrm { ~  ~ \cal ~ { ~ M ~ } ~ } \mathcal { E } = \left. \boldsymbol { \mathscr { E } } _ { \mathbf { \Phi } _ { k , \mathrm { i } } } \right. _ { \mathbf { \Phi } _ { k = \overline { { \boldsymbol { I } } , N } , \mathrm { i = } \overline { { 1 , 5 } } } } ,$ define the following parameters of the set $\mathcal { M } _ { c } ( m , n )$ of SWC-waves:

(1) $\mathcal { I } _ { k , 0 }$ —time interval of the life cycle of $C _ { k } -$ wave, $k = \overline { { 1 , N } }$ ; (2) ${ \mathcal { I } } _ { k , i } - i { \mathrm { t h } }$ phase of $C _ { k }$ -wave, $k = \overline { { 1 , N } }$ ; $i = { \overline { { 1 , 5 } } }$ , namely,

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { f _ { k , 1 } \equiv \mathcal { J } _ { k , 1 } - \mathrm { * O r i g i n } \mathrm { * p h a s e } ; } \\ { f _ { k , 2 } \equiv \mathcal { J } _ { k , 2 } - \mathrm { * G r o w t h } \mathrm { * } \mathrm { p h a s e } ; } \\ { f _ { k , 3 } \equiv \mathcal { J } _ { k , 3 } - \mathrm { * G u l m i n a t i o n } \mathrm { * } \mathrm { p h a s e } ; } \\ { f _ { k , 4 } = \mathcal { J } _ { k , 4 } - \mathrm { * D e c r e a s e } \mathrm { p h a s e } ; } \\ { f _ { k , s } \equiv \mathcal { J } _ { k , s } - \mathrm { * O e c a y } \mathrm { p h a s e } ; } \end{array} \right. } \end{array}
$$

(3) $\tau _ { k , 0 }$ —life cycle duration of $C _ { k }$ -wave, $k = \overline { { 1 , N } }$ ;   
(4) $\tau _ { k , i }$ —duration of phase $f _ { k , i }$ , of $C _ { k }$ -wave, $k = \overline { { 1 , N } } , i = \overline { { 1 , 5 } }$ ;   
(5) $\mathcal { E } _ { k , 0 }$ —power of $C _ { k }$ -wave, $k = \overline { { 1 , N } }$ ; $i = { \overline { { 1 , 5 } } }$ ;   
(6) $\mathcal { E } _ { k , i }$ —power of phase $f _ { k , i }$ , of $C _ { k }$ -wave, $k = \overline { { 1 , N } }$ ; $i = { \overline { { 1 , 5 } } }$ .

Definition 1 We will call J ¼ J k;i k 1;N;i 1;5 interval matrix; $\chi = \left| \left| \tau _ { k , i } \right| \right| _ { k = \overline { { 1 , N } } , i = \overline { { 1 , 5 } } }$ —chronometric matrix, and $\mathcal { E } = \left| \left| \mathcal { E } _ { k , i } \right| \right| _ { k = \overline { { 1 , N } } , i = \overline { { 1 , 5 } } }$ energy matrix ofthe evolutionary structuration process $\pi _ { s w c } ^ { e s } ( { \mathcal L } _ { c } ( m , n ) )$ of family $\boldsymbol { \mathcal { M } } _ { c } ( \boldsymbol { m } , n )$ of systemic world conflict waves.

Definition 2 Let the family $\mathcal { M } _ { c } ( \boldsymbol { m } , \boldsymbol { n } )$ of SWC-waves be a uniform complete space-time object defined by block matrix $\textsf { a }$ . We will call $\alpha$ —the ensemble of SWC-waves of systemic world conflicts, briefly, $( S W C ) _ { \alpha }$ -ensemble.

Let us represent it as follows:

$$
\begin{array} { r } { \big ( S W C \big ) _ { \alpha } = \mathrel { \left\{ \left[ C _ { 1 , 1 } \cap C _ { 1 , 2 \dots } \cap C _ { 1 , 5 } \right] \in \left[ C _ { 2 , 1 } \cap C _ { 2 , 2 \dots } \cap C _ { 2 , 5 } \right] \subset \ldots \odot \left[ C _ { \mathrm { N } , 1 } \cap C _ { \mathrm { N } , 2 \dots } \cap C _ { \mathrm { N } , 5 } \right] \right.}  }  \end{array}
$$

where $\ll \int \ d \Omega _ { \rangle \rangle }$ is an operator of local “systemic merge” of “fragments” $C _ { \mathrm { k , i } }$ and $C _ { \mathrm { k , i + 1 } }$ of $C _ { \mathrm { k } }$ -wave, which correspond to phases $f _ { \mathrm { k , i } }$ and $f _ { \mathrm { k , i + 1 } } , \ k = \overline { { 1 , N } } , i = \overline { { 1 , 4 } }$ ; $\langle \langle \mathsf { G } _ { \mathsf { N } }$ is operator of global system merge of $C _ { k }$ and $C _ { k + 1 }$ waves, $k = \overline { { 1 , N - 1 } }$ . We will call

![](images/b6f27225fb8655eb32cd083b48620f1ca401ae544b51dbc49cc4aedfd7b4d7de.jpg)  
Fig. 4.27 Geometric image («phase portrait») of $C _ { \mathrm { k } }$ -wave

number $d i m \big ( \big ( S W C \big ) _ { \alpha } \big ) \equiv N \cdot$ —the dimension of ensemble $( S W C ) _ { \alpha }$ , and time interval $\mathcal { I } ( m , n )$ the interval of manifestation of $( S W C ) _ { \alpha }$ -ensemble.

# 4.7.2 Geometric Images of $C _ { \mathrm { K } }$ -Waves and Ensemble of $( S W C ) _ { \alpha }$ -Waves of Systemic World Conflicts

Let us consider the following geometric images (phase portraits) of $C _ { \mathrm { k } }$ -waves and ensemble of $( S W C ) _ { \alpha }$ -waves of systemic world conflicts:

1. Geometric Image of $C _ { \mathrm { k } }$ -wave, $k = \overline { { 1 , N } }$ , can be represented as the graph (Fig. 4.27a) of the following step function:

$$
\bar { h } _ { C _ { k } } ( t ) = \left\{ \begin{array} { l l } { \mathcal { E } _ { k , 1 } , t \in \left( n _ { k - 1 , 5 } , n _ { k , 1 } \right] , } \\ { \quad \mathcal { E } _ { k , 2 } , t \in \left( n _ { k , 1 } , n _ { k , 2 } \right] , } \\ { \quad \mathcal { E } _ { k , 3 } , t \in \left( n _ { k , 2 } , n _ { k , 3 } \right] , } \\ { \quad \mathcal { E } _ { k , 4 } , t \in \left( n _ { k , 3 } , n _ { k , 4 } \right] , } \\ { \quad \mathcal { E } _ { k , 5 } , t \in \left( n _ { k , 4 } , n _ { k , 5 } \right] , } \end{array} \right.
$$

(where $\mathcal { E } _ { k , \mathrm { i } }$ —is defined from (4.39), (4.40)), or as a graph of some continuous function $\bar { h } _ { C _ { k } } ( t )$ , approximates function $\bar { h } _ { C _ { k } } ( t )$ on the interval $\left[ m _ { k } , n _ { k } \right]$ (Fig. 4.27b).

![](images/505385c7ab5d2d44ed14bc758ef511c9b37ba669c0af36b12c3e13e525d86cf8.jpg)  
Fig. 4.28 A fragment $\left\{ C _ { k } \mathsf { C } _ { \mathsf { C } _ { k + 1 } } \mathsf { C } _ { { k + 2 } } \right\}$ of «collective phase portrait» of the $( \mathrm { S W C } ) _ { \alpha } -$ ensemble $\left\{ C _ { 1 } \mathsf { G } C _ { 2 } \mathsf { G } \ldots \mathsf { G } C _ { N } \right\}$

2. Geometric Image of the Ensemble of $( S W C ) _ { \alpha }$ -waves of systemic world conflicts (“collective phase portrait” of the family $\mathcal { M } _ { c } ( \boldsymbol { m } , n )$ of $C _ { \mathrm { k } }$ -waves, $k = \overline { { 1 , N } } )$ can be represented as the graph (Fig. 4.28a) of the following step function:

$$
\bar { h } _ { C } ( t ) = \bar { h } _ { C _ { k } } ( t ) , t \in [ m _ { k } , n _ { k } ] , k = \overline { { 1 , N } } ,
$$

(where function $\bar { h } _ { C _ { k } } ( t )$ is defined from (4.46)), or by the graph of some continuous function $\bar { h } _ { C } ( t )$ that approximates function $\bar { h } _ { C } ( t )$ on the interval $[ m , n ]$ (Fig. 4.28b).

# 4.7.3 Significant Features of SWC-Concept

We will assume that the correspondence of the SWC-concept under study to the structural harmony principle is its main key feature (F1) [29].

Let

$$
T ( C _ { k } ) = \tau _ { k , 0 } , \tau _ { N - 1 , 0 } = \tau _ { N , 0 } = k _ { c } .
$$

Then, according to (4.38) and (4.41), variation in life cycle duration of the $T ( C _ { k } )$ —sequence of $C _ { k }$ -waves, $k = \overline { { 1 , N } }$ , obeys the following principle:

$$
T ( C _ { k } ) = F _ { N - k + 1 } \cdot k _ { c } ,
$$

where $F _ { N - k + 1 }$ —is a number from the Fibonacci sequence. This testifies that golden section is present in the structure of $( S W C ) _ { \alpha }$ -ensemble; and according to the structural harmony principle [23], in any self-organizing system, special time scale corresponds to each operating mode that varies according to variation of structural states of the system. This time scale is “tied” to a certain invariant of generalized golden section as a characteristic of steady state of the system.

We will call constant $k c$ a universal time metric quantum of the life cycles of $C _ { k }$ - waves of $( S W C ) _ { \alpha }$ -ensemble. In what follows, we will call the Fibonacci regularity (4.38), (4.41), (4.49), (4.50) of the development of systemic world conflicts the F-regularity.

The second key feature (F2) of the considered concept is that the universal effect of acceleration of historical time is revealed in the proposed dynamic model of $C .$ - waves [19, 24, 27] since according to (4.38), (4.41) successive reduction of the

![](images/b902e756f10c551b2ba5675d662181c47660ad6e3aae87a9ac410af12eaf76c8.jpg)  
Fig. 4.29 Illustration of strict order of $C _ { k }$ -waves with respect to power $\mathcal { E } _ { i , k }$ of phases $f _ { k , i }$ $, k = { \overline { { 1 , \mathbf { N } } } } , \ i = { \overline { { 1 , 5 } } }$ of their evolutionary development

$$
{ \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c } { \operatorname { F } ( { \mathrm { N } } ) \to \ \operatorname { F } ( { \mathrm { N } } - 1 ) \to \cdots \to \operatorname { F } ( { \mathrm { N } } - 1 + 1 ) \to \cdots \to \operatorname { F } ( 2 ) \to \operatorname { F } ( 1 ) \to \operatorname { F } ( 0 ) = { \underline { { \operatorname { F } } } } } & & & & & & & & & \\ { \downarrow } & { \downarrow } & & { \downarrow } & & & & { \downarrow } & & & { \downarrow } & & & \\ { { \mathfrak { D } } _ { g } ^ { \texttt { C } _ { 1 } } \to } & { \complement } & { \complement } & { \to \cdots \to } & { \complement } & { \underset { \downarrow } { \to } } & { \to \cdots \to } & { \complement _ { N - 1 } \to } & { \mathbb { C } _ { N } } & & & & \\ { \downarrow } & & { \downarrow } & & & { \downarrow } & & & { \downarrow } & & & { \downarrow } & & & \\ { \mathrm { T } _ { 1 } } & { \to } & { \Sigma } & { \Sigma } & { \to \cdots \to } & { \mathbb { T } _ { k } } & { \to \cdots \to } & { \mathbb { T } _ { N - 1 } \to } & { \mathbb { T } _ { N } } & & & & \\ { \downarrow } & & { \downarrow } & & & { \downarrow } & & & { \downarrow } & & & { \downarrow } & & \\ { \Omega _ { 1 } } & { \to } & { \Omega _ { 2 } } & { \to \cdots \to } & { \Omega _ { k } } & { \to \cdots \to } & { \Omega _ { N - 1 } \to } & { \Omega _ { N - 1 } \to } & { \Omega _ { N } } & { \to } & & & { \uparrow } \end{array} }
$$

duration of life cycles of $C$ -waves of the development of systemic world conflicts takes place as an essential component of the integral evolutionary development of the civilization.

The third important property (F3) of $C _ { k }$ -waves is their strict hierarchy with respect to the power $\mathcal { E } _ { i , k }$ of phases $f _ { k , i }$ , $k = \overline { { 1 , \mathrm { N } } }$ ; $i = { \overline { { 1 , 5 } } }$ , of their evolutionary development (Fig. 4.29).

Based on the features F1–F3 and taking into account (4.34–4.48) and Figs. 4.27, 4.28, it follows that the family $\boldsymbol { \mathcal { M } } _ { c } ( \boldsymbol { m } , n )$ of $C _ { k }$ -waves forms the sequence of irregular, self-similar, local objects that, in turn, allows us to consider the $( S W C ) _ { \alpha } .$ - ensemble of waves of systemic world conflicts as a global, integral, self-organizing space–time object of fractal nature.

# 4.7.4 Correlation of Processes of Evolutionary Development of Civilization $\boldsymbol { \Pi } _ { C } ^ { E d }$ and Development of C-Waves of Systemic World Conflicts $\pi _ { s w c } ^ { e s } ( { \mathcal L } _ { c } ( m , n ) )$

Let us denote by M civilization as an integral, open, dynamic, self-organizing system. Let $\Omega ( \mathbf { M } )$ be the set of various states of system M. Let also $\Psi : \mathcal { I } _ { \infty } \longmapsto \Omega ( \mathbf { M } )$ , where $\mathcal { I } _ { \infty } \equiv \{ \mathcal { I } ( \boldsymbol { m } , \boldsymbol { n } ) \} _ { { m } , { n } \in { Z } }$ be mapping generated by the process $\pi _ { C } ^ { e d }$ of natural evolutionary development of system M.

Definition 3 We will call $\Psi [ \mathcal { I } ( m _ { k } , n _ { k } ) ] \equiv \Omega ( C _ { k } ) = \Omega _ { k } , k = \overline { { 1 , N } }$ , the $( { \mathcal { F } } , k )$ -state of system $\mathcal { M }$ and call $\Psi \big [ \mathcal { I } \big ( m _ { k , i } , n _ { k , i } \big ) \big ] \equiv \Omega \big ( C _ { k , i } \big ) = \Omega _ { k , i } , k = \overline { { 1 , N } } , i = \overline { { 1 , 5 } } ,$ , the $( \mathcal { F } , k , i )$ -state of system $\mathcal { M }$ .

Since $F _ { N - k + 1 } \in \varnothing \forall k > N$ , the sequence of Fibonacci numbers $\left\{ F _ { N - k + 1 } \right\} _ { k \in N }$ is degenerated for $k > N$ ; therefore, the F-regularity revealed on the time interval $\mathcal { I } ( m , n )$ for the development of systemic world conflicts on the time interval $t > n$ is not true anymore.

Figures 4.29 and 4.30 show the diagrams $D _ { g }$ , $D _ { l o c } ^ { ( k ) }$ , and $D _ { l o c }$ , which illustrate the correlation between process $\pi _ { C } ^ { e d }$ of evolutionary development of the civilization and process $\pi _ { s w c } ^ { e s } ( \mathcal { L } _ { c } ( m , n ) )$ of evolutionary structurization of the sequence of $C _ { k }$ -waves of systemic world conflicts (in the global and local contexts) (Fig. 4.31).

![](images/b33d5c3db7ce741935ab38358f3c9c4a3cbe3c1472d2d966bff75d38028b4753.jpg)  
Fig. 4.31 Illustration of the correlation between the process $\pi _ { C } ^ { e d }$ of evolutionary development of the civilization and process $\pi _ { s w c } ^ { e s } ( { \mathcal L } _ { C } ( m , n ) )$ of evolutionary structurization of the family of $C _ { k }$ - waves of systemic world conflicts (local context): a for $C _ { k }$ -waves; $\mathbf { b }$ for the family $\mathcal { M } _ { c } ( \boldsymbol { m } , n )$ of $C _ { k }$ -waves $( T _ { k , i } \equiv \mathcal { I } { \left( m _ { k , i } , n _ { k , i } \right) } , \Omega _ { k , i } \equiv \Psi \left[ \mathcal { I } { \left( m _ { k , i } , n _ { k , i } \right) } \right] \in \Omega ( \mathcal { M } ) , k = \overline { { 1 , N } } , i = i = \overline { { 1 , 5 } } )$

# 4.7.5 The Problem of Identification (Recognition) of $c$ -Waves of Systemic World Conflicts for Big Historical Data

Let us use the above definitions and notation and consider the general solution scheme for the problem of identification of $C$ -waves of systemic world conflicts for big historical data.

The First Stage. Statistical analysis of historical data and definition of the set $W _ { c } ( r , l )$ of all world conflicts that took place from year rth to year lth. By world conflicts we will mean conflicts that claimed no less than 1000 lives according to available information sources.

The Second Stage. Generating the sequence $\left\{ \mathcal { L } _ { w c } ^ { ( s ) } \right\} _ { s \in \mathcal { ( I } ( r , l ) ) }$ of groups of world conflicts (4.34).

The Third Stage. Solving the problem of the existence, on the chosen time intervals $\mathcal { I } ( m , n )$ , of block matrices of the form $\boldsymbol { \alpha } = [ \mathcal { I } \pmb { \chi } \mathcal { E } ]$ that satisfy conditions (4.38–4.45) and developing the algorithms to construct such matrices.

We will distinguish two essentially different cases.

Case 1 Assume that the required block matrix $\boldsymbol { \mathfrak { X } }$ is constructed on the time interval: $\mathcal { I } ( \boldsymbol { m } , \boldsymbol { n } )$ , where $r \leq m < n \leq l .$ This means that the family $\mathcal { M } _ { c } ( \boldsymbol { m } , n )$ of identified $C _ { k }$ -waves, $k = \overline { { 1 , N } }$ , “completely falls within” the initial time interval $\mathcal { I } ( r , 1 )$ . It is obvious that in this case the family $\mathcal { M } _ { c } ( \boldsymbol { m } , n )$ was “revealed” and “remained” as a completed integral object in the historical past.

In this case, for the process of evolutionary structurization of the $( S W C ) _ { \alpha }$ - ensemble of waves of systemic world conflicts on the time interval $\mathcal { I } ( m , n )$ , we will call block matrix $\alpha$ an empirical matrix; $\mathcal { I }$ an empirical interval matrix; $\pmb { \chi }$ an empirical chronometric matrix; and $\mathcal { E }$ an empirical energy matrix.

Case 2 Let on the considered time interval $\mathcal { I } ( r , \ l )$ only the fragment $\big \{ C _ { 1 } \mathsf { G } _ { } C _ { _ 2 } \mathsf { G } _ { \therefore \cdot } \mathsf { G } _ { } C _ { _ M } \big \}$ of some integral ensemble $\big ( S W C \big ) _ { \alpha } = \big \{ C _ { 1 } \mathsf { G } C _ { 2 } \mathsf { G } _ { \beta \dots } \mathsf { G } C _ { N } \big \}$ be “revealed” and “completely fall” within it, and let it be identified by the first $M$ rows of some block matrix $\boldsymbol { \mathfrak { X } }$ of the form (4.34), namely, by elements $\mathcal { T } _ { k , i } , \ \tau _ { k , i } , \ \mathcal { E } _ { k , i } .$ , $k = \overline { { 1 , M } } , i = \overline { { 1 , 5 } }$ , constructed on the basis of empirical material. It is natural that this number $M$ should be large enough for the hypothetical statement about the manifestation of the F-regularity for the first $M$ waves of $( S W C ) _ { \alpha }$ -ensemble.

A “missing” fragment $\left\{ C _ { M + 1 , } C _ { M + 2 } , \dots \dots , C _ { N } \right\}$ of the ensemble, which is hypothetically defined by the unknown elements $\mathcal { T } _ { k , i } , \tau _ { k , i }$ , and $\mathcal { E } _ { k , i }$ for $M < k \leq N ,$ , $i = { \overline { { 1 , 5 } } }$ , can be “restored” according to (4.38–4.45), by extrapolating the revealed F-regularity for $M < k \leq N , i = { \overline { { 1 , 5 } } }$ . To improve and correct the values of ${ \mathcal { I } } _ { k , i }$ , $\tau _ { k , i }$ , and $\mathcal { E } _ { k , i }$ for $M < k \ \leq \ N , \ i = \ \overline { { 1 , 5 } }$ , we can use additional information and factors of various nature from adjacent scientific fields (Fig. 4.32). In this case, we

(a) [ $\mathcal { I } _ { 1 , 0 }$ $\mathcal { I } _ { 1 , 5 }$ $C _ { 1 }$ $\mathcal { I } _ { 2 , 0 }$ J1 $C _ { 2 }$   
7 M0 JM1 JMs $C _ { M }$ JM+1 M+1,0 JMH,1. $\mathcal { I } _ { \mathrm { M } + 1 , 5 }$ 1 Determining M+2,0 M+2,5 CM+2 empiricalvalues … JTE JN $\underline { { \mathcal { I } _ { \mathrm { N . l } } } }$ $\underline { { \mathcal { I } _ { \mathrm { N } , 5 } } }$ $C _ { N }$ fork=1,M,i=1,5 立 Establishing empirical   
(b) $\tau _ { { \scriptscriptstyle 1 } , { \scriptscriptstyle 0 } }$ $\tau _ { { \mathfrak { l } } , { \mathfrak { l } } }$ $C _ { 1 }$ F-pattern $\tau _ { 2 , 1 }$ $\cdots \tau _ { 2 , 5 }$ $C _ { 2 }$ ↓ Extrapolation:   
$\mathcal { X } = \left| \frac { \tau _ { _ { \mathrm { M } , 0 } } } { \left| \tau _ { _ { \mathrm { M } + 1 , 0 } } \begin{array} { c c c c } { { \tau _ { _ { \mathrm { M } , 1 } } } } & { { \cdots } } & { { \tau _ { _ { \mathrm { M } , 5 } } } } \\ { { \overline { { \tau } } _ { _ { \mathrm { M } + 1 , 0 } } } } & { { \tau _ { _ { \mathrm { M } + 1 , 1 } } } } & { { \cdots } } & { { \tau _ { _ { \mathrm { M } + 1 , 5 } } } } \end{array} \right| C _ { M } } \right|$ CM $C _ { M + 1 } |$ hypotheticalvalues determining ： $\tau _ { \mathrm { M } + 2 , 5 }$ 1 CM+2 / for $k = \overline { { M + 1 , N } } , i = \overline { { 1 , 5 } }$ $\mathcal { I } _ { \boldsymbol { k } , i } , \mathsf { T } _ { \boldsymbol { k } , i } , \pounds _ { \boldsymbol { k } , i } .$ L $\underline { { \textrm { N . 0 } } }$ TN1 $\underline { { \tau _ { \mathrm { ~ N } , 5 } } }$ $C _ { N }$ →   
(c) [ $\mathcal { E } _ { 1 , 0 }$ $\boldsymbol { \varepsilon } _ { \scriptscriptstyle { 1 , 1 } }$ ε $\displaystyle \mathcal { E } _ { 1 , 5 }$ $C _ { 1 }$ $\mathcal { E } _ { 2 , 0 }$ 3 C2.1 $C _ { 2 }$ £ £ ..εMs   
5 三 EM+1. EM41 . εMH., $C _ { M + 1 }$ $C _ { M }$ Additional conditions 3 £ 3 CM+2.0 CM+2.5 CM+2Y … ENO 3 CN1 .£ CN.5 CN

will talk about the hypothetical F-regularity of the development of systemic world conflicts on the time interval $\mathcal { I } ( \boldsymbol { m } , n )$ . For the process of evolutionary structurization of $( S W C ) \alpha$ -ensemble on the time interval $\mathcal { I } ( m , n )$ , we will call block matrix $\textsf { \textsf { Q } }$ hypothetic matrix, $\mathcal { I }$ hypothetic interval matrix, $\pmb { \chi }$ hypothetic chronometric matrix, and $\mathcal { E }$ hypothetic energy matrix.

![](images/a42a801603edb462bd71e62ff65c4f6cb02e11fd8c07ab9810de7007f34748cf.jpg)  
Fig. 4.33 Illustration of the invariance of the development of big $C _ { k }$ -waves with respect to the evolution of the nature of world conflicts, $k = \overline { { 1 , 7 } }$

# 4.7.6 Big C-Waves of Systemic World Conflicts

According to the basic definition, various classes (families) of $C$ -waves of systemic world conflicts can hypothetically exist on different time intervals. However, as follows from [25, 53], of greatest interest among them are classes of $C$ -waves that envelope superbig time intervals, whose F-regularity of the development is invariant with respect to the evolution of the nature of world conflicts. In what follows, it is such $C \mathrm { \cdot }$ -waves that we will call big waves of systemic world conflicts (briefly, big $C _ { }$ - waves). Note that knowledge about the structural parameters of big $C$ -waves plays an important role in the development of new metric approaches in solving problems of predicting global periodic civilization processes of various nature [1, 2, 53].

On the basis of systematically generalized results of analysis of the empirical sequence of world conflicts that took place from $2 5 0 0 ~ \mathrm { B C }$ to 2007 AD [4–6], the studies [7–9] identify the ensemble $\mathrm { ( S W C ) } _ { \alpha } = \left\{ C _ { 1 } \mathsf { G } C _ { 2 } \mathsf { G } \ldots \mathsf { G } C _ { 7 } \right\}$ of big $C$ -waves of world conflicts (of dimension dim $( \left( S W C \right) _ { \alpha } ) = 7 ;$ on superbig time interval $\mathcal { I }$ $( - 7 5 0 ; 2 0 9 2 )$ of approximately 3000 years, which envelopes various epochs of the development of the civilization. The invariance of F-regularity of the development of the identified $C _ { k }$ -waves with respect to the evolution of the nature of world conflicts is illustrated by Fig. 4.33.

![](images/03f78c6794c97fdd1e7947d67050949ebc2c1cc0b63289984c75b6a474f4a386.jpg)  
Fig. 4.34 Contribution of energy safety (ES) threat to the conflict of 21st century [2]

On the time interval $\mathcal { I } ( - 7 5 0 , 2 0 0 7 )$ , six “exhibited” $C _ { k }$ -waves of systemic world conflicts were identified. Structural parameters of the seventh, final (predicted) wave $C _ { 7 }$ are found by extrapolating the revealed F-regularity for the fragment $\left\{ C _ { 1 } \mathsf { G } _ { \mathsf { } } C _ { _ 2 } \mathsf { G } _ { C _ { 3 } } \mathsf { G } _ { C _ { 4 } } \mathsf { G } _ { C _ { 5 } } \mathsf { G } _ { C _ { 6 } } \right\}$ of the $( S W C ) _ { \alpha }$ -ensemble of waves of systemic world conflicts.

To improve and update the predicted values of structural parameters of wave $C _ { 7 }$ , we used additional information from various adjacent scientific fields. For example, we took into account the influence of 12 global threats that can “heat up” the global world conflict generated by the wave $C _ { 7 }$ , called the “Conflict of the 21st century” (Table 4.3).

We also took into account possible influence of some other special local factors on the values of structural parameters of the predicted $C _ { 7 }$ -wave. Some of them are presented in Fig. 4.34 for energy safety (ES) threat, where $t _ { H K } ^ { * }$ is the Horner– Kapitsa singularity point [21]; $t _ { N } ^ { * }$ is the Newton singularity point. We also specified critical time intervals related to exhaustion of traditional energy resources of the Earth: oil (O), gas (G), and uranium (U).

We have found the values of elements ${ \mathcal { I } } _ { k , i }$ , $\tau _ { k , i }$ , $\mathcal { E } _ { k , i }$ , $k = \overline { { 1 , 7 } } , i = \overline { { 1 , 5 } }$ , of the hypothetic block matrix $\boldsymbol { \alpha } = [ \mathcal { I } \pmb { \chi } \mathcal { E } ]$ of the process of evolutionary structurization of $( S W C ) _ { \alpha }$ -ensemble $\{ C _ { 1 } \mathsf { G } _ { } C _ { 2 } ^ { } \mathsf { G } _ { \bot \bot } \mathsf { G } _ { } C _ { 7 } ^ { } \} { \mathsf { c } }$ of big $C _ { k }$ -waves of systemic world conflicts.

Elements $\mathcal { T } _ { k , i } , k = \overline { { 1 , 7 } } , i = \overline { { 1 , 5 } }$ , of the hypothetical interval matrix $\mathcal { I }$ of the process of evolutionary structurization of the sequence of $C _ { k }$ -waves on time interval $\mathcal { I } ( - 7 5 0 ; 2 0 9 2 )$ are as follows:

， $\cdot \mathcal { T } _ { 1 , 0 } = I ( - 7 0 5 ; 4 0 1 )$ $\begin{array} { r l r l } & { - 7 0 3 5 . 4 0 1 ) , } & & { \mathcal { I } _ { 1 , 1 } = I ( - 7 . 8 0 5 5 - 5 0 0 ) , } & { \mathcal { I } _ { 1 , 2 } = I ( - 4 9 9 5 - 3 3 5 ) } \\ & { \mathrm { i } 0 2 . 1 0 7 4 \rangle , } & & { \mathcal { I } _ { 2 , 1 } = I ( 4 0 2 . 6 8 1 ) , } & & { \mathcal { I } _ { 2 , 2 } = I ( 6 3 2 . 8 2 6 ) , } \\ & { 0 7 5 . 1 4 9 7 ) , } & & { \mathcal { I } _ { 3 , 1 } = I ( 1 0 7 5 . 1 1 4 6 ) , } & & { \mathcal { I } _ { 3 , 2 } = I ( 1 1 4 7 . 1 0 7 1 2 0 ) , } \\ & { 4 9 8 . 5 1 7 4 9 ) , } & & { \mathcal { I } _ { 4 , 1 } = I ( 1 1 9 8 . 1 5 6 6 ) , } & & { \mathcal { I } _ { 4 , 2 } = I ( 1 5 6 7 . 1 6 8 8 ) , } \\ & { 5 2 0 . 1 5 9 1 9 , } & & { \mathcal { I } _ { 5 , 1 } = I ( 1 7 5 0 . 1 7 8 8 ) , } & & { \mathcal { I } _ { 5 , 2 } = I ( 1 7 9 9 . 1 8 0 ) , } \\ & { 0 9 0 . 2 0 9 9 2 , } & { \mathcal { I } _ { 6 , 1 } = I ( 1 2 0 0 . 1 9 2 0 ) , } & & { \mathcal { I } _ { 7 , 2 } = I ( 1 0 2 9 . 2 0 9 1 2 ) , } \\ & { - 3 0 3 . 4 4 , } & & { \mathcal { I } _ { 1 , 4 } = I ( 2 0 0 2 . 4 0 0 ) , } & & { \mathcal { I } _ { 1 , 5 } = I ( - 6 2 . 4 0 1 ) , } \\ & { 8 2 . 7 9 7 0 , } & { \mathcal { I } _ { 7 , 4 } = I ( 9 7 1 . 1 0 7 4 ) , } & & { \mathcal { I } _ { 2 , 5 } = I ( 9 7 . 1 0 0 4 ) , } \\ & { 2 0 8 . 1 2 8 1 , } & & { \mathcal { I } _ { 3 , 4 } = I ( 1 2 8 2 . 1 4 3 6 ) , } & & { \mathcal { I } _ { 3 , 5 } = I ( 1 4 3 9 . 1 4 9 7 ) , } \\ & { 6 3 9 . 1 6 0 0 , } & { \mathcal { I } _ { 4 , 4 } = I ( 1 6 6 1 . 1 7 8 ) , } & { \mathcal { I } _ { 4 , 5 } = I ( 1 7 . 1 9 1 . 1 2 9 1 ) , } \\ & { 6 3 9 . 1 8 0 9 , } & { \mathcal { I } _ { 4 , 4 } = I ( 1 6 1 . 1 7 8 ) , } & { \mathcal { I } _ { 4 , 5 } = I ( 1 1 . 9 1 . 1 2 0 9 ) , } \\ & { 8 . 1 9 9 , } &  \mathcal { I } _  \end{array}$   
$\mathcal { T } _ { 2 , 0 } = I ( 4 0 2 ; 1 0 7 4 ) .$   
$\mathcal { T } _ { 3 , 0 } = I ( 1 0 7 5 ; 1 4 9 7 )$   
$\mathcal { T } _ { 4 , 0 } = I ( 1 4 9 8 ; 1 7 4 9 )$   
$\mathcal { T } _ { 5 , 0 } = I ( 1 7 5 0 ; 1 9 1 9 )$   
$\mathcal { T } _ { 6 , 0 } = I ( 1 9 2 0 ; 2 0 0 7 )$   
$\mathcal { T } _ { 7 , 0 } = I ( 2 0 0 8 ; 2 0 9 2 )$   
:  
$\mathcal { I } _ { 1 , 3 } = I ( - 3 3 4 ; - 6 3 )$   
$\mathcal { I } _ { 2 , 3 } = I ( 8 2 7 ; 9 7 0 )$   
$\mathcal { T } _ { 3 , 3 } = I ( 1 2 0 8 ; 1 2 8 1 )$   
$\mathcal { T } _ { 4 , 3 } = I ( 1 6 3 9 ; 1 6 6 0 )$   
$\mathcal { T } _ { 5 , 3 } = I ( 1 8 0 1 ; 1 8 1 9 )$   
$\mathcal { T } _ { 6 , 3 } = I ( 1 9 8 9 ; 1 9 9 6 )$   
1 $\mathcal { T } _ { 7 , 3 } = I ( 2 0 4 8 ; 2 0 6 0 )$

Elements $\tau _ { k , i }$ , $k = \overline { { 1 , 7 } } , i = \overline { { 1 , 5 } }$ , of the hypothetical chronometric matrix $\pmb { \chi }$ of the process of evolutionary structurization of the sequence of $C _ { k }$ -waves on the time interval $\mathcal { I }$ (−750; 2092) are as follows:

$$
\begin{array}{c} \chi : \{ \begin{array} { l l } { \tau _ { 1 , 0 } = 1 1 0 7 , } & { \tau _ { 1 , 1 } = 2 0 6 , } \\ { \tau _ { 2 , 0 } = 6 7 3 , } & { \tau _ { 2 , 1 } = 2 3 0 , } \\ { \tau _ { 3 , 0 } = 4 2 3 , } & { \tau _ { 3 , 1 } = 7 2 , } \\ { \tau _ { 4 , 0 } = 2 5 2 , } & { \tau _ { 4 , 1 } = 6 9 , } \\ { \tau _ { 5 , 0 } = 1 7 0 , } & { \tau _ { 5 , 1 } = 2 9 , } & { \tau _ { 6 , 2 } = 2 , } \\ { \tau _ { 6 , 0 } = 8 8 , } & { \tau _ { 6 , 1 } = 3 9 , } & { \tau _ { 6 , 2 } = 3 0 , } \\ { \tau _ { 7 , 0 } = 8 5 , } & { \tau _ { 7 , 1 } = 1 2 , } & { \tau _ { 7 , 2 } = 2 6 , } \end{array}  \quad \tau _ { 1 , 3 } = 2 7 2 , \quad \tau _ { 1 , 4 } = 4 6 4 , \quad \tau _ { 1 , 5 } = 4 6 4 ,  \\ { \tau _ { 7 , 3 } = 3 2 , } & { \tau _ { 3 , 4 } = 1 0 4 , } \\ { \tau _ { 4 , 0 } = 2 5 , } & { \tau _ { 4 , 1 } = 1 2 , } \end{array} 
$$

Elements $\mathcal { E } _ { k , i }$ , $k = \overline { { 1 , 7 } } , i = \overline { { 1 , 5 } }$ , of the hypothetical energy matrix $\mathcal { E }$ of the process of evolutionary structurization of the sequence of $C _ { k }$ -waves on the time interval $\mathcal { I } ( - 7 5 0 ; 2 0 9 2 )$ :

A key feature of the identified family of big $C _ { k }$ -waves, $k = \overline { { 1 , 7 } }$ , of systemic world conflicts is that the most powerful (predicted) final $C _ { 7 }$ -wave completely “falls within” the 21st century, and according to different independent sources [2, 24, 26, 27, 30, 54–58], the peak of “System tsunami of the 21st century” or “New phase passage” is in its middle. If the trends formed at the previous phases of the history remain the same, these shocks will hypothetically lead the mankind to another phase of the development (a combination of technological progress and a big war [58] as the most probable scenario).

Canada 0 Population 35848 610 S GDP per capita: \$42183.295   
00o0 SUSTAINABLEDEVELOPMENTINDEX N2 1,116 N1Australia . Ne3Germany Verylow Low Medium High Very High   
品 QUALITYOFLIFE Ne12 1,398 le ， 1.0 Canada 0.5 Economic: 0,722 PeerGroup Environmental: 0,765 Social: 0,638 Is lec Harmonizationdegree: 0,951 Very low Low Medium High Very High   
D SAFETY OFLIFE N1 1,763 BB Biodiversity Balance 0,215 ， CI Conflicts Intencity 0,224 IG InformationGap 0,191 BB CP Corruption Perception 0,136 SF10 E CI GD ES EnergySafety GlobalDiseases 0,060 0,406 GINI 0 IG GW GlobalWarming 0,575 WALO CP ND Natural Disasters 0,340 NI MilitaryProlifiration 0,098 NM ES W WateFfdess 03 ND GD GW Very low Low Medium High Very High PeerGroup Countriesby Safetyof life Australiak Luxembourgthrlads,NewZlad,oayingaporewdenwitlad,Uiteddo,

UnitedStates

Establishing the relationship between the results of the studies obtained in the previous sections, namely:

– regularity of the emergence of systemic world conflicts (Sect. 4.2);

Finland O Population 5479531 \$ GDP percapita: \$43401.228 SUSTAINABLEDEVELOPMENTINDEX Ne5 1,096 N4 Switzerland . Ne6 Denmark   
Verylow Low Medium High Very High   
品 QUALITY OF LIFE N911 1,399 1,0 Finland 0.5 Economic: 0,634 PeerGroup Environmental: 0,822 Social: 0,674 ls lec Harmonization degree： 0,947   
Very low Low Medium High Very High   
D SAFETYOFLIFE N2 1,696 BB Biodiversity Balance 0,243 ， CI Conflicts Intencity 0,224 IG Information Gap 0,203 BB CP Corruption Perception 0,101 SF1,0 CI G Enebal Disetyes 0,534 GINI 0 IG GW Global Warming 0,451 WALO nCP ND NaturalDisasters 0,331 NI MilitaryProlifiration 0,218 NM ES S WeFrg 030 ND GD GW   
Verylow Low Medium High Very High PeerGroupCountriesby Safety oflife   
Australiatriagidaemrk,ceGmnyelnd,eladaly   
Luxembosiid States

interrelation between the periodic processes in the global economy and systemic world conflicts (Sect. 4.3); the relationship between the sequence of 11-year Schwabe-Wolf cycles of solar activity and the family of C-waves of global systemic conflicts (Sect. 4.5);

Australia Population 23789338 GDP per capita: \$49755.315   
00o0 SUSTAINABLEDEVELOPMENTINDEX N1 1,120 Ng2 Canada Very low Low Medium High Very High   
g QUALITYOFLIFE le Ne2 . 1,459 1,0 Australia 0,5 Economic: 0,724 PeerGroup Environmental: 0,788 Social: 0,694 ls lec Harmonizationdegree: 0,955 Verylow Low Medium High Very High   
园 SAFETYOFLIFE Ne3 1,687 BB Biodiversity Balance 0,234 ， CI Conflicts Intencity 0,224 IG Information Gap 0,178 BB CP Corruption Perception 0,154 SF10 CI E Enera Sisetyes 0,25 GINI 0 IG GW GlobalWarming 0,547 WAO CP ND Natural Disasters 0,360 NI MilitaryProlifiration 0,222 NI ES WA WaterAccess 0,310 ND GD GINI Inequality 0,426 GW SF StateFragility 0,125 Verylow Low Medium High Very High PeerGroup Countriesby Safety of life Austria,girkidydaly

Luxembourgthrlads,NewZlad,oayingaporewdenwitlad,Uiteddo, UnitedStates

– the impact of global threats on the sustainable development of countries and regions of the world (Sect. 4.6).

We present the generalized profiles of the three most secure countries in the world (Canada—Fig. 4.35, Finland—Fig. 4.36, Australia, Fig. 4.37), the two

United States .0 Population 320896618 GDP percapita: \$57638.159 SUSTAINABLEDEVELOPMENTINDEX Ne15 1,065   
0UoU N14UnitedKingdom ， No16 Ireland Verylow Low Medium High Very High   
奇 QUALITYOFLIFE Ne7 1,419 10e United States Economic: 0,759 0.5 PeerGroup Environmental: 0,761 Social: 0,640 1s lec Harmonization degree: 0,933 Verylow Low Medium High Very High   
园 SAFETYOFLIFE Ne19 1,559 BB BiodiversityBalance 0,736 L CI Conflicts Intencity 0,685 IG Information Gap 0,161 BB CP Corruption Perception 0,188 SF10 F CI ES EnergySafety 0,002 GINIO IG GD Global Diseases 0,405 GW GlobalWarming 0,997 WALOO nCP ND Natural Disasters 0,371 NI MilitaryProlifiration 0,375 NM 3ES S WateFrg 0.3 ND GD GW   
Very low Low Medium High Very High Peer Group Countries by Safety of life   
Australiataeirkdeyedelda

Korea,gsyeeUed countries with the largest nuclear potential (USA—Fig. 4.38, Russia—Fig. 4.39) and three countries with the lowest level of national security (Angola—Fig. 4.40, Kenya—Fig. 4.41, Mozambique—Fig. 4.42).

RussianFederation .0 Population 144 096870 GDPpercapita: \$8748.369   
1 SUSTAINABLE DEVELOPMENTINDEX Ne62 0,769 Ne63 China   
Verylow Low Medium High Veryhigh   
品 QUALITYOFLIFE 1,0 le N78 ， 0,862 Russian 0.5 Federation Economic: 0,388 PeerGroup Environmental: 0,747 Social: 0,443 ls lec Harmonization degree: 0,566   
Verylow Low Medium High Veryhigh SAFETYOFLIFE   
园 Ne46 1,339 BB BiodiversityBalance 0,473 ， C Conflicts Intencity 0,685 GP InfruptionPerception 0,21 SF2B CI ES EnergySafety 0,050 GINI IG GD Global Diseases 0,431 GW Global Warming 0,861 WA 0 mCP ND Natural Disasters 0,342 NI MilitaryProlifiration 0,894 N ES SN Wete rages 0.88 ND GD GW   
Very low Low Medium High Veryhigh PeerGroup Countriesby Safetyoflife   
Albania,Agetinbanbdoseluelietnosailriad Chile,Ciaotaica,roatiayueogiaeeceuaHugaryel   
Malaysia,icgoliateegroan,maoiauiiabal TurkeyUkraine Angola 品 Population 27859305 GDP percapita: \$3308.700   
Dool SUSTAINABLE DEVELOPMENT INDEX Ne133 0,453 Ne134Mozambique   
Very low Low Medium High Veryhigh   
品 QUALITY OF LIFE Ne134 ， 0,385 1,0 F Angola 0.5 Economic: 0,338 0.9 PeerGroup Enviromental: 0,28 Is lec Harmonization degree: 0,785   
Very low Low Medium High Veryhigh SAFETYOFLIFE   
园 Ne135 0,903 BB Biodiversity Balance 0,460 L CI Conflicts Intencity 0,685 IG Information Gap 0,838 BB CP Corruption Perception 0,777 SF1O CI ES GD EnergySafety GlobalDiseases 0,546 0,876 GINI JG GW Global Warming 0,447 WA4 0,0 mCP ND NaturalDisasters 0,513 NI MilitaryProlifiration 0,565 NM yES WA WaterAccess 0,943 ND 手 GD GINI Inequality 0,638 GW SF StateFragility 0,728   
Very low Low Medium High Veryhigh PeerGroup Countriesby Safety of life   
BurkinaFasoCmbodia,CmeronCentralAfricanepublic，otedlvoire,thiopiaambiaGuemla   
Guinea,Keoodgraialimique,gigergeiai   
PhilippinesleraeilditedebicfiaogoUga Kenya .0 Population 47236259 GDP percapita: \$1455.360 SUSTAINABLEDEVELOPMENTINDEX Ne112 0,538 N2111 RepublicoftheCongo ， Ne113Malawi   
Very low Low Medium High Veryhigh   
品 QUALITYOFLIFE Ne107 0,650 le ， 国 Kenya 0,5 Economic: 0,428 PeerGroup Environmental: 0,441 Social: 0,442 S lec Harmonizationdegree: 0,869   
Verylow Low Medium High Veryhigh   
园 SAFETYOFLIFE Ne136 0,881 BB Biodiversity Balance 0,552 . CI Conflicts Intencity 0,685 IG InformationGap 0,510 BB CP Corruption Perception 0,703 SF10 E CI ES EnergySafety 0,609 GINI IG GD Global Diseases 0,855 GW GlobalWarming 0,442 WA CP ND Natural Disasters 0,780 NI MilitaryProlifiration 0,683 NM ES WN Weterage 0.58 ND GD GW   
Very low Low Medium High Veryhigh PeerGroup Countriesby Safety of life   
Angola,BurkinaFaso,Cambodia,Cameroon,CentralAfricanepublic,Cotedlvoire,EhiopiaGambia   
Guatemalaaotogriiueggerga   
PhilippinesegaleraLoewaild，UitedeblicoiaogoUgada Mozambique .0 Population 28010691 GDP percapita: \$382.069   
Uool SUSTAINABLE DEVELOPMENTINDEX Ne134 0,433 Ne135 Syria Verylow Low Medium High Veryhigh   
g QUALITY OF LIFE Ne135 0,377 Mozambique 0,5 Economic: 0,372 0.0 PeerGroup Environmental: 0,177 Social: 0,390 Is lec Harmonizationdegree: 0,858 Very low Low Medium High Veryhigh SAFETYOFLIFE   
园 Ne137 0,856 BB BiodiversityBalance 0,478 ， CI Conflicts Intencity 0,685 IG InformationGap 0,799 BB CP Corruption Perception 0,693 SF10 E CI E Eneba Diseayes 0,605 GINI IG GW GlobalWarming 0,439 WA 0.0 mCP ND Natural Disasters 0,524 NI MilitaryProlifiration 0,737 NM ES W WeteFfadess 0.708 ND GD GW Very low Low Medium High Veryhigh PeerGroup Countriesby Safety of life   
Angola,Burkinasombdiamroonetralricanepbic,otedlre,ioiaia Guatemalainaotogcrwiiicggergeia Philippines,enegalerraLeonewailand，UitedepublicofananiaTogoUgandaee

# 4.8 Conclusions

1. The generalization and formalization of approaches to the recognition of C-waves of global systemic conflicts through big historical data have been carried out and general concept of description and interpretation of these waves has been proposed. On the basis of intellectual analysis of big data on the conflicts, taking place since $7 5 0 ~ \mathrm { B } . \mathrm { C }$ . up to now, have been analyzed and their general pattern has been revealed. There has been made an attempt to foresee the next global conflict called the conflict of the 21st century. Its nature and main characteristics have been analyzed.

2. The hypotheses for a metric relation between the global periodic processes, namely between the sequence of 11-year cycles of solar activity, so called Kondratieff cycles of the development of the global economy, and the process of evolutionary structuration of the family of the C-waves of global systemic conflicts have been formulated. There has also been made an attempt to predict these processes in the 21st century by using a metric approach.

3. The possible scenarios of the development of the conflict of the 21st century have been constructed and analyzed. This analysis led to the following conclusions:

3:1. Since for $\mathrm { ~ \bf ~ k ~ } > 7$ , the sequence of Fibonacci numbers $\left\{ F _ { 8 - k } \right\} _ { k \in N }$ for the sequence of big $C _ { k }$ -waves, $\mathrm { k } = \overline { { 1 , 7 } }$ , is degenerated, the revealed F-regularity fails on the time interval $\mathrm { ~ t ~ } > 2 0 9 2$ . Therefore, natural questions arise: What the 21st century has in store for the civilization? What is the nature of the final state of civilization as a system? What should happen to the world civilization after 2092, in particular, in the $2 2 \mathrm { n d }$ century? Probably, the final cycle of some global evolutionary chain of the development of the mankind begins?

3:2. One can find the answer to this question in the studies by two outstanding scientists of the last century, can be found in the studies of the outstanding scientists of the last century, Vernadskiy [22] and Moisejev [25]. Independently one from the other, they formulated a very close idea: if the mankind, in the planetary scale, does not change radically its behavior (using its mind and its labor for self-destruction), in the middle of the 21st century there can occur the conditions under which people cannot exist. These conclusions were made for the paradigm permanent for the whole history of the mankind: “unlimited and increasing consumption” and for the technosphere (set of technological lifestyles) unfriendly for human inhabitance, developed in the 19th and beginning of the 21st centuries.

3:3. If the mankind can change the paradigm of its behavior in the planetary scale, for example, to “harmonic coexistence” and radically transform the technosphere to “nature-like” (friendly to the human environment, based on the convergence of nano-, bio-, information, cognitive, and socio-humanitarian technologies [53]), then the regularity revealed for the previous paradigm of the development of systemic world conflicts, which corresponds to the Fibonacci sequence, will fail for the new paradigm, which will allow the mankind to continue its mission on the Earth.
