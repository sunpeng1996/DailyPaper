---
title: Equivalence testing and run-count design for stochastic machine-learning experiments
title_zh: 随机机器学习实验的等价性测试与运行次数设计
authors:
- Dmytro Knopov
- Nadiya Shvai
affiliations:
- National University of Kyiv-Mohyla Academy
- Cyclope.ai
arxiv_id: '2610.23700'
url: https://arxiv.org/abs/2610.23700
pdf_url: https://arxiv.org/pdf/2610.23700
published: '2026-10-16'
collected: '2026-10-20'
category: Training
direction: 机器学习训练实验 · 等价性检验设计
tags:
- experimental design
- equivalence testing
- statistical power
- stochastic training
- hypothesis testing
one_liner: 提出随机ML实验等价性验证协议与闭式公式，可计算给定目标所需的实验运行次数
practical_value: '- 算法迭代对比效果是否等价时，不要仅依赖2-3次实验结果，可采用文中TOST+两层方差模型验证是否在预设等价margin内，避免误判

  - 新算法上线前的离线/在线A/B测试，可复用文中闭式公式计算所需实验次数，保障80%+统计效力下的结果可信度

  - 小样本pilot实验估算方差时，用方差上置信界替代点估计，可大幅降低实验次数不足导致的结论偏差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前机器学习训练方法等价性判断通常仅基于2-3次跑批的非显著差异，结论可信度不足，缺乏标准化的等价性验证流程与实验次数设计方法。
### 方法关键点
1. 构建两层（种子×item）方差模型，分离运行间离散度与item级噪声，采用双单侧检验（TOST）验证预设margin内的等价性，搭配两层bootstrap适配复合统计量；
2. 给出闭式公式，可基于等价margin、目标统计效力直接计算单方法所需运行次数，搭配shifted-t优化校准两层随机过程。
### 关键结果数字
- 仿真验证公式在单方法≥5次运行的设计区间内准确率达标；
- 0.01 AUROC等价margin、80%统计效力下，即使两方法完全等价也需要至少12次运行才能验证，仅跑2次的验证成功率仅3%；
- 两阶段pilot+正式实验设计中，采用pilot方差的上置信界可大幅降低实验规模不足问题。
