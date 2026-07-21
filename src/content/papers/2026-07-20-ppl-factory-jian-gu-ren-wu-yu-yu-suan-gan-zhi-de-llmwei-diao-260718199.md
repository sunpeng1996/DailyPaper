---
title: 'PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling
  to Reasoning'
title_zh: PPL-Factory：兼顾任务与预算感知的LLM微调高效数据选择框架
authors:
- Hang Zhang
- Warren J. Gross
affiliations:
- McGill University
arxiv_id: '2607.18199'
url: https://arxiv.org/abs/2607.18199
pdf_url: https://arxiv.org/pdf/2607.18199
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: 大模型高效微调 · 数据选择
tags:
- Data Selection
- Fine-tuning
- Perplexity
- LLM
- Efficient Training
one_liner: 基于任务定制困惑度评分与预算动态选择规则，用少量训练数据实现优于全量微调的效果
practical_value: '- 业务场景LLM微调（如生成式推荐文案、Agent推理能力微调）时，可复用任务感知NLL评分逻辑：推理类任务拆分思维链与答案的NLL加权计算，精准筛选高价值样本，无需全量数据即可达到目标效果，降低微调成本

  - 小数据预算场景（如冷启动品类的推荐SFT数据不足），可复用预算感知选择策略：低预算（<30%全量数据）时选中游困惑度样本加随机采样保多样性，高预算时选低困惑度样本去噪，效果优于随机采样

  - 计算资源有限的场景优先选择Perplexity-based数据选择方案，仅需forward推理，比梯度、嵌入类数据选择方法算力开销低，单卡即可完成全流程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM全量微调算力成本高，现有数据选择方法要么依赖启发式规则（如数据质量、推理长度）泛化性差，要么基于梯度、嵌入的方案算力开销大；传统困惑度选择仅计算全序列PPL，忽略语言建模、推理等不同任务的目标差异，极低数据预算下效果骤降甚至不如随机采样，亟需轻量、适配多任务、不同数据预算的高效数据选择方案。

### 方法关键点
- 任务感知NLL评分：CLM任务对分块文本计算平均token NLL；推理任务拆分思维链、答案两部分，按α=1、β=0.5加权计算组合NLL，精准匹配不同任务的学习目标
- 预算感知选择规则：数据预算高（>30%全量）时选低NLL（易）样本去噪；预算中等时选中游NLL样本保信息量；预算极低（<20%）时在NLL中游区间随机采样，兼顾信息密度与数据多样性，避免选择偏差
- 整体流程仅需用冻结的预训练模型做forward推理计算NLL，无额外梯度计算、外部代理模型依赖，算力开销极低

### 关键结果
在4个基准数据集测试，对比随机采样、传统PPL选择、梯度类GraNd/EL2N、Data Whisperer等SOTA方法：1% GSM8K训练数据下准确率超过所有SOTA；10%数据下GSM8K准确率超全量微调0.9、MATH准确率超全量4.8；CLM任务用10%数据即可接近全量微调的PPL效果，训练成本线性降低。

**最值得记住的一句话**：没有通用最优的固定PPL筛选区间，数据选择策略必须同时匹配下游任务目标与可用数据预算，才能在低开销下实现最优效果。
