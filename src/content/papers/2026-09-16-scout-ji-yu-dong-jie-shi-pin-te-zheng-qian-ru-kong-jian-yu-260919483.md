---
title: 'SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction
  over Frozen Video Features'
title_zh: SCOUT：基于冻结视频特征嵌入空间预测的跨虚实文本行人检索
authors:
- Abdarahmane Traoré
- Andy Couturier
- Éric Hervet
affiliations:
- Embia
- Université de Moncton
arxiv_id: '2609.19483'
url: https://arxiv.org/abs/2609.19483
pdf_url: https://arxiv.org/pdf/2609.19483
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 跨模态检索 · 冻结模型对齐 虚实域迁移
tags:
- Text-based Person Retrieval
- Sim-to-Real
- Frozen Encoder
- Cross-modal Alignment
- Reranking
one_liner: 提出冻结编码器架构SCOUT，仅训练轻量预测器实现跨虚实文本行人检索，效果接近高成本微调交叉编码器
practical_value: '- 跨模态检索场景可复用冻结大模型+轻量预测器对齐架构，大幅降低训练成本，无需微调基座编码器

  - 选择预训练跨模态基座时，可先用无训练的嵌入空间几何匹配度评分排序候选模型，减少试错成本

  - 低资源Sim-to-Real场景可结合ExPLoRA参数高效微调+无训练属性分解重排，快速提升Top排序精度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
Sim-to-Real场景下的文本行人检索此前依赖高成本微调的交叉编码器，训练资源消耗大，落地门槛高，亟需低资源的冻结编码器方案。
### 方法关键点
将跨模态检索转化为嵌入空间预测任务，基座采用完全冻结的V-JEPA视频编码器和EmbeddingGemma文本编码器，仅训练由Qwen3.5-0.8B解码器初始化的轻量预测器，将视频Patch token映射到文本编码器的嵌入空间，采用双向InfoNCE损失训练；后续可叠加ExPLoRA参数高效微调视频编码器、无训练VLM属性分解重排两个优化杠杆，进一步提升Top精度。
### 关键结果
无训练的嵌入空间对齐评分与检索准确率的斯皮尔曼相关系数最高达1.0；两个优化杠杆共提升R@1 2.2个点；在AI City Challenge 2026 Track4数据集上，全检索-融合-重排系统mAP@10达84.25，单冻结模型mAP@10达60.63；训练总消耗仅95 GPU小时，远低于基线交叉编码器的16 GPU天
