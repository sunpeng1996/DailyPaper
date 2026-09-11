---
title: 'An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics'
title_zh: 训练Nemotron斩获国际数学奥赛金牌的开源全流程方案
authors:
- Ivan Moshkov
- Stephen Ge
- George Armstrong
- Wei Du
- Sadegh Mahdavi
- Igor Gitman
affiliations:
- NVIDIA
arxiv_id: '2609.10712'
url: https://arxiv.org/abs/2609.10712
pdf_url: https://arxiv.org/pdf/2609.10712
published: '2026-09-08'
collected: '2026-09-11'
category: Reasoning
direction: 大模型数学推理 · 全开源流水线
tags:
- LLM Reasoning
- Math Reasoning
- Supervised Fine-Tuning
- Reinforcement Learning
- Open Source
- Inference Pipeline
one_liner: 基于Nemotron 3 Ultra构建无外部工具的纯自然语言推理系统，2026 IMO获30分达金牌线，全流程组件开源
practical_value: '- 多checkpoint ensemble的收益远高于单模型堆采样量：可直接迁移到推荐系统的多召回/多排序模型融合、Agent任务的多生成模型互补，用更低计算量覆盖更多长尾场景

  - generate-verify-refine的迭代链路可复用在电商文案生成、推荐理由个性化生成、广告合规校验场景，先批量生成候选，再用专门的校验模块做质量筛查，最后基于反馈迭代优化，大幅降低bad
  case率

  - 校验链路的分层阈值设计可迁移到推荐链路的粗/精/重排阶段：召回/粗排阶段用宽松阈值保留潜力候选，精排阶段用严格规则滤除bad case，终选阶段用多模型打分选最优，平衡效率和效果

  - 多任务混合SFT的数据集构造思路：可用于垂直领域小样本微调，同时加入生成、校验、修正类样本，让模型同时具备生成和自检能力，降低后续推理链路的校验成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
已有的IMO金牌级数学推理系统要么依赖形式化证明器等外部工具，要么闭源不可复现，行业缺乏纯自然语言复杂推理任务的全流程可落地参考方案，同时也需要明确训练策略、推理链路设计对复杂推理效果的实际影响。

### 方法关键点
- 底座基于Nemotron 3 Ultra 550B MoE，训练2个专用checkpoint：SFT在41万+高质量数学证明样本上微调，覆盖生成、校验、修正、元校验4类任务，支持426K长上下文；RL用异步RL框架优化证明生成能力，奖励仅保留正确性指标
- 推理采用两阶段流水线：第一阶段迭代搜索，3个checkpoint并行生成候选，RL+SFT双checkpoint全票通过校验的候选进入池子，未通过则基于校验反馈迭代修正，最多8轮；第二阶段终选，3个checkpoint共48次IMO风格打分，选均值最高的提交
- 全程无外部工具、形式化证明器、联网依赖，纯自然语言完成全流程

### 关键结果
2026 IMO官方赛事获30/42分，超过金牌线29分，全程消耗4800 GB200 GPU小时，生成23.1亿token；30题开发集上，ensemble方案比单RL checkpoint总分高8分，多checkpoint分摊采样量比单checkpoint翻倍采样量收益高5倍以上；双checkpoint全票校验的假阳率仅1.1%

> 最值得记住的结论：复杂推理任务的收益主要来自互补的微调checkpoint、校验引导的迭代优化、终选阶段的充足计算投入，而非更复杂的路由或修正策略，过度过滤反而会丢弃有潜力的候选
