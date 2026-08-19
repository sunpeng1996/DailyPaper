---
title: Recirculation
title_zh: Recirculation：无需重训的Transformer推理时循环优化方法
authors:
- Michael C. Mozer
- Shoaib Ahmed Siddiqui
- Danny Sawyer
- Sunny Sanyal
- Rosanne Liu
affiliations:
- Google DeepMind
- University of Texas, Austin
arxiv_id: '2608.17981'
url: https://arxiv.org/abs/2608.17981
pdf_url: https://arxiv.org/pdf/2608.17981
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM推理优化 · 状态跟踪增强
tags:
- Inference Optimization
- State Tracking
- Transformer
- Recurrence
- Activation Steering
one_liner: 在推理阶段为Transformer引入深层到浅层的激活泄漏循环，不改原权重即可提升模型性能
practical_value: '- 电商多轮客服、搜索对话Agent可直接接入基础版Recirculation，选择模型中层作为目标层、比其高5-7层作为源层，α取0.1~0.15，几乎无额外成本即可降低多义词歧义、上下文理解错误率

  - 对推理精度要求高的场景（如电商选品助手、广告文案生成）可接入自适应Recirculation，仅训练轻量MLP生成token级混合系数，无需微调大模型即可将GSM8k类推理任务精度提升21%

  - 生成式推荐长会话场景可复用Recirculation设计思路，将深层已经对齐的用户意图表示泄漏回浅层，减少长会话中的用户意图漂移问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer前馈架构的状态更新受模型深度限制，深层完成的语义消解结果无法被浅层访问，导致多轮对话、长文本理解中的上下文歧义错误（如多义词bank先后被理解为河岸、金融机构），现有循环Transformer、CoT等方案要么需要全量重训，要么推理延迟显著升高。

### 方法关键点
- 基础Recirculation：推理阶段每处理一个token后，将深层源层的激活归一化到和浅层目标层相同L2范数，按系数α与原浅层激活加权混合，全程冻结原模型权重
- 自适应Recirculation：新增轻量MLP，根据每个token的源/目标层激活动态生成向量形式的混合系数，进一步优化效果，原大模型权重完全保持不变
- 区别于Looped Transformer：Recirculation的循环同时跨层和跨输入步，支持任意长度的状态跟踪，无深度限制

### 关键结果
在Gemma3全系列模型上验证，基础版Recirculation在10个语言建模数据集上最高降低困惑度35%，GSM8k pass@1精度提升4.4%；自适应Recirculation平均降低困惑度23%，GSM8k pass@1精度提升21%，效果超过对全模型的微调；方案对Ministral3、Qwen3、Phi2等多类开源模型均适用，仅需调整源/目标层和α即可获得收益。

### 核心结论
Transformer残支流天然存在跨层表示对齐特性，无需重训仅靠推理时的激活自引导就能大幅提升模型性能
