---
title: 'WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web
  Agents'
title_zh: WebArena-Pro：面向Web智能体的异构多模态可复现评测基准
authors:
- Imene Kerboua
- Fatemeh Pesaran Zadeh
- Xing Han Lù
- Weijian Qi
- Alexander Miller
- Junyi Song
- Yunjia Tian
- Dongjin Kang
- Seyeon Choi
- Marzia Nouri
affiliations:
- INSA Lyon
- Seoul National University
- McGill University
- Mila – Quebec AI Institute
- The Ohio State University
arxiv_id: '2611.17955'
url: https://arxiv.org/abs/2611.17955
pdf_url: https://arxiv.org/pdf/2611.17955
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Web Agent 多模态可复现评测
tags:
- WebAgent
- Benchmark
- Multimodal
- Reproducible Evaluation
- Browser Agent
one_liner: 推出覆盖20个自托管Web应用、支持音视频模态的可复现Web Agent评测基准
practical_value: '- 做电商Web自动化Agent评测时，可复用其Docker容器化+单任务状态重置的方案，解决页面/数据漂移导致的评测不可复现问题

  - 涉及音视频内容的电商导购/内容审核Agent，可直接复用`transcribe()`/`extract_frames()`工具封装模式，降低多模态交互开发成本

  - 跨系统工作流Agent（如跨商家后台/客服系统/商品上架系统的运营Agent），可参考其跨站点任务设计逻辑，构建业务场景测试集

  - Agent效果验证时，可借鉴其「确定性后端校验→启发式规则校验→LLM终审」的多级评分逻辑，平衡校验成本与准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Web Agent基准存在三大缺陷：自托管类基准仅覆盖少量应用、仅支持文本/视觉模态，无法模拟真实异构工作流；线上站点类基准存在页面、数据漂移问题，评测不可复现；均未将音视频作为核心观测模态，无法覆盖含媒体内容的真实Web任务，制约Web Agent的落地迭代。
### 方法关键点
- 构建6个领域共20个自托管Web应用容器，模拟Notion、Slack、Airbnb、Spotify等主流产品交互逻辑，每个任务执行前独立重置容器状态，彻底避免环境漂移
- 扩展Agent动作空间，新增`transcribe()`/`extract_frames()`/`listen()`/`watch()`四类音视频操作，支持将音视频内容作为核心观测输入
- 任务构建采用「人工标注→LLM辅助过滤低价值/不可行任务→二次人工校验」流水线，共产出300个独立模板任务，含204个单站点、96个跨站点、79个音视频任务
- 评分采用DAG结构的多级校验机制：先通过后端状态查询、动作规则匹配做确定性校验，无法判定的再用LLM终审，同时支持部分完成度打分
### 关键结果
在12款模型、4类Agent架构上测试，最优的Codex（GPT 6.1 Sol）和Claude Code（Claude Opus 5.5）总体成功率仅为62.3%；跨站点任务比单站点成功率低10~25pct；无音视频工具时，强依赖音视频内容的任务成功率接近0。
### 核心结论
当前Web Agent在真实异构多模态、跨系统工作流场景下的能力仍有巨大缺口，可复现的标准化评测是Agent落地前的核心刚需。
