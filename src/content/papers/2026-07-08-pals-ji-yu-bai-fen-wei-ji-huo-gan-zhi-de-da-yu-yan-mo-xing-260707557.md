---
title: 'PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning'
title_zh: PALS：基于百分位激活感知的大语言模型分层剪枝方法
authors:
- Yazdan Jamshidi
- Alexey Shvets
affiliations:
- Palo Alto Networks
arxiv_id: '2607.07557'
url: https://arxiv.org/abs/2607.07557
pdf_url: https://arxiv.org/pdf/2607.07557
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: 大语言模型 · one-shot 剪枝压缩
tags:
- LLM Pruning
- One-shot Pruning
- Sparsity Allocation
- Activation Outlier
- Model Compression
one_liner: 基于激活百分位动态分配每层剪枝率，零额外成本提升LLM one-shot剪枝性能
practical_value: '- 业务侧LLM轻量化部署（如电商导购Agent、生成式推荐语义理解模型）时，可直接在现有Wanda剪枝pipeline上叠加PALS策略，仅需增加激活百分位计算的微开销，就能在同等稀疏度下保留更好的模型效果

  - 层重要度评估优先选用激活99百分位这类捕捉离群值的统计量，不要使用梯度相关指标，后者在LLM one-shot剪枝场景下效果甚至不如随机分配的剪枝率

  - 剪枝率的层间波动范围控制在±5%可兼顾效果和稳定性，过宽的波动范围会导致层间信息瓶颈，反而大幅降低模型整体性能

  - 若业务使用Mistral/LLaMA-3这类较新、训练充分的模型，各层利用率更均匀，分层动态剪枝的增益极小，直接用统一剪枝即可，无需额外开发'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Wanda、SparseGPT等one-shot LLM剪枝方法对所有Transformer层施加统一稀疏度，忽略不同层的功能差异（早层做基础表征、晚层对接输出、中间层冗余度更高），导致剪枝后性能损失过大；传统小模型剪枝常用的梯度重要度评估在大模型场景下的有效性未经验证，同等稀疏度下的性能还有明显提升空间。

### 方法关键点
- 层重要度用激活99百分位衡量：在小批量校准数据（128条2048token的C4样本）上统计每层激活绝对值的99百分位，标准化后作为层重要度，精准捕捉对模型效果至关重要的激活离群值。
- 分层稀疏度带约束分配：根据层重要度动态调整每层剪枝率，越重要的层剪枝率越低，同时强制剪枝率在全局目标的±5%范围内波动，避免个别层剪枝过度形成信息瓶颈。
- 剪枝逻辑复用Wanda流程：权重评分、剪枝执行完全沿用Wanda的规则，无额外微调需求，仅增加百分位计算的可忽略开销。

### 关键实验
在LLaMA-2-7B、LLaMA-3-8B、Mistral-7B三个模型上测试，对比统一剪枝Wanda、SparseGPT、梯度分配、随机分配等baseline：50%稀疏度下，LLaMA-2-7B的WikiText-2困惑度从Wanda的12.92降至10.96，相对提升15.2%，4项下游零样本任务平均准确率提升1个百分点；LLaMA-3-8B增益仅0.3%，Mistral-7B无任何增益；梯度分配的困惑度高达47.32，效果远差于随机分配的24.37。

### 核心结论
LLM one-shot剪枝场景下，梯度大小无法反映离散权重移除的实际影响，激活离群值是更可靠的层重要度信号，且剪枝率层间波动控制在±5%时效果与鲁棒性最优。
