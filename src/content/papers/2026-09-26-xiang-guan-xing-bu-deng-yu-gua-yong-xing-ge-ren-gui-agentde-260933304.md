---
title: 'Relevance Does Not Imply Applicability: Experience Activation for Personal
  GUI Agents'
title_zh: 相关性不等于适用性：个人GUI Agent的经验激活框架
authors:
- Fuyao Zhang
- Xuan Wang
- Zherui Li
- Jiaming Zhang
- Longtao Huang
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
- Alibaba
arxiv_id: '2609.33304'
url: https://arxiv.org/abs/2609.33304
pdf_url: https://arxiv.org/pdf/2609.33304
published: '2026-09-26'
collected: '2026-10-13'
category: Agent
direction: GUI Agent 个性化经验复用优化
tags:
- GUI Agent
- Experience Reuse
- Personalization
- Proactive Suggestion
- Training-free
one_liner: 提出免训练ExpActivator框架，通过决策级经验激活大幅提升GUI Agent个性化执行与主动建议效果
practical_value: '- 可复用「先召回相关候选，再决策级细粒度激活」的范式替代传统RAG全量塞上下文的做法，既节省token又提升效果，比如电商导购Agent处理用户模糊需求时，先召回历史相关会话，再匹配当前页面状态激活对应操作参考

  - 主动建议场景可借鉴「双重阈值+场景+时间加权」的激活规则，先卡绝对支持度阈值再排序，避免误触发，比如电商APP主动推送、语音助手routine建议可复用这套逻辑降低打扰率

  - 免训练适配思路可直接落地：用现有冻结模型的隐层特征做匹配，不需要额外训练记忆控制器，快速在现有业务Agent上叠加个性化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化GUI Agent普遍采用任务级检索全量拼接历史上下文的方案，默认相关经验对任务内所有决策都有效，但实验发现这类方案仅对任务首步有提升，剩余90%步骤增益几乎为0，主动建议场景下也无法准确判断触发时机，核心问题是**任务级相关性≠决策级适用性**：前者是任务维度的匹配，后者依赖决策时刻的具体场景。

### 方法关键点
- 提出免训练框架ExpActivator，从任务级检索转向决策级经验激活，覆盖两个粒度：
  1. 步骤级激活：执行时先召回Top-K相关历史轨迹，每步用冻结GUI backbone的视觉隐层特征匹配当前屏幕与历史状态，只激活最匹配的历史动作作为参考，每步刷新匹配结果
  2. 任务级激活：主动建议时先通过语义聚类生成用户routine，结合场景匹配+24小时循环时间加权计算支持度，只有同时满足总频次、同场景频次、上下文支持度三个阈值才触发建议，否则静默
- 所有编码器、backbone均保持冻结，仅通过离线预计算历史隐向量、在线轻量内积匹配实现，无额外训练成本

### 关键实验
在AndroidIntent数据集（82用户、135个APP、1.5w+历史记录）上测试，对比4个主流开源GUI backbone、5种基线方法：
- 个性化执行：轨迹内步骤成功率平均提升28%，整体步骤成功率比最优基线高20%，历史token用量仅为基线的1/5
- 主动建议：Matthews相关系数是最优基线的2.3倍，平均精度达84%

### 核心结论
Experience pays where it is activated, not where it is appended（经验在被激活的地方产生价值，而非被拼接的地方）
