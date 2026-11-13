---
title: Pretraining Data Statistics Shape the Phases of Learning Entity Comparison
  in Language Models
title_zh: 预训练数据统计特征决定大语言模型实体比较的学习阶段
authors:
- Yik Siu Chan
- Jing Huang
- Yanai Elazar
- Atticus Geiger
affiliations:
- University of Maryland
- Stanford University
- Bar-Ilan University
- Goodfire
- Pr(Ai)2R Group
arxiv_id: '2611.16882'
url: https://arxiv.org/abs/2611.16882
pdf_url: https://arxiv.org/pdf/2611.16882
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 大语言模型训练动态 · 启发式学习
tags:
- LLM Training Dynamics
- Entity Comparison
- Pretraining Data
- Heuristic Learning
- Training Phases
one_liner: 揭示LLM实体比较学习的三阶段规律，证明预训练数据分布是阶段演化的核心驱动
practical_value: '- 开发电商商品比对、导购Agent等涉及实体属性比较的应用时，需确保任务监督数据占比超过临界阈值，避免模型停留在频率/位置启发式阶段输出错误结果

  - 微调LLM4Rec或商品相关任务时，可适当平衡长尾商品的采样频率，将实体分布从天然Zipf分布拉平，加速模型掌握正确的属性匹配逻辑，降低热门实体偏好偏差

  - 可复用论文的特征消融方法诊断LLM推荐/问答系统的决策逻辑：通过移除频率、位置特征后的准确率变化，判断模型是真的掌握任务逻辑还是依赖shortcut，提升可解释性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有研究对预训练数据如何因果驱动LLM能力演化的规律不明确，实体比较任务是测试策略演化的理想场景，可解释LLM是用正确逻辑还是快捷方式答题，对电商商品比对、信息检索类应用的模型优化有直接指导价值。

### 方法关键点
- 训练163M规模小LM，混合OLMo-2预训练自然文本与不同比例的实体比较合成数据，控制实体频率分布为Zipf或均匀分布
- 用L1正则化逻辑回归拟合模型输出，通过特征消融（移除频率/位置/真值特征后的准确率下降）判断各阶段的主导策略
- 验证OLMo-2系列1B/7B/13B/32B模型的训练阶段演化规律是否与小模型实验一致

### 关键结果
1. 实体比较学习存在固定三阶段顺序：早期频率启发式→中期位置启发式→晚期正确算法，该规律在163M到32B参数的模型中普遍存在
2. 任务监督数据占比低于0.01%时，模型永远停留在前两个启发式阶段；占比提升到1%时，模型直接跳过位置阶段进入正确算法阶段
3. 实体频率从天然Zipf分布改为均匀分布时，频率阶段时长缩短60%以上，正确算法阶段提前30%出现
4. 仅13B以上规模的OLMo模型能从纯自然文本预训练中自发进入正确算法阶段，1B/7B参数模型永远停留在位置启发式阶段

**最值得记住的一句话**：LLM学习复杂任务时会优先采用最易获取的启发式快捷方式，只有当任务相关信号足够强时才会切换到正确算法，预训练数据的实体分布是可调控的核心杠杆。
