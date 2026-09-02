---
title: 'PaperBanana-Interact: Scientific Diagram Refinement with Multi-Turn Human
  Feedback'
title_zh: PaperBanana-Interact：基于多轮人类反馈的科研图表精调系统
authors:
- Xueqing Wu
- Ashwin Balasubramanian
- Bingxuan Li
- Dawei Zhu
- Kai-Wei Chang
- Yale Song
- Yiwen Song
- Rui Meng
- Tomas Pfister
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- Google
- University of Illinois Urbana-Champaign
- Peking University
arxiv_id: '2608.30241'
url: https://arxiv.org/abs/2608.30241
pdf_url: https://arxiv.org/pdf/2608.30241
published: '2026-08-30'
collected: '2026-09-02'
category: Agent
direction: Agent 多轮交互生成优化
tags:
- MultiAgent
- Multi-Turn Generation
- User Simulator
- Feedback Alignment
- Multimodal Generation
- Benchmark
one_liner: 提出多Agent多轮科研图表精调框架及对应基准，解决多轮生成的质量漂移与遗忘问题
practical_value: '- 多轮交互生成场景可复用「内部 critique-refine 双Agent循环」架构，缓解多轮迭代的质量漂移和历史信息遗忘问题

  - 多轮系统评测阶段可引入用户模拟器生成自动化反馈，大幅降低真人标注成本，提升基准迭代效率

  - 电商场景多轮商品图/营销素材生成优化，可直接迁移本框架的反馈对齐与历史状态保留机制'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
前置14人用户研究显示，所有用户对初始生成的科研图表都有修改需求，86%认为精调后满意度更高，但现有多轮生成流程研究存在空白，基线系统普遍存在质量漂移、历史需求遗忘两大问题，且真人多轮标注成本高难以规模化评测。
### 方法关键点
1. 构建包含292张图像、3518条用户需求的多轮图表生成基准MTPaperBananaBench；
2. 设计自动用户模拟器，逐轮识别未满足需求并生成自然语言反馈，降低标注成本；
3. 提出多Agent系统PaperBanana-Interact，通过内部批评-精调闭环实现多轮迭代优化。
### 关键结果
相比基线系统，质量得分提升11.9~18.6分，遗忘率降低3.7~6.2分，多轮迭代中质量持续上升而非下降。
