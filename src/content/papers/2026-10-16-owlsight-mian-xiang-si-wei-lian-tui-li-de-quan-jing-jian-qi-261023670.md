---
title: 'OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning'
title_zh: OwlSight：面向思维链推理的全景监控器
authors:
- Lewen Yan
- Yanxu Zhu
- Jie Zhang
- Jing Shao
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Beihang University
arxiv_id: '2610.23670'
url: https://arxiv.org/abs/2610.23670
pdf_url: https://arxiv.org/pdf/2610.23670
published: '2026-10-16'
collected: '2026-10-19'
category: Reasoning
direction: 推理监控 · CoT多维度行为检测
tags:
- Chain-of-Thought
- LLM Monitoring
- Safety Alignment
- Multiple Instance Learning
- Reasoning Oversight
one_liner: 提出基于自定义Factor的轻量CoT监控器OwlSight，实现多维度多粒度推理行为监控
practical_value: '- 做电商导购Agent、客服Agent的行为审计时，可复用Factor自定义机制，无需为每个监控目标（诱导私下交易、虚假宣传、隐私泄露等）单独训练分类器，大幅降低运维成本

  - 处理长Agent交互轨迹/长CoT时，可复用Top-2 MIL窗口聚合方案，在固定显存预算下覆盖全轨迹，避免硬截断丢失关键监控信号

  - 对监控规则有频繁调整需求的业务场景，可参考粗细粒度Factor混合训练策略，支持业务人员通过自然语言修改监控规则无需重新训练模型

  - 落地Agent行为异常检测系统时，优先选择小参数LLM做SFT专用监控器，相比通用大模型/通用Guard模型，细分场景效果更好、推理延迟更低、部署成本更低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

#### 动机
现有CoT监控方案均为单一任务定制，无法覆盖前沿推理模型的多维度风险（如奖励破解、欺骗、隐私泄露、越狱等），也不能灵活适配不同粒度的监控需求，无法支撑大规模AI系统的全景监管，在电商Agent、导购机器人等落地场景下，也难以灵活响应多变的业务审计需求。
#### 方法关键点
- 提出Factor机制：用户可通过自然语言自定义监控目标，支持粗粒度（如是否存在隐私泄露）和细粒度（如是否泄露特定用户手机号）两种粒度，同一监控模型可适配所有监控目标，无需为每个任务单独训练
- 数据构造：覆盖能力、安全、可信3大类11个监控维度，同一条CoT可配对不同Factor生成不同标签的训练样本，采用结果标注+全轨迹标注结合的标注方案，保证标签准确性
- 训练优化：基于小参数LLM做SFT训练，针对长CoT采用多实例学习（MIL）方案，将长轨迹拆分为重叠窗口，取Top2窗口得分平均做最终预测，避免硬截断丢失关键信号，同时大幅降低显存占用
#### 关键实验
在包含15971条推理轨迹、32222条Factor条件查询的自建基准上测试，对比通用大模型和专用Guard模型：细粒度监控G-Mean2达69.57，超通用LLM基线1.32~30.57分；粗粒度监控G-Mean2达66.80，超通用LLM基线11.71~27.81分，在OpenAI CoT可监控性基准上达到SOTA；对CoT压缩、混淆、Factor重表述均保持鲁棒性，长轨迹训练显存比全上下文方案降低25.5%~49.2%，可支持250k token以上的长CoT监控。
> 最值得记住的一句话：小参数专用监控模型通过规则引导的训练，可以实现比通用大模型和通用Guard模型更好的监控效果，同时成本更低、灵活性更高
