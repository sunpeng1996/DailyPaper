---
title: 'ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate
  Hallucinations in Large Vision-Language Models'
title_zh: ReWEIGH：校准Token级有序视觉证据缓解大视觉语言模型幻觉
authors:
- Jihae Jeong
- Junha Choi
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology (POSTECH)
arxiv_id: '2608.19075'
url: https://arxiv.org/abs/2608.19075
pdf_url: https://arxiv.org/pdf/2608.19075
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态大模型 · 幻觉缓解解码优化
tags:
- LVLM
- Hallucination Mitigation
- Training-free
- Decoding Optimization
- Inference Acceleration
one_liner: 提出无训练解码干预ReWEIGH，校准token级视觉证据降低LVLM幻觉，推理延迟增量可忽略
practical_value: '- 电商多模态商品理解、直播内容审核、AI导购等LVLM落地场景，可直接复用ReWEIGH无训练解码方案，无需微调即可降低属性幻觉，不影响原有业务效果

  - 推理侧可借鉴prefill阶段缓存视觉证据的工程优化策略，额外延迟仅1.33%，适配线上高吞吐的多模态调用场景

  - token级证据阈值校准的思路可迁移到生成式推荐的多模态商品文案生成场景，避免生成商品不存在的规格、功能等描述'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LVLM推理时易受强语言先验干扰，生成无图像支撑的幻觉内容，现有解码干预方案普遍存在计算成本与幻觉抑制效果的权衡问题，无法兼顾线上性能要求。
### 方法关键点
1. 采用跨视觉位置的词汇排序聚合视觉证据，规避不同位置概率量级不可比的问题；
2. 基于无标注图像预计算token专属证据参考阈值，推理prefill阶段缓存图像证据，仅对低于参考阈值的候选token施加有限惩罚；
3. 完全无训练，无需修改模型结构与权重。
### 关键结果
在4种7B LVLM骨干上，幻觉物体提及量最高降低21.3%，同时保留甚至提升通用描述与推理性能；缓存证据后单token推理额外延迟仅1.33%，效果可覆盖6种架构、32B参数量级模型。
