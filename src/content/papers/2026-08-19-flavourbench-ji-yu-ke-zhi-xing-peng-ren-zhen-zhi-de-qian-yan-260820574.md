---
title: 'FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground
  Truth'
title_zh: FlavourBench：基于可执行烹饪真值的前沿大语言模型排序基准
authors:
- Josef Chen
- Erim Hayretci
affiliations:
- Independent Researcher
- Imperial College London
arxiv_id: '2608.20574'
url: https://arxiv.org/abs/2608.20574
pdf_url: https://arxiv.org/pdf/2608.20574
published: '2026-08-19'
collected: '2026-08-24'
category: Eval
direction: 大语言模型自动化评测基准构建
tags:
- LLM-Evaluation
- Automated-Benchmark
- Ground-Truth
- Model-Ranking
- Open-Ended-Task
one_liner: 构建基于可执行烹饪真值的自动化LLM基准，无需人工/模型裁判即可公平排序前沿模型
practical_value: '- 做LLM生成类任务（如推荐文案、搜索query改写）评测时，可借鉴预枚举所有合理候选+预打分的设计，替代人工/模型裁判，消除对齐偏差

  - 多模型效果对比时，采用bootstrap+符号翻转检验+Holm校正的统计方法，可严谨判定效果差异的显著性，降低随机波动干扰

  - 多任务评测架构设计可复用：统一控制每个模型的有效样本量，消除缺失值带来的排名偏差，保证榜单公平性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有开放式LLM基准依赖人工偏好、第三方模型裁判或严格精确匹配规则，要么存在裁判与被测模型的对齐偏差，要么会丢失合理答案间的质量差异，评测公平性和准确性不足。
### 方法关键点
构建FlavourBench自动化评测基准，基于Epicure烹饪系统预生成所有候选答案的0-100分连续分数映射；测试任务为给定8种食材选3种组合，覆盖食材替换、搭配、约束组合三类共534个任务，评测时直接查表打分，无需事后解释；采用5万次anchor-cluster bootstrap计算95%置信区间，10万次符号翻转检验完成351组模型配对对比，搭配Holm校正控制假阳性，统一保证每个模型的有效响应数，消除缺失值偏差。
### 关键结果
两个独立测试集相关系数r=0.89、秩相关系数ρ=0.80；Grok 4.6以65.1分位列第一（95% CI 61.0-69.2），351组模型对比中101组差异显著；所有评测数据、离线验证工具全量开源。
