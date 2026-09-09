---
title: 'A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM'
title_zh: A*-Thought-V2：基于LLM几何动力学的高效隐式推理框架
authors:
- Xiaoang Xu
- Siyuan Liu
- Shuo Wang
- Junlan Feng
- Fanyu Meng
- Zhu Zhang
- Jixun Wang
- Xiaorong Wang
- Zihan Zhou
- Xin Li
affiliations:
- Beijing University of Posts and Telecommunications
- The Hong Kong Polytechnic University
- Tsinghua University
- JIUTIAN Research
- OpenBMB
arxiv_id: '2609.07821'
url: https://arxiv.org/abs/2609.07821
pdf_url: https://arxiv.org/pdf/2609.07821
published: '2026-09-07'
collected: '2026-09-09'
category: Reasoning
direction: 大模型隐式推理 · 显隐序列交错
tags:
- Chain-of-Thought
- Latent Reasoning
- LLM Efficiency
- Geometric Dynamics
- SFT
one_liner: 基于CoT隐状态轨迹几何对齐准则实现显隐交错推理，兼顾准确率提升与推理成本下降
practical_value: '- 做Agent推理链路优化时，可借鉴几何对齐准则筛选冗余推理步骤，将偏离目标的验证、修正等步骤压缩为latent token，既保留推理信息又降低KV
  cache占用与推理延迟，适合电商导购、客服Agent的实时响应场景

  - 训练端可复用Embedding Forcing + Label Forcing范式：对冗余步骤的embedding做均值池化生成latent向量，用步骤内所有token的one-hot均值做软标签监督，相比硬剪枝可降低信息损失，适合长文本生成（如商品文案、推荐理由生成）的SFT训练效率优化

  - 可复用角度阈值的语义划分规则：<30°为核心执行步骤、>90°为校验/修正分支，在推荐理由生成、搜索query理解等场景中，可快速过滤无意义的中间冗余内容，平衡生成质量与长度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Chain-of-Thought（CoT）可大幅提升LLM推理能力，但长推理链会带来极高的计算、上下文占用成本，现有硬剪枝方法易丢失有效推理信息，隐式推理方法又缺乏显式步骤选择的可解释准则，亟需兼顾推理信息保留与效率提升的方案。

### 方法关键点
- 将CoT建模为隐状态空间的轨迹，通过3D PCA将问题、中间步骤、答案的隐表示投影到统一空间，计算每步局部转移方向与全局问题到答案方向的夹角，夹角小于阈值的步骤保留为显式文本，大于阈值的冗余步骤压缩为连续latent token
- 提出Embedding Forcing与Label Forcing训练范式：前者将冗余步骤的token embedding均值池化为单步latent embedding，显隐交错组成输入序列；后者用冗余步骤所有token的one-hot均值作为软标签监督latent token预测，混合标准CE损失与latent损失联合优化
- 推理时通过begin/end of latent标签切换模式，latent位置用上一步最后一层隐状态作为输入，复用KV cache实现连续推理

### 关键实验
在Qwen3.5-9B、Qwen3.6-27B两个基座上，用OpenR1-Math-3k做训练数据，在Math500、AIME系列、ARC-Challenge、GPQA-Diamond共6个数据集上对比SwiReasoning、CopT、A*-Thought等基线：平均准确率最高提升2.6%，响应长度减半，Accuracy per Computation Unit（ACU）最高提升2.29×，预处理时间较A*-Thought降低94.6%，训练时间较标准SFT最高降低80.3%。

CoT冗余步骤的几何方向特征与语义高度相关，将偏离全局目标的步骤压缩为隐表示而非直接丢弃，可实现推理效果与效率的双赢。
