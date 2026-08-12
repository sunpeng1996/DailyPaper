---
title: 'iFAN: Inference-Aware Learning for Plain Mask Transformers'
title_zh: iFAN：面向普通掩码Transformer的推理感知训练框架
authors:
- Fang Li
- Yu He
- Haoyang Tong
- Lichen Ma
- Jingling Fu
- Wenxiao Fan
- Tongxuan Liu
- Luohang Liu
- Ke Zhang
- Junshi Huang
affiliations:
- JD.com
- Beijing Institute of Technology
- Xi'an Jiaotong University
- University of Chinese Academy of Sciences
arxiv_id: '2608.03216'
url: https://arxiv.org/abs/2608.03216
pdf_url: https://arxiv.org/pdf/2608.03216
published: '2026-08-06'
collected: '2026-08-12'
category: Training
direction: Transformer训练 · 推理感知优化
tags:
- Transformer
- Self-Distillation
- Ranking Loss
- Training Framework
- Inference Efficiency
one_liner: 提出推理感知训练框架iFAN，无推理额外开销即可提升掩码Transformer分割效果
practical_value: '- 排序类任务（如召回、粗排）可借鉴APMR思路，对齐预测置信度与真实排序质量，抑制高置信度低精度的候选结果，提升排序准确性

  - 多层Transformer架构的推荐模型可引入Cross-Layer Self-Distillation，将中间层的优质预测蒸馏到最后一层，无需改动推理逻辑即可涨点

  - 训练时新增辅助损失、蒸馏目标但推理完全复用原有链路的设计思路，可直接复用到业务模型迭代，兼顾效果与推理效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Query-based掩码Transformer训练阶段未针对推理时的query竞争逻辑做显式优化，存在两个核心错配：概率得分最高的query不一定输出最准确的掩码，最终层解码可能丢弃中间层的更优预测。
### 方法关键点
1. 提出通用训练框架iFAN，仅新增训练侧损失，推理完全保留原有高效的最终层解码逻辑，无额外开销。
2. 引入Adjusted Probability-Mask Ranking（APMR）损失，对齐query竞争结果与掩码真实质量，抑制高置信度低精度的query。
3. 引入Cross-Layer Self-Distillation（CLSD），将中间层的优质预测蒸馏迁移到最终层，避免有效信息丢失。
### 关键结果
在COCO、ADE20K、Cityscapes等数据集上，全景分割平均提升1.20 PQ，实例分割平均提升1.30 AP，语义分割平均提升0.63 mIoU，额外参数量、FLOPs、推理延迟可忽略。
