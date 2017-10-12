## Honeywords
A naive implementation of system discussed in 'Honeywords: Making Password-Cracking Detectable' ( Ari Jueles, Ron Rivest)

Link to paper: [Honeywords: Making Password-Cracking Detectable](https://people.csail.mit.edu/rivest/pubs/JR13.pdf)

This is a simple flask based implementation of a honeywords system that stores 9 random passwords selected from the list of most common user passwords. The system makes use of Amazon Key Management Service (KMS) and boto3 to deploy the honeychecker, and maintains the index of the correct password encrypted by a key stored in KMS. The requirements are specified in the requirements.txt file. 

To get started with Amazon KMS, read the docs [here](docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)
