---
title: 'When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K
  Causal Reasoning in LLMs'
title_zh: 多有效答案场景下基于符号验证的LLM因果推理最优采样选择
authors:
- Omatharv Bharat Vaidya
- Connor Thomas Jerzak
- Zayne Rea Sprague
- Fangcong Yin
- Nhat Ho
affiliations:
- The University of Texas at Austin
- New York University
arxiv_id: '2608.03506'
url: https://arxiv.org/abs/2608.03506
pdf_url: https://arxiv.org/pdf/2608.03506
published: '2026-08-04'
collected: '2026-08-05'
category: Reasoning
direction: 因果推理 · 符号验证 Best-of-K 选优
tags:
- Causal Reasoning
- Symbolic Verification
- Best-of-K
- Self-Consistency
- LLM Inference
one_liner: 提出无训练符号验证框架CALVER，解决多有效答案下因果推理采样选优的投票失效问题
practical_value: '- 做best-of-K采样时，若业务任务存在多个正确解（比如电商多归因路径选择、推荐策略因果效应评估），不要直接用多数投票/语义聚类，可基于领域可执行规则做符号验证选优，效果优于LLM评委、奖励模型，且无训练成本

  - 对于可形式化规则的任务（比如广告投放因果效应校验、营销活动合规性检查），无需训练奖励模型，直接写确定性校验逻辑，单样本毫秒级CPU可跑，仅增加7%左右的推理成本

  - 从非结构化文本提取结构信息（比如从商品评价/客服对话提取因果关系）时，若提取可靠性低于40%，不要强依赖单条提取结果做全局求解，对每个生成样本做独立校验选优效果更好；提取可靠性高时优先用全局求解'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有Self-Consistency等best-of-K采样方法依赖多数投票选最优，在因果推理等存在多有效答案的场景会完全失效：有效答案的票数被拆分，反而常见错误答案得票最高，即使升级到72B大模型作为评委也无法解决这个问题。

### 方法关键点
- 提出无训练的CALVER（Causal Axiom-Level Verification）框架，要求LLM输出符合6槽结构化schema：图、查询、策略、推导记录、计算结果、答案，不限制自由文本推理部分
- 基于Pearl因果公理（d分离、后门调整、干预等），对每个采样trace的6个槽做确定性二进制校验，满分6分，选择得分最高的最早trace作为输出，全程不需要参考标注答案
- 支持两种模式：给定因果图模式直接用源图校验；无给定图时从每个trace独立抽取因果图做本地校验，适配从文本推理因果的场景

### 关键实验
主基准为CLEAR多有效答案因果推理数据集，对比基线包括多数投票、Jaccard medoid、奖励模型、LLM评委、模型置信度：CALVER准确率达42.1%，比所有基线高至少11.3个百分点，72B LLM评委效果和投票基本持平；K=32时CALVER准确率达57.9%，比投票高25.4个百分点，优势随采样数增大而扩大；跨10个公开贝叶斯网络、文本抽图场景、逻辑推理任务均有稳定增益，单trace校验仅需1-8ms CPU，仅比投票多7%的推理成本。

### 最值得记住的一句话
当任务存在多个有效答案时，聚合单位应该是「候选是否符合任务有效性规则」，而非「答案字符串出现频率」
