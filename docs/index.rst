.. toctree::
   :hidden:

   Home <self>
   Installation <install>
   API reference <_autosummary/eotransform>

Welcome to eotransform's documentation!
=======================================

The eotransform package defines the basic transform protocol to be used in the streamed source to sink concept.
It also provides some generic transformer and sink implementations such as `Compose` or `Result`.

By providing a common contract, it aims to facilitate modularisation of processing pipelines.
The general concept of Source -> Transform -> Sink makes it easier to process data in a streamed fashion, hiding I/O.
Have a look at the projects `README <https://github.com/TUW-GEO/eotransform/blob/main/README.md>`_ file for examples.

Streaming
---------

The most straightforward way of processing data is doing it serially, i.e., fetching a data block, processing it, then fetching the next, and so on.

.. figure:: _static/images/serial.png
   :alt: serial process

   Serial method, waiting for data before processing.

This simple concept is easy to implement and maintain, as it doesn't have to deal with concurrency.
It also makes it easier to debug and reason about, which is why for many tasks it is sufficient.

However, certain problems, especially in the realm of high performance computing, have high demands on throughput.
In that case, throughput can be increased by a streaming approach.

.. figure:: _static/images/streamed.png
   :alt: serial process

   Stream next data-block while processing previous one.

Data block fetching is interleaved with processing, effectively hiding the I/O or other inherently serial processes such as compression/decompression.
This, however, comes at the cost of increased complexity, as you need to worry about concurrency issues.
eotransform provides you with a :doc:`streamed_process <_autosummary/eotransform.streamed_process.streamed_process>`, which takes care of most of the heavy lifting.
This includes for instance, setting up producer and consumer queues, or passing exceptions across thread boundaries.
The package also provides implementation for the Result pattern, inspired by `Rust's result type <https://doc.rust-lang.org/std/result/>`_, to provide a flexible mechanism for concurrent error handling.