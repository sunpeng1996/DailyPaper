---
title: 'Learning from Success and Failure: Acquiring Adaptive Dialogue Strategies
  for Social Robots'
title_zh: 从成功与失败交互中学习社交机器人自适应对话策略
authors:
- Sanae Yamashita
- Yuki Okafuji
arxiv_id: '2609.19570'
url: https://arxiv.org/abs/2609.19570
pdf_url: https://arxiv.org/pdf/2609.19570
published: '2026-09-17'
collected: '2026-09-20'
category: Agent
direction: 人机交互Agent 对话策略构建与优化
tags:
- LLM
- VLM
- Dialogue Strategy
- Human-Robot Interaction
- Experience Reuse
one_liner: 结合VLM用户属性识别与LLM，复用成败交互数据自动构建可解释对话策略库降低落地成本
practical_value: '- 业务对话Agent迭代中可直接复用失败交互日志作为约束规则，无需仅依赖正样本，大幅降低优质样本采集成本

  - 多模态交互场景（如直播导购Agent、线下智能导购屏）可复用「VLM识别用户属性+LLM生成个性化对话策略」架构，提升交互适配性

  - 可参考该思路构建可解释的策略知识库，避免全黑盒LLM生成，方便人工运营干预和迭代，降低线上风险'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统社交机器人对话系统需人工设计对话策略与用户属性识别规则，依赖专业经验；真实落地场景数据采集成本高，大量失败交互数据被浪费，仅用成功样本的策略学习方案落地可行性低
### 方法关键点
1. 采用VLM+LLM两级架构：VLM负责从多模态交互中识别用户属性，联合对话历史输入LLM生成匹配用户属性的个性化对话策略
2. 同时从成功、失败交互日志中抽取规则，将失败策略作为生成约束补充成功策略，自动构建可解释的对话策略知识库
### 关键结果
引入失败策略作为约束后，对话策略效果显著优于仅使用成功策略的基线；整套pipeline可直接基于真实落地日志迭代维护策略库，大幅降低对话系统开发成本
