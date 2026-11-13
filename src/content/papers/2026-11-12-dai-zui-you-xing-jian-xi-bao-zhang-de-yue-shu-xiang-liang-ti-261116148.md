---
title: Calibrated Early Termination with Bounded Optimality Gaps for Constrained Vector
  Search
title_zh: 带最优性间隙保障的约束向量搜索校准式提前终止算法
authors:
- Xinyu Zhang
- Jingze Li
- Baihua Zheng
- Weiwei Sun
affiliations:
- Fudan University
- Singapore Management University
arxiv_id: '2611.16148'
url: https://arxiv.org/abs/2611.16148
pdf_url: https://arxiv.org/pdf/2611.16148
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 向量检索 · 提前终止优化
tags:
- Vector Search
- Early Termination
- ANN Search
- HNSW
- Retrieval Optimization
one_liner: 提出带严格结果正确性概率保障的约束向量搜索提前终止规则CaST，比现有方案快最多45.5%
practical_value: '- 电商搜索/推荐的HNSW向量召回层可直接复用CaST的校准式提前终止逻辑，在保证95%返回结果正确性的前提下，降低平均检索耗时4.8%~45.5%，提升检索吞吐量

  - 借鉴其单调规则类+动态规划求解的思路，针对业务自定义约束（如同品类商品不超过N个的多样性约束），快速适配最优提前终止阈值策略，替代人工调参

  - 可复用其固定序列二项检验的校准方法，给现有召回模块的结果正确性加上可量化的概率保障，避免平均召回达标但部分query结果质量波动大的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
向量搜索是推荐、RAG系统的核心检索层，现有基于HNSW等图索引的向量搜索要么采用固定访问预算，效率极低（ε=0.05时预算是中位数完成时间的5.8~7.1倍），要么基于学习的提前终止方案仅保证平均召回，无法给出单query返回结果正确性的严格概率保障；尤其是带品类约束、多样性约束的k-NN查询场景，现有方案的结果准确率仅70%左右，无法满足业务质量要求。

### 方法关键点
- 定义仅依赖搜索轨迹的运行最小得分、答案是否装满两个观测的单调停止规则类，将风险约束下的最优停止问题转化为序多胞体上的线性规划，通过动态规划求解得到嵌套阶梯规则链
- 采用固定序列二项检验对规则链校准，保证返回结果错误率≤ε的置信度达1-δ
- 通过拉格朗日弱对偶给出规则类最优成本的下界，量化实现规则与理论最优的间隙

### 关键实验结果
在百万级Amazon商品、arXiv论文等4个公开数据集上测试，对比固定预算、LAET、DARTH、Level+cap等10+基线，在ε=0.05（95%结果正确率）的要求下，CaST耗时比所有校准后的基线少4.8%~45.5%，且最优性间隙≤13.2%（95%置信度），即最多比理论最优规则的检索成本高13.2%。

### 最值得记住的一句话
带业务约束的向量检索提前终止无需依赖人工调参或平均指标拟合，可同时实现可量化的结果质量保障与接近理论最优的检索效率。
