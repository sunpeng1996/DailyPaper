---
title: Multi-Faceted Evaluation and Mitigation of Emotion Hallucinations in MLLMs
title_zh: 多模态大模型情感幻觉的多维度评估与缓解方法
authors:
- Bowen Zeng
- Peipei Song
- Weidong Chen
- Shengeng Tang
- Song Ye
- Yuanhong Zhong
- Beier Zhu
- Xun Yang
arxiv_id: '2609.11154'
url: https://arxiv.org/abs/2609.11154
pdf_url: https://arxiv.org/pdf/2609.11154
published: '2026-09-10'
collected: '2026-09-11'
category: Multimodal
direction: 多模态大模型 · 情感幻觉评估与缓解
tags:
- MLLM
- Emotion Hallucination
- Evaluation
- Training-free
- Reasoning
one_liner: 提出多维度情感幻觉量化指标EHR与免训练缓解框架HMER，跨架构降低MLLM情感幻觉
practical_value: '- 可复用EHR多维度评估框架，优化电商MLLM客服、商品图文/短视频情感理解场景的幻觉检测粒度，避免粗粒度评估漏判

  - HMER免训练双记忆模块（幻觉记忆+锚点记忆）可直接迁移到生成式推荐文案生成、AI导购的幻觉缓解场景，无需重训模型大幅降低落地成本

  - 多维度分面修正思路可用于商品评价情感分析、内容情感标签生成等任务，减少错误情感标签对推荐排序、广告投放的负向干扰'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
MLLM在开放式情感理解场景存在普遍的情感幻觉问题，现有封闭式评估协议无法适配情感理解多认知维度、自由文本输出的评估需求，且现有幻觉缓解方法存在「部分维度幻觉降低、其他维度恶化」的粗粒度修正缺陷。
### 方法关键点
1. 提出EHR（Emotion Hallucination Rate）评估指标，从表情、动作、音频、本能、逻辑、结论6个维度量化情感幻觉水平
2. 提出免训练缓解框架HMER，通过幻觉记忆模块定位幻觉内容做targeted logit修正，搭配锚点记忆模块保留可靠中间推理状态稳定生成，实现分维度细粒度幻觉抑制
### 关键结果
在19款不同架构MLLM上验证了情感幻觉的普遍性，HMER可跨架构有效降低各维度情感幻觉率，无其他维度幻觉恶化的副作用
