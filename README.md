# SMART CONTRACT

This project is a blockchain implementation meant for educational purposes. It uses a blockchain as a ledger to store the details and status of contracts made between users.
The front end can be accessed at http://54.214.220.132/app_sc/ (for credentials, email me at sharan.amutharasu@gmail.com)

## Features
Blockless: Edits to blockchain are usually appended in 'blocks'(set of elements). Future blockchains will however, evolve to not require block level manipulation, overcoming many problems posed by the block method. This project tests this kind of a blockless blockchain (i.e. chain).

Centralised manipulation and distribution: Blockchain's security approach is 'safety in numbers'. The sheer number of copies of a ledger make it impossible to commit fraud. Decentralized manipulation of the blockchain is also possible due to this.
	But for use by companies and governments, a lot more centralised control will be required. To balance both, this project enables blockchain manipulation and distribution by host server and decentralized storage and verification for security.
	This also makes unnecessary for all users to have servers to communicate blockchain data.
	Blockchain data is simply offered as a downloadable file.
	
	
## Workflow

1. User1 and user2 decide to enter into a contract
2. User1 or user2 creates the contract with all its details(product/service, quantity, agreed cost)
	a. While creating, user receives a public access key and his/her contract password
	b. Contract is divided into two transaction parts, one for each user. (Typically, one giving a fixed amount of money and the other a defined product/service)
3. The contract creator shares the public access key with the contract partner
4. The partner uses the public access key to verify the contract details, approves the contract and receives his/her contract password
5. When the contract is approved, its details are added to the blockchain encrypted with the public access key
6. When each user completes his transaction part, he/she uses his contract password to confirm it
7. On confirmation by each user, the blockchain is appended with the updated status of the contract as complete
8. For verification, the users can share the public access key with any verifying authority or witness, who will be able to see the details and status of the contract but not modify it

The public access keys and both contract passwords are hashed and added to the blockchain during contract approval. Therefore any change is allowed only after the input passwords are compared against the blockchain ones.

## To be added

Update option: A python script that directly updates the local blockchain data

Verification: For more security, a verification option that checks n copies(during updating of their respective local copies) to verify the contract status of the contract under verification.

## Disclaimer

This project is strictly educational. There are several security loop holes and effeciency concerns that have to be addressed before commercial application. The contributors are not responsible for any such actions or their consequences.

### Authors

* **Sharan Amutharasu** - *Initial work* - (https://github.com/sharan-amutharasu)

See also the list of [contributors](https://github.com/sharan-amutharasu/smart-contract/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. No use/duplication is allowed without acknowledgement.

