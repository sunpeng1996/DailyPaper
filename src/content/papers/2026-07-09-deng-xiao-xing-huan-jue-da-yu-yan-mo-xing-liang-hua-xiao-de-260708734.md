---
title: 'The Illusion of Equivalency: Statistical Characterization of Quantization
  Effects in LLMs'
title_zh: 等效性幻觉：大语言模型量化效应的统计特征分析
authors:
- Baha Rababah
- Cuneyt Gurcan Akcora
- Carson K. Leung
affiliations:
- University of Manitoba, Canada
- Red River College Polytechnic, Canada
- University of Central Florida, USA
arxiv_id: '2607.08734'
url: https://arxiv.org/abs/2607.08734
pdf_url: https://arxiv.org/pdf/2607.08734
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM后训练量化 · 行为一致性评估
tags:
- Quantization
- Post-Training Quantization
- LLM Evaluation
- Attention Layer
- Correctness Agreement
one_liner: 提出正确性一致性指标揭示量化LLM行为偏移规律，定位注意力Q/K层为量化高敏感组件
practical_value: '- 部署LLM驱动的推荐/Agent服务时，不能仅用perplexity/准确率评估量化模型，新增正确性一致性指标衡量与基线模型的决策对齐度，避免业务效果出现不可预期波动

  - 做低比特量化优化时，对注意力Q、K投影层分配更高比特精度，V、O层可采用更激进压缩策略，平衡推理效率和效果稳定性

  - 业务场景选型量化方案时，优先选择Q4_K及更高比特配置，Q3_K为可接受的性能损耗临界点，避免使用Q2_K带来显著行为漂移

  - 自建量化方案可复用文中的统计漂移（均值/偏度/峰度）、分布散度（KL/KS）指标，提前定位量化带来的模型结构损伤，减少全量业务评测成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有后训练量化的评估仅依赖准确率、困惑度等聚合指标，无法捕捉量化带来的模型细粒度行为偏移：很多时候量化模型的聚合指标与基线接近，但具体样本的决策结果存在显著差异，会导致LLM驱动的业务（如推荐话术生成、Agent决策）出现不可预期的效果波动。
### 方法关键点
- 提出**正确性一致性（CA）**指标：统计基线与量化模型同时预测正确的样本占比，独立于绝对准确率衡量决策层面的对齐度
- 从两个维度量化注意力层权重的量化漂移：统计特征（均值/偏度/峰度/标准差）、分布散度（KL散度/KS统计量/余弦相似度/欧氏距离）
- 覆盖llama.cpp的8bit到2bit全系列量化方案（legacy/K-quantization），做层粒度的系统性扫描
### 关键结果
在Llama3.2-3B、Vicuna-7B、Mistral-7B、Llama3.1-8B四个主流开源模型，以及WikiText2、C4、HellaSwag、Winogrande、ARC数据集上验证：
1. 8~5bit量化下结构漂移极小，Q4_K为安全量化上限，Q3_K开始出现可感知的性能下降，Q2_K会发生显著行为崩坏
2. 注意力Q、K投影层的量化漂移是V、O层的2~3倍，为量化最高敏感组件
3. 当量化模型的准确率仅下降1~2个百分点时，正确性一致性已经下降5~10个百分点，传统指标完全无法感知这类行为漂移

量化模型与基线模型的等效性只是幻觉，即使准确率、困惑度接近，两者的决策行为也可能存在显著差异。
