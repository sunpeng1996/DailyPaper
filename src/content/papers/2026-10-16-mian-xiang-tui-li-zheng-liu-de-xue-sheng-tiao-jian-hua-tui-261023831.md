---
title: 'Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation'
title_zh: 面向推理蒸馏的学生条件化推理链构建框架ReDiST
authors:
- Shaoang Li
- Yanhang Shi
- Yufei Li
- Mingfu Liang
- Frank Shyu
- Sandeep Pandey
- Luke Simon
- Xi Liu
- Jian Li
affiliations:
- Stony Brook University
- Meta AI
arxiv_id: '2610.23831'
url: https://arxiv.org/abs/2610.23831
pdf_url: https://arxiv.org/pdf/2610.23831
published: '2026-10-16'
collected: '2026-10-19'
category: Training
direction: 推理蒸馏 · 小模型跨域泛化
tags:
- Reasoning Distillation
- Chain-of-Thought
- Knowledge Distillation
- LLM Fine-tuning
- Transfer Learning
one_liner: 提出学生条件化推理链构建与蒸馏框架ReDiST，同时提升源任务与跨域推理性能
practical_value: '- 做业务侧Agent/多跳问答小模型蒸馏时，可复用学生条件化监督构建思路：不直接用大模型生成的CoT当监督，优先基于学生自身推理草稿修订，再用冻结的学生模型做候选筛选，适配学生推理风格，大幅提升跨域泛化能力

  - 兼顾域内效果与跨域迁移的训练可借鉴损失设计：采用「(1-α)全序列损失 + α答案位置增强损失」的混合目标，α取0.1~0.2即可在不明显损失域内性能的前提下，提升跨场景适配性，可直接复用到电商搜索多query理解、商品咨询问答等场景

  - 缺乏人工标注推理链的场景可复用ReDiST的离线数据构造pipeline：仅需答案标签即可自动生成高质量推理监督数据，降低标注成本，适合业务侧快速迭代小版本推理模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有推理蒸馏方案要么仅用答案监督，要么直接采用大模型生成的推理链作为训练目标，存在明显缺陷：仅答案监督会严重损伤模型跨域泛化能力，而通用推理链往往和目标学生模型的推理能力、表达风格不匹配，即使答案正确也无法起到有效监督作用，且源任务性能提升和跨域迁移效果往往不可兼得，亟需适配学生本身的推理链构建方法。
### 方法关键点
- 双分支处理学生草稿：对答案正确的学生推理草稿，仅基于给定证据做修订优化；对答案错误的草稿，额外输入正确答案辅助修复，生成多组候选推理链
- 学生适配的候选筛选：用冻结的同源学生模型作为Reader，仅保留能让Reader恢复出正确答案的候选，再选择正确答案预测概率最高的候选作为监督目标
- 可控蒸馏策略：修复得到的样本加权m倍放入训练集，损失采用混合目标：`L=(1-α)L_full + αL_ans`，α控制答案位置的监督权重，默认取0.15
### 关键实验
以MuSiQue多跳QA为源训练数据集，2Wiki、HotpotQA、QuALITY为跨域测试集，对比Answer-only、原始推理链、STaR、MBT-R等7类基线。在Qwen3-8B上，源任务EM达58.4%，比Answer-only高2.2个百分点；2Wiki跨域EM达68.6%，比Answer-only高20.7个百分点，比最强基线MBT-R高5.3个百分点，效果在Qwen3、Gemma4两个模型族的4个不同规模模型上均稳定成立。
**最值得记住的结论：** 源任务性能提升不代表跨域泛化能力提升，推理蒸馏的监督数据需要同时兼顾内容正确性和目标学生的可学习性。
