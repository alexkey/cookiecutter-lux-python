import argparse


class CustomHelpFormatter(argparse.HelpFormatter):

    def _format_action(self, action: argparse.Action) -> str:
        # pylint: disable=attribute-defined-outside-init
        if isinstance(action, argparse._SubParsersAction):
            self._subaction_max_length = max(
                len(i) for i in [self._format_action_invocation(a)
                                 for a in action._get_subactions()]
            )

        if isinstance(action, argparse._SubParsersAction._ChoicesPseudoAction):
            subaction = self._format_action_invocation(action)
            width = self._subaction_max_length
            help_text = self._expand_help(action) if action.help else str()

            return '{indent_first}{:{width}}{indent_help}{}\n'.format(
                subaction, help_text,
                indent_first=' '*2, width=width, indent_help=' '*10
            )
        elif isinstance(action, argparse._SubParsersAction):
            return '\n{}'.format(''.join(
                self._format_action(a) for a in action._get_subactions()
            ))
        else:
            return super()._format_action(action)
