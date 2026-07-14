---
title: 'Requential Coding: Pushing the Limits of Model Compression with Self-Generated
  Training Data'
title_zh: Requential编码：基于自生成训练数据突破模型压缩极限
authors:
- Shikai Qiu
- Marc Finzi
- Yujia Zheng
- Kun Zhang
- Andrew Gordon Wilson
affiliations:
- New York University
- Carnegie Mellon University
arxiv_id: '2607.11883'
url: https://arxiv.org/abs/2607.11883
pdf_url: https://arxiv.org/pdf/2607.11883
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: 大模型压缩 · 泛化性理论保证
tags:
- Model Compression
- LLM
- Generalization Bound
- Knowledge Distillation
- PAC-Bayes
one_liner: 提出不依赖参数量与数据熵的Requential编码，实现量级级压缩提升并给出大模型SOTA泛化保证
practical_value: '- 端侧推荐/Agent小模型离线蒸馏场景可借鉴该框架思路，用student自生成样本+teacher选样降低蒸馏数据传输带宽成本，提升离线蒸馏效率

  - 垂直领域LLM训练的数据筛选环节，可通过该编码的压缩长度量化数据集可学习结构占比，优先选择压缩效率高的商品描述/用户行为文本类数据集

  - 大模型泛化性评估可复用该方法的PAC-Bayes bound思路，替代传统量化相关的泛化估计，更准确判断推荐/广告大模型的过拟合风险

  - 小参数模型轻量化部署时，可搭配Requential编码+蒸馏方案，实现比4-bit PTQ更高的压缩率且性能损失更小，适合端侧推荐模型下沉'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有模型压缩方法存在核心缺陷：参数类方法（如量化）码长随参数量线性增长，不感知参数实际存储的有效信息量；prequential编码虽通过训练轨迹压缩规避该问题，但需要编码完整数据序列，码长受数据熵影响大，高熵数据下压缩效率极低，且两类方法都无法有效解释大模型的泛化性规律。

### 方法关键点
- 核心采用Requential编码框架：待压缩的student模型自生成候选训练样本，更强的teacher模型仅编码选中样本的索引，码长仅对应teacher与student分布的KL散度，与参数量、数据熵完全无关
- 基于相对熵编码（REC）传输选中样本索引，仅当teacher与student预测分歧时消耗比特，双方通过共享PRNG种子同步候选样本序列，无需传输原始训练数据
- 优化teacher选择策略：加入teacher EMA平滑、等损失投影两种trick，进一步降低teacher-student KL，缩短最终码长

### 关键结果
在OpenWebText、CIFAR-5M、FineWeb数据集上对比基准方法：
1. 100M参数模型压缩码长比prequential编码低1-2个数量级，同性能下码长低于4-bit PTQ的理论下限
2. 针对10亿参数级计算最优LLM，得到SOTA PAC-Bayes泛化界，优于零损失4-bit PTQ的泛化界，且泛化间隙随模型规模扩大呈幂律下降
3. 可准确分离数据集的可学习结构与随机噪声，同等数据量下文本的可学习信息是图像的数倍

最值得记住的结论：计算最优训练的大模型参数量增长时，压缩码长呈亚线性增长，泛化性会随规模提升持续变好。
