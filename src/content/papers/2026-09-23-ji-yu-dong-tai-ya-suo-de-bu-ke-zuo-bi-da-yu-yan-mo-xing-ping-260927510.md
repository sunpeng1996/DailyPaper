---
title: 'Uncheatable Eval: Dynamic Compression-Based Evaluation of Language Models'
title_zh: 基于动态压缩的不可作弊大语言模型评估方法
authors:
- Kaifeng Tan
- Yudong Li
- Linlin Shen
affiliations:
- Shenzhen University
- Tsinghua University
arxiv_id: '2609.27510'
url: https://arxiv.org/abs/2609.27510
pdf_url: https://arxiv.org/pdf/2609.27510
published: '2026-09-23'
collected: '2026-09-24'
category: Eval
direction: 大语言模型 · 抗污染评估
tags:
- LLM-Evaluation
- Data-Contamination
- Dynamic-Benchmark
- Lossless-Compression
- Base-Model
one_liner: 提出用新文本无损压缩率作为指标的动态LLM评估基准，规避训练数据污染问题
practical_value: '- 业务侧自研/选型LLM基座时，可复用压缩率评估法，无需构造复杂测试集即可快速验证基座通用能力，规避公开基准的数据污染问题

  - 对比不同架构（注意力/混合/循环）基座的长文本处理能力时，可通过不同上下文长度下的压缩率变化做量化衡量，适配电商商品文案、用户长行为序列建模等场景的选型需求

  - 评估无指令对齐的预训练基座时，无需额外做SFT即可完成能力验证，大幅降低小尺寸基座选型的时间成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM公开评估基准易被预训练数据污染，结果可信度低，且常规任务范式无法适配指令遵循能力弱的基座模型评估需求。

### 方法关键点
1. 搭建动态基准，定期采集最新发布的公开文本作为测试集，从数据端降低污染风险
2. 基于模型预测能力与无损压缩能力的正相关性，直接用文本压缩率作为评估指标，无需指令对齐即可评估基座能力
3. 覆盖14类文本领域，支持不同上下文长度下的模型能力对比

### 关键结果
完成80款模型的评测，得到3个核心结论：
1. 压缩性能随模型尺寸增大呈稳定scaling趋势
2. 注意力、混合、循环架构的压缩性能随上下文长度增长的变化规律存在显著差异
3. 压缩率与零样本MMLU准确率强负相关，可作为基座通用能力的快速评估指标
