---
title: Reliable Behavior Discovery via False Discovery Rate Control
title_zh: 基于错误发现率控制的可靠大模型行为模式发现方法
authors:
- David Madras
- Zi Wang
- Marco Andreetto
- Ken Burke
- Caroline Pantofaru
- Utsav Prabhu
affiliations:
- Google DeepMind
arxiv_id: '2611.27104'
url: https://arxiv.org/abs/2611.27104
pdf_url: https://arxiv.org/pdf/2611.27104
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 大模型可靠性 · 错误发现率控制
tags:
- FDR Control
- Behavior Discovery
- E-value
- Hypothesis Testing
- Large Language Models
one_liner: 提出可证明FDR可控的DISCO算法，在大模型行为发现任务上优于现有eBH类方法
practical_value: '- 电商推荐/广告的bad case模式挖掘场景，可复用「启发式Agent挖候选模式+eBH统计校验」的两阶段框架，避免将个别偶发bad
  case误判为普遍系统问题，降低运营误判率

  - 构建Agent自主发现用户行为规律、商品属性关联的流程时，可引入DISCO的迭代e-process更新机制，在保证模式可靠性的前提下，提升有效模式的召回率30%以上

  - 大模型生成推荐理由、广告文案的场景，可借鉴FDR控制思路对生成内容的属性（如优惠信息准确性、合规性）做批量校验，将错误信息的占比控制在预设阈值内'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型行为模式发现多依赖启发式Agent方法，假阳性率极高（FDR可达0.4-0.95），大量个别异常案例被误判为普遍行为模式，无法支撑模型对齐、故障排查、合规审计等对可靠性要求高的场景，亟需可从理论上证明错误发现率可控的行为发现方法。

### 方法关键点
- 形式化定义行为发现问题，将其转化为多假设检验任务，明确将FDR（错误发现率）作为核心可靠性度量指标
- 提出DISCO算法：采用迭代bandit式框架，基于粗粒度e-process动态更新每个候选假设的证据值，通过冻结e值超过阈值或查询次数达上限的假设，实现对实际检验假设数的自适应，无需预定义候选假设总量
- 理论上证明DISCO在温和假设下可实现FDR≤α的可控性，支持用实际观测到的检验假设数作为eBH的输入，避免预定义假设数过高导致的检验效力损失

### 关键实验
实验覆盖合成数据、2个文本大模型任务、3个图像生成模型任务，对比基线包括传统eBH方法、5类启发式LLM行为发现方法（自报告、自适应红队等）。核心结果：1）启发式方法不加FDR控制时FDR普遍高于0.4，最高达0.95，几乎没有实用价值；2）加eBH后可将FDR控制在0.1的目标水平，但真发现数平均下降36%；3）DISCO在FDR稳定低于0.1的前提下，真发现数比eBH类方法平均提升约60%，预计算的FDR保证有效概率达97%。

### 核心结论
所有依赖LLM自动挖掘模式的业务流程，都必须加一层统计校验控制假阳性，否则输出的模式大部分都是不可靠的。
