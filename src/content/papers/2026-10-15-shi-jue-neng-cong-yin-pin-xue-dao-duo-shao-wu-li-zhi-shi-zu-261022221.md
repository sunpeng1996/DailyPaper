---
title: How Much Physics Can Vision Learn from Audio? Probing and Distilling Damping
  Structure
title_zh: 视觉能从音频学到多少物理知识？阻尼结构的探测与蒸馏
authors:
- Zainab Afolabi
- Vadim Selyutin
- Zhao Gao
- Babs Khalidson
- Mohamed Ghoneim
affiliations:
- Amazon Web Services
arxiv_id: '2610.22221'
url: https://arxiv.org/abs/2610.22221
pdf_url: https://arxiv.org/pdf/2610.22221
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 跨模态蒸馏 · 物理属性推理
tags:
- Cross-Modal Distillation
- CLIP
- Physical Reasoning
- Knowledge Distillation
- Multimodal Learning
one_liner: 通过跨模态蒸馏将音频编码的阻尼物理知识迁移到冻结CLIP，提升视觉模型物理属性推理能力
practical_value: '- 针对单模态模型无法感知隐含属性的问题，可采用跨模态（如从音频/传感器模态蒸馏知识到视觉模态）方案补全特征

  - 冻结预训练大模型backbone仅训练投影头的蒸馏方案，算力成本低，可快速复用在多模态特征对齐业务场景

  - 涉及材质/物理属性识别的电商场景（如商品摔损风险预判、材质真伪识别）可参考该蒸馏框架优化视觉模型能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有视觉模型难以推断阻尼等决定材料行为的隐含物理属性，而音频可通过冲击后的振动衰减直接编码这类属性，模态间存在显著的能力gap。

### 方法关键点
1. 探测冻结音频、视觉编码器对品质因子Q（阻尼量化指标）的排序能力，用Spearman秩相关ρ评估效果；
2. 以冻结音频编码器为教师，冻结CLIP为视觉骨干，仅训练投影头完成跨模态知识蒸馏；
3. 采用留一材料剔除协议消除类别偏差对评估的干扰，对比单帧、4帧视觉输入的效果差异。

### 关键结果
音频编码器的Q排序ρ达0.73，单帧CLIP仅为0.28；4帧输入+蒸馏方案在留一材料场景下ρ从0.234提升至0.338，较4帧基线高0.053，效果覆盖14/17种测试材料。
