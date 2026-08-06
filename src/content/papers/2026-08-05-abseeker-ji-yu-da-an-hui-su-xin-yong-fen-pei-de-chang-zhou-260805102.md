---
title: 'ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit
  Assignment'
title_zh: ABSeeker：基于答案回溯信用分配的长周期搜索Agent训练框架
authors:
- Yijun Lu
- Rui Ye
- Jiajun Wang
- Yuwen Du
- Tian Jin
- Songhua Liu
- Siheng Chen
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.05102'
url: https://arxiv.org/abs/2608.05102
pdf_url: https://arxiv.org/pdf/2608.05102
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent · 长周期搜索信用分配优化
tags:
- SearchAgent
- CreditAssignment
- GRPO
- SFT
- LongHorizonReasoning
one_liner: 通过答案回溯的细粒度信用分配，用8.5k样本训练4B搜索Agent性能追平30B级模型
practical_value: '- 做电商导购/多轮搜索Agent训练时，可复用ABC框架：从已知正确商品/答案回溯关键决策点（如品牌、价格、属性约束），给每步交互打分，无需浪费失败轨迹中的有效动作

  - SFT阶段可直接套用加权损失方案：基于step得分用sigmoid映射权重，强化高价值动作的梯度贡献，压低错误/冗余步骤权重，比全轨迹统一SFT效果提升显著

  - RL阶段可替换GRPO的轨迹级奖励为step级奖励，配合低γ值（如0.25）做短步优势传导，适配多步搜索、多轮导购这类长交互任务的训练

  - 小参数模型做Agent可参考样本高效训练方案：仅用8.5k标注轨迹就能让4B模型追平30B模型效果，适合端侧/低算力场景的搜索Agent落地'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期搜索Agent需要多步连续动作完成信息检索、验证、整合，现有训练方法（SFT/RL）对轨迹内所有步骤统一赋权，无法区分有效动作、错误/冗余动作：成功轨迹里的无效动作会被误强化，失败轨迹里的有效探索会被误惩罚，稀疏的轨迹级奖励严重限制长交互Agent的性能上限。
### 方法关键点
- 提出Answer-Backtracked Credit Assignment（ABC）细粒度信用分配框架：分为两步，第一步**答案回溯线索恢复**：从已知标准答案反向检索验证，抽取出连接问题到答案的中间实体、事实、关系等核心线索；第二步**线索锚定步骤打分**：基于预设规则给每步交互打0-2分，发现/验证正确线索加0.8，排除错误候选加0.4，错误舍弃正确线索减0.8，提交正确答案加1，提交错误答案减1，基础分为1.0
- 基于step级得分优化训练流程：ABC-SFT阶段用sigmoid函数把step得分映射为损失权重，重新加权每步的SFT损失；ABC-GRPO阶段把step得分直接作为GRPO的步级奖励，计算discounted advantage优化策略
### 关键实验
基于Qwen3.5-4B训练，仅用8.5k条轨迹：无上下文管理时BrowseComp得分37.3%、BrowseComp-ZH得分39.1%，加上下文管理后得分提升到55.3%、52.9%，远超同规模4B基线，性能追平30B级搜索Agent；GAIA-text得分81.6%，超过所有30B级基线。

**最值得记住的一句话**：即使失败的Agent交互轨迹里也有10%左右的有效动作，通过答案回溯的细粒度信用分配可以充分挖掘这些信号，大幅提升小模型Agent的训练效率和性能。
