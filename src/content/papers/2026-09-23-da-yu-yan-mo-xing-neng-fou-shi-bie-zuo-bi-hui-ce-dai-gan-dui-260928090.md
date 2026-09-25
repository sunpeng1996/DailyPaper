---
title: Can LLMs Catch a Rigged Backtest? A Clean-Control Calibration Benchmark
title_zh: 大语言模型能否识别作弊回测：带干净对照的校准基准
authors:
- Makar Ulesov
- Vladislav Smirnov
- Omar Ibrahim
- Arsenii Bobovnikov
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- University of Pittsburgh
arxiv_id: '2609.28090'
url: https://arxiv.org/abs/2609.28090
pdf_url: https://arxiv.org/pdf/2609.28090
published: '2026-09-23'
collected: '2026-09-25'
category: Eval
direction: 大模型评估 · 回测审计校准基准
tags:
- LLM Evaluation
- Backtest Auditing
- Benchmark
- Calibration
- False Positive Mitigation
one_liner: 构建带干净对照的配对回测审计基准，量化LLM回测审计的校准性能与误报问题
practical_value: '- 可复用「配对对照基准」设计思路，在推荐/广告模型离线A/B测试、策略效果审计时，固定其他变量仅改核心逻辑，精准区分真实效果和数据泄露/过拟合

  - 评估LLM审计类任务性能不能仅看召回率，新增「干净样本误报率」指标，避免广告合规审核、推荐策略作弊识别等场景出现大量误判增加人工成本

  - 设计LLM审计类prompt时增加「干净样本感知提示」，可在不降低缺陷召回的前提下大幅降低误报率，可直接迁移到电商内容审核、策略漏洞检测场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
回测审计本质是校准问题，仅追求缺陷高召回会导致大量合法干净策略被误标记，反而降低审计效率，现有基准缺乏配对对照设计，无法分离模型的真缺陷识别能力和高怀疑先验导致的误报。
### 方法关键点
构建96条配对基准数据集，每条缺陷回测对应仅修改1个方法细节、其余变量（策略、日期、代码风格、报告框架等）完全一致的干净对照样本；设计确定性打分器，拆分缺陷召回、干净对照误报、证据定位、修复建议相关性4个维度的评估指标。
### 关键结果
基于4个大模型接口的1440份缓存审计结果测试：DeepSeek审计器在闭集+干净感知提示下缺陷召回达100%；开放提示下93.8%的干净代码被误标，加入干净感知警告后DeepSeek代码误报率从20.8%降至0%且召回不变；仅用召回指标会导致3/4的模型排名完全一致，加入干净对照准确率指标可拉开79分的排名差。
