---
title: 'More Than Just Style: Benchmarking Personality Influence in Large Language
  Models'
title_zh: 《不止风格差异：大语言模型人格倾向影响的基准测试》
authors:
- Yuhao Liu
- Mengyu Wang
- Xiao Chen
- Lu Liu
affiliations:
- University of Exeter
- University of Edinburgh
- Nanchang University
arxiv_id: '2611.12392'
url: https://arxiv.org/abs/2611.12392
pdf_url: https://arxiv.org/pdf/2611.12392
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: 大语言模型行为特性 · 基准构建
tags:
- LLM
- Personality
- Benchmark
- Evaluation
- Prompt Engineering
one_liner: 提出SPACE基准框架，可分离LLM内在人格倾向、能力与指令的影响，验证人格倾向的持久性
practical_value: '- 搭建拟人化电商导购Agent时，不要仅依赖prompt调整人设，需针对性做SFT注入稳定人格，避免用户感知到人设前后矛盾

  - 用LLM做推荐理由生成、客服应答时，可参考SPACE的对照评估方法提前校验模型输出的风格稳定性，降低用户体验翻车概率

  - 设计LLM驱动的Agent决策模块时，要考虑内在人格倾向对决策偏好的影响，不能默认prompt指令能100%覆盖行为约束'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM输出除受显式prompt、指令影响外，还存在类似人类人格的内在行为偏好，这类偏好会干扰模型对场景的解读与决策，且目前缺乏方法将其与模型能力、指令的影响清晰拆分。
### 方法关键点
提出SPACE基准框架，搭配人格验证、能力评估、分层情境任务三类互补数据集，以及多引导条件对照评估协议，可精准分离内在人格倾向、模型能力、即时指令三者对输出的影响。
### 关键结果
- 仅靠prompt调整仅能改变生成表层风格，LLM内在人格倾向具备强持久性，无法被相反指令轻易覆盖
- 内在人格倾向对LLM任务表现有可观测的显著影响，落地场景中需重点评估该特性的作用
