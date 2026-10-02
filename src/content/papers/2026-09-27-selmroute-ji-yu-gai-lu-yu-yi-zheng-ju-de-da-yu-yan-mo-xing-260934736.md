---
title: 'SeLMRoute: Probabilistic Semantic Evidence for Large Language Model Routing'
title_zh: SeLMRoute：基于概率语义证据的大语言模型路由框架
authors:
- Vasilis Perifanis
- Nikolaos Pavlidis
- Symeon Symeonidis
affiliations:
- Indigma Innovations
- Democritus University of Thrace
- Athena Research Center
arxiv_id: '2609.34736'
url: https://arxiv.org/abs/2609.34736
pdf_url: https://arxiv.org/pdf/2609.34736
published: '2026-09-27'
collected: '2026-10-02'
category: LLM
direction: LLM路由 · 可解释语义特征
tags:
- LLM Routing
- Probabilistic Representation
- Interpretable AI
- Model Selection
- Cost-Performance Tradeoff
one_liner: 基于概率语义证据的可解释LLM路由框架，效果超现有SOTA，支持灵活部署目标
practical_value: '- 多模型路由类任务（电商多LLM客服路由、Agent工具/LLM路由）可复用「先提取查询可解释语义特征再做路由决策」的拆分架构，特征独立于候选池，新增模型无需重新提取历史特征，迭代效率高

  - 语义特征保留概率分布而非硬标签的设计，可直接迁移到电商Query意图识别、用户需求分层任务，保留不确定性信息能提升下游分类/排序效果

  - 业务部署多LLM时可参考论文16个语义探针（推理深度、约束密度、精确性要求等）的设计，快速适配性能优先、成本优先等不同路由目标，无需修改特征层

  - 高QPS场景下可通过特征重要性筛选探针，论文中用12个探针仅损失0.15%精度，减少34%语义提取Token消耗，可平衡效果和延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM路由方法大多直接基于Query embedding、聚类结果学习决策，仅依赖语义相似度无法区分同领域Query的能力要求差异（比如同是Python相关Query，查语法和调试复杂异步程序对模型能力要求完全不同），且决策可解释性差，语义特征与路由目标、候选模型池耦合，迭代成本高。

### 方法关键点
- 拆分路由流程为3个独立模块：语义证据提取→性能预测→路由决策，语义特征与候选模型、部署目标完全解耦
- 定义16个可解释语义探针（8个二元类：是否需要数学推理、代码推理等；8个4级评分类：推理深度、约束密度、精确性要求等），保留每个探针的概率分布输出，构成40维语义特征向量，而非硬标签
- 用轻量CatBoost多输出回归器基于语义特征预测每个候选模型的性能，支持可配置的路由目标，可灵活切换性能优先、成本-性能权衡等不同策略

### 关键实验
在LLMRouterBench的15个数据集共11481条Query、20个候选模型的性能优先场景下，SeLMRoute AvgAcc达72.08%，优于现有SOTA（Avengers为71.94%），比最优单模型高3.27个百分点；13个旗舰模型的性能-成本场景下，平均PerfGain达2.66%；用开源Laya模型替代闭源JEV语义提取器，仍比最优单模型高1.3个百分点。

**最值得记住的一句话：** 路由类任务中，可解释的细粒度语义特征+概率分布保留，不仅能达到甚至超过黑盒embedding的效果，还能大幅提升架构灵活性和部署适配性。
