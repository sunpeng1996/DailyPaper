---
title: 'Game Arena: Strategic LLM Evaluation in Competitive Environments'
title_zh: Game Arena：竞争环境下的大语言模型策略评估平台
authors:
- Bovard Doerschuk-Tiberi
- Yao Yan
- Justin Chiu
- Hann Wang
- Timothy Chung
- Martyna Plomecka
- John Schultz
- Jon Lipovetz
- Clayton Drazner
- Yuchen Zhuang
arxiv_id: '2609.31473'
url: https://arxiv.org/abs/2609.31473
pdf_url: https://arxiv.org/pdf/2609.31473
published: '2026-09-24'
collected: '2026-09-28'
category: Eval
direction: LLM评估 · 动态博弈基准
tags:
- LLM Evaluation
- Dynamic Benchmark
- Strategic Reasoning
- Game Theory
- Kaggle
one_liner: Kaggle推出开放动态LLM竞技评估平台，覆盖三类博弈场景解决静态基准饱和问题
practical_value: '- 可复用动态对抗评估框架思路，替代静态A/B测试评估推荐Agent/导购Agent的策略博弈能力，比如大促场景下的竞价、用户话术对抗效果

  - 三类博弈场景的评估指标可迁移：完美信息场景（如规则明确的优惠券发放策略）、非完美信息场景（如用户隐藏偏好下的推荐）、多智能体场景（如多广告主竞价排序）的能力评估都可参考对应指标设计

  - 平台的可扩展架构可复用，支持自定义业务场景的博弈评估任务，快速迭代LLM驱动的业务策略能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
静态LLM基准（如MMLU、GSM8K）已接近性能饱和，区分前沿模型能力的效度持续下降，且无法有效评估模型在策略规划、不确定环境自适应、鲁棒性等实际落地所需的核心能力，缺乏动态可扩展的评估方案。

### 方法关键点
1. 推出开放可扩展的Kaggle Game Arena评估平台，支持LLM开展头对头竞技对抗，对战强度随参与模型能力提升自然增长，避免饱和问题
2. 内置三类试点博弈环境：完全信息场景（国际象棋）、非完全信息场景（扑克）、多人博弈场景（狼人杀），覆盖不同决策场景的能力评估需求
3. 基于大规模真实对战ground-truth数据计算评估指标，架构支持新游戏/自定义场景扩展，保证评估可复现、透明、可泛化

### 关键结果
已完成三类场景的全量模型竞赛验证，可稳定区分不同LLM的策略决策能力，评估结果无静态基准的饱和缺陷。
