---
title: How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt
  Structure
title_zh: LLM推理提示结构自审计：评估结论的可复现性研究
authors:
- Dipankar Sarkar
affiliations:
- Skelf Research
arxiv_id: '2609.30074'
url: https://arxiv.org/abs/2609.30074
pdf_url: https://arxiv.org/pdf/2609.30074
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: LLM评估 · 可复现性优化
tags:
- LLM Evaluation
- Reproducibility
- Prompt Engineering
- Ranking Stability
- Sensitivity Analysis
one_liner: 以LLM提示结构推理为案例，验证小样本LLM评估排名可信度低并给出优化建议
practical_value: '- 做LLM4Rec、Agent prompt效果评测时，需新增cluster bootstrap检验排名稳定性，避免误选表现不稳定的模型

  - 内部LLM选型/效果对比时，必须留存每次运行的原始输出、记录评测日期，避免模型下线后结论无法复现

  - 不可将模型输出可复现性等价于准确率，需搭配少量人工标注ground truth校验实际业务效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前LLM系统评估普遍基于小样本prompt集输出模型排名表，结论可信度缺乏系统性验证。
**方法**：以LLM提示结构推理任务为案例，测试5个模型家族的8个开源变体（参数量覆盖8B~675B），禁用KV cache，留存293份原始中间表示，采用cluster bootstrap、敏感性分析等方法审计评估结论的稳定性。
**结果**：相同请求的节点集Jaccard系数仅0.39~0.96，72%的prompt-模型对无法输出完全一致的结构；排名中仅最差的2个模型稳定性达86%、99%，中游4个模型稳定性仅27%~48%，前2名稳定性均为68%，无法可靠选出最优模型；两种合理的重复实验合并规则会导致4/8的模型排名变动，整体指标波动7个百分点；4个测试端点在实验后10周内下线，实验完全无法复现。
