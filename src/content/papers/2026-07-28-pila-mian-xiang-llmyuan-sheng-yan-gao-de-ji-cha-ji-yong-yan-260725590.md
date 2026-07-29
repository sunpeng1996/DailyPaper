---
title: 'PILA: Plug-and-Play Insertion for LLM-native Advertising'
title_zh: PILA：面向LLM原生广告的即插即用广告插入框架
authors:
- Zhaowei Zhang
- Yuhan Fu
- Yihang Zhang
- Xiaohan Liu
- Ceyao Zhang
- Xiaoyuan Zhang
- Yipeng Kang
- Tonghan Wang
- Yaodong Yang
affiliations:
- Peking University
- Tsinghua University
- University of Michigan
- BIGAI
- Shanghai Qi Zhi Institute
arxiv_id: '2607.25590'
url: https://arxiv.org/abs/2607.25590
pdf_url: https://arxiv.org/pdf/2607.25590
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式广告 · 即插即用插入框架
tags:
- LLM-native Advertising
- Plug-and-Play
- Sidecar Pattern
- Response Rewriting
- Contrastive Decoding
one_liner: 提出即插即用的LLM原生广告插入侧边车框架，无需修改上游系统即可平衡用户体验与广告效果
practical_value: '- 可复用Sidecar架构设计：无需修改现有LLM/Agent生产链路（包括闭源API、RAG/多Agent工作流），即可叠加广告插入、内容合规、个性化改写等后置处理能力，完全不侵入原有系统。

  - 小样本训练流程可迁移：先用强模型生成10k级别高质量<查询-无广告响应-带广告响应>种子，再通过轻量模型做保留广告标签的多样性扩增，仅用25k样本即可微调出效果优秀的重写模型，大幅降低标注成本。

  - 强度控制方案可直接复用：基于Contrastive Decoding的单参数ρ调节机制，部署阶段无需重训即可灵活调整广告植入显著度，适配不同场景的用户体验/商业化收益平衡需求。

  - 电商大模型导购、智能客服场景可直接落地该框架，相比直接Prompt植入广告的方案，用户体验和广告转化效果均有显著提升。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM原生广告方案大多耦合在内容生成过程中，需要微调基础模型或访问模型内部状态，完全无法适配闭源LLM API、Agent工作流等主流生产场景，且容易损害原有回答质量，平衡用户体验与商业化收益的难度极高，亟需非侵入式的通用广告插入方案。

### 方法关键点
- 架构采用云原生Sidecar模式，将广告插入转化为条件响应重写任务，仅需输入用户查询、上游生成的无广告响应、待插入广告信息，即可输出自然植入广告的响应，完全不侵入上游系统。
- 数据构造：基于NaiAD基础设施，用Claude Opus 4.5生成10k高质量<查询-无广告响应-带广告响应>种子，再用Claude Haiku 4.5对广告周边上下文做多样性改写扩增，最终得到25k训练样本，微调Qwen3-4B/8B得到PILA重写模型。
- 强度控制：基于说服知识模型（PKM），采用Contrastive Decoding思路，通过超参数ρ调节PILA模型与原始基座模型的输出权重，实现部署阶段无需重训即可灵活调整广告植入显著度。

### 关键实验
基于NaiAD公开的6大行业广告数据集，对比prompt-based、MOSAIC采样、单模型SFT三类基线，PILA-8B平均得分比三类基线分别高34.2%、47.3%、7.7%；作为插件接入GPT-5.4、Gemini、Claude、Deepseek等7款主流商业LLM时，PILA-4B/8B可分别将整体表现平均提升17.2%、18.4%，同时实现用户侧体验与广告侧效果的帕累托改进。

### 最值得记住的一句话
对于闭源LLM/复杂Agent链路的商业化改造，非侵入式的后置Sidecar处理相比侵入式的模型修改/微调，是兼顾落地可行性、效果、成本的更优选择。
