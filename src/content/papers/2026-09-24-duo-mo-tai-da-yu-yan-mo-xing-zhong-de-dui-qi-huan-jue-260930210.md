---
title: The Alignment Illusion in Multimodal Large Language Models
title_zh: 多模态大语言模型中的对齐幻觉
authors:
- Hong-Han Wang
- Yuntao Wang
- Hu Ding
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.30210'
url: https://arxiv.org/abs/2609.30210
pdf_url: https://arxiv.org/pdf/2609.30210
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态大模型 · 跨模态对齐度量优化
tags:
- MLLM
- Cross-modal Alignment
- Representation Similarity
- PA Gap
- Evaluation Metric
one_liner: 发现MLLM传统跨模态对齐度量存在对齐幻觉，提出PA gap精准衡量真实跨模态内容交互
practical_value: '- 多模态商品理解/多模态推荐MLLM微调时，禁用CKA/SVCCA等传统标量对齐分作为跨模态融合效果代理指标，避免被对齐幻觉误导

  - 可复用PA gap指标评估多模态Agent、多模态搜推系统中MLLM的真实跨模态内容交互效果，判断视觉信息是否被有效利用

  - 多模态召回/排序链路用到MLLM特征时，可通过PA gap快速定位视觉特征被权重诱导对齐的问题层，优化MLP投影层参数'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有MLLM研究普遍将层间图文相似度作为跨模态内容融合的核心证据，默认标量对齐分可反映内容级交互，但该假设从未经过严格受控验证。

### 方法关键点
对13款覆盖5个架构、参数区间0.5B~72B的MLLM做视觉流受控干预，将投影层输出视觉token替换为高斯噪声，验证4种常用标量对齐度量的有效性；定位对齐幻觉根源为LLM通路各向异性MLP下投影导致的权重诱导对齐，提出PA gap（前两个主角度余弦的差值），可区分权重诱导相似度与多向视觉结构。

### 关键结果
替换视觉token为高斯噪声后任务准确率骤降，但CKA、SVCCA等4种常用标量度量均无法稳定区分损坏流与原始流；梯度视觉损坏场景下，PA gap追踪任务准确率的一致性远优于传统标量度量；结构化无关图像场景下，PA gap可暴露内部几何与任务准确率脱节的区间。
