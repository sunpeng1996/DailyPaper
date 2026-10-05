---
title: 'EditHero: A Benchmark for Long-Horizon Part-Level 3D Editing and Vibe Modeling'
title_zh: EditHero：长时序部件级3D编辑与风格建模基准
authors:
- Ruihan Yu
- Yu-Ju Tsai
- Muyao Niu
- Runyi Li
- Lian Fu
- Hanqing Liu
- Zheng-Hui Huang
- Yonghao Yu
- Sho Kuno
- Ming-Hsuan Yang
affiliations:
- Alaya Lab
- The University of Tokyo
- Institute of Science Tokyo
- University of California, Merced
arxiv_id: '2610.02298'
url: https://arxiv.org/abs/2610.02298
pdf_url: https://arxiv.org/pdf/2610.02298
published: '2026-09-30'
collected: '2026-10-05'
category: Other
direction: 长时序3D编辑 · 智能体方法对比评测
tags:
- 3D Editing
- LLM Agent
- VLM
- Benchmark
- Iterative Generation
one_liner: 推出首个长时序部件级3D编辑基准，对比非智能体与LLM/VLM智能体编辑方案优劣
practical_value: '- 电商3D商品素材多轮迭代编辑场景，可复用LLM/VLM Agent底向上编辑思路，仅修改指定部件，避免全局重生成导致的无关内容漂移

  - 做多轮交互生成类任务（如用户多轮修改商品海报、定制3D商品）的效果评估时，可参考EditHero的基准构建逻辑，引入确定性校验引擎+人工标注的多轮测试序列，衡量方法的指令遵循度与不变区域保留能力

  - 业务选型可参考论文结论：非Agent端到端生成方法适合时延要求高、容错率高的场景；Agent方法适合编辑精度要求高、时延不敏感的场景（如高端定制3D商品建模）'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D编辑方法仅在单次编辑场景下评测，不符合实际生产中资产需经过多轮迭代修改、每轮仅改动指定部分、其余内容完全保留的真实需求。
### 方法关键点
1. 推出EditHero，业界首个长时序部件级3D编辑基准，覆盖几何、纹理两类编辑需求，配套自然语言指令、对应目标图像；内置确定性装配引擎可生成每轮编辑的精确目标，所有编辑序列均经过人工校验。
2. 基于该基准对比两类3D编辑方案：非Agent方法采用顶向下全局重生成逻辑，从学习到的3D表示中推断需要保留的内容；LLM/VLM Agent方法采用底向上逻辑，通过代码检查网格，仅重写指令要求修改的部件。
### 关键结果
非Agent方法常漏执行指定修改，且会干扰应保留的区域；多数LLM的指令遵循度更高，所有LLM对未编辑区域的保留效果更优，但单轮编辑耗时达分钟级。
