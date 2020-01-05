import logging

LOGGER = logging.getLogger(__name__)

class CallbackManager(object):
    ARGUMENTS = 'arguments'

    @staticmethod
    def _dict_arguments_match(value, expectation):
        """Checks an dict to see if it has attributes that meet the expectation.

        :param dict value: The dict to evaluate
        :param dict expectation: The values to check against
        :rtype: bool

        """
        LOGGER.debug('Comparing %r to %r', value, expectation)
        for key in expectation:
            if value.get(key) != expectation[key]:
                LOGGER.debug('Values in dict do not match for %s', key)
                return False
        return True

    @staticmethod
    def _obj_arguments_match(value, expectation):
        """Checks an object to see if it has attributes that meet the
        expectation.

        :param object value: The object to evaluate
        :param dict expectation: The values to check against
        :rtype: bool

        """
        for key in expectation:
            if not hasattr(value, key):
                LOGGER.debug('%r does not have required attribute: %s',
                             type(value), key)
                return False
            if getattr(value, key) != expectation[key]:
                LOGGER.debug('Values in %s do not match for %s', type(value),
                             key)
                return False
        return True



    def _arguments_match(self, callback_dict, args):
        """Validate if the arguments passed in match the expected arguments in
        the callback_dict. We expect this to be a frame passed in to *args for
        process or passed in as a list from remove.

        :param dict callback_dict: The callback dictionary to evaluate against
        :param list args: The arguments passed in as a list

        """
        if callback_dict[self.ARGUMENTS] is None:
            return True
        if not args:
            return False
        if isinstance(args[0], dict):
            return self._dict_arguments_match(args[0],
                                              callback_dict[self.ARGUMENTS])
        return self._obj_arguments_match(args[0].method
                                         if hasattr(args[0], 'method') else
                                         args[0], callback_dict[self.ARGUMENTS])


template_dict  ={"name":"wqzhang","age":10}

print(dict_arguments_match({"name":"wqzhang","age1":10},{"name":"wqzhang","age":10}))