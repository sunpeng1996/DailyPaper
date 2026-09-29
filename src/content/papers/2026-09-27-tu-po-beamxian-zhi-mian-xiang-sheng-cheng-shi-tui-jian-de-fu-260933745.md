---
title: 'Beyond the Beam: Constructive Repair and Candidate Completion for Generative
  Recommendation'
title_zh: 突破Beam限制：面向生成式推荐的ID修复与候选补全方法
authors:
- Zijun Zhao
- Peng Zhang
- Gang Zhang
- Yuanchi Ma
- Hui He
- Zhendong Niu
affiliations:
- Beijing Institute of Technology
- China Meteorological Administration
- Tsinghua University
- Singapore Management University
arxiv_id: '2609.33745'
url: https://arxiv.org/abs/2609.33745
pdf_url: https://arxiv.org/pdf/2609.33745
published: '2026-09-27'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · Semantic ID动态优化
tags:
- GenRec
- Semantic ID
- Beam Search
- Catalog Expansion
- Inference Optimization
one_liner: 通过最小替换ID修复与边界引导候选补全，突破生成式推荐Beam搜索的召回瓶颈
practical_value: '- 类目更新时可复用最小替换ID分配策略：用最小费用流求解保留旧ID的最优ID映射，减少模型重训成本，避免老item召回效果下降

  - 推理阶段可引入协同信号+生成似然的融合排序：补充冷启动/新item的特征信号，召回初始Beam搜索以外的高相关item

  - 可复用边界引导的候选补全+提前终止策略：用前缀得分上界优先评估高潜力候选，满足停止条件即可返回全局Top-K，降低推理延迟'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐依赖生成Semantic ID召回item，类目扩展后大量新item的ID无法进入Beam搜索候选池，重训/重切分ID成本高，且会导致老item效果受损，现有方案无法兼顾旧ID保留与新item召回。

### 方法关键点
- 先推导ID修复的可行边界：固定生成器与旧ID的前提下，明确支持新item进入Top-K的ID分配的上下限区间，输出不变性证书可识别不受ID调整影响的查询
- 训练阶段用最小费用流求解最小替换ID修复方案：生成多个候选映射后，选训练集NDCG最高的共享映射，仅微调模型适配新映射，无需全量重训
- 推理阶段融合生成似然与协同信号作为统一排序得分，基于前缀得分上界优先评估Beam外高潜力候选，满足终止条件即可认证全局Top-K，无需遍历全量item

### 关键实验
在Amazon Reviews的Beauty、Tools、Toys三个数据集上，对比DACT、Reformer等11个SOTA基线，T5 backbone下Recall@10相对最优基线提升15.5%~46.3%，NDCG@10提升15.2%~44.4%；LC-Rec decoder-only backbone下也实现全数据集NDCG@10提升，单query推理延迟仅10ms左右。

**最值得记住的一句话**：生成式推荐的召回瓶颈不止来自生成器本身，Beam搜索的截断损失可通过轻量的ID调整+候选补全方案低成本解决。
