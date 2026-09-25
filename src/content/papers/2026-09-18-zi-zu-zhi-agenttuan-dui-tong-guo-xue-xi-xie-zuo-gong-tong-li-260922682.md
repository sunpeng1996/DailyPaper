---
title: Self-Organizing Agent Teams Learn to Reason Together
title_zh: 自组织Agent团队通过学习协作共同完成推理任务
authors:
- Aneesh Pappu
- Mirac Suzgun
- Yongchan Kwon
- Federico Bianchi
- Batu El
- Mykel J. Kochenderfer
- Hancheng Cao
- James Zou
affiliations:
- Stanford University
- Together AI
- Goizueta Business School, Emory University
arxiv_id: '2609.22682'
url: https://arxiv.org/abs/2609.22682
pdf_url: https://arxiv.org/pdf/2609.22682
published: '2026-09-18'
collected: '2026-09-25'
category: MultiAgent
direction: 多Agent 自组织协作推理优化
tags:
- MultiAgent
- Collaborative Reasoning
- Self-Organizing
- Team Strategy
- Transfer Learning
one_liner: 提出自组织Agent团队（SAT），通过少量样本学习通用协作策略，跨任务迁移大幅提升推理性能
practical_value: '- 多Agent协作场景可复用SAT的离线策略学习范式：用少量历史样本让指定Agent复盘协作过程，迭代生成通用协作规则（如审单、异常处理角色分配），无需硬编码流程，适合复杂商品审核、客诉处理等Agent团队场景

  - 策略选择阶段可借鉴「coverage-greedy」的策略池构建逻辑：优先保留跨场景迁移性好的协作策略，避免过拟合特定任务，适配推荐场景下多模态内容理解、多目标排序等跨域需求

  - 可参考demonstrability结论设计协作流程：在推理结果可验证性高的场景（如营销文案合规检查、订单逻辑校验）优先部署多Agent协作，增益远高于单Agent；对主观类任务（如用户偏好打分）需额外强化结果校验环节'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent系统多依赖固定协作协议、预定义任务分解或路由规则，无法在问题结构未知的场景下动态组合各Agent的局部推理结果，难以产出单个Agent无法独立生成的更优解；人类团队可通过协作经验自发形成分工、沟通流程，这一能力尚未在AI Agent团队中有效落地。

### 方法关键点
- Self-Organizing Agent Teams（SAT）架构核心为固定Agent阵容，由指定高能力Agent通过复盘历史协作过程，迭代优化包含角色分工、对话阶段、参与规则、信息流模式的通用协作策略，仅用少量训练样本离线完成策略学习后冻结策略池，直接迁移到未见过的任务
- 协作策略用领域特定语言定义，核心是多轮会话阶段的配置，不预设具体子任务拆分，推理过程中Agent可动态交换、校验、补全局部推理结果，实现协作计算
- 测试阶段用策略池中的所有策略生成候选解，搭配每步可校验的推理证书，由指定Judge Agent选择最优解，区分「生成正确解」和「识别正确解」两个核心环节

### 关键实验
数学物理赛道用15个AIME 2024题训练策略，在5个推理基准上平均准确率达66.7%，比最强单Agent高17.9pp，比完美路由Oracle高7.7pp，AIME 2026上超出Oracle 13.4pp；知识逻辑赛道用25个GPQA题训练，跨3个基准平均准确率72.8%，策略池覆盖度达87.9%。跨8个基准的相关性分析显示，任务的推理可验证性（demonstrability）与SAT相对单Agent的提升幅度斯皮尔曼相关系数达0.90（p=0.005）。

### 核心结论
Agent团队的组织协作能力本身可作为独立的可学习能力，无需预定义任务拆分即可通过少量样本学习通用策略，产出单个成员无法独立生成的正确解。
