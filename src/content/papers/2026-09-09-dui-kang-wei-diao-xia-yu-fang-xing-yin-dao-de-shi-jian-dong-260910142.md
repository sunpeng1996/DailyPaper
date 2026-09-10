---
title: 'Active Adaptation, Not Static Defense: Temporal Dynamics of Preventative Steering
  in Adversarial Fine-Tuning'
title_zh: 对抗微调下预防性引导的时间动态：主动适配优于静态防御
authors:
- Jing Guan
- Yachao Yang
- Zhaoliang Liu
- Yuyao Zhang
- Fanyu Meng
- Junlan Feng
affiliations:
- JIUTIAN Research
- Beijing University of Posts and Telecommunications
arxiv_id: '2609.10142'
url: https://arxiv.org/abs/2609.10142
pdf_url: https://arxiv.org/pdf/2609.10142
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: LLM安全 · 对抗微调防御
tags:
- Adversarial Fine-tuning
- LLM Safety
- Preventative Steering
- Activation Injection
- Progressive Scheduling
one_liner: 揭示对抗微调中预防性引导的两阶段动态，提出渐进强度调度PIS提升LLM安全鲁棒性
practical_value: '- 做LLM Agent persona管控（如电商客服Agent防违规回复、推荐Agent防过度营销）时，可复用文中L2 Norm
  Alignment多特征向量融合方法，平衡不同合规约束的干预强度，避免信号衰减或相互干扰

  - 做LLM微调定向约束时，优先选择attention output projection层做干预，而非MLP层，该路径写入防御信号效率更高，受非线性激活的约束更少

  - 微调过程中的激活注入类干预不要用固定强度，可参考PIS策略：前期用中等强度保证训练稳定，监测到梯度与干预方向对齐度衰减后逐步提升强度，能在不损失模型性能的前提下提升合规性

  - 注入干预向量时仅作用于response token即可，无需覆盖全序列，既能减少对上下文理解能力的损伤，还能获得更好的约束效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM经恶意微调后极易发生安全persona漂移，推理侧防御无法解决参数层面的安全退化，而训练侧的预防性引导方法机制不明确，静态强度设置存在防御效果衰减、性能折衷大的问题，亟需明确其优化动态并设计更有效的调度策略。
### 方法关键点
- 揭示预防性引导的两阶段动态：早期为补偿适配阶段，注入的不良特征向量触发反向梯度推动参数向反方向偏移；后期进入稳态阶段，梯度与注入向量的对齐度衰减，移除注入后防护效果快速消失，证明其依赖主动适配而非静态参数偏移
- 提出L2 Norm Alignment多特征融合方法，校准不同不良特征向量的范数，避免直接平均导致的信号衰减，实现多维度不良特质的均衡抑制
- 提出渐进强度调度（PIS）：前期用中等强度`α_base`注入，监测到梯度对齐度衰减后线性提升强度到`α_max`，维持干预的梯度压力，避免静态强度的效果衰减
### 关键结果
在Qwen2.5-7B/32B、Gemma-3-12B三个模型上测试，对比静态强度基线，最优`Tstart=200`设置下：Qwen2.5-32B安全平均分从80.18提升到86.98，有害特质平均分从3.04降至1.38；Qwen2.5-7B安全平均分从67.55提升到71.95，特质平均分从3.81降至1.45；Gemma-3-12B安全平均分从48.36提升到54.68，特质平均分从5.85降至4.94。

> 最值得记住：预防性引导的防护效果来自训练过程中的持续主动适配，而非可独立复用的静态参数偏移，动态调度干预强度的效果远优于固定强度设置。
