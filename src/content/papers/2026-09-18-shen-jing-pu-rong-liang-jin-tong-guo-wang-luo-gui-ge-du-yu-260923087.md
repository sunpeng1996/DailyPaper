---
title: 'Neural Spectral Capacity: Measuring and Designing Architectures from Network
  Specification Alone'
title_zh: 神经谱容量：仅通过网络规格度量与设计模型架构
authors:
- Chenyu Zhu
- Ruoyu Zhao
- Zhichao Lu
affiliations:
- Department of Computer Science, City University of Hong Kong
arxiv_id: '2609.23087'
url: https://arxiv.org/abs/2609.23087
pdf_url: https://arxiv.org/pdf/2609.23087
published: '2026-09-18'
collected: '2026-09-25'
category: Training
direction: 大模型架构设计 · 无训练代价选型
tags:
- Neural Architecture Search
- Transformer
- Model Pruning
- LLM
- Training-free Proxy
one_liner: 提出仅靠架构规格计算的神经谱容量，搭配DP求解器秒级输出资源约束下最优架构
practical_value: '- 业务侧LLM/Transformer选型时，可用NSC替代参数量/FLOPs作为度量，同预算下快速筛选性能更优的架构，无需预训练验证

  - 线上LLM/推荐Transformer服务做结构化剪枝时，用NSC-DP无需校准数据，秒级生成同资源约束下的最优剪枝方案，大幅降低剪枝成本

  - 自研推荐/广告侧Transformer模块（如序列建模、多兴趣）时，可复用NSC的层加性优化逻辑，快速完成深度/宽度/FFN比例的全局最优分配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有参数量、FLOPs指标无法区分同预算下不同结构的Transformer性能差异，主流训练-free架构搜索代理需要实例化模型、依赖输入数据，且仅能通过黑盒搜索得到局部最优结果，在LLM尺度下搜索成本极高，亟需仅靠架构规格就能计算、支持全局优化的架构度量指标。
### 方法关键点
- 基于随机矩阵理论的Marchenko–Pastur定律，提出神经谱容量NSC，仅通过权重矩阵的维度、初始化方差就能计算，无需实例化模型、输入数据或梯度计算，可捕捉深度、头数、FFN比例等参数量感知不到的结构信息
- 利用NSC的层加性特性，设计NSC-DP动态规划求解器，将资源约束下的架构优化转化为有界背包问题，可秒级返回全局最优架构，保证结果最优性
- 适配Transformer、CNN等多种架构，支持架构搜索、模型剪枝等多场景
### 关键实验
在7类Transformer和CNN架构上验证：FlexiBERT场景下，参数量差异<10%的架构对排名Kendall τ达0.505，远高于参数量的0.082；Transformer-XL架构搜索仅需2秒，PPL优于人工设计基线；LLaMA-7B剪枝到5.7B时，8项常识推理任务平均得分65.47，优于最优基线1.64个百分点，速度快5900倍，无需任何校准数据。
### 核心结论
同参数量下的Transformer性能差异可通过权重矩阵的奇异值谱度量，无需训练就能快速找到资源约束下的最优架构。
