---
title: 'When History Misleads: Asymmetric Margin Supervision for Instruction-Guided
  LLM Generative Recommendation'
title_zh: 面向指令引导LLM生成式推荐的非对称边距监督方法
authors:
- Ming Yin
- Yuhan Yang
- Chen Chen
- Xinyu Lin
- Wentao Shi
- Fangcong Yin
- Chaofei Yang
- Chao Yang
- Jiyan Yang
- Hui Zhang
affiliations:
- Duke University
- Meta
arxiv_id: '2610.02600'
url: https://arxiv.org/abs/2610.02600
pdf_url: https://arxiv.org/pdf/2610.02600
published: '2026-10-01'
collected: '2026-10-05'
category: GenRec
direction: 生成式推荐 · 指令历史冲突优化
tags:
- Generative Recommendation
- LLM4Rec
- Semantic ID
- Margin Loss
- Instruction Tuning
one_liner: 提出AIMS框架解决生成式推荐中历史行为误导当前指令请求的问题，无需修改推理逻辑
practical_value: '- 训练Trick可直接复用：做指令引导生成式推荐时，可直接接入ACS非对称损失，仅通过竞争item回传梯度，避免与CE对目标item的优化冲突，无需修改推理逻辑，落地成本极低

  - 冲突场景优化思路：电商搜索/推荐中用户当前query与历史行为冲突的场景（如之前买母婴用品现在搜美妆），可借鉴反事实边距构造思路，无需过滤历史输入即可降低误导历史的权重，比历史裁剪方案保留更多个性化信息

  - 工程落地经验：AIMS默认单历史事件删除、仅取1个边界竞争item即可拿到最优收益，多事件删除仅增加计算量无明显涨点，适配工业级训练吞吐要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
指令引导的LLM生成式推荐需要同时响应当前指令与匹配历史偏好，但二者冲突时历史行为经常覆盖指令需求，现有优化方案存在两个核心缺陷：一是历史事件对预测的影响大小与其对目标item的正负向支持完全无关，无法无监督筛选有效历史；二是仅优化目标item分数可能出现竞争item分数涨幅更高的情况，反而降低排序效果。
### 方法关键点
- 以冻结的SFT模型为参考，对初始排序正确的请求遍历单历史事件删除，仅保留同时提升目标item分数、且目标与边界竞争item（top10外第一个或top10最后一个）边距的删除，取最大边距作为反事实监督目标
- 训练采用交叉熵+非对称辅助损失ACS，计算ACS时目标item的分数被detach，梯度仅从竞争item回传，避免与CE优化冲突；训练输入保留完整历史，推理逻辑完全无需修改
### 关键实验
覆盖Meta工业内容数据集、Qilin、KuaiSearch-Lite三个公开/工业数据集，在Llama3.1、Gemma3、Qwen3共6个不同规模的LLM骨干上，AIMS相比Continued CE基线Recall@10相对提升4.0%-10.9%，所有场景下均优于CFT、S-DPO、LETTER等现有SOTA基线，指令与历史冲突越严重的场景收益越高。
### 核心结论
生成式推荐中优化目标item的绝对分数对排序提升作用有限，优化目标与边界竞争item的相对边距才是真实提升业务指标的核心，非对称梯度路由可有效避免多损失优化冲突
