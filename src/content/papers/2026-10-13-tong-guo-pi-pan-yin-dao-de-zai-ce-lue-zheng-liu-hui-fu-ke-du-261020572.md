---
title: Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
title_zh: 通过批判引导的在策略蒸馏恢复可靠监督信号
authors:
- Kaixiang Zhao
- Tianrun Yu
- Shangzhe Li
- Yuxiao Yang
- Amanda Hughes
- Weitong Zhang
- Taylor W. Killian
affiliations:
- Brigham Young University
- University of North Carolina at Chapel Hill
arxiv_id: '2610.20572'
url: https://arxiv.org/abs/2610.20572
pdf_url: https://arxiv.org/pdf/2610.20572
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: LLM 蒸馏训练 · 在策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Reasoning
- Critique-guided Learning
one_liner: 提出CriticOPD方法，利用教师错误识别能力修复在策略蒸馏监督可靠性，提升小模型推理性能
practical_value: '- 做小模型蒸馏（比如大模型推荐/Agent决策能力蒸馏到小模型）时，可借鉴CriticOPD思路：学生生成错误序列后不用直接截断或教师接管，先用教师输出错误修正反馈引导学生重写后再蒸馏，既降低分布偏移又提升监督可靠性

  - 电商生成式内容优化（商品文案、客服话术小模型蒸馏）可复用「错误识别+引导重写+特权信息训练」范式：大模型识别坏case错误点引导小模型重写，大模型带反馈打分，小模型不带反馈学习，推理无需额外模块即可提升生成质量

  - 对有明确校验标准的任务（如营销规则推理、优惠券 eligibility 判断），可把规则校验当作参考答案直接套用CriticOPD流程，相比普通蒸馏错误率降低约4%，训练总算力仅为普通OPD的0.42倍，性价比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在策略蒸馏（OPD）解决了离线蒸馏的学生生成前缀分布与训练分布不匹配的问题，但存在严重缺陷：当学生生成错误前缀后，教师模型即便能识别错误，也会顺着错误继续生成，导致监督信号可靠性骤降，53%的错误序列token对应教师恢复准确率<0.2，约1/3的训练token监督信号不可靠；现有截断、教师接管等方法又会重新引入分布偏移，效果受限。

### 方法关键点
- 利用教师模型的「错误识别能力与续写正确性的不对称性」：即便教师从错误前缀续写准确率低，错误识别精度仍稳定在73%~81%，以此为核心设计CriticOPD
- 流程：学生生成rollout后，正确序列用标准OPD训练；错误序列由教师带参考答案输出错误位置与修正指导，学生保留前缀到最后一个错误点，带critique作为特权信息重写后续部分
- 训练损失：教师带critique对重写序列打分，学生不带critique学习重写部分的token损失，既保证监督信号可靠性，又不需要推理时额外输入

### 关键实验
用Qwen3-4B-Instruct作为教师，蒸馏Qwen3-0.6B、1.7B两个小模型，在6个数学推理基准上测试，对比SFT、KD、OPD、FastOPD、RelayOPD等10余种基线：CriticOPD比标准OPD在1.7B模型上平均提升4.57个百分点，0.6B模型上提升4.06个百分点，竞赛级数学题上最高提升7.36个百分点，训练总算力仅为标准OPD的0.42倍，非数学任务性能基本无损。

### 最值得记住的一句话
利用大模型错误识别能力远强于错误前缀下续写能力的不对称性，通过批判引导的重写可以在几乎不增加分布偏移的前提下大幅提升蒸馏监督信号的可靠性
