---
title: 'Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game
  Mechanics'
title_zh: Avalon-ToM-Bench：基于阿瓦隆游戏的细粒度心理理论评测基准
authors:
- Yen-Shan Chen
- Yu Chian Duan
- Chih-En Kuo
- Jian-Bin Wu
- Yun-Nung Chen
affiliations:
- National Taiwan University
- CyCraft AI Lab, Taiwan
arxiv_id: '2608.09638'
url: https://arxiv.org/abs/2608.09638
pdf_url: https://arxiv.org/pdf/2608.09638
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: 大模型心理理论(ToM)能力评测
tags:
- Theory of Mind
- Benchmark
- LLM Evaluation
- Asymmetric Information
- Activation Steering
one_liner: 基于阿瓦隆非对称游戏机制构建2×2维度ToM评测基准，揭示LLM的ToM缺陷多为表达而非表示问题
practical_value: '- 做多Agent交互场景（如电商导购、竞价广告多主体博弈）的ToM能力评测时，可复用2×2拆解框架：认知/动机 × 推理/行动，精准定位能力瓶颈，避免仅看端到端效果的模糊性

  - 优化Agent推理能力时，优先做推理专项训练而非仅堆Chain-of-Thought（CoT）类推理时策略，实验显示专项训练提升是CoT的10倍（+11.0pp
  vs +1.1pp）

  - ToM类推理任务的性能优化可参考线性探针+Activation Steering方案，将模型隐层中已学到但未输出的正确推理结果显式提取出来，无需额外训练数据

  - 做信息不对称场景的推理任务（如推荐用户意图推断、广告对手策略预判）时，可复用视角约束设计，强制模型基于指定角色的已知信息推理，避免全知视角偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有ToM评测存在两类缺陷：静态场景过于简化，缺失真实社交推理所需的信息不对称、欺骗、多主体动态特性；端到端游戏类评测仅看胜负，无法区分缺陷来自规则掌握不足、规划能力弱还是真实ToM能力缺失，也无法定位缺陷是模型没学会（表示问题）还是学会了没说出来（表达问题）。

### 方法关键点
- 基于桌游《阿瓦隆》的非对称信息机制，将ToM拆解为2×2可分离维度：认知（他人的知识边界）/动机（他人的目标意图） × 推理（被动读取心理状态）/行动（主动生成/解读策略动作），对应4类具体任务：视角选取、策略发信、意图归因、隐性协同。
- 所有408个评测样例来自真实游戏记录，均为视角约束的二分类判断，标签基于游戏规则和指定角色的已知信息客观生成，同时附带34题规则测试集，明确区分规则掌握度和ToM能力。
- 搭配线性探针、Activation Steering、真值注入三类分析方法，可定位模型ToM缺陷的根源。

### 关键结果
对28款不同规模、闭源/开源、推理训练/普通的LLM评测得到核心结论：
1. 模型平均规则掌握准确率达84.77%，但ToM任务平均准确率仅71.98%，规则熟练不代表ToM能力达标。
2. 线性探针从模型隐层解码ToM正确答案的准确率达77~82%，远高于模型自身CoT输出的62~70%，说明多数ToM错误是表达问题，不是表示问题。
3. 推理时加CoT仅平均提升1.1pp，且效果不稳定，27%的样本结果翻转；而专项推理训练平均提升11.0pp，效果稳定。

**最值得记住的一句话：LLM的心理理论能力瓶颈大概率不是没学到相关知识，而是没学会把内部表征的正确推理结果表达出来，靠推理时加CoT远不如提前做专项推理训练见效**
