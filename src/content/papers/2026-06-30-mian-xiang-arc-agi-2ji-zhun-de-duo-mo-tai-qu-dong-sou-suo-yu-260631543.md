---
title: Modality-Driven Search with Holistic Trace Judging for ARC-AGI-2
title_zh: 面向ARC-AGI-2基准的多模态驱动搜索与全轨迹整体判定求解器
authors:
- Johan Land
affiliations:
- Independent Researcher
arxiv_id: '2606.31543'
url: https://arxiv.org/abs/2606.31543
pdf_url: https://arxiv.org/pdf/2606.31543
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: 抽象推理 · 多模态候选生成+全轨迹判定
tags:
- Multi-Modality Reasoning
- LLM-as-Judge
- Test-Time Compute
- Candidate Diversification
- Holistic Evaluation
one_liner: 通过多模态独立候选生成+全轨迹整体判定，在ARC-AGI-2上领先SOTA单模型18.7个百分点
practical_value: '- 多模态候选生成思路可迁移到复杂推理类Agent（如电商规则推断、售后工单推理）：用文本/代码/多模态输入分别独立生成候选方案，提升假设覆盖度，避免单一模态的认知偏差

  - 全轨迹整体判定可替代传统多数投票/单点打分：解决少数正确候选被淹没的问题，可直接复用到生成式推荐的候选择优、AIGC文案/素材的质量判定场景，将所有候选的完整推理链放入单个长上下文prompt让LLM综合对比，准确率更高

  - 自适应早停策略可优化推理成本：当多候选出现高置信度共识时提前终止后续昂贵的生成步骤，适合搜索推荐的query理解、商品规则判定等对成本敏感的业务场景，平衡效果与算力开销

  - 负结论可复用：预设严格的推理模板/输出格式会系统性降低候选假设多样性，在需要发散推理的业务场景（如新类目需求挖掘、活动创意生成）应避免过度约束prompt'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型做抽象推理时普遍存在「confidently wrong」问题，即使推理链路流畅也可能得出错误结论，传统多数投票等择优方法会淹没正确的少数候选；ARC-AGI-2这类少样本视觉推理基准对模型的抽象泛化能力要求极高，单模型效果瓶颈明显。

### 方法关键点
- 多模态驱动候选生成：拆分文本、图像、代码三类独立生成通道，共29个异构生成器（8个文本、10个图像、11个代码），故意用极简无约束prompt最大化候选多样性，支持自适应早停（候选高共识时提前终止）降低成本
- 上下文保留的整体判定：将所有候选的完整推理轨迹放入单个长上下文prompt，3个并行GPT-5.2 judge直接对比所有链路，选出top2候选后加权计分（第一得2分、第二得1分）得到最终pass@2结果，允许judge融合多个候选的正确片段生成新答案

### 关键实验结果
在ARC-AGI-2半私有验证集上达到72.9%准确率，单任务成本$38.99，比SOTA单模型GPT-5.2 Pro、Gemini 3 Pro高+18.7个百分点；在公开测试集上准确率76.1%，单任务成本$19.69。对比多数投票基线，整体判定多找回7个正确的少数候选，仅占总系统成本的13%。

### 最值得记住的一句话
对于前沿未解决的复杂推理任务，正确答案往往是少数候选，多样化生成+全链路整体对比的效果远好于单一模型推理或多数投票。
