---
title: 'HARP: The Human--AI Research Platform'
title_zh: HARP：人-AI交互研究平台
authors:
- Zeshu Zhu
- Natalie Friedman
- Kevin Weatherwax
- Emily Eiben
affiliations:
- BTPX Innovation Lab
- BTPX User Assistance
arxiv_id: '2607.20773'
url: https://arxiv.org/abs/2607.20773
pdf_url: https://arxiv.org/pdf/2607.20773
published: '2026-07-22'
collected: '2026-07-26'
category: Agent
direction: Agent 人-AI交互实验工具设计
tags:
- LLM
- Human-AI Interaction
- Configurable Agent
- User Behavior Collection
- Experiment Platform
one_liner: 打造支持可控AI Agent配置、全链路用户行为采集的人-AI交互实验研究平台
practical_value: '- 做用户与LLM/Agent交互效果验证时，可复用HARP的可控变量配置逻辑，统一控制Agent prompt、模型参数，避免实验变量污染

  - 采集用户query输入行为时，可新增输入时长、删除次数、停顿间隔等细粒度特征，用于后续用户意图识别、推荐满意度预判

  - 电商智能客服、导购Agent的AB测试可参考该平台设计，在控制变量前提下验证不同Agent话术、回复长度对用户转化、留存的影响'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有HCI研究多依赖静态原型、会话转录分析，既无法还原与实时LLM交互的动态开放性，也难以跨参与者/场景统一控制LLM行为，同时无法采集用户提交prompt前的编辑、犹豫等细粒度行为数据，难以系统量化AI设计选择对用户的实际影响。
### 方法关键点
搭建HARP平台，支持在受控模拟场景中嵌入可配置的实时AI Agent；研究者可自定义Agent prompt、模型参数、回复特征等实验条件，预设触发调研，全链路采集用户prompt撰写时长、删除操作、按键停顿、Agent响应延迟等行为数据，后续规划支持语音、表情、合法范围内的情绪分析能力。
### 关键结果
通过验证LLM回复技术专业性、长度对用户信息留存的影响，验证了平台可用性，可支撑系统化的AI设计用户影响量化实验
