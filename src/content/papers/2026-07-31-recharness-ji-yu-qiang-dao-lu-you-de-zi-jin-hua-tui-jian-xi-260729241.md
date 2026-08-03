---
title: 'RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender
  Systems'
title_zh: RecHarness：基于强盗路由的自进化推荐系统智能代理框架
authors:
- Haoran Ling
- Yuecheng Li
- Zeyu Song
- Jing Yao
- Shuwen Kang
- Chi Lu
- Wenjin Wu
- Peng Jiang
affiliations:
- Georgia Institute of Technology
- Kuaishou Technology
arxiv_id: '2607.29241'
url: https://arxiv.org/abs/2607.29241
pdf_url: https://arxiv.org/pdf/2607.29241
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 自动化推荐模型迭代优化
tags:
- Multi-Armed Bandit
- LLM Agent
- Recommender System
- AutoML
- Self-Evolving
one_liner: 结合多臂强盗路由与LLM推理，在有限试错预算下自动化迭代优化推荐模型
practical_value: '- 工业推荐模型迭代场景可直接复用「多臂强盗路由选优化方向+LLM生成具体代码修改」的解耦架构，避免LLM无约束探索浪费算力，试错成功率可提升一倍以上

  - 优化陷入局部瓶颈时可借鉴jump-basin机制，阈值触发结构调整类探索方向，搭配局部重调窗口评估结构变更的长期收益，避免错过高潜力的架构类优化

  - 可落地Experiment Skill设计，自动沉淀历史迭代的成功经验、失败避坑规则，给LLM做上下文参考，减少重复无效的代码修改，提升迭代效率

  - 该架构已在成熟的工业广告推荐场景验证收益，可直接接入现有生产推荐系统的迭代流程，替代部分人工迭代工作'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业推荐模型的架构、损失、训练策略迭代高度依赖人工，效率低；直接用LLM Agent做自动迭代易无约束探索，在有限训练/验证试错预算下稳定性差、资源利用率低，亟需更可控的自动迭代框架。

### 方法关键点
- 流程解耦：将优化拆为「方向选择+代码生成」两步，预定义局部调整（超参、正则微调）、结构跳转（架构、损失修改）两类编辑臂，用Thompson采样的多臂强盗路由基于历史标量验证反馈选优化方向，LLM仅在选定方向内生成具体代码修改
- 局部最优逃逸：设计jump-basin机制，连续多轮迭代收益低于阈值时开放结构跳转臂，跳转修改后配套多轮局部重调窗口，评估结构变更的长期收益后再决定是否采纳
- 双通道反馈：标量验证收益更新强盗路由的后验概率，指导后续方向分配；文本实验日志、成功/失败经验沉淀为Experiment Skill，给LLM做上下文参考，降低重复试错率

### 关键结果
离线适配8类不同范式的推荐模型，在Amazon公开序列推荐数据集平均HR@10最高较基线提升85.85%，KuaiRec短视频场景TPM基线的WT-MAE、WR-MAE分别下降26.37%、26.41%；ablation显示带强盗路由的版本试错成功率达47.92%，是随机路由/LLM直接选方向的2倍以上，单轮最大收益达24%。快手短视频广告场景7天线上A/B测试，优化后的模型ADVV提升2.084%、Revenue提升0.534%、Exposure提升0.559%。

推荐模型自动迭代的核心是在有限预算下将试错资源向高潜力方向倾斜，LLM负责具体代码生成、方向选择交给统计路由机制的组合效率远高于LLM全流程自主探索。
