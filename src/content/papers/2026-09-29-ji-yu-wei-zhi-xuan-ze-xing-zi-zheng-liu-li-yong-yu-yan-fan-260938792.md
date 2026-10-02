---
title: Training LLM Judges from Language Feedback via Position-Selective Self-Distillation
title_zh: 基于位置选择性自蒸馏利用语言反馈训练LLM评判器
authors:
- Ilgee Hong
- Changlong Yu
- Zhenghao Xu
- Xin Liu
- Yuwei Zhang
- Qin Lu
- Bing Yin
- Tuo Zhao
affiliations:
- Georgia Institute of Technology
- Amazon
- UC San Diego
arxiv_id: '2609.38792'
url: https://arxiv.org/abs/2609.38792
pdf_url: https://arxiv.org/pdf/2609.38792
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: LLM对齐·自蒸馏训练优化
tags:
- LLM-Judge
- Self-Distillation
- Reward-Model
- Entropy-Shift
- RLHF
one_liner: 提出基于熵移的位置选择性自蒸馏方法，提升LLM评判器主观任务泛化性能，较RL高2-9个点
practical_value: '- 训练电商场景的LLM评判器（如商品文案打分、推荐理由质量评估、Agent服务回复校验）时，可在标注偏好时新增1-2句决策理由，用自蒸馏替代传统结果监督RL，主观任务准确率可提升2~9个百分点，客观任务无损失

  - 自蒸馏训练时直接复用熵移位置掩码trick：计算每个token位置的学生-教师熵移，屏蔽前70%高熵移位置（即易导致过拟合的锐化信号），无需自定义token选择策略即可提升OOD泛化能力，4B/30B规模下ρ=0.7均为最优参数

  - 偏好标注无需生成复杂的长评分rubric，仅收集1~2句简洁的决策rationale即可，效果优于7倍长度的生成式rubric，可大幅降低标注成本

  - 若需将训练好的评判器用作RLHF的奖励模型，该方法选出的高主观质量内容相对RL训练的评判器胜率提升7.6个百分点，可直接用于生成式推荐、Agent回复的质量对齐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有结果监督RL训练LLM评判器的方案，仅用最终判决的标量奖励为所有token赋值，忽略偏好标注自带的自然语言决策理由，无法为准则选择类token提供独立监督，在主观任务（如文案吸引力、回复有用性评估）上泛化性能差；普通全位置自蒸馏易引导模型死记特定准则表达，同样存在OOD泛化短板。
### 方法关键点
- 定义单位置熵移ΔHt = 学生模型（无反馈输入）的token分布熵 - 教师模型（条件接入偏好理由）的token分布熵，正ΔH为上下文锐化（教师集中到特定准则表达，易过拟合），负ΔH为上下文扩散（教师分散到多组语义等价准则，利于泛化）
- 提出位置掩码策略，单生成序列内屏蔽熵移最高的ρ比例位置，仅保留低熵移位置计算自蒸馏损失，优先保留扩散类监督信号
- 偏好反馈直接复用标注自带的1-2句决策理由即可，无需额外生成复杂评分规则
### 关键结果
在HELPSTEER3-PREFERENCE数据集训练，OOD测试集为RM-BENCH、REWARDBENCH V2：
- 自蒸馏方案较Dr.GRPO基线在主观任务上准确率高2~9个百分点，客观任务性能相当
- 加熵移掩码后较普通自蒸馏总体准确率提升1.34（4B）、2.33（30B）个百分点，30B规模效果超过DeepSeek-R1、Llama-3.3-Nemotron-Super-49B-GenRM等基线，接近Claude-Sonnet-4
- 作为RLHF奖励模型使用时，选出的创作类回复胜率较RL训练的评判器高7.6个百分点；最优掩码比例ρ=0.7在4B/30B规模下均生效

用自然语言反馈做自蒸馏训练LLM评判器时，优先保留低熵移的扩散类位置监督，既能充分利用标注理由信号，又能避免过拟合特定表达，大幅提升主观任务的OOD泛化性能
