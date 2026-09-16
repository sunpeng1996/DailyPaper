---
title: Disentangling Representation Evolution in Transformers through Directional
  Decomposition
title_zh: 基于方向分解的Transformer表征演化解耦研究
authors:
- Shwai He
- Haichao Zhang
- Shen Yan
affiliations:
- University of Maryland, College Park
- Northeastern University
- ByteDance
arxiv_id: '2609.15975'
url: https://arxiv.org/abs/2609.15975
pdf_url: https://arxiv.org/pdf/2609.15975
published: '2026-09-13'
collected: '2026-09-16'
category: LLM
direction: 大模型表征分析 · 方向分解
tags:
- Transformer
- Representation Learning
- Model Compression
- Pre-training
- Attention Mechanism
one_liner: 将Transformer层更新分解为平行/垂直分量，揭示鲁棒性差异并优化压缩与预训练流程
practical_value: '- 做LLM4Rec/生成式推荐的推理优化时，可移除注意力value空间非自token的平行分量，长上下文召回任务性能损失<0.5%，有效降低计算冗余

  - 大模型量化/剪枝时，优先降低垂直分量的失真度，该指标和压缩后业务性能相关性>0.97，比传统L2失真的预测准确度高

  - 预训练电商/广告垂直域LLM时，加入平行分量抑制正则项，引导模型容量向语义转向的垂直分量倾斜，2.7B规模模型下游任务最高提升1.5个百分点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer层通过残差加性更新演化表征，大量参数被用于生成与输入方向平行的缩放分量，其功能冗余性长期未被明确；传统模型压缩依赖的L2损失无法区分方向敏感/不敏感误差，常出现量化后效果骤降问题。
### 方法关键点
- 双空间方向分解框架：将残差空间子层更新、注意力value空间聚合结果拆分为平行分量（仅调大小不改语义方向）、垂直分量（改变语义方向）
- 排除自token的干预设计：分解value空间聚合结果时保留自token直接消息，避免误删token身份载体导致性能暴跌
- 覆盖推理编辑、压缩诊断、预训练优化三个全生命周期场景验证分量功能差异
### 关键结果
- 推理干预：垂直分量微小偏差就会导致PPL暴涨数个量级，平行分量在[0,3]区间缩放PPL波动<1.3；30B MoE模型移除value空间平行分量后，零-shot任务性能仅降0.1个百分点
- 压缩诊断：垂直分量失真度与压缩后模型性能相关性>0.97，平行分量失真无预测价值
- 预训练优化：训练时抑制注意力平行分量，2.7B模型下游任务平均性能提升1.5个百分点，验证损失全程低于基线
### 核心结论
Transformer表征演化的核心语义信息由垂直转向分量承载，平行缩放分量普遍冗余，可针对性优化降低计算开销、提升训练效率
