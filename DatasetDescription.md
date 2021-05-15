# Description of the DataSet

### They have provided three Dataset for this purpose :

1. portfolio - containing offer ids and metadata about each offer (duration, type, etc.)
2. profile - demographic data for each customer.
3. transcript - records for transactions, offers received, offers viewed, and offers completed.



### The description of each column in the dataset is as follows :

* portfolio.json
  1. id (string) - offer id
  1. offer_type (string) - a type of offer ie BOGO, discount, informational
  1. difficulty (int) - the minimum required to spend to complete an offer
  1. reward (int) - the reward that is given for completing an offer
  1. duration (int) - time for the offer to be open, in days channels (list of strings)
* profile.json
  1. age (int) — age of the customer
  1. became_member_on (int) — the date on which the customer created an app account
  1. gender (str) — gender of the customer (note some entries contain ‘O’ for other rather than M or F)
  1. id (str) — customer-id
  1. income (float) — customer’s income
* transcript.json
  1. event (str) — record description (ie transaction, offer received, offer viewed, etc.)
  1. person (str) — customer-id
  1. time (int) — time in hours since the start of the test. The data begins at time t=0
  1. value — (dict of strings) — either an offer id or transaction amount depending on the record
