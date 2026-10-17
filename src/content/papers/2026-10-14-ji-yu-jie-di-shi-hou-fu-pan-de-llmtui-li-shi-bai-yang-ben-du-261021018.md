---
title: 'Failure Is the Mother of Success: Recovering Supervision with Grounding Hindsight'
title_zh: 基于接地事后复盘的LLM推理失败样本监督恢复方法
authors:
- Sheldon Yu
- Tong Yu
- Nikki Lijing Kuang
- Zhendong Chu
- Zhenwei Tang
- Sungchul Kim
- Lina Yao
- Julian McAuley
- Junda Wu
affiliations:
- University of California San Diego
- Adobe Research
- University of Virginia
- University of Toronto
- University of New South Wales
arxiv_id: '2610.21018'
url: https://arxiv.org/abs/2610.21018
pdf_url: https://arxiv.org/pdf/2610.21018
published: '2026-10-14'
collected: '2026-10-17'
category: Reasoning
direction: LLM推理训练 · 失败样本监督恢复
tags:
- GRPO
- LLM reasoning
- hindsight distillation
- reinforcement learning
- failure supervision
one_liner: 提出RSHD方法从GRPO全失败样本组恢复监督信号，提升LLM推理能力无额外推理开销
practical_value: '- 做Agent推理训练时可复用RSHD思路，对GRPO全失败样本组生成修正提示、重放验证后蒸馏，无需额外推理成本即可提升难例处理能力

  - 推荐系统用LLM生成候选文案/Semantic ID时，可借鉴失败样本重蒸馏机制，对低质量生成样本自动生成修正指导，迭代优化生成效果

  - 可复用「失败诊断→重放验证→知识蒸馏」pipeline到搜索Query改写、商品文案生成等场景，自动从bad case中挖掘监督信号'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
GRPO是当前LLM推理训练的主流强化学习方法，但当同一问题的采样轨迹全部失败时，组内相对优势为0，无梯度信号无法学习，这类全失败组在难例上占比极高（MATH最难级别占比达50%），现有方法要么泄露测试时不可得的参考答案，要么未验证自生成指导的有效性，无法有效利用失败样本的价值。
### 方法关键点
- 提出Replay-Selected Hindsight Distillation（RSHD），流程分三步：1）对每个失败轨迹，让模型在不看参考答案的情况下生成不超过80词的修正note，诊断错误并给出改进方向；2）对note做泄露检测后，用带note的prompt重新采样k=2次，仅当重放成功率高于原组成功率时保留该note；3）将保留note对应的重放样本，通过特权上下文自蒸馏的方式迁移到无note的plain prompt策略中，蒸馏权重为note对每个token的正向提升幅度，clip到0-2之间
- 训练时仅更新原策略，推理时完全不需要额外输入，无任何推理开销，可无缝兼容现有GRPO训练流程
### 关键结果
在Qwen3-1.7B/4B/8B三个尺度模型上验证，训练域为数学推理（MATH数据集）和科学问题（MMLU-Pro数据集），对比Base、GRPO、OPSD、SEED等基线：
- 4B模型在MATH-500上准确率达84.5%，比GRPO高7.6个点
- 科学域训练后在域外GPQA-Diamond匹配准确率达27%，比GRPO高17.4个点
- 最难的MATH Level 5问题上增益达10.8个点，基础模型完全解不出的问题上增益达8.5个点
### 核心结论
失败样本不是无效数据，对失败原因的可验证复盘是比盲目增加采样更高效的能力提升路径。
