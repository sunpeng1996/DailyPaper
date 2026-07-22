---
title: 'Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven
  Perceptual Realignment'
title_zh: 通过显著性驱动感知对齐缓解大视觉语言模型的幻觉问题
authors:
- Pengxu Chen
- Yao Zhu
- Guangming Zhu
- Jun Sheng
- Jincai Huang
- Xiangyang Ji
- Liang Zhang
affiliations:
- Xidian University
- Tsinghua University
- Shanghai Road Transport Development Center
- Hunan Institute of Advanced Technology
arxiv_id: '2607.16841'
url: https://arxiv.org/abs/2607.16841
pdf_url: https://arxiv.org/pdf/2607.16841
published: '2026-07-18'
collected: '2026-07-22'
category: Multimodal
direction: 多模态大模型 · 幻觉缓解优化
tags:
- LVLM
- Hallucination
- KV Cache
- Attention Mechanism
- Contrastive Decoding
one_liner: 无训练开销的SDPR框架，从注意力、KV缓存、解码三层缓解LVLM幻觉，运行开销极低
practical_value: '- 电商多模态商品理解、AI直播话术生成、图生商品文案等LVLM落地场景，可直接复用SDPR的无训练优化方案，无需重训即可降低幻觉，几乎不增加线上
  latency

  - 可借鉴KV cache对齐思路，在多模态生成任务中仅保留与查询相关的视觉特征，减少长生成路径下的视觉信息退化，提升商品属性识别、图文匹配的准确率

  - 显著性驱动的注意力重分配方法可迁移至多模态召回排序场景，过滤非语义冗余token的干扰，提升跨模态检索、用户query与商品的匹配精度'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
LVLM在多模态理解场景表现优异，但生成内容易出现与视觉证据不符的幻觉，现有方法大多针对语言先验偏差或跨模态不平衡优化，未覆盖感知与记忆阶段的渐进式视觉信息退化问题。
### 方法关键点
训练无关的SDPR框架从全生成链路对齐视觉感知，包含三个核心模块：1）显著性驱动注意力重分配，释放被非语义沉没token劫持的注意力，恢复关键视觉证据；2）显著性驱动缓存对齐，修复KV cache中的空间畸变，生成过程中保留查询相关视觉特征；3）先验约束对比解码，惩罚由主导语言先验导致的不忠实预测。
### 关键结果
在多类LVLM架构上验证，SDPR在幻觉检测基准和通用多模态基准上均优于SOTA方法，无额外训练成本，仅带来可忽略的运行开销
