---
title: 'A Refresh Interval Does Not Fully Specify a Refresh Schedule: Learning-Rate-Dependent
  Placement in Kronecker-Preconditioned Language Model Training'
title_zh: Kronecker预条件大模型训练：刷新调度需结合学习率调整放置位置
authors:
- Xinyu Wang
- Zhiwei Zhai
- Yu Gu
- Zijun Yu
- Sicheng Lyu
- Jingrui Tian
- Lei Ding
- Ziyang Song
- Xiao-Wen Chang
affiliations:
- McGill University
- The Chinese University of Hong Kong
- University of Manitoba
- Ohio University
arxiv_id: '2610.18695'
url: https://arxiv.org/abs/2610.18695
pdf_url: https://arxiv.org/pdf/2610.18695
published: '2026-10-13'
collected: '2026-10-14'
category: Training
direction: 大模型训练优化 · 预条件刷新调度
tags:
- Optimizer
- LLM Training
- Kronecker Preconditioning
- Scheduling
- Hyperparameter Tuning
one_liner: 发现Kronecker预条件优化器的刷新位置影响训练效果，最优位置随学习率、模型规模反转
practical_value: '- 电商/导购Agent的LLM微调若使用二阶预条件优化器，可根据学习率阶段调整刷新位置：低学习率阶段晚刷新，高学习率阶段早刷新，无需额外计算成本即可降低NLL

  - 固定刷新预算时优先选择均匀间隔的刷新调度，在多数语料下表现优于非均匀调度，可节省调度调参成本

  - 做优化器/训练策略对比时，不能仅测试单一学习率点，需覆盖调优区间上下至少1-2个学习率，避免得到完全反转的错误结论

  - 小模型上验证的刷新策略迁移到更大规模的垂域LLM（如电商商品理解大模型）时，需重新校验最优调度，模型越大偏好反转的学习率阈值越低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Kronecker类预条件优化器（如Shampoo、Mousse）是LLM训练的主流高效二阶优化器，但其曲率特征分解计算成本高，现有调度策略仅通过刷新频率控制成本，完全忽略了相同刷新次数下，刷新位置的差异会带来效果差异，单学习率下的策略对比极易得到误导性结论。
### 方法关键点
- 控制变量实验设计：固定总刷新次数、首尾刷新位置，仅调整中间刷新的放置步点，保证不同调度的计算成本完全一致
- 测试对象为64M~929M参数的GPT风格模型，使用Mousse优化器在FineWeb等6个公开单域语料上训练
- 定义偏好边界λ×作为两种刷新位置效果反转的学习率阈值，对比不同学习率、模型规模、训练长度下的效果差异
### 关键结果
- 350M模型上，相同4次刷新预算下，低学习率时晚放中间刷新更优，高学习率时早放更优，最优与最差调度的NLL差最高达0.095
- 相同预算下均匀间隔的刷新调度在多数语料上优于非均匀调度，NLL最多提升0.051
- 偏好边界随模型规模增大而下降，929M模型的反转学习率比64M低约40%
- 常用的谱宽度 stale 指标无法预测偏好反转，因曲率变化大多发生在训练早期、调度分歧之前

最值得记住的结论：二阶优化器的刷新调度不能仅依赖固定间隔，必须结合学习率、模型规模调整，单学习率下的优化策略对比结论极可能不可靠
