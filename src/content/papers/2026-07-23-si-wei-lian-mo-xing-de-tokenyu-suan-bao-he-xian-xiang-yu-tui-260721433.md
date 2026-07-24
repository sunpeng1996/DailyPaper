---
title: Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence
  in Chain-of-Thought Models
title_zh: 思维链模型的Token预算饱和现象与推理不收敛机制化早检测
authors:
- Renuka Oladri
- Niveda Jawahar
- Abdirisak Mohamed
affiliations:
- University of Maryland
- SAP Labs, LLC
arxiv_id: '2607.21433'
url: https://arxiv.org/abs/2607.21433
pdf_url: https://arxiv.org/pdf/2607.21433
published: '2026-07-23'
collected: '2026-07-24'
category: Reasoning
direction: LLM推理效率优化 · 收敛早检测
tags:
- Chain-of-Thought
- Inference Optimization
- Probing
- Early Exit
- Reasoning Model
one_liner: 揭示CoT推理Token预算饱和规律，提出基于模型内部激活的推理不收敛早检测方法
practical_value: '- 部署自定义thinking token预算截断策略：对于电商导购/商品属性抽取等常规推理任务，可参考256token阈值，截断多余思考token，在损失<5%准确率的前提下降低推理成本30%+

  - 推理任务的收敛早筛可复用内部激活探针方案：对于Agent长程规划/复杂商品选品推理等高成本场景，可在推理前100token时抽取上层中间层激活做二分类预测，提前终止不收敛任务，节省40%左右无效算力

  - 推理任务效果预判优先选内部信号而非表面特征：做推理质量预评估时，优先用中上层激活特征，比logit熵、重复率等表面特征的预测效果高3%-7%，早阶段优势更明显'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
CoT推理模型的推理成本随思考token长度指数上升，但行业普遍默认「思考越长效果越好」，缺乏单样本维度的token投入产出比量化研究，大量无效推理循环浪费算力，亟需低成本的推理不收敛早检测方法降低部署成本。

### 方法关键点
- 预算约束实验：适配预算强制机制实现自定义LogitsProcessor，在指定思考token数达到阈值时强制输出`</think>`终止思考，扫描不同预算下的准确率变化
- 收敛早检测实验：给DeepSeek-R1-Distill-Qwen-7B的28层加前向钩子，在推理50-300token的9个checkpoint抽取隐藏层激活，训练线性探针预测最终收敛性，对比仅用logit熵、重复率等表面特征的行为基线

### 关键实验结果
在GSM8K、MATH-500、AIME三个数学推理基准上测试：① GSM8K和MATH-500仅需256思考token就能达到无约束条件下95%的准确率，额外token无效果增益；② AIME任务呈现明显双模态分布：56.5%的样本能自然收敛，准确率96.5%，43.5%的样本即使给10000token也不收敛，准确率仅11.5%，浪费40%左右算力；③ 基于激活的探针在8/9的checkpoint上优于行为基线，早阶段50token时AUC优势达0.074，信号峰值出现在第20层（共28层），AUC 0.608；④ 2025年全新AIME题验证收敛-准确率关联不受记忆效应影响，收敛样本准确率100%，不收敛样本准确率0。

### 核心结论
推理模型的准确率远早于思考终止时就已经确定，无效的长思考没有任何价值，基于内部激活的早检测能在几乎不损失效果的前提下大幅降低推理成本。
