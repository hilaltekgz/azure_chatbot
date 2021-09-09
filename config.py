#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0c5db947-b505-48dd-8112-0d1e892301b2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "0BH~bgZ45vyrmya3.zEObC5y4h9~g8h_mD")
