---
title: 'Free Lunch Uncertainty: Sequence-Level Rényi Entropy from Particle Decoding
  for Adaptive LLM Reasoning'
title_zh: 零边际成本序列级Rényi熵：基于粒子解码的自适应LLM推理
authors:
- Erfan Baghaei Potraghloo
- Milad Heidari Sorkhehdizaj
- Shahab Rahimirad
- Aliasghar Pourghani
- Seyedarmin Azizi
- Souvik Kundu
- Abolfazl Hashemi
- Joseph Campbell
- Vijay Gupta
affiliations:
- University of Southern California
- Purdue University
- Intel
arxiv_id: '2611.13414'
url: https://arxiv.org/abs/2611.13414
pdf_url: https://arxiv.org/pdf/2611.13414
published: '2026-11-10'
collected: '2026-11-11'
category: Reasoning
direction: LLM自适应推理 · 不确定性量化
tags:
- Uncertainty Quantification
- Rényi Entropy
- Sequential Monte Carlo
- Adaptive Inference
- LLM Reasoning
one_liner: 基于Power-SMC解码中间量零成本计算序列级Rényi熵，提升选择性预测性能并降低推理算力开销
practical_value: '- 若使用Power-SMC等粒子类解码做Agent推理/生成式推荐文案生成，可直接复用SRE1/2作为零成本置信度信号，无需额外模型调用或Reward
  Model，AUROC比常用的log-prob高0.022~0.044

  - 自适应算力分配策略可直接迁移到电商大模型应用：用小粒子预算（如N=8）先做探针，高SRE的难样本（如复杂用户query、多步导购推理）再用大算力解码，平均省34%算力同时无损精度

  - 做LLM推理置信度校准时可直接选择Rényi熵阶数1/2，该阶数在10/13的实验设置下性能最优，无需额外调参，泛化性好

  - 序列级熵计算要做累加而非取均值，论文显示除以长度的均值token熵会损失11%~48%的AUROC，该trick可直接用于所有序列类置信度计算场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM不确定性信号存在明显缺陷：token级局部信号（如mean token entropy、单样本log-prob）无法表征完整生成序列的分布不确定性；基于多采样的信号（如self-consistency、semantic entropy）算力开销高。同时Power-SMC等粒子解码方法采用固定粒子预算，存在简单问题算力浪费、难问题精度不足的痛点。

### 方法关键点
- 利用Power-SMC解码过程中已计算的粒子重要性权重，零边际成本估计序列级Rényi熵（SRE），无需额外模型调用、采样或标注
- 基于Rényi链式法则扩展得到不同阶数的步长熵族，证明阶数>1的熵与top token概率强相关，阶数1/2的熵对应每步搜索努力的对数累加，对序列分布不确定性的表征能力最优
- 设计双阶段自适应粒子分配策略：先用N=8粒子做探针计算SRE，低SRE的简单问题直接用探针结果，高SRE的难问题升级到N=64粒子解码

### 关键结果
在MATH500、GSM8K两个推理数据集，覆盖Qwen2.5、Llama3.1共4个模型的13个设置下：
1. SRE1/2在10个设置下是最优零成本置信度信号，MATH500上AUROC比log-prob高0.022~0.044，统计显著
2. 双阶段自适应策略在MATH500上匹配N=64固定预算的精度，平均减少34.2%的粒子用量

最值得记住的一句话：粒子解码过程中丢弃的归一化常数信息本身就是高质量的序列级不确定性信号，无需额外成本即可同时提升置信度估计性能和降低推理算力开销
