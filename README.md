![Coverage badge](https://raw.githubusercontent.com/TUW-GEO/eotransform/python-coverage-comment-action-data/badge.svg)
# eotransform

Defines the basic transform protocol to be used in the streamed source to sink concept. Also provides some generic 
transformer implementations such as `Compose` or `Result`.

## What can I use eotransform for?

The eotransform package defines Source, Transform, and Sink protocols, to facilitate the creation of modularised processing pipelines.
Adhering to a common contract, makes it easier to mix and match processing blocks, allowing for better code reusage, and more flexible pipelines.
We also provide a `streamed_process` function, which you can use for I/O hiding when implementing these protocols.
The package also provides some common transformations, and sinks like `Compose` or `Result`.

## Getting Started

### Installation
```bash
pip install eotransform
```

### Examples

#### Transformer protocol
This example shows how to implement the `Transformer` protocol for a simple multiplication:

snippet: example_transformer_multiply

#### Sink protocol
This code snippet illustrates how to implement the `Sink` protocol, using a simple accumulation example:

snippet: example_sink_accumulate


#### Streamed pipeline using the "Result" pattern
In the following example we show how to combine `ApplyToOkResult` and `SinkUnwrapped` to process data in a streamed fashion with proper error handling across thread boundaries.

snippet: example_streamed_results

## Streaming
The following briefly describes the concept of streaming, and how it can be used to hide I/O processes.

The most straightforward way to process data is to first load it and then process it:

![serial process](doc/images/serial.png)

This has the advantage of being simple to implement and maintain, as you don't need to be concerned with issues of parallelism.

For many cases this will work sufficiently well, however, it can stall your processing pipeline because it needs to wait for data to be fetched.
Often an easy way to increase throughput is to interleave the I/O or data fetching with processing chunks:

![streamed process](doc/images/streamed.png)

With this streaming process you can utilise resources more effectively.

## Dependencies
eotransform requires Python 3.8 and has these dependencies:

snippet: dependencies