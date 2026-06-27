---
title: Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models
title_zh: 自进化大多模态模型视觉Token注意力增强方法VISE
authors:
- Shravan Venkatraman
- Ritesh Thawkar
- Omkar Thawakar
- Rao Muhammad Anwer
- Hisham Cholakkal
- Salman Khan
- Fahad Khan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Aalto University
- Australian National University
- Linköping University
arxiv_id: '2606.27373'
url: https://arxiv.org/abs/2606.27373
pdf_url: https://arxiv.org/pdf/2606.27373
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: 多模态大模型·无监督自进化训练
tags:
- LMM
- Self-Evolution
- Visual Grounding
- Unsupervised Training
- Hallucination Reduction
one_liner: 提出单模型无监督自进化框架VISE，用两种不变性奖励强化多模态模型视觉token注意力
practical_value: '- 可复用「区域扰动（ghosting）+ 语义不变性奖励」的无监督优化思路，优化电商商品图caption、视觉问答模型，减少商品属性/品类幻觉，无需标注数据即可降低生成错误率

  - 几何不变性奖励可迁移到商品主体定位、场景化商品识别任务的无监督微调，提升多模态模型对商品空间位置的理解稳定性，适配主图抠图、场景搭配等业务需求

  - 单模型自进化框架（无需多角色/外部奖励模型）适合用海量无标注商品图做低成本post-tuning，小模型（2B-8B）增益更显著，可快速落地轻量多模态业务场景

  - 工程上可参考其微调策略：冻结视觉编码器，仅用LoRA更新多模态投影层、FFN与解码器注意力投影，避免破坏预训练视觉表征，训练更稳定且成本低'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有自进化LMM依赖多角色自博弈与答案一致性奖励，仅优化输出自洽性，无法保证解码器真正关注视觉内容，会出现「视觉欠条件」问题——生成时依赖语言先验而非图像证据，导致幻觉、图文不符，在图像描述、细粒度VQA等任务上甚至出现性能退化；同时多角色框架易出现训练不稳定、角色坍缩等问题，亟需无需标注的自进化方法直接强化视觉条件。

### 方法关键点
- 框架：VISE单模型无监督自进化，无需多角色分工、外部奖励模型或人工标注，仅用原始无标注图像即可训练
- 几何不变性奖励：对图像施加仿射/裁剪/翻转等已知空间变换，要求模型对同一查询的目标框预测与原框的几何投影一致（GIoU计算奖励），强化空间维度的视觉绑定
- 语义不变性奖励（核心）：将模型预测的目标区域做高斯模糊（ghosting），仅当模型在原图判断目标存在、模糊后判断不存在时给予奖励，直接惩罚不依赖视觉证据的生成
- 优化策略：采用KL正则化的REINFORCE算法，动态调整KL系数维持目标散度；用LoRA微调，冻结视觉编码器，仅更新多模态投影层、FFN与解码器注意力投影，避免破坏预训练视觉表征

### 关键实验
实验覆盖18个基准，涵盖图像描述、VQA/推理、幻觉三类任务，对比VisPlay、EvoLMM、VisionZero等主流自进化基线，在Qwen3-VL、InternVL3、Gemma3、Llama-3.2-VL四个骨干家族上均验证有效。核心结果：Qwen3-VL-2B上，COCO CIDEr提升+16.85，TextCaps提升+19.66，Chair-I物体幻觉降低5.0分，所有任务无性能退化；小模型增益显著大于大模型，语义不变性奖励贡献了约80%的性能提升。

### 最值得记住的一句话
自进化多模态模型的优化不能仅追求答案一致性，直接约束解码器对视觉token的注意力、强化证据绑定，才能带来无tradeoff的全任务增益。
