#!/usr/bin/env python

"""Tests for `bids_stats_model_builder` package."""


import unittest
from click.testing import CliRunner

from bids_stats_model_builder import bids_stats_model_builder
from bids_stats_model_builder import cli


class TestBids_stats_model_builder(unittest.TestCase):
    """Tests for `bids_stats_model_builder` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'bids_stats_model_builder.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
