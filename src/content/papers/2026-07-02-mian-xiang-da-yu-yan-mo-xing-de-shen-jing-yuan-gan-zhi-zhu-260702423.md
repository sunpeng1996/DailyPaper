---
title: Neuron-Aware Active Few-Shot Learning for LLMs
title_zh: 面向大语言模型的神经元感知主动少样本学习框架
authors:
- Zhuowei Chen
- Liwei Chen
- Christian Schunn
- Raquel Coelho
- Xiang Lorraine Li
affiliations:
- University of Pittsburgh, USA
arxiv_id: '2607.02423'
url: https://arxiv.org/abs/2607.02423
pdf_url: https://arxiv.org/pdf/2607.02423
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LLM垂域适配 · 主动少样本选择
tags:
- Active Learning
- Few-shot Learning
- Neuron Analysis
- LLM Adaptation
- In-context Learning
one_liner: 基于LLM内部FFN神经元激活信号设计双准则样本选择策略，提升主动少样本学习性能
practical_value: '- 垂域LLM适配（如电商商品属性识别、广告文案生成、客服意图分类的少样本ICL）场景下，若使用开源LLM，可替换原有语义相似/熵选demo的方案为NEUFS的神经元感知选择策略，相同标注成本下可提升1~5%的任务效果

  - 复用神经元共识指标（激活的唯一神经元数量）做LLM生成结果的幻觉检测，可用于推荐系统中LLM生成推荐理由、Agent调用工具前的决策可靠性校验，比输出层熵的检测相关性高~10%

  - 适配不同参数LLM时可直接复用论文的τ调优经验：7B及以下小模型τ设为0~0.3，优先保障样本多样性；8B及以上大模型τ设为0.5，平衡多样性与幻觉样本选择，省去从零调参成本

  - 该方案仅适用于可访问FFN激活、unembedding矩阵的开源LLM，闭源API场景无法直接复用，可优先应用在部署了开源LLM的内部业务流程中'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有主动少样本学习（AFSL）通过筛选高价值未标注样本做少样本demo，降低垂域LLM适配的标注成本，但主流方法依赖输出层预测熵、外部语义嵌入做选择信号：熵受LLM过自信、幻觉问题影响无法准确反映真实知识缺口，外部语义嵌入默认语义相似等价于知识相似，忽略任务相关的模型内部认知状态，导致demo选择效果不佳。
### 方法关键点
- 基于LLM每层FFN的神经元激活构建样本表示，通过Early Unembedding计算每个神经元对最终预测的贡献，过滤得到任务相关的有效激活神经元集合，替代外部语义嵌入
- 双准则样本选择：用激活神经元集合的Jaccard距离做K-Medoids聚类，保障demo覆盖不同知识电路，提升多样性；统计样本激活的唯一神经元数量作为神经元共识，数量越高表示模型内部知识冲突越多、越容易幻觉，优先选择这类样本标注
- 加权融合聚类中心距离与神经元共识得分，从每个聚类中选最优样本，超参数τ控制多样性与幻觉优先的权重
### 关键结果
在MMLU-Pro（推理）、Edu-Feedback（教育分类）、TREC（问题分类）3个数据集，覆盖Llama3 3B/8B、Qwen3 4B/8B 4个模型，对比Entropy、TypiClust、Patron等6个基线：Qwen3-4B上MMLU-Pro准确率达0.452，超语义+熵结合的Patron 6.1pp；Edu-Feedback F1达0.692，超TypiClust 6.6pp；TREC准确率达0.878，超FastVoteK 0.7pp。
LLM内部神经元激活信号比输出层熵、外部语义嵌入更能真实反映模型的知识缺口，是少样本选择、幻觉检测的更可靠原生信号。
