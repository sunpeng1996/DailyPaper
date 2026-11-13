---
title: Factored One-sided Adam-Moment for Practical and Scalable SOAP
title_zh: 面向实用可扩展SOAP的因子化单侧Adam矩优化器FOAM
authors:
- Jaemyung Yu
- Byeongho Heo
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2611.16905'
url: https://arxiv.org/abs/2611.16905
pdf_url: https://arxiv.org/pdf/2611.16905
published: '2026-11-11'
collected: '2026-11-13'
category: Training
direction: 大模型预训练 · 二阶优化器改进
tags:
- Optimizer
- SOAP
- LLM Pre-training
- Second-order Optimization
- Efficient Training
one_liner: 提出仅保留输入侧预处理的因子化SOAP变体FOAM，近AdamW成本实现SOAP级优化效果
practical_value: '- 训练业务垂直域LLM（电商商品理解、推荐排序小模型、Agent规划模型）时，可直接替换AdamW为FOAM，仅增加7.4%峰值训练内存，比AdamW快7%达到相同损失，效果接近SOAP但训练成本减半

  - 大batch分布式训练场景下（如推荐多任务模型、大规模召回模型训练），FOAM的损失退化远小于AdamW，2M token batch下仍能达到AdamW
  0.5M batch的效果，可进一步压缩训练周期

  - 优化器二次开发可复用「输入侧预处理+行/列因子化二阶矩」的设计思路，在几乎不损失优化效果的前提下，大幅降低二阶优化器的内存和计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
二阶优化器SOAP收敛速度远超AdamW，但优化器状态内存是AdamW的4.5倍，且需周期性执行两次特征分解，单步计算开销极高，工业界落地难度大，亟需在保留SOAP优化效果的前提下，将运行成本降到接近AdamW的水平。
### 方法关键点
- 仅保留输入侧Kronecker因子，去掉输出侧因子，减少O(m²)内存占用，特征分解次数从2次降为1次，Transformer层Hessian输出侧近对角的特性保证该近似几乎无损
- 用行/列均值的EMA作为因子化二阶矩估计，替换SOAP的稠密旋转二阶矩，将二阶矩存储从O(mn)降到O(m+n)，基于K-FAC假设该估计可精确恢复SOAP的稠密二阶矩，实际相对误差仅15-20%，对更新影响可忽略
- 复用Purifying Shampoo的自适应特征分解跳过规则，训练后期特征漂移小时可跳过分解，进一步降低计算开销
### 关键实验
在124M~1.56B参数的GPT风格LLM预训练（FineWeb数据集）上对比AdamW、Muon、SOAP等基线：760M参数下，FOAM验证损失仅比SOAP高0.005 nat，优化器状态仅为SOAP的一半，达到AdamW最终损失的耗时和AdamW基本持平（10.53h vs 10.55h），而SOAP需要22.66h；FOAM在3倍学习率范围内的鲁棒性和AdamW相当，2M token大batch下损失退化远小于AdamW，仍能达到AdamW 0.5M batch的效果。
### 核心结论
二阶优化器落地的核心是在效果无损的前提下做符合模型结构特性的简化，而非一味追求理论上的精确拟合。
