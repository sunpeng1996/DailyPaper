---
title: Negative-Only Policy Optimization for One-Sided Verifiable Rewards
title_zh: 面向单侧可验证奖励的纯负向策略优化算法NOPO
authors:
- Jiacheng Xu
- Shuo He
- Fuxiang Zhang
- Chaojie Wang
- Bo An
affiliations:
- Nanyang Technological University
- Skywork AI
arxiv_id: '2611.17287'
url: https://arxiv.org/abs/2611.17287
pdf_url: https://arxiv.org/pdf/2611.17287
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 大语言模型RL训练 · 单侧可验证奖励
tags:
- Policy Optimization
- RLVR
- One-sided Verification
- NPO
- LLM Training
one_liner: 仅利用高置信负样本做RL优化，无需信任验证通过样本，跨任务提升pass@k表现
practical_value: '- 电商推荐/广告的低质/违规内容过滤场景，可复用NOPO的纯负向优化逻辑：仅用高置信违规样本做惩罚，不将过审样本直接当作正例，避免奖励过审但用户不感兴趣的「捷径」内容，降低奖励黑客风险

  - Agent工具调用/结构化输出类业务，当只有失败验证逻辑（比如API调用报错、格式错误）没有完备正确性校验时，可直接复用NOPO训练框架：样本级用reference-relative
  NPO损失，组级用未被否决样本占比做更新权重，无需额外标注正样本

  - 生成式推荐的item/文案生成场景，可借鉴单侧验证的核心假设：违规/低质样本判定准确率远高于优质样本判定准确率，优先用负样本优化规避明显错误，再结合轻量正样本信号做精调，大幅降低标注成本

  - 大模型RL落地时如果缺少高质量标注正样本，可优先用NOPO范式替代GRPO等依赖正负样本的RL方法，不仅能提升离线指标，还能获得更好的跨场景泛化性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
带可验证奖励的强化学习（RLVR）是当前提升LLM推理能力的主流范式，但现实场景中几乎不存在能100%判断输出正确性的完备验证器：绝大多数验证器只能检测明确的错误（比如代码单元测试不通过、结构化输出格式非法、推理步骤存在显式逻辑错误），无法证明输出完全正确。这种单侧验证（OSV）的不对称性导致传统RLVR方法（如GRPO）将验证通过样本当作正例强化时，会大量奖励仅通过部分校验的「捷径」解，不仅无法真正提升模型能力，还会导致过拟合、泛化性差的问题。

### 方法关键点
- 核心优化原则：仅将验证不通过的样本作为高置信度负例使用，验证通过样本仅代表未被否决，完全不作为可信正例参与优化
- 样本级损失：采用reference-relative NPO损失对负样本做惩罚，当负样本被当前策略压制到低于参考模型概率时，梯度会自动衰减，避免过度偏离基础模型能力
- 组级门控机制：每轮对同一个prompt采样G个输出，若组内没有未被否决的样本则直接跳过该轮更新；否则用组内未被否决样本占比作为权重缩放负向更新幅度，避免无方向的「远离」更新导致模型漂移

### 关键实验
基于Qwen3-4B/8B基础模型，在代码、逻辑、数学三类任务上对比GRPO、EM-RL、w-Reinforce等基线：
- 平均pass@16相对GRPO提升8.0%（4B）、8.0%（8B），9/10的任务子项排名第一
- 推理时采样数k从1扩到512，优势持续扩大，CodeContests任务pass@512达到66.95%，比GRPO高18.41个百分点，证明模型能力边界被真正拓展
- 跨基准迁移时平均pass@16相对GRPO提升26.6%，无明显过拟合问题

### 核心结论
当验证器只能可靠识别错误、无法可靠识别正确解时，仅用负样本做保守优化的效果远好于强行用不可靠正样本做强化。
