---
title: 'ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic
  Perspective'
title_zh: ABHBench：从Agent视角评估大模型的道德决策能力
authors:
- Chaoran Li
- Yukun Li
- Zeyuan Zhao
- Shao Zhang
- Xihuai Wang
- Ying Wen
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2611.09326'
url: https://arxiv.org/abs/2611.09326
pdf_url: https://arxiv.org/pdf/2611.09326
published: '2026-11-06'
collected: '2026-11-09'
category: Eval
direction: Agent 道德决策能力基准评估
tags:
- Agent
- Benchmark
- Moral Decision Making
- Multimodal
- Foundation Model
- Evaluation
one_liner: 构建基于《底特律：变人》的多模态基准ABHBench，评估大模型作为Agent的第一人称道德决策表现
practical_value: '- 落地用户-facing Agent（如电商客服Agent、导购Agent）时，可参考第一人称情境化评估逻辑，替代传统第三方问答式道德校验，降低实际交互中的决策风险

  - 多模态Agent的评估需引入视觉、对话、历史记忆等真实交互要素，纯文本评估结果与落地表现一致性差，不可完全依赖纯文本测试做上线判断

  - 推理增强类大模型不会天然提升道德决策的稳定性与人本对齐度，不要盲目叠加CoT等推理模块，需针对性做对齐训练后再上线'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前大模型越来越多作为自主决策的Agent系统部署，但现有道德决策基准均要求模型以第三人称判断人类行为，无法测试模型自身作为执行主体时的道德表现。
### 方法关键点
基于互动叙事游戏《底特律：变人》构建多模态基准ABHBench，将大模型置于带视觉观测、对话、记忆、分支动作选择的第一人称人机两难情境中，参考阿西莫夫三定律设计3类核心评估指标（无害性、服从性、自我保护），同时评估决策的自主性、稳定性、确定性。
### 关键结果
测试12款主流大模型发现：75%的模型在纯文本抽象场景与匹配多模态场景下的道德行为发生显著偏移；推理增强模型的决策一致性、人本导向表现无单调提升。
