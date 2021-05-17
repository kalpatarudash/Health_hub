require('dotenv').config()
const HDWalletProvider = require('@truffle/hdwallet-provider')
const Web3 = require('web3')
const compiledFactory = require('./build/Factory.json');

// console.log(  process.env.mnemonic, `https://rinkeby.infura.io/v3/${process.env.infura_API}` )

const abi = compiledFactory.abi;
const bytecode = compiledFactory.evm.bytecode.object;

let provider = new HDWalletProvider({
  mnemonic: {
    phrase: process.env.mnemonic
  },
  providerOrUrl: `https://rinkeby.infura.io/v3/${process.env.infura_API}`,
  chainId: '4'
});

// console.log(abi);
// console.log(bytecode);

const web3 = new Web3(provider)

const deploy = async () => {
  try {
  const accounts = await web3.eth.getAccounts();
  console.log(accounts[0]);
  const results = await new web3.eth.Contract(JSON.parse(JSON.stringify(abi)))
     .deploy({data: '0x' + bytecode}) 
     .send({from: accounts[0], gas:'1000000'});
  // console.log("abi: ", JSON.stringify(abi));
  console.log("contract successfully deployed to address: ", results.options.address);
  }
  catch(error) {
    console.error('error: ', error);
  }
};

deploy();



