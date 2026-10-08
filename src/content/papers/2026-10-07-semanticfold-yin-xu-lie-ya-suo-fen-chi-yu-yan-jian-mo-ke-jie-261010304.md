---
title: 'SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability,
  and Reasoning'
title_zh: SemanticFold：隐序列压缩分离语言建模、可解码性与推理能力
authors:
- Mingyan Liu
- Min Huang
affiliations:
- 香港中文大学（深圳）
arxiv_id: '2610.10304'
url: https://arxiv.org/abs/2610.10304
pdf_url: https://arxiv.org/pdf/2610.10304
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: 大语言模型 · 隐序列压缩与能力评估
tags:
- LLM Compression
- Latent Sequence Compression
- KV Cache Optimization
- Reasoning Evaluation
- Frozen LLM Tuning
one_liner: 提出冻住Decoder Transformer的隐序列压缩方法，证实不同能力保留指标不可互换
practical_value: '- 做LLM驱动的电商文案生成、推荐理由生成、Agent推理任务的推理优化时，不能仅用NLL、PPL等通用指标验收，必须针对业务场景做专项压测，避免指标好看但实际业务效果掉点

  - 可复用SemanticFold的轻量压缩方案：仅微调百万级参数的压缩器，冻结LLM主干，压缩长上下文（如用户历史行为序列、多轮对话上下文）的中间隐状态，降低KV
  cache占用，适配长序列推荐、多轮Agent场景

  - 压缩边界选择无需过度追求余弦相似度最优方案，1.3~1.7压缩比下随机合法边界与最优边界无显著效果差距，工程上可简化实现降低压缩阶段的计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM压缩方案普遍依赖PPL、NLL等单一指标衡量能力保留度，但工程实践中频繁出现指标达标但下游推理、生成效果大幅跳水的问题，缺乏可控的实验手段明确不同能力保留指标的关联关系，也没有通用的压缩安全阈值指导落地。
### 方法关键点
- 针对冻结权重的Decoder-only Transformer，在指定中间层将相邻隐状态对通过轻量压缩器合并为单个隐状态，输入token、主干权重、输出层完全不变，可精确控制压缩比R
- 压缩器采用加权平均+残差MLP结构，仅需训练百万级参数，远小于主干模型参数量，训练成本极低
- 设计四类独立评估端点：固定目标续写NLL、输出分布与原生模型的KL散度、任务标签线性可解码性、推理任务实际准确率
### 关键结果
- 测试覆盖Qwen3、SmolLM2、Pythia系列模型，评估数据集包括WikiText、9个BBH推理任务共450条Prompt
- Qwen3-1.7B在R=1.7压缩比下，固定目标续写NLL下降0.135，但推理准确率下降5.2个百分点；尾保护策略将输出分布与原生模型的DKL从1.404降至0.527，但推理准确率仅提升1.56个百分点（置信区间过零，无统计显著性）
- 压缩边界选择上，余弦相似度选边界与随机合法边界在R=1.3、1.7下无显著准确率差距
### 核心结论
没有通用的LLM压缩安全阈值，能力保留度完全依赖下游任务与具体模型，任何单一指标都不能作为所有场景效果合格的证明
