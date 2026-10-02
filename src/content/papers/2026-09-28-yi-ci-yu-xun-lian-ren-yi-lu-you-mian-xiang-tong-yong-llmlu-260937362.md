---
title: 'Pretrain Once, Route Anywhere: Towards a Foundation Model for LLM Routing'
title_zh: 一次预训练、任意路由：面向通用LLM路由的基础模型RouteFM
authors:
- Guannan Lai
- Han-Jia Ye
affiliations:
- 南京大学人工智能学院
- 南京大学软件新技术国家重点实验室
arxiv_id: '2609.37362'
url: https://arxiv.org/abs/2609.37362
pdf_url: https://arxiv.org/pdf/2609.37362
published: '2026-09-28'
collected: '2026-10-02'
category: LLM
direction: LLM系统 · 通用路由基础模型
tags:
- LLM Routing
- Foundation Model
- In-context Learning
- Transfer Learning
- Model Selection
one_liner: 提出跨异构环境预训练的通用LLM路由基础模型RouteFM，无需重训即可适配新任务新模型池
practical_value: '- 多LLM调用的Agent/广告文案生成场景可直接复用RouteFM框架，新增模型/切换业务域时无需重训路由，仅需提供候选模型的少量历史行为数据即可完成适配，大幅降低运维成本

  - 电商推荐冷启动场景可借鉴其「无ID绑定的行为建模+目标条件检索+候选池联合对比」架构，新用户/新商品无需依赖固定ID embedding，仅靠行为序列即可建模偏好/能力，提升冷启动排序效果

  - 多Agent任务调度系统可复用其episodic预训练范式，跨异构任务预训练通用路由能力，新增任务类型时无需调整模型参数，仅通过上下文信息即可完成最优Agent的路由决策'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM路由方法均为单环境局部拟合，路由模型绑定特定业务的查询分布与候选模型池，一旦出现业务域切换、候选模型新增、模态变化等场景，就需要重新收集标注数据、重训路由模型，运维成本极高，能力无法跨场景复用，亟需可迁移的通用路由范式。
### 方法关键点
- 无身份依赖建模：不使用模型ID、参数规模等显式身份特征，仅基于历史查询embedding、响应质量、推理成本三类行为数据建模候选模型能力
- 双分支表征融合：将可变长度的行为序列压缩为固定长度的能力Profile，同时保留原始行为序列，目标查询分别从两个分支检索相关证据，残差融合得到候选的目标适配表征
- 候选池联合对比：所有候选表征输入Transformer做联合编码，路由决策基于候选相对表现而非独立打分，同时支持动态调整质量-成本权重适配不同部署需求
- episodic预训练：跨异构路由环境构造训练episode，随机变化任务、候选池规模、上下文长度、候选顺序，训练出的通用路由能力部署时完全冻结，无需微调
### 关键实验结果
预训练使用4个公开路由数据集共173万条查询-模型观测数据，跨模态迁移测试在未参与预训练的MMR-Bench上进行：每候选仅8条行为观测时，比最强基线高2.23个质量点；仅用1%的观测数据即可达到Weighted kNN的全量观测效果；新增模型仅需8条观测就超过所有需要重训的基线方案。
### 核心结论
LLM路由本质是可迁移的目标条件排序能力，无需绑定固定环境的ID和分布，一次预训练+上下文适配即可覆盖绝大多数动态部署场景
