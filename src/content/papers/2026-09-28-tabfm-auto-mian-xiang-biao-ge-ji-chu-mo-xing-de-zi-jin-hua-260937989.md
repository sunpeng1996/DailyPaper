---
title: 'TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models'
title_zh: TabFM-Auto：面向表格基础模型的自进化数据流水线框架
authors:
- Deqing Fu
- Huangyuan Su
- Rajat Sen
- Taman Narayan
- Sujay Sanghavi
- Abhimanyu Das
- Weihao Kong
affiliations:
- Google Research
- Google DeepMind
- University of Southern California
- Harvard University
- University of Texas at Austin
arxiv_id: '2609.37989'
url: https://arxiv.org/abs/2609.37989
pdf_url: https://arxiv.org/pdf/2609.37989
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 表格基础模型流水线优化
tags:
- LLM Agent
- Tabular Foundation Model
- AutoML
- Pipeline Optimization
- Zero-shot Learning
one_liner: 结合LLM Agent与冻结表格基础模型，通过自进化数据流水线大幅提升零样本表格任务性能
practical_value: '- 电商结构化数据场景可复用「冻结大模型+Agent迭代外围流水线」架构，无需微调大模型，仅迭代预处理、特征、后处理逻辑，成本低收益高，适合用户行为、交易等表格类预测/推荐任务

  - 特征迭代可参考分层策略：优先用LLM挖掘字段语义生成领域特征（如复购率、客单价衍生特征），再补充统计特征、关联特征，大幅降低人工特征工程成本

  - 新业务冷启动场景下，该方案比从零训练的AutoML模型效果更优（论文中比AutoGluon高300+Elo），适合小样本下的推荐/转化率预测任务

  - 搜索到的预处理、特征逻辑可直接迁移到同领域其他冻结表格模型，无需重复搜索，适合业务多模型并行部署场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有表格基础模型（TFM）仅基于数值、类别索引预训练，忽略列名、任务描述等语义信息，零样本性能受限；传统MLE Agent需从零搜索模型结构、特征、超参全链路，搜索空间大噪声高，易过拟合，两者互补性未被有效挖掘。
### 方法关键点
- 架构配对**冻结TabFM**与LLM编码Agent，Agent仅迭代数据流水线，不改动TabFM权重，无梯度训练开销，评估速度快无训练噪声
- 流水线拆分为4个可迭代模块：数据清洗（缺失值/异常值处理、目标变换）、语义特征工程（基于列名生成领域特征、统计关联特征）、上下文采样（适配TFM上下文窗口，分层采样平衡样本）、后处理（概率校准、目标逆变换），同时支持调整TabFM推理参数
- 迭代逻辑以3折交叉验证分数为优化目标，沙箱环境运行避免测试集泄露，最优流水线直接部署
### 关键实验结果
- 覆盖TabArena 51个公开表格数据集（38分类+13回归）、MLE-Bench 8个表格竞赛数据集
- 对比基线包括原生TabFM、TabFM+、AutoGluon 1.5、TabPFN系列、现有MLE Agent等
- 5种TabFM-Auto配置包揽TabArena总榜前5，最优版本将TabFM Elo从1785提升至2013（+228），比AutoGluon 1.5高344 Elo；搜索到的流水线可直接迁移到其他TFM，带来69~143 Elo提升；在MLE-Bench表格任务上排名所有MLE Agent第一

最值得记住的结论：冻结预训练大模型+Agent迭代外围数据/推理流水线，是比Agent从零搜索全链路模型方案效果更好、成本更低的落地路径
