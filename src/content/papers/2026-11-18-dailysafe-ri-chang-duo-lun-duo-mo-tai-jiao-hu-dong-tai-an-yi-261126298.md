---
title: 'DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal
  Interactions'
title_zh: DailySafe：日常多轮多模态交互动态安全意识评估基准
authors:
- Xuankun Rong
- Xinhao Deng
- Wenzhang Jiang
- Ziheng Peng
- Siyuan Liang
- Wenke Huang
- Pablo Arbelaez
- Mang Ye
affiliations:
- Wuhan University
- Ant Group
- Tsinghua University
- Renmin University of China
- Nanyang Technological University
arxiv_id: '2611.26298'
url: https://arxiv.org/abs/2611.26298
pdf_url: https://arxiv.org/pdf/2611.26298
published: '2026-11-18'
collected: '2026-11-21'
category: Eval
direction: 多模态大模型 · 动态安全评估基准
tags:
- MLLM
- Safety Evaluation
- Multi-turn Interaction
- Multimodal
- Benchmark
one_liner: 推出覆盖10个日常领域的多轮多模态动态安全评估基准DailySafe，补齐静态安全评估场景缺口
practical_value: '- 可复用多轮动态风险识别的评估框架，优化电商导购Agent、客服MLLM的安全审核流程，规避用户多轮交互中的隐性合规风险

  - 可参考该基准的场景构建逻辑，为业务内多模态Agent定制针对性安全测试用例，覆盖日常交互下的非对抗性安全风险

  - 面向用户的生成式推荐Agent可借鉴动态安全感知思路，多轮对话中实时跟踪上下文风险，在满足需求的同时规避合规问题'
score: 6
source: huggingface-daily
depth: abstract
---

- 动机：现有MLLM安全基准多聚焦孤立有害请求或对抗场景，未覆盖日常合法任务多轮多模态交互中逐步暴露的隐性安全风险，缺少动态安全意识评估能力
- 方法关键点：构造DailySafe基准，覆盖10个日常领域、42类任务，包含195个自然多轮多图交互场景，基于真实用户对话主题和公开安全知识构建，安全标注随对话轮次、视觉信息动态更新，评估MLLM在支持用户合法目标的同时识别、应对动态风险的能力
- 关键结果：基准已完全开源，可直接用于MLLM日常场景安全能力评测，大幅拉近多模态安全评估与真实AI助手落地需求的差距
