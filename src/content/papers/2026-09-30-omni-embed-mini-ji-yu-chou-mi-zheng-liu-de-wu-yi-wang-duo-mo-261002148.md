---
title: 'Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation'
title_zh: Omni-Embed-Mini：基于稠密蒸馏的无遗忘多模态绑定嵌入模型
authors:
- Mohammed Irfan Kurpath
- Jaseel Muhammad Kaithakkodan
- Sahal Shaji Mullappilly
- Ivan Laptev
- Hisham Cholakkal
affiliations:
- Mohamed Bin Zayed University of Artificial Intelligence (MBZUAI)
arxiv_id: '2610.02148'
url: https://arxiv.org/abs/2610.02148
pdf_url: https://arxiv.org/pdf/2610.02148
published: '2026-09-30'
collected: '2026-10-03'
category: Multimodal
direction: 多模态嵌入 · 跨模态对齐蒸馏
tags:
- Multimodal Embedding
- Knowledge Distillation
- LoRA
- Contrastive Loss
- Cross-Modal Alignment
one_liner: 0.9B参数轻量多模态嵌入模型，冻结文本编码器对齐6种模态，无文本检索退化，比同类模型小2.7-9.5倍
practical_value: '- 可复用「冻结文本编码器+模态侧LoRA+轻量投影」的跨模态对齐架构，迭代多模态能力时不会退化已有文本检索效果，适配电商多模态商品检索、短视频内容推荐场景

  - 采用「多模态样本对应稠密caption的预训练文本嵌入作为蒸馏监督信号」的方案，无需额外训练teacher模型，大幅降低多模态嵌入模型的训练门槛与成本

  - Matryoshka SigLIP对比损失+在线动态难负例挖掘的训练组合，可直接迁移到跨模态召回模型训练，提升跨模态召回的精度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有文本嵌入模型扩展多模态能力时普遍出现文本检索效果退化问题，且开源全模态嵌入模型参数量高达数十亿，部署成本高。
### 方法关键点
1. 冻结文本侧所有参数作为锚点，仅在非文本模态编码器上新增轻量投影层和分阶段LoRA适配器完成跨模态对齐；
2. 无需单独训练teacher模型：将每个多模态样本的级联稠密caption输入冻结文本编码器得到的embedding作为监督信号，保证师生侧向量空间几何完全一致；
3. 训练结合Matryoshka SigLIP对比损失，搭配随编码器效果提升动态调优的在线混合难负例挖掘器。
### 关键结果
0.9B参数版本支持6种模态统一映射到共享余弦空间，文本检索在MTEB-v2 BEIR-8上达49.57 nDCG@10无退化，参数量比同类开源模型小2.7~9.5倍；2.3B版本效果对标闭源Gemini Embedding 2，全模态平均得分更优。
