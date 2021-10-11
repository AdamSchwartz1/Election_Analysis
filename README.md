# Election_Analysis

## Project Overview
A colorado board of elections official has given me the task of finding the following results for a recent election audit of a local congressional election.

1. Tally the total number of votes.
2. Gather a list of the candidates.
3. Find the total number of votes each candidate received.
4. Find the percent of votes each candidate received.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python, 3.9.1, Visual Studio Code, 1.60.2

## Summary
The results of the analysis show that:
1. There were a total of 369,711 total votes.
2. There were 3 candidates:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
3. Candidate results were:
  - Charles Casper Stockham had 23.0% of the votes with 85,213 votes.
  - Diana DeGette had 73.8% of the votes with 272,892 votes.
  - Raymon Anthony Doane had 3.1% of the votes with 11,606 votes.
4. The winner was:
  - Diana DeGette, who had 73.8% of the votes with 272,892 votes

## Challenge Overview
For the challenge, I took a deeper look in to the election audit and analyzed the voting data for each county. I calculated the following information for each county.
1. Total number of votes for each county.
2. The percentage of votes that came from each county.
3. And which county had the highest voter turnout.

## Challenge Summary
The results of the challenge are stated below:
1. Total votes and percentage of votes:
  - Jefferson County had 10.5% of the votes with 38,885.
  - Denver County had 82.8% of the votes with 306,055.
  - Arapahoe County had 6.7% of the votes with 24,801.
2. County with highest voter turnout:
  - Denver had the highest voter turnout with 82.8% of the votes with a total of 306,055 votes.

### Future elections
This template could be very helpful in tolling data for future elections. The framing of it is already there but with a few minor changes, this would work for any election. One change that could be made is instead of having this template set up for just county elections, I could add an input statement that would allow an option to select the type of election it is (i.e. county, state, national.) Once that input is selected, you could reference that in the print statement or text file so it will say which type of election it is. My second suggestion is that I only explicity stated who won the election; a lot of times people like to know the order in which the candidates finished. I could build in a conditional statement that would list the candidates in order from who finished first to who finished last. These are just two improvements I think I could make to improve this election tool.

