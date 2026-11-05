---
title: 'Context--Answer Metamodels: Forecasting LLM Activations Before the First Answer
  Token'
title_zh: 上下文-答案元模型：生成首个回答token前预测LLM激活值
authors:
- Tommy He
- Thomas Jiralerspong
affiliations:
- Tufa Labs
- Mila, Université de Montréal
arxiv_id: '2611.06837'
url: https://arxiv.org/abs/2611.06837
pdf_url: https://arxiv.org/pdf/2611.06837
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM 预生成激活预测与跨模型迁移
tags:
- LLM Activation
- Metamodel
- Pre-generation Forecast
- Cross-model Transfer
- Safety Probe
one_liner: 训练4类元模型从LLM上下文激活预预测回答激活的点/分布，支持跨模型迁移
practical_value: '- 电商/广告Agent内容风险预筛：生成营销文案、客服回答前，通过上下文激活直接预判输出是否涉及违规、虚假宣传，无需多次采样rollout，大幅降低高并发场景下的推理成本

  - 生成式推荐质量预判：调用大模型生成推荐理由、个性化话术前，预判断生成内容的相关性、合规性，提前过滤低质请求，提升用户体验

  - 大模型迭代探针复用：业务从旧LLM升级到新LLM时，原有激活预测探针无需完全重训，仅少量微调即可复用，降低模型迁移成本

  - 低资源场景生成效果评估：无需多次采样计算pass@k，仅通过上下文激活即可预测生成结果的分布方差，适合边缘端、高并发的推荐/客服场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型随机解码下，同一个prompt会生成多个不同回答，评估输出分布、风险通常需要多次采样rollout，计算成本极高，高并发的电商推荐、客服Agent场景下难以落地，亟需在生成首个回答token前即可预判输出的特征与分布。

### 方法关键点
- 两类预测目标：点预测输出回答平均池化激活的期望，分布预测输出回答激活的完整分布
- 4类元模型实现：线性岭回归、MLP做点预测，高斯模型、流模型（Flow）做分布预测
- 特征处理：线性模型取上下文最后一个token激活值，神经模型用32-bin上下文激活trace + 单全局query注意力池化做输入
- 监督信号：同一个prompt对应多次不同随机种子的解码结果，用平均池化的回答激活作为监督

### 关键结果
- 数据集：训练用LMSYS-Chat-1M的50万条prompt，OOD测试用WeirdChat、IFEval数据集
- 点预测效果：50万训练量下MLP域内R2达0.88，OOD WeirdChat R2达0.76，IFEval R2达0.72
- 跨模型迁移：Qwen2.5的上下文激活预测Qwen3.5回答激活的R2达0.81，仅比同模型预测低0.046
- 行为预测：预测激活的行为检测AUPRC比直接用上下文基线最高提升12%

### 核心结论
LLM预填充阶段的上下文激活已蕴含后续生成回答的绝大多数特征信息，无需完整生成即可实现高精度的输出质量与风险预判。
