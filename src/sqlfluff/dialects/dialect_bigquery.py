"""The BigQuery dialect.

This inherits from the ansi dialect, with changes as specified by
https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax
"""

from ..parser import (BaseSegment, NamedSegment, OneOf, Ref, Sequence)

from .dialect_ansi import ansi_dialect


bigquery_dialect = ansi_dialect.copy_as('bigquery')

bigquery_dialect.add(
    DoubleQuotedLiteralSegment=NamedSegment.make('double_quote', name='literal', type='quoted_literal')
)


@bigquery_dialect.segment()
class IntervalFunctionSegment(BaseSegment):
    """An interval with a function as value segment."""
    type = 'interval_function'
    match_grammar = Sequence(
        Ref('IntervalKeywordSegment'),
        Ref('FunctionSegment'),
        OneOf(
            Ref('QuotedLiteralSegment'),
            Ref('DatepartSegment')
        )
    )


bigquery_dialect.replace(
    QuotedIdentifierSegment=NamedSegment.make('back_quote', name='identifier', type='quoted_identifier'),
    LiteralGrammar=OneOf(
        Ref('QuotedLiteralSegment'), Ref('DoubleQuotedLiteralSegment'), Ref('NumericLiteralSegment'),
        Ref('BooleanLiteralGrammar'), Ref('QualifiedNumericLiteralSegment'), Ref('IntervalFunctionSegment'),
        Ref('IntervalLiteralSegment')
    ),
)
