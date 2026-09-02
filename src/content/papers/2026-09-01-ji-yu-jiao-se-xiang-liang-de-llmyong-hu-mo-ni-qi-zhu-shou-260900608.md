---
title: Investigating Assistant Bias in LLM User Simulators Using a Role Vector
title_zh: 基于角色向量的LLM用户模拟器助手偏见研究
authors:
- Daeheon Jeong
- Yoonjoo Lee
- Eugene Choi
- Sinie van der Ben
- Juho Kim
affiliations:
- KAIST
- University of Michigan
- Seoul National University
- ETH Zürich
- SkillBench
arxiv_id: '2609.00608'
url: https://arxiv.org/abs/2609.00608
pdf_url: https://arxiv.org/pdf/2609.00608
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent评测 · LLM用户模拟器优化
tags:
- User Simulator
- Activation Steering
- Assistant Bias
- Role Vector
- Agent Evaluation
one_liner: 从LLM激活层提取用户角色向量，量化并干预用户模拟器的助手偏见
practical_value: '- 电商客服、导购Agent自动评测场景：用用户角色向量干预LLM用户模拟器，生成更真实的不满、中途终止交互等非合作行为，避免高估Agent性能

  - 生成用户行为训练数据时，控制干预系数α在0.1-0.2区间，平衡用户行为逼真度与个性化画像一致性，α过高会覆盖用户特征、过度夸张行为

  - 可将用户角色激活值作为用户模拟质量的监控信号，其与模拟真实度正相关（皮尔逊r=0.426），多轮对话中激活值下降提示出现角色漂移

  - 提取角色向量的对比激活加（CAA）方法可复用，要模拟特定行为用户（如投诉、薅羊毛用户）时，可构造对应行为的角色向量，无需全量微调'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM用户模拟器成为Agent规模化评测的主流方案，替代成本高昂的人工评测，但普遍存在「助手偏见」：模型天生倾向合作、推进任务完成，很少复现真实用户的不满、中途退出等行为，导致Agent性能被系统性高估，普通的prompt角色扮演无法抵消模型训练阶段注入的助手偏好，亟需从表征层解析该偏见的机制并提出干预方案。

### 方法关键点
- 数据：从LMSYS-Chat-1M分层采样24类共720条对话，覆盖多领域对话场景
- 用户角色向量提取：让目标LLM分别从用户、助手视角生成同一段对话的反思，过滤不符合角色的低质量反思后，取指定层首token激活的均值差作为用户角色向量
- 推理干预：将归一化的用户角色向量按系数α叠加到生成时的隐藏层激活，α控制干预强度

### 关键实验
- 单轮请求生成：α=0.3时用户相似度得分比无干预基线高0.5分，超过prompt诱导的用户角色基线，干预效果集中在模型11-13层
- 多轮对话任务：在SimulatorArena数学辅导基准上，α=0.3时整体模拟逼真度比基线高0.12分，其中写作风格相似度提升0.23分；但α>0.2会过度夸张用户行为（疑问率比真实数据高36个百分点），且会掩盖用户个性化画像特征
- 诊断信号：无干预时用户角色激活值和模拟真实度皮尔逊相关系数达0.426，多轮对话中激活值随轮次增加下降，对应角色漂移现象

### 核心结论
LLM的助手偏见是可量化的表征层属性，适度的激活干预可提升用户模拟逼真度，但需平衡通用角色特征和个性化画像的冲突
