---
title: 'Devils in Question Relay: Source-Conditioned Relay Steering to Mitigate Hallucinations
  in Audio-visual Large Language Models'
title_zh: 源条件中继引导方法缓解视听大语言模型的跨模态混淆幻觉
authors:
- Yu Zhang
- Pingrui Zhang
- Xuefeng Bai
- Pengfei Zhang
- Yang Xiang
- Kehai Chen
affiliations:
- Harbin Institute of Technology, Shenzhen
- Peng Cheng Laboratory
- Fudan University
arxiv_id: '2609.37568'
url: https://arxiv.org/abs/2609.37568
pdf_url: https://arxiv.org/pdf/2609.37568
published: '2026-09-28'
collected: '2026-10-03'
category: Multimodal
direction: 多模态大模型 · 跨模态幻觉缓解
tags:
- AVLLM
- Hallucination Mitigation
- Multimodal LLM
- Training-free
- Cross-modal Interference
one_liner: 揭示视听大模型跨模态幻觉的问题中继机制，提出免训练SECRET方法缓解源混淆grounding幻觉
practical_value: '- 多模态交互场景（如商品短视频/直播理解Agent）可复用问题中继干扰分析思路，定位输入模态的冲突传导路径

  - 免训练的特征引导思路可直接迁移至多模态推荐的Query理解模块，无需重训模型即可缓解跨模态信息冲突导致的召回/排序错误

  - 不同模态通路干预的对比表征构建方法，可用于优化多模态商品检索的Query embedding生成，提升检索准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Audio-visual large language models (AVLLMs) 普遍存在源混淆grounding幻觉：未被要求的模态线索会诱导输出不符合指定模态要求的结果，严重影响落地可靠性，现有方法对该幻觉的内部产生机制研究不足。

### 方法关键点
通过路径干预与表征分析，首次揭示问题中继机制：问题状态同时携带所需源证据与干扰模态线索，是幻觉产生的核心节点；据此提出免训练方法SECRET，通过不同模态通路干预生成对比问题表征，将原始问题状态引导向所需模态证据方向，消除干扰。

### 关键结果
在CMM、AVHBench两个基准测试上，跨3种AVLLMs均优于现有免训练方法，相比基线模型最高提升18.0、7.1个百分点，在模态专属字幕生成等开放生成任务上也具备通用性。
