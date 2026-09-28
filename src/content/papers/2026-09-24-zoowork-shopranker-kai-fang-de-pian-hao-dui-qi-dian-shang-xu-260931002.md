---
title: 'ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker'
title_zh: ZooWork-ShopRanker：开放的偏好对齐电商重排序模型家族
authors:
- Siqiao Xue
- Shuxuan Liu
- Ning Hu
affiliations:
- ZooWork Team
arxiv_id: '2609.31002'
url: https://arxiv.org/abs/2609.31002
pdf_url: https://arxiv.org/pdf/2609.31002
published: '2026-09-24'
collected: '2026-09-28'
category: RecSys
direction: 电商搜索重排 · LLM偏好对齐
tags:
- Reranker
- E-commerce
- Preference Alignment
- LLM Judge
- Distillation
- LoRA
one_liner: 基于多LLM跨家族偏好标注构建0.6B/4B/8B开源电商重排模型及无污染评测基准
practical_value: '- 多LLM跨家族双向标注范式可复用：使用不同派系LLM做标注、双向排列消除位置偏差、按共识划分金/银/铜标签层级，可低人力成本获取高质量电商偏好标注，适合冷启动重排模型的训练数据构建

  - 训练&部署路径可直接迁移：大模型对齐后蒸馏小模型+仅更新LoRA适配器，不损失通用重排能力，推理无额外开销；0.6B小模型在结构化商品场景性能追平4B base，吞吐提升2.8x，适合生产降本

  - 硬约束场景优先用规则标注：通用偏好对齐无法解决显式预算阈值遵从问题，少量针对性程序标注的专项模型效果远优于大模型通用对齐，适合价格/合规类强约束的电商搜索场景'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
通用开放重排模型在电商场景迁移效果差，仅关注语义相关性，不识别用户查询中的硬约束（预算、受众、品类、排除项等），在有硬约束的查询上准确率比无约束场景低14-20分，甚至低于随机水平；同时真实流量只有query和候选，没有干净的pairwise偏好标签，难以大规模监督训练。

### 方法关键点
- 构建SHOPRANK-BENCH评测基准：基于私有搜索流量的10511条无污染偏好pair，用3个不同派系LLM做双向标注消位置偏，按共识分为金（3/3同意）、银（2/3同意）、铜（1/3同意）三个层级，同时提供结构化/自然语言双格式商品描述，配套属性优先级、预算两个诊断数据集
- 模型训练：8B旗舰版直接基于多LLM标注的pairwise数据用Bradley-Terry损失做偏好对齐，4B和0.6B小模型用对齐后的8B做老师蒸馏软标签，再用标注pair做精修；全流程仅更新LoRA适配器，底座权重冻结

### 关键实验
对比BGE、Jina、Qwen3等开源SOTA重排模型，8B版本在结构化商品场景准确率83.4%，比最强开源基线Jina-m0高4.2个点，比未对齐的Qwen3-8B base高4.2个点；4B版本准确率81.2%，同样超过Jina-m0；0.6B版本在结构化场景性能与4B base无统计差异，吞吐提升2.8倍；所有模型在MTEB通用重排任务上无明显性能损失。

最值得记住的结论：电商重排的核心是查询相关的两层决策逻辑（先满足硬约束再比软偏好），手搓的固定属性优先级规则与真实用户偏好负相关，从标注数据中学习约束优先级远优于人工规则。
