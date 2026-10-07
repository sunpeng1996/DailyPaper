---
title: Do LLMs Act on What They Know? From Partner Representations to Cooperative
  Actions
title_zh: 大语言模型多智能体协作中知识到合作动作的落地差距研究
authors:
- Yuhwan Jeong
- Jinnyeong Yang
- Kuk-Jin Yoon
affiliations:
- KAIST Visual Intelligence Lab
arxiv_id: '2610.08129'
url: https://arxiv.org/abs/2610.08129
pdf_url: https://arxiv.org/pdf/2610.08129
published: '2026-10-06'
collected: '2026-10-07'
category: MultiAgent
direction: 多智能体协作 · 沟通规则适配
tags:
- Multi-Agent
- LLM-Probing
- Activation-Patching
- Hanabi
- Cooperative-Agent
one_liner: 量化LLM多智能体协作中伙伴规则可解码性与行为落地的差距，对比两类干预效果
practical_value: '- 搭建多角色协作Agent系统（如电商客服-商家协同、广告策略Agent群）时，优先将识别到的合作方习惯/规则直接翻译成当前步的动作推荐给到LLM，效果远好于仅告知规则描述，跨模型测试显示平均协作得分可提升1.7以上

  - 做用户意图挖掘、合作方行为模式识别的业务场景，可使用轻量线性probe直接从LLM隐状态解码目标规则，无需微调LLM权重，成本极低，意图类规则解码准确率最高可达87%以上

  - 若业务要求LLM严格遵循给定规则执行动作，可通过少量数据微调LoRA适配器学习规则到动作的映射，论文测试显示微调后规则执行准确率接近100%，协作得分可触达环境上限'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM广泛应用于人机、多智能体协作场景，但现有实践发现即使LLM具备较强任务推理能力，依然难以和陌生协作方对齐非预设的沟通规则；过往研究未明确区分「是否能识别协作方规则」和「是否能按规则执行动作」两个核心环节，无法针对性优化协作效果。
### 方法关键点
- 基于Hanabi合作卡牌游戏构造控制变量环境，协作双方各自持有独立的「目标选择（左/右标记卡）+ 意图映射（颜色/rank对应玩/弃）」沟通规则，接收方LLM权重全程冻结；
- 用线性probe从LLM隐状态解码协作方的真实规则，定义**Knowing**（规则解码准确率）和**Doing**（动作符合规则的比例）两个核心评价维度；
- 对比两类干预方案：规则陈述（直接告知LLM协作方规则）、行动翻译（将规则转化为当前步的具体动作推荐），同时验证激活迁移等干预手段的效果。
### 关键实验
覆盖8款主流开源LLM（Qwen3、Llama3.1、Gemma3等），以Qwen3-8B为例：无干预基线条件下，意图规则解码准确率达81.4%，但意图动作符合率仅59.1%，目标动作符合率仅51.5%；提供真实规则陈述时，目标动作符合率提升至82.1%，但意图动作符合率几乎无变化；提供真实规则的行动翻译时，目标动作符合率达96.2%、意图达86.7%，游戏得分较基线提升2.15，仅比环境天花板低0.67。
### 核心结论
LLM内部可解码的信息不代表会被用于决策，将规则翻译成当前步的具体动作推荐，比单纯输出规则描述的协作适配效率高得多
