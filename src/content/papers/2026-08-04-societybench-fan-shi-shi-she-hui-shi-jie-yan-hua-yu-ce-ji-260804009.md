---
title: 'SocietyBench: Forecasting Counterfactual Social-World Evolution'
title_zh: SocietyBench：反事实社会世界演化预测基准
authors:
- Zhenran Wang
- Zhonghan Bian
- Jinsong Li
- Zhangyang Qi
arxiv_id: '2608.04009'
url: https://arxiv.org/abs/2608.04009
pdf_url: https://arxiv.org/pdf/2608.04009
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM与Agent社会能力评测基准
tags:
- Benchmark
- LLM Evaluation
- Agent Evaluation
- Counterfactual Reasoning
- Social Dynamics
one_liner: 构建反事实社会事件演化预测基准，从双维度评估LLM与Agent的社会动态理解与预测能力
practical_value: '- 做热点事件相关的推荐/广告投放预测时，可复用实体匿名+时间偏移方法，避免模型依赖预训练历史热点记忆，更准确测试真实泛化预测能力

  - 评估事件趋势预测类Agent的效果时，可直接采用概率校准、时序精度两个正交维度的评分体系，避免单一指标遗漏能力缺陷

  - 构建电商大促、舆情演化等业务场景的专用评测集时，可复用「事件主题→多源数据爬取→时序事实/舆情分层→截断点预测题库」的流水线框架'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM/Agent基准多聚焦任务完成能力，缺少对社会事件动态理解、演化预测这类社会能力的量化评测，且真实事件评测易受模型预训练记忆干扰。

### 方法关键点
1. 端到端流水线：输入单句事件主题，爬取5个平台的新闻/社媒内容，生成带日期索引的时序线，拆分事实层与舆情层，每个时间截断点生成经过审计的预测问题库
2. 反事实构造：三阶段流程替换所有命名实体、按事件偏移所有日期，保留事件结构的同时抹除预训练记忆可匹配的表层标签
3. 双维度评分：概率校准、时序精度两个正交的百分制评分轴

### 关键结果
在中英双语5类异构事件、125个预测点上，6个前沿LLM最优得分仅75.0/100（随机基线50分）；同基座的3种Agent框架未带来性能提升，2种无模型启发式方法得分低于所有LLM；单事件单维度得分差距可达21.4分，验证多事件评测的必要性。
