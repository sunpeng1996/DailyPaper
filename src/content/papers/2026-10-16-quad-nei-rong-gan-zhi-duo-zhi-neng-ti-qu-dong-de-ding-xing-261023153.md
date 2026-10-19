---
title: 'QuAD: Quantitative Assessment via Distribution-Alignment for Qualitative Data
  Quality Enabled by a Content-Aware Multi-Agent System'
title_zh: QuAD：内容感知多智能体驱动的定性数据质量定量评估框架
authors:
- Wenshuo Zhang
- Leixian Shen
- Qiqi Zhou
- Shuchang Xu
- Feiyang Hao
- Huamin Qu
- Haobo Li
- Zhao Chen
- Lin-Ping Yuan
affiliations:
- The Hong Kong University of Science and Technology
- Shanghai Jiao Tong University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.23153'
url: https://arxiv.org/abs/2610.23153
pdf_url: https://arxiv.org/pdf/2610.23153
published: '2026-10-16'
collected: '2026-10-19'
category: MultiAgent
direction: 多智能体协作 · 数据质量评估
tags:
- Multi-Agent System
- LLM-as-Judge
- Data Quality Evaluation
- Instruction Optimization
- Distribution Alignment
one_liner: 提出多智能体定性数据评估框架，通过分布对齐实现数据集分析适配性量化与关键样本筛选
practical_value: '- 做LLM-as-Judge类评估任务时，可复用两阶段迭代指令生成+自适应锚点的设计，解决prompt敏感、打分漂移问题，提升评估一致性，适配电商评论质量评估、创意素材打分等场景

  - 数据集层面的质量评估可借鉴分布对齐思路，针对UGC内容、用户评论数据集，先对齐标签分布与语义聚类分布，判断数据集是否适配后续分析目标，减少无效人力投入

  - 处理大规模文本样本时，可复用差异化打分策略：小样本用O(N²) pairwise LLM打分保精度，大样本用O(N)标量投影降本，适配不同业务量级需求'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
传统定性数据（用户调研回复、开放评论等）分析依赖人工，成本高且效率低；现有自动化方法多聚焦单样本质量评估，缺乏数据集层面的适配性判断，容易导致人力投入到与分析目标不匹配的数据集上；同时LLM-as-Judge范式存在prompt敏感、打分漂移、一致性差等问题，无法满足可靠的跨样本差异计算需求。

### 方法关键点
- 核心架构分两部分：内容感知多智能体系统计算响应间语义差异，四象限评估框架做分布对齐分析
- 多智能体系统设Oracle/Updater/Evaluator三个角色，通过两阶段迭代生成领域适配的评估指令，加入自适应锚点动态维护语义参考集，缓解打分漂移
- 四象限评估对比元数据定义的外部分析分布与响应聚类的内部分布，输出GMR/DDR/DP/DC四个联合指标，同时自动挖掘代表性/异常样本
- 适配不同数据量：小数据集用pairwise LLM打分保精度，大数据集用标量投影降为O(N)复杂度控制成本

### 关键实验结果
- 合成数据集实验：相比人工撰写prompt，指令生成模块将打分与ground truth的Spearman相关度从-0.083~0.599提升到0.708~0.830；自适应锚点配置平均相关度最高达0.743（pairwise模式）、0.776（标量模式）
- 真实用户饮食调研数据集验证：QuAD的标签 mismatch AUC达0.749，远超TF-IDF的0.551，人工评估正确性、实用性中位数达6/7分

### 核心结论
定性数据没有绝对的好坏之分，只有是否适配特定分析目标的适配度，需结合分布对齐信号与代表性样本综合判断
