---
title: 'WeightLoop: Weight-Space Programming with Experimental Feedback'
title_zh: WeightLoop：融合实验反馈的权重空间编程框架
authors:
- Mengran Li
- Bo Li
- Weijing Zhao
- Chengyang Zhang
- Boyu Zhang
- Jinfeng Xu
- Zelin Zang
- Victor C. M. Leung
- Stan Z. Li
affiliations:
- Hong Kong Institute of Science and Innovation
- University of Macau
- Sichuan University
- Sun Yat-sen University
- The University of British Columbia
arxiv_id: '2611.07319'
url: https://arxiv.org/abs/2611.07319
pdf_url: https://arxiv.org/pdf/2611.07319
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 自迭代权重编辑优化框架
tags:
- Weight-Space-Programming
- Model-Editing
- Recursive-Self-Improvement
- Experimental-Feedback
- Parameter-Optimization
one_liner: 通过LLM一次性生成固定权重编辑程序，基于实验反馈无重训迭代优化预测器
practical_value: '- 推荐/广告系统可复用该架构：仅用LLM一次性生成符合业务目标的固定权重编辑规则，后续仅用AB实验/用户反馈迭代模型，无需反复调用LLM或全量重训，大幅降低迭代成本

  - 排序任务可借鉴其输出层定向编辑技巧：仅调整输出层极少量权重即可优化排序效果，保留原有模型的通用特征表示能力，尤其适合新业务冷启动快速适配

  - 可将线上业务反馈（如点击、转化偏差）直接对接编辑流程，自动生成候选参数修改方案，经小流量验证有效后上线，缩短实验结论的落地周期'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有实验反馈仅能指导单次决策，无法直接转化为部署模型的持久化更新，传统模型重训/持续微调成本高、周期长。权重空间编程（WSP）已证明LLM可直接理解、修改模型参数，结合递归自提升（RSI）的反馈循环思路，可实现低代价的模型持续迭代。
### 方法关键点
- 一次性调用GPT-6 Astra基于任务目标、模型结构生成固定可执行的权重编辑程序，后续迭代无需额外LLM调用，也不需要梯度回传重训
- 编辑程序仅修改预先指定的可编辑参数（如MLP输出层权重、线性模型系数、XGBoost叶子节点值），其余参数保持不变，完全兼容原有模型推理接口
- 基于新到的实验反馈计算预测偏差，生成候选参数修改方案，经三折交叉验证确认有效后写入模型checkpoint，每次更新都基于初始参数，避免误差累积
### 关键结果
实验基于公开细胞功能筛选数据集，对比基线包括原始模型、随机参数编辑、全量100样本训练模型：单轮排序任务中，编辑后模型在8个终点-预算设置中7个优于原始模型，全部优于随机编辑；序列发现任务中3个任务的平均D100分别比原始模型提升0.0334、0.0207、0.0147；MLP模型仅修改0.00044%的参数即可实现排序效果提升，更新后可通过原有接口直接重载。

仅通过LLM一次性生成编辑规则、用业务反馈定向修改极少量参数，就能实现模型的持续迭代，成本远低于全量重训或重复调用LLM
