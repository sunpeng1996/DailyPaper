---
title: 'Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals
  for On-Policy Self-Distillation'
title_zh: 将技能蒸馏进权重而非提示：基于抽象技能的同策略自蒸馏方法
authors:
- Yubo Jiang
- Fengying Xie
- Zhiguo Jiang
- Haopeng Zhang
affiliations:
- Beihang University
- Tianmushan Laboratory
- Meituan
arxiv_id: '2608.09826'
url: https://arxiv.org/abs/2608.09826
pdf_url: https://arxiv.org/pdf/2608.09826
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: LLM训练 · 同策略自蒸馏
tags:
- Self-Distillation
- On-Policy RL
- Skill Transfer
- Knowledge Distillation
- LLM Training
one_liner: 提出SKALD同策略自蒸馏框架，将抽象技能从训练特权上下文迁移到模型权重，无需测试时技能输入
practical_value: '- 做Agent技能内化时可复用该双分支架构：训练时仅给teacher分支输入特权技能提示，student分支用业务正常输入，蒸馏完成后测试/推理无需额外技能prompt，既降低推理成本，又避免prompt工程的不稳定问题

  - 用RLHF/GRPO训练推荐/广告场景的大模型排序/文案生成能力时，若存在大量全对/全错的rollout组（奖励无区分度，占比通常超过60%），可叠加该特权信号蒸馏补充监督，解决奖励稀疏问题

  - 蒸馏训练出现teacher-student分布不匹配导致的不稳定时，可直接复用退火指数倾斜目标trick：初始大τ压低学生概率极低的teacher token权重，逐渐退火到0恢复交叉熵，适配LoRA微调、全参数训练等多种场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
基于可验证奖励的强化学习（如GRPO）在rollout组内全对或全错时，组归一化优势为0，无梯度信号，这类无效组在实验中占比高达63%~68%，是奖励稀疏的核心来源之一。传统技能应用多放在推理提示中，依赖prompt工程且增加推理成本；现有蒸馏方案要么需要额外大模型作为在线teacher，要么用完整参考答案作为特权信号，存在分布不匹配、答案泄露等问题。
### 方法关键点
- 双分支共享参数架构：同一个基座模型实例化两个上下文视图，student分支仅输入任务query（与部署完全一致），teacher分支额外输入经过答案过滤的抽象结构化技能卡片（包含原理、适用场景、常见错误），无需额外大模型作为在线teacher
- 退火指数倾斜目标函数：初始τ=0.8，自动降低teacher偏好但学生概率极低的token权重，缓解分布不匹配导致的训练不稳定；训练过程中τ从0.8线性退火到0，最终恢复为常规teacher交叉熵，等价于前向KL梯度
- 经验门控机制：仅当初始采样的teacher准确率高于student时才启动蒸馏，过滤无效技能信号；蒸馏仅在学生自己生成的前缀上执行，保证同策略
### 关键结果
在5个数学基准（MATH500、AMC23、AIME24、AIME25、Minerva）上测试，对比GRPO基线，0.6B、1.7B、4B参数规模下avg@8分别提升+2.46、+4.85、+12.01；1.7B规模下，仅在零方差rollout组上蒸馏就能恢复84.7%的全量收益，比同算力GRPO高+4.06，比训练时给学生加技能上下文、测试时移除的方案高+3.77。
> 最值得记住的结论：将技能内化到模型权重的效果远优于放在推理提示中，还能完美补充RL在奖励无区分度场景的监督信号缺失。
