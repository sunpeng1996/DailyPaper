---
title: 'AI Isn''t Getting Dumber, We''re Getting Pickier: Rising Standards in Human
  Evaluation of Large Language Models'
title_zh: AI未退化人类标准提升：大语言模型人工评估的偏好漂移研究
authors:
- Zihan Chen
- Lei Nico Zheng
- Di Zhu
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2611.14333'
url: https://arxiv.org/abs/2611.14333
pdf_url: https://arxiv.org/pdf/2611.14333
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: 大语言模型 · 人工评估漂移研究
tags:
- Human_Evaluation
- LLM
- Evaluation_Drift
- Chatbot_Arena
- Human_Feedback
one_liner: 基于Chatbot Arena百万盲测数据证实LLM人工评估绝对标准随时间上升，相对排序稳定
practical_value: '- 做生成式推荐/AI文案的人工评估时，放弃跨时间段绝对评分基准，优先用同批次相对排序对比，避免标准漂移导致指标失真

  - 训练RLHF/RLAIF模型时，人类反馈标注需分批次做时间校准，长期迭代的标注流程定期插入固定基准集监控标注标准变化

  - 智能导购/Agent产品迭代时，不要仅靠用户差评率上升判定模型退化，需同步做固定基准的离线A/B测试验证效果变化'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
用户频繁反馈ChatGPT等LLM效果退化，但此前研究未区分模型本身变化与人类评估标准漂移的混淆影响，无法解释退化感知的来源。
### 方法关键点
基于Chatbot Arena 2023年5月-2024年8月的126万+固定版本模型对的盲测投票数据，控制模型版本、投票人、prompt、语言、界面等变量，分离评估标准漂移的独立影响。
### 关键结果数字
相同固定模型对的「两者都差」投票占比月增1.71个百分点（均值17.1%），2024年达月增1.91个百分点，14组跨两年观测的模型对该占比从15.5%升至23.3%；模型相对排序无明显趋势，更强模型的决胜票占比2024年保持平稳；该漂移为全平台通用趋势，加入其他模型对的月份效应即可消除单模型对的漂移影响。
