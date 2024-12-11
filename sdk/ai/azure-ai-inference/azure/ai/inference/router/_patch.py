# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=line-too-long,R
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import abc
from azure.ai.inference import (
    ChatCompletionsClient,
    EmbeddingsClient,
)

from azure.ai.inference.aio import (
    ChatCompletionsClient as AsyncChatCompletionsClient,
    EmbeddingsClient as AsyncEmbeddingsClient,
)
from azure.ai.inference.models import (
    ChatCompletions,
    StreamingChatCompletions,
    AsyncStreamingChatCompletions,
)

class ModelConfig(abc.ABC):
    @abc.abstractmethod
    def 
class ModelRouter(abc.ABC):
    @abc.abstractmethod
    def complete(self) -> ChatCompletions:
        pass
    
def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """