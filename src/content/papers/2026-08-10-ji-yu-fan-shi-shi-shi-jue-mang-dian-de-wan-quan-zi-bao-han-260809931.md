---
title: 'Perception Before Supervision: Self-Contained Visual Distillation from Counterfactual
  Blind Spots'
title_zh: 基于反事实视觉盲点的完全自包含多模态大模型自蒸馏框架
authors:
- Shravan Venkatraman
- Omkar Thawakar
- Ritesh Thawkar
- Abdelrahman Shaker
- Rao Muhammad Anwer
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Aalto University
arxiv_id: '2608.09931'
url: https://arxiv.org/abs/2608.09931
pdf_url: https://arxiv.org/pdf/2608.09931
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 多模态大模型 · 自监督自蒸馏
tags:
- MLLM
- Self-Distillation
- Counterfactual
- LoRA
- Contrastive Learning
one_liner: 无需外部标注或工具，通过识别自身视觉盲点实现MLLM稠密token级自蒸馏，超依赖GPT-4o的基线
practical_value: '- 电商多模态搜索/推荐场景的MLLM微调可直接复用该框架：用海量无标注商品图自蒸馏，提升商品文字OCR、属性识别、细粒度特征匹配能力，无需额外标注成本

  - 三Gate反事实筛选逻辑可迁移到推荐模型自监督优化：挖掘用户行为盲点（如用户漏看的高相关item、query歧义点），构造正负样本对做排序模型自蒸馏

  - 同模型多视图正负teacher+KL锚定的蒸馏架构可复用：无需额外大模型作为teacher，降低训练成本同时避免模型通用能力退化，适合业务端小样本微调场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前多模态大模型（MLLM）自提升存在两类局限：基于奖励的方法仅能提供粗粒度标量反馈，无法给出token级修正信号；蒸馏类方法依赖外部标注、分割工具或更强的教师模型，难以做到完全自包含。细粒度视觉感知的核心瓶颈往往不是模型容量不足或标注数据不够，而是模型无法稳定利用自身已经编码的感知信息。
### 方法关键点
- 三Gate反事实盲点筛选：同时满足三个条件定位有效盲点：裁剪区域后模型答案分布与原图差异大、高斯模糊擦除该区域后答案分布与原图差异小、裁剪后答案分布熵更低，确保区域是模型能感知但全图输入时未利用的信息
- 多源候选区域构造：结合模型自grounding提议、2×2网格、3×3网格三种方式生成候选区域，覆盖不同粒度的潜在盲点，全流程无外部工具参与
- 对比自蒸馏目标：采用同模型EMA权重构造正负教师，裁剪视图为正教师引导模型关注有效区域，擦除视图为负教师推动模型远离注意力盲区，加入KL锚定正则约束模型不偏离原有通用能力
### 关键结果
基于Qwen3-VL-8B-Instruct验证，仅用1.5万张无标注图像生成2590个训练样本，对比6个自进化基线，在12个benchmark上全指标领先，无任何性能退化：OCRBench提升3.60，MMStar细粒度感知提升3.38，MMStar逻辑推理提升3.08，性能超越依赖GPT-4o构造训练数据的基线。
### 核心结论
MLLM细粒度视觉感知的瓶颈并非模型容量不足，而是未能有效激活自身已编码的感知能力，完全可以通过挖掘自身反事实行为实现无外部依赖的自提升
