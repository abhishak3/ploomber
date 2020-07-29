from ploomber.cli.parsers import _custom_command, CustomParser


def main():
    parser = CustomParser(description='Plot a pipeline')
    parser.add_argument(
        '--output',
        '-o',
        help='Where to save the plot, defaults to pipeline.png',
        default='pipeline.png')
    dag, args = _custom_command(parser)
    dag.plot(output=args.output)
    print('Plot saved at:', args.output)
