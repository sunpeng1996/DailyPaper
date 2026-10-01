---
title: 'AutoDataBench: A Data-centric Testbed for Accelerating Auto Research'
title_zh: AutoDataBench：面向自动化研究加速的以数据为中心的测试平台
authors:
- Ruifeng Yuan
- Yizhi Li
- Yaxin Du
- Fengyu Cai
- Yiqi Liu
- Hou Pong Chan
- Chenghua Lin
- Yun Chen
- Jian Yang
- Bryan Dai
affiliations:
- The Hong Kong Polytechnic University
- Shanghai Jiao Tong University
- The University of Manchester
- Shanghai University of Finance and Economics
- Beihang University
arxiv_id: '2609.40097'
url: https://arxiv.org/abs/2609.40097
pdf_url: https://arxiv.org/pdf/2609.40097
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent能力评测 · 数据智能
tags:
- LLM Agent
- Benchmark
- Data Intelligence
- Auto Research
- Training Data Curation
one_liner: 构建隔离非数据因素的可控测试床，系统评估LLM数据智能能力，其优化轨迹可用于下游模型训练
practical_value: '- 做业务数据治理Agent时，可参考该测试床的控制变量法：固定训练流程、模型结构、算力预算，仅评估Agent的数据策略效果，避免性能归因混淆

  - 电商/推荐场景的训练数据优化可复用三类任务范式：数据诊断修复（清洗标注错误的用户行为/SFT样本）、数据组织（构造召回模型hard negative样本）、数据构造（生成领域知识注入的QA样本）

  - 业务落地数据优化策略时必须单独预留OOD验证集：实验显示LLM优化的ID性能高不代表OOD泛化性好，避免过拟合现有标注分布

  - 可沉淀数据治理、样本构造的Agent迭代轨迹作为训练数据，用于微调垂直领域专用数据Agent，降低重复优化成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自动化研究基准混淆了训练框架、超参、算力、数据等多种优化来源，无法准确归因Agent性能提升的核心因素，而数据质量是决定模型效果的核心变量，亟需可控测试床专门评估LLM理解、处理、优化训练数据的能力（数据智能）。

### 方法关键点
- 变量隔离设计：固定每个任务的训练框架、模型结构、算力预算、原始数据集，仅允许Agent输出数据干预策略，确保评估聚焦数据智能
- 覆盖三类核心数据智能任务：数据诊断修复（清洗带噪声的工具调用训练数据集）、数据组织（构造embedding模型的对比学习训练样本）、数据构造（生成知识注入的QA训练样本）
- 双重评估维度：除目标任务的in-distribution（ID）效果，额外设置hidden OOD测试集评估泛化性，同时记录Agent对数据干预效果的预测，评估其数据因果推理能力
- 轨迹复用机制：收集Agent迭代优化的全交互轨迹，可作为训练数据提升下游模型能力

### 关键结果
评测7款前沿LLM，核心数字如下：
1. 工具调用数据修复任务：LLM最高ID准确率达82.45，接近人工清洗参考值81.65，OOD BFCL准确率最高59.44
2. Embedding样本构造任务：LLM最高ID nDCG@10达41.66，接近专家策略的40.62，但OOD性能普遍低于专家的34.76，最高仅30.18
3. 知识注入样本构造任务：LLM最高Novel准确率达62.40，比专家策略的48.40高14个百分点
4. 测试床的Agent优化轨迹加入mid-training后，SWE-bench Multilingual性能提升5.66个点，CRUXEval提升2.12个点

> 最值得记住的话：以数据为中心的Agent能力评估必须隔离非数据变量，ID性能提升不代表OOD泛化性，优化轨迹本身也是高价值的训练数据
