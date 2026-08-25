---
title: 'SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning'
title_zh: 面向长序列推理的自反思策略优化框架SRPO
authors:
- Jialong Liu
- Yuling Shi
- Ning Yang
- Xiaodong Gu
- Zuchao Li
affiliations:
- 武汉大学
- 上海交通大学
- 中国科学院自动化研究所
arxiv_id: '2608.23493'
url: https://arxiv.org/abs/2608.23493
pdf_url: https://arxiv.org/pdf/2608.23493
published: '2026-08-24'
collected: '2026-08-25'
category: Training
direction: Agent长序列推理策略优化
tags:
- SRPO
- Policy Optimization
- Long-Horizon Reasoning
- Self-Reflection
- On-Policy Distillation
- Agent Training
one_liner: 无需外部奖励模型或大教师，通过自反思将稀疏反馈转为稠密token级监督，提升长序列推理与Agent性能
practical_value: '- 对于电商导购Agent、多轮搜索推荐Agent这类长交互任务，可直接复用SRPO两阶段流程：先让Agent自生成错误反思补丁，再蒸馏到基模型，无需额外标注成本，解决稀疏
  reward 下的信用分配问题

  - 训练时采用LoRA rank=128适配SRPO即可达到全量微调97.8%的性能，显存占用降低72%，适合中小模型快速迭代业务效果

  - 可借鉴反思补丁的设计：强制生成2-5条结构化诊断+可执行建议，避免冗长反思带来的语义漂移；优先用模型自生成的反思而非大模型输出的反思，避免分布不匹配导致效果下降

  - 电商多轮转化任务（如加购、下单）可复用反向KL做稠密token级监督的思路，比传统终端reward的RL方法训练效率提升3.8倍，效果更优'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM后训练方法（PPO、GRPO等）在长序列推理、多轮Agent任务上存在严重的信用分配问题，仅靠终端稀疏反馈梯度方差大、样本效率极低，还易出现熵塌陷；传统推理时自反思方法会导致上下文语义漂移，训练时引入外部大教师模型成本高、分布不匹配问题严重，亟需低成本高效的长序列任务训练框架。

### 方法关键点
- 两阶段pipeline：第一阶段收集初始rollout的终端反馈，让模型自生成2-5条紧凑的反思补丁（包含错误诊断+修正建议），将补丁拼接到原始prompt前重构输入，得到带事后信息的教师分布；第二阶段用基模型（学生）生成on-policy rollout，最小化学生输出与教师分布的反向KL散度，实现稠密token级监督蒸馏。
- 核心设计：采用reset-with-memory机制而非迭代追加反思，避免语义漂移；用反向KL而非正向KL做监督，更聚焦最优策略模式；采用组相对优势估计，无需额外价值函数，训练更稳定。
- 无额外依赖：全程用同一个模型同时做学生和教师，不需要外部奖励模型、更大的教师模型，训练成本大幅降低。

### 关键结果
在数学推理基准AIME'24、Agent基准WebShop/ALFWorld/SWE-Bench-Lite上测试，对比GRPO、PPO、外部大教师蒸馏等基线：Qwen3-8B base上AIME'24准确率达73.3%，仅用8%的SFT训练FLOPs；WebShop成功率64.7%、ALFWorld 76.8%、SWE-Bench-Lite 31.2%，总训练FLOPs比GRPO减少3.8倍；LoRA-128适配可达到全量微调97.8%的性能，显存占用降低72%。

### 核心结论
LLM可以利用自身的事后反思能力作为动态教师，无需外部大模型就能实现自举式的性能提升，尤其适合稀疏反馈的长序列交互任务。
