---
title: Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models
title_zh: 门控序列模型中近零词向量引发的无报错训练停滞问题
authors:
- Xin Liu
- Boyuan Sun
- Yuxin Wang
- Haoran Song
- Mingjian Zhao
- Mengyu Liu
affiliations:
- Washington University in St. Louis
- Nankai University
arxiv_id: '2611.04449'
url: https://arxiv.org/abs/2611.04449
pdf_url: https://arxiv.org/pdf/2611.04449
published: '2026-11-02'
collected: '2026-11-04'
category: Training
direction: 大模型训练 · 稳定性优化
tags:
- training_stability
- gated_sequence_model
- Mamba
- gradient_clipping
- AdamW
- weight_decay
one_liner: 发现门控序列模型近零嵌入触发梯度溢出静默丢批次，提出2种无开销修复方案
practical_value: '- 业务用Mamba/xLSTM做长序列召回/多轮Agent全参数微调时，优先选权重绑定的checkpoint，或把输入embedding排除出weight
  decay，避免近零嵌入产生

  - 微调非绑定权重的门控模型时，直接加3行代码实现GroupClip，将embedding和主干梯度分开裁剪，避免FP32溢出丢批次，适配多语言/自定义业务token场景

  - 自研门控模型做生成式推荐/长序列用户建模时，将SiLU门替换为GateFloor（SiLU(z)+δ，δ取0.01~0.1），从训练源头避免梯度放大，PPL几乎无损失

  - 遇训练损失不下降无报错时，优先排查自定义业务token、低频次商品标签的embedding norm是否低于1e-6'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Mamba、xLSTM等门控序列模型被广泛用于长上下文推荐、多轮Agent场景，从业者全参数微调时经常遇到损失不下降且无任何报错的问题，此前无明确根因解释。调研发现52.6%的非权重绑定门控开源模型存在norm低于1e-6的近零token，这些token由AdamW weight decay对训练中未出现的稀有token持续收缩产生，Transformer可通过注意力恢复正常尺度，但门控模型会出现极端梯度放大。

### 方法关键点
- 根因定位：近零输入会让SiLU门/线性查询输出趋近于0，历史状态被压缩，Pre-RMSNorm反向传播时每层梯度放大1e3倍，多层叠加后梯度超过FP32阈值1.84×10^19，全局梯度裁剪溢出为inf，所有批次梯度被静默置零
- 已发布checkpoint修复方案GroupClip：3行代码将输入embedding梯度与主干梯度分开裁剪，embedding梯度用FP64计算norm避免溢出，一步即可修复近零嵌入，无额外时间/内存开销
- 从零训练修复方案GateFloor：在SiLU门输出加0.01~0.1的正偏移，零输入时门输出仍为正，从源头避免梯度放大，效果与基线持平

### 关键结果数字
- 调研291个开源LLM仓库，0%权重绑定模型存在近零嵌入，52.6%非绑定门控模型存在近零嵌入
- 泰卢固语持续预训练场景下，默认FP32裁剪会丢失19.8%的批次更新，GroupClip将停滞步数降为0，1000步的效果比基线快20%达标
- GateFloor在370M参数规模下，可将近零嵌入的梯度降低超过28个数量级，PPL仅差±0.17，吞吐量无损失

> 最值得记住的一句话：门控序列模型全参数训练遇到无报错损失停滞时，90%以上概率是近零自定义/稀有token触发的梯度溢出，优先排查embedding norm或直接上GroupClip
