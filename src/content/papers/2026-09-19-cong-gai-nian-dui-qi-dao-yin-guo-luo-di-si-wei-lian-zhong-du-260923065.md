---
title: 'From Concept Alignment to Causal Grounding: An Intervention Test of Chain-of-Thought
  Faithfulness'
title_zh: 从概念对齐到因果落地：思维链忠实度的干预测试
authors:
- Qianli Wang
- Yilong Wang
- Dennis Wei
- Jingyi Sun
- Simon Ostermann
- Pepa Atanasova
- Nils Feldhus
affiliations:
- Technische Universität Berlin
- IBM Research
- University of Copenhagen
- University of Groningen
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2609.23065'
url: https://arxiv.org/abs/2609.23065
pdf_url: https://arxiv.org/pdf/2609.23065
published: '2026-09-19'
collected: '2026-09-22'
category: Eval
direction: 推理评估 · 思维链忠实度检测
tags:
- Chain-of-Thought
- Sparse Autoencoder
- Faithfulness
- Causal Intervention
- Mechanistic Interpretability
one_liner: 基于共享稀疏自编码器提出关联与因果两类指标，定量检测LLM思维链内部推理忠实度
practical_value: '- 电商/广告Agent的推理合规校验可复用共享SAE方案，直接提取LLM内部推理概念，无需依赖黑盒输入输出行为推测逻辑，精准识别虚假CoT

  - 高风险场景（如智能导购、广告投放推理）的CoT忠实度评估优先采用因果指标∆p，表层概念对齐仅能提升8%的高因果贡献概率，无法保证推理真实性

  - 基于开源LLM搭建推理链路时，CoT忠实度峰值集中在中后层而非输出层，做推理对齐/干预时优先针对中后层的共享概念，优化效率更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Chain-of-Thought（CoT）忠实度评估多基于输入输出行为或输入归因，属于黑盒检测，无法探知LLM内部真实推理过程，也无法判断CoT提到的概念是否真的因果驱动最终输出，在高风险场景下虚假CoT会引发严重的信任问题。
### 方法关键点
- 用同一套共享Sparse Autoencoder（SAE）分别编码「直接预测」和「带CoT预测」两个路径下答案位置的残差激活，构建统一的内部概念空间
- 提出3个关联指标（CC-SAE、Jaccard相似度、预测对齐召回率）量化两个路径的概念重叠度，衡量表层对齐程度
- 提出因果指标∆p，通过消融两个路径共享的激活概念，测量答案概率的下降幅度，定量评估共享概念对输出的因果贡献
### 关键结果
在Llama-3.1-8B、Gemma-2系列、Qwen3系列共5个LLM、GSM8K/LogiQA等4个推理数据集上测试：
- 关联指标整体对齐度较高，但和因果指标相关性极弱，高对齐仅能提升8%的高因果贡献概率，无法直接代表忠实度
- CoT因果忠实度峰值普遍在中后层而非最终输出层，不同架构呈现分布式（Qwen3）或局部化（Llama3.1）两种忠实度分布模式
- 同模型族下参数越大整体忠实度越高，低忠实度计算会被压缩到更少的浅层
> 最值得记住的一句话：仅靠CoT的表层语义或概念对齐无法判断其忠实度，必须通过对内部概念的因果干预才能验证CoT是否真的驱动了模型输出
