---
title: 'The Router Within: Eliciting Native Skill Routing from a Frozen LLM'
title_zh: 从冻结大模型中挖掘原生技能路由能力的轻量方案Gavel
authors:
- Ruishuo Chen
- Xun Wang
- Yu Chen
- Zhuoran Li
- Longbo Huang
affiliations:
- Institute for Interdisciplinary Information Sciences, Tsinghua University
arxiv_id: '2609.15982'
url: https://arxiv.org/abs/2609.15982
pdf_url: https://arxiv.org/pdf/2609.15982
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent 轻量技能路由优化
tags:
- Skill Routing
- Frozen LLM
- Linear Projection
- Agent
- Product of Experts
one_liner: 仅训练2个线性层从冻结LLM提取原生路由信号，性能超过带1.2B-16B参数的外部路由流水线
practical_value: '- 做Agent技能/工具路由无需额外搭建大参数检索重排流水线，仅需给现有冻结LLM加2个共7.9M参数的线性投影层，训练成本极低且零样本迁移能力强，大幅降低算力开销

  - 新技能入库仅需一次前向传播生成key bank，无需重新训练模型，适配电商频繁更新的工具/服务/运营规则的动态场景

  - 多路由信号融合采用Product of Experts方案，比传统召回后仅靠重排打分的方式效果更优，该思路可直接迁移到推荐系统多通路召回结果融合场景

  - LLM约70%深度的中间压缩谷层语义表征质量最高，做语义向量、用户意图识别时可优先选取该层隐藏状态，无需依赖最后一层输出'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent技能路由的两种主流方案均存在明显缺陷：渐进式披露需要把所有技能元数据塞入上下文，挤占窗口资源、分散模型注意力，只能硬性限制技能库规模；检索重排方案将选择逻辑交给外部独立模型，脱离Agent本身的语义理解能力，泛化性差，且无法随Agent基座升级自动提升路由效果。

### 方法关键点
- 仅训练2个线性投影矩阵（共7.9M参数），从冻结LLM约70%深度的中间压缩谷层读取路由信号，全程不向上下文注入任何技能文本，不挤占任务窗口
- 第一阶段Glance：技能安装时通过单次前向传播得到中间层状态，投影为key bank后用ε-cover压缩到原大小的1/8.5，失真不超过1.6个点；任务侧直接复用解码过程产生的中间层状态投影为query，通过token级最大相似度投票得到全库技能排名
- 第二阶段Verdict：仅对Glance输出的短名单技能，复用安装时的前向前缀续接任务，一次性读取任务生成似然和技能适配性yes/no判断两个原生信号
- Glance相似度、生成似然、适配性判断三个信号作为独立专家做乘积融合，得到最终路由结果

### 关键实验
- 数据集：3个公开技能选择基准，以及自建的372条覆盖4类多轮场景的Agent轨迹基准SkillTraj
- 对比基线：带8B/0.6B外部嵌入+重排的检索流水线、渐进式披露方案
- 核心结果：基于Qwen3-32B基座，比最强基线在书面任务上最高提升13.4个Hit@1点，多轮中途路由场景最高提升21.9个点；Skill-Use基准上正确技能触发率达90.9%，超过Codex中参数规模大得多的前沿模型

**最值得记住的一句话**：冻结LLM本身已经具备技能选择需要的全部能力，仅需轻量读出层即可释放该能力，无需额外部署大参数路由模型。
