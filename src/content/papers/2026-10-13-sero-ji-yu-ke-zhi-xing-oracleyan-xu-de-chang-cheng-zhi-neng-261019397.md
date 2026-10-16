---
title: 'SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic
  Reinforcement Learning'
title_zh: SERO：基于可执行Oracle延续的长程智能体强化学习框架
authors:
- Dingyi Rong
- Yue Shi
- Chaofan Ma
- Zongrui Wang
- Jiezhang Cao
- Yixin Cao
- Liang He
- Ning Liu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2610.19397'
url: https://arxiv.org/abs/2610.19397
pdf_url: https://arxiv.org/pdf/2610.19397
published: '2026-10-13'
collected: '2026-10-16'
category: Agent
direction: 长程Agent · 强化学习训练优化
tags:
- Reinforcement Learning
- Long-horizon Agent
- Oracle Guidance
- On-policy Distillation
- GRPO
one_liner: 为长程智能体强化学习引入带策略可达性加权的可执行多步Oracle延续辅助训练
practical_value: '- 电商导购、搜索交互类Agent的RL训练可复用SERO的辅助损失设计：不修改原有RL业务流程，仅额外添加Oracle辅助loss，侵入性极低，适配现有GRPO/PPO等训练框架

  - 多步修正信号加权技巧可迁移到业务Agent的专家纠正场景：对运营/规则给出的多步操作序列，按当前策略对前置步骤的兼容性动态加权，避免不匹配的深层步骤干扰训练，尤其提升OOD场景泛化

  - 环境快照恢复的训练范式可复用在可模拟的交互业务场景（如电商导购模拟环境）：对策略走到的失败状态，恢复环境后用专家规则走通全链路，生成多步训练样本，解决稀疏奖励下有效样本缺失问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent的RL训练受限于当前策略探索到的轨迹边界，稀疏延迟奖励下credit assignment极难；现有On-policy Distillation仅用单步Oracle修正信号，忽略修正后环境变化带来的后续多步决策监督，无法覆盖训练初期完全缺失的有效行为分支。

### 方法关键点
- 框架设计：作为纯辅助损失兼容所有现有On-policy RL算法，推理阶段完全不需要Oracle，无额外 overhead
- 可执行Oracle延续：收集当前策略的在线轨迹后，随机选中访问过的状态恢复环境快照，用训练阶段专属Oracle执行多步交互到任务结束，生成全链路的Oracle动作-观测对作为训练样本
- 策略可达性加权：用冻结的行为策略计算每一步Oracle动作的兼容性，第k步的监督权重为前置k步兼容性的乘积，动态压低当前策略难以到达的深层Oracle步骤的权重，随策略迭代自动扩展有效监督深度
- 改进门控：仅当Oracle分支的收益高于原策略同状态的后续收益时，才加入该分支的监督，避免负向干扰

### 关键实验
在ALFWorld家居指令跟随、WebShop电商交互两个长程Agent benchmark上测试，基于Qwen2.5-1.5B/7B模型，对比GRPO、GraphGPO、HGPO等SOTA RL基线：1.5B规模下GraphGPO+SERO将ALFWorld分布内/外成功率从90.63%/88.02%提升到95.83%/91.67%，WebShop任务成功率从77.93%提升到79.27%；7B规模下GraphGPO+SERO将ALFWorld分布外成功率大幅提升11.2个百分点，OOD泛化收益显著。

最值得记住的结论：训练阶段对策略访问的失败状态做环境快照恢复、生成专家全链路执行样本+动态加权的辅助训练范式，能用极低的侵入性大幅提升长程交互Agent的性能与泛化能力。
