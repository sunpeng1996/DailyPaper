---
title: Rubric Rewards from Item Response Theory
title_zh: 基于项目反应理论的评分规则奖励计算框架RRT
authors:
- Milad Yazdani
- Yaser Souri
- Xiren Zhou
- Pranit Chawla
- Dena Shahriari
- Subhojit Som
- Xia Song
affiliations:
- University of British Columbia
- Microsoft
arxiv_id: '2609.35646'
url: https://arxiv.org/abs/2609.35646
pdf_url: https://arxiv.org/pdf/2609.35646
published: '2026-09-28'
collected: '2026-09-30'
category: Training
direction: 大语言模型RL训练 · 评分规则奖励优化
tags:
- Item Response Theory
- RLHF
- GRPO
- Reward Modeling
- Rubric Evaluation
one_liner: 将项目反应理论引入评分规则奖励聚合，提升GRPO训练效果并降低大模型评判成本
practical_value: '- 电商/广告场景的多维度AIGC文案（商品标题、广告创意、推荐理由）RLHF训练，可复用RRT的评分聚合逻辑，替代固定权重打分，区分相同总分下的不同文案质量，提升奖励信号区分度

  - 做LLM-as-a-Judge自动化评估时，可复用RRT的自适应Fisher选择策略，优先选择对当前样本区分度最高的评估维度，最多可降低50%的评判API调用成本

  - 推荐系统多目标排序融合场景，可借鉴IRT的难度、区分度参数建模思路，对CTR、CVR、停留时长等业务指标动态分配权重，替代固定加权和，提升排序结果的稳定性和业务效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于评分规则（rubric）的LLM强化学习训练多采用固定权重加总各维度评判结果的方案，存在两大核心痛点：一是不同评判模式可能得到相同总分，无法有效区分样本真实质量，奖励信号区分度不足；二是评判维度越多，大模型评判请求量越大，训练成本居高不下。
### 方法关键点
- 基于项目反应理论（IRT）构建Rubric Response Theory（RRT）框架，为每个评分维度建模难度、区分度两个参数，通过Response Parameter Network（RPN）从prompt和维度文本直接预测参数
- 以样本质量的贝叶斯后验估计值作为GRPO的奖励信号，替代固定权重加总，最大化奖励信号的局部信噪比
- 采用在线EM算法随策略迭代动态更新RPN参数，适配训练过程中不断变化的样本分布
- 基于Fisher信息设计自适应维度选择策略，优先选择对当前样本组区分度最高的维度评判，降低评判请求量
### 关键结果
在Medical、Science、RaR Science、RubricBench 4个数据集上对比GRPO、POW3R、DIVA等基线：采用Qwen3.5-4B作为策略模型时，RRT宏观维度得分比Vanilla GRPO高1.7个点，在难/极难维度上领先2.8~5.6个点；仅用50%评判预算时，自适应Fisher选择的RRT得分与全量评判的GRPO差距小于0.1个点，可减少约50%的评判时间，RRT额外计算开销仅为Vanilla GRPO的0.123%。
### 核心结论
固定权重的评分规则加总无法适配不同样本分布下的维度区分度差异，结合IRT的动态奖励建模可同时提升奖励信号质量与评估效率
