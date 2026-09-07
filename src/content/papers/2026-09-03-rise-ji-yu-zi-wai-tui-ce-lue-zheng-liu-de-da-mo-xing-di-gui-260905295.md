---
title: 'RISE: Recursive Improvement via Self-Extrapolating Policy Distillation'
title_zh: RISE：基于自外推策略蒸馏的大模型递归优化方法
authors:
- Yang Li
- Semih Yavuz
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.05295'
url: https://arxiv.org/abs/2609.05295
pdf_url: https://arxiv.org/pdf/2609.05295
published: '2026-09-03'
collected: '2026-09-07'
category: Training
direction: LLM后训练 · 自外推策略蒸馏优化
tags:
- On-policy Distillation
- RLVR
- Self-Improvement
- Policy Distillation
- LLM Training
one_liner: 无需外部模型或特权上下文，外推自身RLVR训练轨迹构造教师实现递归性能提升
practical_value: '- 做电商/广告大模型RLHF/RLVR优化时，可复用RISE的自外推蒸馏框架，无需额外强教师模型，仅用历史训练轨迹就能把稀疏reward转化为dense
  token级监督，提升训练效率和性能

  - Agent多轮交互任务（如电商导购Agent、推荐会话Agent）训练时，可直接复用logit空间外推实现，无需额外存储多份模型参数，工程落地成本极低，仅1.3-1.6x耗时就能获得明显性能增益

  - 训练超参可直接复用：外推系数β采用线性衰减策略（从1.2降到1），锚点用EMA平滑（η=0.1），rollout直接复用RLVR阶段采样结果，无额外采样成本，适配大规模训练场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy distillation（OPD）能为LLM后训练提供token级稠密监督，但现有方案瓶颈明显：外部教师存在分布不匹配问题，基于特权上下文的自蒸馏受限于ICL能力，无法生成可靠的token级监督；而RLVR等方法仅能提供序列级稀疏奖励，存在严重的信用分配难题，无法指导token级优化。

### 方法关键点
- 核心思路：外推模型自身RLVR训练轨迹构造合成未来教师，计算当前checkpoint和历史锚点在参数空间或logit空间的位移，放大β>1倍得到教师，无需外部模型或特权上下文
- 双阶段训练循环：先通过RLVR阶段获得稀疏奖励驱动的参数更新，锚定正确优化方向；再通过OPD阶段把外推教师的token级分布蒸馏到学生模型，实现稠密监督的精细化调整
- 两种落地实现：权重空间外推（直接做参数任务算术，输出逻辑更一致）、logit空间外推（一阶近似，无需操作参数，落地成本更低）；β采用随训练衰减的调度，锚点支持EMA平滑提升稳定性

### 关键结果
在数学推理、多域STEM、代码生成、多轮Agent任务上均优于纯RLVR和特权自蒸馏基线：OLMo3-7B数学推理平均准确率+8.8个点，ALFWorld Agent任务成功率+9.4个点，训练耗时仅为纯RLVR的1.3-1.6倍，无额外采样成本，同时不损失OOD泛化性能。

最值得记住的一句话：LLM自身的训练轨迹本身就包含足够的结构信息，可以作为自改进的教师源，无需引入外部知识就能把稀疏奖励转化为稠密监督信号。
