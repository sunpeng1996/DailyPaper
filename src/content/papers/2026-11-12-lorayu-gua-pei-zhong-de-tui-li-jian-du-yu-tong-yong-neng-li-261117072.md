---
title: Reasoning Supervision and Capability Retention in LoRA Domain Adaptation
title_zh: LoRA域适配中的推理监督与通用能力保留研究
authors:
- Saleh Ashkboos
- Dhruv Desai
- Lavinia Ghita
affiliations:
- NVIDIA
arxiv_id: '2611.17072'
url: https://arxiv.org/abs/2611.17072
pdf_url: https://arxiv.org/pdf/2611.17072
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 大模型微调 · LoRA训练优化
tags:
- LoRA
- Domain Adaptation
- Reasoning Supervision
- Fine-tuning
- Capability Retention
one_liner: 系统对比三类LoRA微调范式，证实仅标签响应式LoRA兼顾域内性能与通用能力保留
practical_value: '- 业务侧LoRA域适配优先选用仅标签的响应式LoRA，不要盲目引入推理蒸馏：实测推理监督不仅不会提升域内分类性能，还会劣化校准效果、增加训练成本，可直接复用在电商类目预测、用户意图分类等分类任务的微调中

  - LoRA超参数调优可直接复用论文验证的最优范围：有效学习率（α/r * 原始LR）控制在1.25e-5 ~ 2.5e-5区间，α选8/16小值、LR选5e-5左右低阶值，可大幅减少调参成本

  - 若需兼顾业务分类与Agent通用推理能力，可尝试25%压缩比的推理轨迹蒸馏，能在损失少量域内校准效果的前提下轻微提升通用推理能力，IFEval仅下降2个百分点左右

  - 分类任务LoRA微调无需引入双Adapter拆分rank的方案，实测无性能收益还会增加工程复杂度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LoRA是资源受限场景下大模型域适配的主流方案，但现有方案易出现域内性能提升的同时通用能力严重退化的问题，尤其针对长输入分类任务，如何兼顾域内效果、校准能力和通用推理能力是业务落地的核心痛点，此前缺乏针对推理监督引入方式的系统对比研究。

### 方法关键点
- 以Qwen3-8B为学生模型、Qwen3-32B为教师模型，在20万条金融新闻标题分类数据集上做对比实验，固定LoRA总rank为32
- 对比三类训练范式：1）仅标签响应式LoRA，只监督最终分类标签的损失；2）单Adapter推理监督，用加权混合损失同时监督推理轨迹和标签，λ控制两者权重；3）双Adapter复合训练，拆分rank为轨迹Adapter和标签Adapter，分别用混合损失和仅标签损失训练
- 新增轨迹压缩消融，用教师模型将推理轨迹压缩为原长的25%/50%/75%，对比压缩比的影响

### 关键实验结果
- 数据集为20万条FinHeadlineMix金融新闻标题，共35个分类，域内指标为Acc、Macro-F1、NLL、Brier得分，通用能力保留指标为MMLU-Pro、GPQA、IFEval
- 仅标签LoRA域内Acc较 frozen 基线提升3.3~3.4个百分点，Macro-F1提升4.5~5.8个百分点，通用能力指标与基线基本持平，校准效果（NLL、Brier）提升最显著
- 单/双Adapter推理监督方案域内指标普遍低于仅标签LoRA，仅MMLU-Pro有<1个百分点的轻微提升，无实际业务价值
- 25%压缩比的推理轨迹训练可将校准指标向仅标签方案靠拢，仍未超过后者，且会拉低IFEval约2个百分点

**最值得记住的一句话：针对分类类域适配任务，无特殊推理需求时优先选用仅标签的响应式LoRA，引入推理监督不仅不会带来收益，反而会劣化域内校准效果、增加训练成本**
