---
title: 'MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal
  Search Agents'
title_zh: MMSearch-OPD：长时序多模态搜索Agent的可控难例构造与混合训练方法
authors:
- Huanyao Zhang
- Jiepeng Zhou
- Jiaye Lin
- Ontai Tang
- Jingtian Hao
- Mugeng Liu
- Ru Peng
- Lang Mei
- Xiaohan Yu
- Liyan Liu
affiliations:
- Peking University
- HKUST(GZ)
- Tsinghua University
- The University of Hong Kong
- Huawei Cloud BU
arxiv_id: '2610.22240'
url: https://arxiv.org/abs/2610.22240
pdf_url: https://arxiv.org/pdf/2610.22240
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 多模态搜索Agent 难例构造与训练优化
tags:
- Multimodal Agent
- Search Agent
- Reinforcement Learning
- On-Policy Distillation
- Synthetic Data
one_liner: 提出可控多模态难例生成管道与RL+on-policy蒸馏联合训练方案，显著提升长时序多模态搜索Agent性能
practical_value: '- 难例构造可复用：现有简单VQA/搜索query数据可通过Expand（加推理跳数）、Blur（实体模糊化）、Visualize（加视觉证据）三种算子生成难训练样本，无需从零标注，大幅降低长序列Agent训练数据成本

  - 训练范式可迁移：长序列决策型Agent（如电商多模态商品搜索Agent、导购Agent）可采用SFT初始化+RL+reward加权的on-policy蒸馏联合训练，比纯SFT提升2-3个点准确率，同时优化决策效率

  - 奖励设计可借鉴：除最终结果奖励外，增加无效工具调用、重复搜索等行为惩罚，对失败/低质量轨迹按奖励gap施加动态强度的token级教师指导，指数衰减蒸馏系数避免过度依赖教师

  - 难度分层思路适用：训练数据按难度分层，简单样本做SFT、难样本做RL训练，平衡训练稳定性和性能上限，适配电商复杂多轮导购、跨模态商品检索等场景的Agent训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长时序多模态搜索Agent训练面临两大核心痛点：一是高难度训练样本构造成本极高，需要人工收集实体关系、标注图片、验证证据链，现有数据集多为短推理链的易解问题，无法支撑长序列决策能力训练；二是长序列搜索过程反馈薄弱，仅靠终端奖励无法有效指导中间搜索行为，轨迹级优势信号颗粒度太粗，难以学习复杂跨模态推理流程。

### 方法关键点
- 可控难例生成管道Refine：复用现有简单VQA样本的推理链，通过三个可配置算子调整难度：Expand新增L跳证据链增加搜索深度，Blur对M个实体替换为W条间接线索增加消歧要求，Visualize为N个实体关联P张可检索图片、Q条视觉事实增加跨模态证据要求，最终合成符合「每条证据必要、答案唯一」要求的难样本
- 联合训练范式：先基于高质量轨迹做SFT初始化，再采用RL+on-policy蒸馏（OPD）联合优化：奖励包含最终答案得分+无效/违规搜索行为惩罚，基于GRPO计算RL优势；仅对失败/低质量轨迹施加token级教师指导，指导强度随奖励gap动态调整，蒸馏系数指数衰减逐步降低对教师的依赖

### 关键结果
在7个主流多模态搜索基准上测试，9B参数的MMSearch-OPD平均准确率达60.2%，比同参数原生Agentic Workflow高15.3个点，比之前最优的同规模搜索Agent高9.6个点；纯SFT比基线高13个点，RL+OPD联合训练比纯SFT再高2.3个点；难例生成后单轨迹平均工具调用从6.6次提升到33.7次，有效强化长时序搜索能力。

### 核心结论
将现有易解数据升级为要求持续证据采集的难例，结合结果优化与选择性教师指导，是低成本训练长时序跨模态搜索推理Agent的有效路径。
