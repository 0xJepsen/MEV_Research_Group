# Fee Machanisms

The way that different networks price transactions and computational resources is of great interest. From these computation algorithms we can deduce information about derivation of cost of censorship

## Avalanche

Transaction fees for non-atomic transactions are based on Ethereum's EIP-1559 style Dynamic Fee Transactions, which consists of a gas fee cap and a gas tip cap.

The fee cap specifies the maximum price the transaction is willing to pay per unit of gas. The tip cap (also called the priority fee) specifies the maximum amount above the base fee that the transaction is willing to pay per unit of gas. Therefore, the effective gas price paid by a transaction will be min(gasFeeCap, baseFee + gasTipCap). Unlike in Ethereum, where the priority fee is paid to the miner that produces the block, in Avalanche both the base fee and the priority fee are burned. For legacy transactions, which only specify a single gas price, the gas price serves as both the gas fee cap and the gas tip cap.

C-Chain atomic transactions (i.e. imports and exports from/to other chains) charge dynamic fees based on the amount of gas used by the transaction and the base fee of the block that includes the atomic transaction.

Gas Used:

| Item | Gas  | 
| ----------- | ----------- |
| Unsigned Tx Byte  | 1 |
| Signature   | 1000 |
| Per Atomic Tx   | 10000 | 

Therefore, the gas used by an atomic transaction is 1 * len(unsignedTxBytes) + 1,000 * numSignatures + 10,000

The tx fee additionally takes the base fee into account. Due to the fact that atomic transactions use units denominated in 9 decimal places, the base fee must be converted to 9 decimal places before calculating the actual fee paid by the transaction. Therefore, the actual fee is: gasUsed * baseFee (converted to 9 decimals).

## Polygon

[Resource](https://docs.polygon.technology/docs/develop/eip1559-transactions/how-to-send-eip1559-transactions)

## Solana

[Resource](https://docs.solana.com/implemented-proposals/transaction-fees#congestion-driven-fees)
