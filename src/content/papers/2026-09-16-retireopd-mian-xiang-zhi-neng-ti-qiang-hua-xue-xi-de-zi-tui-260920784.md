---
title: 'RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement
  Learning'
title_zh: RetireOPD：面向智能体强化学习的自退出式同策略蒸馏
authors:
- Yan Yu
- Zhengxi Lu
- Yizhou Liu
- Yichen Pan
- Aozhe Wang
- Qipeng Chen
- Hua Yang
- Wenqi Zhang
- Weiming Lu
- Qianglong Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2609.20784'
url: https://arxiv.org/abs/2609.20784
pdf_url: https://arxiv.org/pdf/2609.20784
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent RL训练 · 自适应同策略蒸馏
tags:
- Reinforcement Learning
- On-Policy Distillation
- LLM Agent
- GRPO
- Knowledge Distillation
one_liner: 提出自适应教师退出的同策略蒸馏框架，让无特权信息的学生内化技能且性能超越教师
practical_value: '- 电商导购Agent、多轮交互推荐场景的RL训练，可复用「先训练带特权信息（运营规则、历史最优策略、召回侧全量特征）的教师，再蒸馏到上线用的轻量无特权学生模型」的范式，既利用特权信息提升训练效率，又不增加推理开销

  - 现有采用GRPO+蒸馏混合训练Agent的业务场景，可直接接入自适应退休机制：监控师生行为差距变化率+学生相对教师成功率，达到阈值后停止蒸馏，不需要预定义退火schedule，可适配不同模型规模和任务，实测能提升10%以上的任务成功率，同时避免教师限制学生性能上限

  - 涉及特权信息蒸馏的场景（如RAG+蒸馏、规则约束+蒸馏的推荐/Agent系统），必须先单独用环境/业务奖励优化教师模型到收敛，不能直接用注入特权信息的未训练模型做教师，否则蒸馏信号不可靠，反而会拉低学生性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮LLM Agent采用RL训练时仅能获得单轨迹级的稀疏奖励，同策略蒸馏（OPD）通过带特权信息的自教师提供token级稠密监督，可加速训练收敛。但现有方案存在两个核心缺陷：一是仅注入特权信息的教师本身未经过任务优化，监督信号不可靠；二是蒸馏收益存在阶段依赖性，学生内化教师技能后，蒸馏梯度会与RL奖励梯度产生冲突，限制学生性能上限，而预定义的蒸馏权重退火、固定阶段切换的方案无法适配不同任务、模型规模的训练动态。

### 方法关键点
- 独立教师构建：师生从同一基座模型初始化，教师先单独用GRPO在带特权技能上下文的条件下训练收敛，再冻结权重提供蒸馏信号，解决教师可靠性问题
- 联合训练阶段：学生无权限访问特权信息，同时优化GRPO环境奖励损失与OPD反向KL蒸馏损失，兼顾稠密监督效率与奖励优化的上限
- 自适应退休机制：每固定窗口监控两个指标：①师生token log概率差的变化率（差距停止缩小即判定梯度冲突）；②学生成功率达到教师的预设比例（默认0.9），同时满足则移除蒸馏损失，后续仅用GRPO训练

### 关键实验结果
在ALFWorld、WebShop两个主流Agent基准上，基于Qwen2.5 1.5B/3B/7B三个模型规模测试，对比GRPO、GRPO+OPD等基线：ALFWorld成功率比纯GRPO高14.1%~18.8%，WebShop准确率高11.8%~19.0%，所有配置下学生性能均超过用于蒸馏的带特权教师。

### 核心结论
同策略蒸馏只是早期训练的临时脚手架而非终身约束，特权信息的价值取决于教师能否将其转化为有效任务行为，而非信息本身。
