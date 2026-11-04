---
title: 'Axion 1.0: Open Agent Foundation Models, Simplified'
title_zh: Axion 1.0：极简训练范式的全开源Agent基础模型
authors:
- Yuqi Jia
- Yunjie Tian
- Jiayu Zheng
- Yijun Liang
- Jingchen Sun
- Mengyu Zhao
- Di Fu
affiliations:
- Duke University
- ByteDance
- University of Maryland, College Park
- University at Buffalo
arxiv_id: '2611.03233'
url: https://arxiv.org/abs/2611.03233
pdf_url: https://arxiv.org/pdf/2611.03233
published: '2026-11-01'
collected: '2026-11-04'
category: Agent
direction: Agent基础模型 极简训练范式
tags:
- AgentFoundationModel
- SFT
- ReinforcementLearning
- SyntheticData
- ToolUse
- OpenSource
one_liner: 用2次轻量SFT加RL的3阶段极简流程训练出对标前沿商用模型的全开源Agent基础模型
practical_value: '- 垂直领域Agent（如电商导购、内容推荐Agent）可复用分阶段训练范式：先做闭域推理SFT，再做工具调用SFT，最后RL对齐长路径决策，无需复杂多阶段DPO/OPD即可获得不错效果

  - 数据构造方法可迁移：针对业务场景（如电商商品属性查询、活动规则计算）用filter-select-compute流程生成可自动验证的工具调用训练数据，过滤闭域可答样本，大幅降低标注成本

  - MoE Agent训练工程优化可复用：用TITO避免tokenization mismatch、R3对齐推理/训练端MoE路由选择，有效降低RL训练不稳定性

  - 轻量迭代验证：业务侧小参数Agent（4B/9B级别）仅用2阶段SFT即可覆盖大部分工具调用、推理需求，可快速上线验证效果，按需加RL提升长路径任务表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent基础模型训练流程日趋复杂，普遍堆叠mid-training、多阶段SFT、DPO/OPD等组件，复现成本高、能力增益来源不透明；且多数开源模型仅开放权重，数据构造、训练流程等核心细节缺失，不利于业务侧二次定制落地。
### 方法关键点
- 3阶段极简训练范式：无额外mid-training/DPO/OPD组件，第一阶段轻量SFT训练自包含推理能力，第二阶段SFT训练工具依赖推理能力，最终用GRPO强化长路径交互决策
- 高质量可验证数据构造：自包含推理数据基于公开种子问题，用4种模型感知的难度增强策略生成，仅保留正确求解轨迹；工具调用数据基于公开结构化数据库，通过filter-select-compute流程自动生成，过滤闭域可答样本确保工具依赖，全程无需人工标注
- 工程优化降低RL不稳定：用TITO机制保留推理端token序列避免重编码偏差，R3机制记录推理端MoE路由决策回放到训练端，大幅降低梯度方差
### 关键结果
- 35B/122B两个版本在6项Agent基准测试中对标前沿商用模型：122B版本在Humanity's Last Exam得分59.0%、FrontierScience Research得分66.7%，超过GPT-5.6 Sol的63.3%；35B版本比同规模Agents-A1在HLE上提升4.6pct、SEAL-0提升5.8pct、FrontierScience Olympiad提升7.0pct
- 训练成本极低：122B版本2阶段SFT仅需7.5小时（240 GPU小时），35B版本仅需2.8小时（90 GPU小时）
### 核心结论
强Agent能力不需要堆叠复杂训练流程，高质量结构化数据+清晰的能力演进训练路径远比重叠的训练组件重要
