import sys
import time

from iopentracing.lib.tracing import init_tracer


def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        span.set_tag('hello-to', hello_to)
        time.sleep(1)
        hello_str = format_string(span,hello_to)
        print_hello(span, hello_str)


def format_string(root_span, hello_to):
    with tracer.start_span('format', child_of=root_span) as span:
        hello_str = 'Hello, %s!' % hello_to
        time.sleep(3)

        span.log_kv({'event': 'string-format', 'value': hello_str})
        return hello_str


def print_hello(root_span, hello_str):
    with tracer.start_span('println', child_of=root_span) as span:
        print(hello_str)
        time.sleep(2)

        span.log_kv({'event': 'println'})
        return hello_str


if __name__ == '__main__':
    tracer = init_tracer('hello-world')

    say_hello("hello_2_param")

    # yield to IOLoop to flush the spans
    time.sleep(2)
    tracer.close()
