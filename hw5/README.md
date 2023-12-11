# id2222-lab5

Manual:

 -alpha N                           : Alpah parameter (default: 2.0)
 -delta N                           : Simulated annealing delta. (default:
                                      0.003)
 -graph VAL                         : Location of the input graph. (default:
                                      ./graphs/ws-250.graph)
 -graphInitColorSelectionPolicy VAL : Initial color celection policy.
                                      Supported, RANDOM, ROUND_ROBIN, BATCH
                                      (default: ROUND_ROBIN)
 -help                              : Print usages. (default: true)
 -nodeSelectionPolicy VAL           : Node selection plicy. Supported, RANDOM,
                                      LOCAL, HYBRID (default: HYBRID)
 -numPartitions N                   : Number of partitions. (default: 4)
 -outputDir VAL                     : Location of the output file(s) (default:
                                      ./output)
 -randNeighborsSampleSize N         : Number of random neighbors sample size.
                                      (default: 3)
 -rounds N                          : Number of rounds. (default: 1000)
 -seed N                            : Seed. (default: 0)
 -temp N                            : Simulated annealing temperature.
                                      (default: 2.0)
 -uniformRandSampleSize N           : Uniform random sample size. (default: 6)