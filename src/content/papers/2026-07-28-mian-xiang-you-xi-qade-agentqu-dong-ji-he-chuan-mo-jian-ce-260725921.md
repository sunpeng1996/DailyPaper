---
title: Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in
  Video Game QA
title_zh: 面向游戏QA的Agent驱动几何穿模检测中VLM性能评估
authors:
- Carlos Celemin
- Benedict Wilkins
- Adrián Barahona-Ríos
- Saman Zadtootaghaj
- Nabajeet Barman
affiliations:
- Sony Interactive Entertainment, London, United Kingdom
arxiv_id: '2607.25921'
url: https://arxiv.org/abs/2607.25921
pdf_url: https://arxiv.org/pdf/2607.25921
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: Agent 智能体自动化异常检测
tags:
- VLM
- Zero-shot Learning
- Anomaly Detection
- Autonomous Agent
- Prompt Engineering
- Benchmark
one_liner: 在自动标注的游戏几何穿模检测任务上benchmark 6款主流VLM的零样本性能与prompt敏感度
practical_value: '- 电商商品图瑕疵检测、直播内容违规检测等视觉异常类业务，可复用「自动探索Agent+自动标注流水线」的零样本benchmark方案，无需大量人工标注即可快速验证多模态模型性能

  - 零样本多模态任务优先选型Gemini-3.1-Flash，其对prompt波动鲁棒性最优；开源VLM需针对性做prompt调优才能平衡precision与recall

  - 多模态异常检测类业务不要直接用单VLM做端到端检测，适合放在第一阶段做高召回候选过滤，后续叠加规则/小模型降低虚警'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
游戏规模提升后人工QA成本高、漏检多，几何穿模等视觉异常会严重损害用户体验，现有方案缺少对主流VLM在Agent驱动的自动检测场景下的系统性评估。
### 方法关键点
搭建自定义探索Agent自动遍历游戏关卡收集视觉帧数据，配套自动标注流水线生成帧级穿模标签，无需人工标注即可完成受控benchmark；在零样本设置下测试Gemini、GPT、Qwen、Gemma、Llama、Ministral共6款VLM，分析4种不同prompt的性能敏感性。
### 关键结果
所有VLM对近接触几何、半遮挡等歧义帧均存在大量误报；Gemini-3.1-Flash整体精度最优，prompt鲁棒性最好；开源VLM的precision-recall随prompt设计波动极大；当前VLM更适合作为多阶段QA流水线中的高召回候选过滤器，而非独立bug检测器。
