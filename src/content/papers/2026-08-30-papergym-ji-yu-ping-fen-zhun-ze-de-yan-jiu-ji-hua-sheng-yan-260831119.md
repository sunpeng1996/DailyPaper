---
title: 'PaperGym: Rubric-Centered Evolution for Research-Plan Generation'
title_zh: PaperGym：基于评分准则的研究计划生成演化训练框架
authors:
- Yuhan Wang
- Zhengxi Lu
- Yuchen Yan
- Kaitao Song
- Wenqi Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
- Apple
arxiv_id: '2608.31119'
url: https://arxiv.org/abs/2608.31119
pdf_url: https://arxiv.org/pdf/2608.31119
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: LLM后训练 · 评分准则驱动优化
tags:
- Rubric-as-Reward
- GRPO
- OPSD
- LLM Post-Training
- Open Generation
one_liner: 将学术论文转化为低泄露训练环境，用两阶段rubric驱动训练提升研究计划生成能力
practical_value: '- 做电商文案生成、推荐理由生成、Agent方案生成等无明确ground truth的开放式任务时，可复用「输入从需求/背景提取、评价准则从方案/效果拆分」的思路，大幅降低标注泄露，避免模型靠复述问题拿奖励

  - 模型对齐训练时可采用OPSD先做rubric条件的自蒸馏暖启动，再上GRPO做奖励优化的两阶段范式，比直接SFT或单阶段GRPO效果提升明显

  - 多维度rubric加权可复用7:3配比：70%权重给任务专属准则、30%给通用准则，平衡任务适配性和输出通用质量

  - 小模型落地做自对齐时若自身评分能力不足，可使用稍大的同系列模型做外部判分器，降低训练成本同时保证评分可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI科学发现自动化依赖高质量研究计划生成，但该任务无明确可验证的ground truth，强化学习缺乏配套的任务-判分训练环境；现有rubric驱动方案存在严重准则泄露（问题与评分准则同源，模型仅靠复述问题即可拿高奖励），且单标量奖励浪费了rubric的细粒度监督信号，SFT又会压缩输出多样性。

### 方法关键点
- 数据构造：将论文拆分为研究目标、背景、方法、实验设计4个独立部分，任务问题仅从目标+背景合成，评分准则仅从方法+实验提取，从源头避免准则泄露
- 两阶段训练：第一阶段做rubric条件的OPSD自蒸馏，将rubric作为特权信息引导模型学习宽泛的合理输出分布；第二阶段做GRPO，将rubric拆解为二元判分项作为奖励，精细化优化策略
- Rubric设计：融合实例专属的方法创新、实验设计准则，以及通用的完整性、合理性准则，加权时专属准则占比0.7，平衡任务适配性和通用质量

### 关键结果
在Qwen3-1.7B/4B/8B三个模型规模上，两阶段训练比SFT在5个基准上平均提升5.6/5.0/4.8分；PaperGym-20k训练的模型三向对比胜率达58.1%，远超RubricHub Science的28.2%；训练后的8B模型在ResearchQA得分73.48，超过参数规模大得多的Kimi K2.6。

### 核心结论
无明确ground truth的开放式生成任务中，低泄露结构化rubric+OPSD暖启动+GRPO优化的范式，效果远优于常规SFT和单阶段RL训练。
