#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "cfe66c9a-39b0-4554-9713-55d5fe29f3fc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "J9X-_uihXVgG55jB9_Qu3~0WlI0GD6I.gP")
