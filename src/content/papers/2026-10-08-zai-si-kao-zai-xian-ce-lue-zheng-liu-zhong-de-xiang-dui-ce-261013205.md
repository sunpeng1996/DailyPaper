---
title: Rethinking Relative Policy Differences Transfer of On-Policy Distillation
title_zh: 再思考在线策略蒸馏中的相对策略差异迁移机制
authors:
- Rong Wu
- Daocheng Fu
- Yu Yang
- Xuemeng Yang
- Siqi Li
- Shu Zou
- Yao Zhu
- Botian Shi
- Bo Zhang
- Cong Zhang
affiliations:
- 浙江大学
- 上海人工智能实验室
- 复旦大学
- 澳大利亚国立大学
- 中国人民大学
arxiv_id: '2610.13205'
url: https://arxiv.org/abs/2610.13205
pdf_url: https://arxiv.org/pdf/2610.13205
published: '2026-10-08'
collected: '2026-10-12'
category: Training
direction: LLM训练 · 在线策略蒸馏
tags:
- On-Policy-Distillation
- Knowledge-Distillation
- RLHF
- SFT
- Policy-Transfer
one_liner: 提出任意对任意的A2-OPD蒸馏框架，明确相对策略差异有效迁移的三大核心条件
practical_value: '- 做LLM驱动的电商Agent/推荐生成模块蒸馏时，优先用RL/SFT得到的策略差作为监督信号，纯模型缩放带来的性能差迁移效率低3-10倍，甚至可能带来负增益

  - 构建蒸馏的专家-参考对时，参考模型不需要是专家的训练基座，选择和目标模型同系列的参考模型可让跨基座迁移成功率从0提升到80%以上

  - 不用盲目追求更大的专家模型，专家与参考的性能差和目标增益的相关系数达0.96，优先选择任务优化带来的策略差更大的配对即可获得最优收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
常规在线策略蒸馏（OPD）依赖远强于学生的教师模型，适用场景受限；近年的相对策略差异迁移虽降低了对教师绝对能力的要求，但缺乏对有效迁移条件的系统性梳理，不清楚哪些策略差能迁移、哪些目标模型能从中收益，亟需明确通用框架和落地规则。

### 方法关键点
- 从隐式奖励视角推导相对策略差异迁移的统一目标，提出任意对任意的A2-OPD框架，将代理专家与代理参考的对数概率比作为隐式奖励，解耦代理对和目标模型的选择，常规OPD是其特例
- 优化时对每步动作的权重做中心化处理，抵消状态相关的归一化项偏移，降低梯度方差，无需计算不可解的配分函数
- 实验覆盖RL、SFT、模型缩放三类策略差来源，跨Qwen2.5/3两个系列多尺寸模型，在数学、代码两个任务域验证

### 关键结果
- 任务优化（RL/SFT）带来的策略差迁移效率远高于纯缩放：同增益下迁移效果是缩放差的7-10倍，代理性能差与目标增益的皮尔逊相关系数达0.96
- 参考模型起过滤作用：选择和目标同系列的参考模型，可让跨系列迁移的目标增益从负转正，最高提升30个百分点以上
- 策略差迁移不依赖模型距离：同系列模型即使KL距离超过1.2，仍可获得60%以上的性能增益实现率，跨系列即使距离小也可能迁移失败

**最值得记住的一句话：** 在线策略蒸馏的核心是迁移任务优化带来的策略改进方向，而非大模型的绝对输出分布
