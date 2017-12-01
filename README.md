# SMART CONTRACT

This project is blockchain implementation for educational purposes. It uses a blockchain to store the details and status of contract made between users.

## Features
Blockless: Edits to blockchain are usually appended in 'blocks'. But the nature of this approach has a lot of disadvantages. Future blockchains will evolve to not require block additions.
	This project tests this feature

Centralised manipulation and distribution: Blockchain's security approach is 'safety in numbers'. The sheer number of copies of a ledger make it impossible to commit fraud.
	But blockchain use by companies/governments will require an amount of centralised control. To balance both, this project enables blockchain manipulation and distribution by host server
	This also makes unnecessary for all users to have servers to communicate blockchain data.
	Blockchain data is simply offered as a downloadable file.
	
	
## Workflow

1. User1 and user2 want to enter into a contract
2. User1 or user2 creates the contract with all its details(product/service, quantity, agreed cost)
	a. While creating, user receives a public access key and a contract password
	b. Contract is divided into two transaction parts, one for each user. (Typically, one giving a fixed amount of money and the other a defined product/service)
3. The contract creator shares the public access key with the contract partner
4. The partner uses the public access key to verify the contract details, approves the contract and receives his/her contract password
5. When the contract is approved, its details are added to the blockchain encrypted with the public access key
6. When each user completes his transaction part, he/she uses his contract password to confirm it
7. On confirmation by each user, the blockchain is appended with the updated status of the contract

The public access keys and both contract passwords are hashed and added to the blockchain during contract approval. Therefore any change is made only after the input passwords are compared against the blockchain ones.

## To be added

Update option: A python script that directly updates the local blockchain data

Verification: For more security, a verification option that checks n copies(during updating of their local copies) to verify the contract status.

### Authors

* **Sharan Amutharasu** - *Initial work* - (https://github.com/sharan-amutharasu)

See also the list of [contributors](https://github.com/sharan-amutharasu/smart-contract/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

