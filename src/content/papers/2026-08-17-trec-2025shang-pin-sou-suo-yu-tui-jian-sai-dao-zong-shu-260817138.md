---
title: Overview of the TREC 2025 Product Search and Recommendation Track
title_zh: TREC 2025商品搜索与推荐赛道综述
authors:
- Dean E. Alvarez
- Surya Kallumadi
- Daniel Campos
- ChengXiang Zhai
- Alessandro Magnani
- Rikiya Takehi
- Michael D. Ekstrand
affiliations:
- University of Illinois Urbana-Champaign
- Coursera
- Snowflake
- Coupang
- Waseda University
arxiv_id: '2608.17138'
url: https://arxiv.org/abs/2608.17138
pdf_url: https://arxiv.org/pdf/2608.17138
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: 电商搜索推荐 · 评测基准构建
tags:
- Product Search
- Query Reformulation
- Complementary Recommendation
- Substitute Recommendation
- Benchmark Dataset
one_liner: 发布TREC 2025电商商品搜索推荐赛道的查询扩展、关系推荐任务数据与基准结果
practical_value: '- 做query扩展时可按query特征做路由：词汇gap类难query用RM3等PRF方法提升precision，复杂任务类query用LLM生成扩展提topK召回，避免单一方法在部分query上性能劣化

  - 做相关品推荐时可参考标注规则明确区分互补/替代关系，互补品推荐难度高于替代品，需单独优化特征与模型，不要混为一谈

  - 做电商搜索推荐评测时可复用赛道的分层评估方案：对query扩展用任务完成NDCG、核心品召回，对关系推荐用带关系标签的NDCG、多样性指标，替代粗粒度的相关性评估

  - 可申请公开的TREC 2025赛道数据集做内部算法预训练/验证，补充自有标注数据的不足，尤其是复杂query、互补/替代品关系的标注样本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商商品搜索与推荐缺乏高质量端到端评测数据集，现有隐式反馈数据集（如Amazon共购数据）存在严重偏差，也无法明确区分商品间互补、替代等细粒度关系；同时复杂任务型query的词汇/语义gap问题缺乏统一benchmark验证优化效果，制约了电商搜索推荐算法的迭代。

### 方法关键点
- 赛道设置两大任务：一是搜索端的query reformulation，分为自动扩展（单条）、交互式扩展（最多4条取最优）两类子任务；二是推荐端的细粒度商品关系推荐，要求分别输出top10互补品、top10替代品、top100带关系标签的相关品
- 数据集基于ESCI数据集构建，包含180万+商品，搜索任务提供3万训练query、3千开发query，测试集包含50条历史难query、50条LLM生成的复杂任务型query；推荐任务用人工标注的商品关系作为真值，避免隐式数据偏差
- 评测指标分层设计：搜索任务用任务完成NDCG、核心商品召回@K、覆盖率、多样性等指标，优先权重核心必需商品；推荐任务用分关系的NDCG、标签一致性、多样性等指标，误标商品给半额分

### 关键实验
对比基线为原生BM25，LLM生成扩展基线在全数据集上平均增益最高，RM3伪相关反馈方法在62%的单query上效果优于BM25；难query场景下RM3的任务完成NDCG达0.459-0.466，优于LLM基线的0.420，LLM仅在召回@100上占优；复杂任务query场景下LLM基线的召回@10达0.096，是BM25（0.037）的2.6倍；推荐任务上所有模型的替代品NDCG显著高于互补品，验证互补品推荐难度更高。

### 核心结论
query扩展的效果主要由query本身的特征决定，而非优化算法，增加query级别的路由策略比单纯优化扩展算法的投入产出比更高
