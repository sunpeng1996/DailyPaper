---
title: 'Prioritize, Don''t Decide: What We Learned Auditing a Deployed Human-in-the-Loop
  CV Sorter'
title_zh: 已部署人在回路简历排序系统审计：优先排序而非直接决策
authors:
- Hadi Mohammadi
- Jeroen Sparla
- Alexandros Paliouras
- Georg Krempl
- Robert A. Bagheri
affiliations:
- AcademicTransfer, Utrecht, The Netherlands
- Utrecht University Department of Methodology, Statistics & Data Science
- Utrecht University Department of Information and Computing Sciences
arxiv_id: '2611.23359'
url: https://arxiv.org/abs/2611.23359
pdf_url: https://arxiv.org/pdf/2611.23359
published: '2026-11-17'
collected: '2026-11-19'
category: Eval
direction: 人在回路排序 · 上线系统审计优化
tags:
- Human-in-the-Loop
- Ranking System
- Cold Start
- Embedding
- Model Audit
one_liner: 审计已上线的人在回路简历排序系统，输出4项可落地的产品优化结论与冷启动方案
practical_value: '- 做排序类业务评估时，需先排除文档长度等明显shortcut特征干扰，避免评估指标失真

  - 人在回路排序场景慎用不确定性采样做下一个待标注样本推荐，会显著增加人工工作量

  - 冷启动阶段用LLM embedding或本地cross-encoder可快速提升排序能力，标注量达24条后可切换为轻量线性模型降低成本

  - 面向人工决策的辅助系统优先做优先级排序而非直接输出决策结论，用户接受度更高'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
学术岗位单vacancy常收到数百份简历，初筛占用评审委员会大量时间，已上线的人在回路简历优先排序器宣称可大幅降低筛选用时，需对其效果真实性做审计验证。
### 方法关键点
系统基线架构为frozen多语言transformer encoder + 每会话独立线性模型，每收到1个人工标注即重训，会话结束后销毁；审计从特征shortcut、评估指标合理性、采样策略效果、冷启动优化4个维度展开。
### 关键结果
1. 控制简历长度消除shortcut后，按系统排序仅需读一半简历即可覆盖95%合格候选人，随机排序需读完全部；
2. LLM embedding可将零标注序贯判别度从0.66提升至0.80，本地cross-encoder可达到相同冷启动效果且无数据外发风险，标注量达24条后大模型增益消失；
3. 不确定性采样策略会让人工阅读量超过无标注基线，不适合人在回路排序场景。
