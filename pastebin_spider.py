# BEFORE USING: Visit the following page and follow the instructions: https://pastebin.com/doc_scraping_api
import pathlib

import inntinn

"""pastebin_spider.py: Pastebin spider process for Inntinn.io"""

__author__ = "Brandon Blackburn"
__maintainer__ = "Brandon Blackburn"
__email__ = "contact@bhax.net"
__website__ = "https://keybase.io/blackburnhax"
__copyright__ = "Copyright 2021 Brandon Blackburn"
__license__ = "Apache 2.0"


#  Copyright (c) 2021. Brandon Blackburn - https://keybase.io/blackburnhax, Apache License, Version 2.0.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#  either express or implied. See the License for the specific
#  language governing permissions and limitations under the License.
#  TL;DR:
#  For a human-readable & fast explanation of the Apache 2.0 license visit:  http://www.tldrlegal.com/l/apache2


if __name__ == "__main__":
    # BEFORE USING: Visit the following page and follow the instructions: https://pastebin.com/doc_scraping_api
    # tls=False only used for testing... we hope you are not running a production MongoDB without TLS!
    inntinn.IPastebin(pathlib.Path.cwd() / "config.json", tls=False).start()
