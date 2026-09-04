---
title: 'Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation'
title_zh: 图景思考：面向推理驱动图像生成的系统化基准测试集
authors:
- Yutong Liu
- Nan Huang
- Xu Cao
- James M. Rehg
affiliations:
- University of Illinois Urbana-Champaign
- New York University
arxiv_id: '2609.02864'
url: https://arxiv.org/abs/2609.02864
pdf_url: https://arxiv.org/pdf/2609.02864
published: '2026-09-02'
collected: '2026-09-04'
category: Eval
direction: 多模态生成 · 推理能力评测基准
tags:
- Image Generation
- Reasoning
- Benchmark
- Unified Generative Models
- Multimodal Evaluation
one_liner: 推出覆盖4类认知领域的RIG-BENCH基准，系统性评测推理驱动图像生成能力
practical_value: '- 做电商商品定制化生成、营销场景图生成时，可复用RIG-BENCH的4类推理维度设计评测指标，避免生成局部合理但全局逻辑错误的素材（如尺寸错误、搭配违背物理规则）

  - 多模态Agent处理视觉推理任务（如用户发搭配需求生成穿搭图）时，可引入RIG-BENCH的测试样本做预上线校验，提升生成内容的逻辑合理性

  - 优化生成式多模态推荐的内容质量时，可参考该基准的压力测试思路，构建业务专属的推理类bad case样本库驱动模型迭代'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有统一生成模型（UGM）、世界模拟器仅依赖表层事件对齐，高层视觉推理能力被严重低估，无法满足「从视觉输入推理潜规则、输出符合逻辑约束的精准视觉结果」的推理生成需求，缺乏系统化的能力评测基准。
### 方法关键点
推出开源RIG-BENCH基准，系统性覆盖4类高认知难度的推理驱动图像生成（RIG）场景：概念类、变换类、模式结构类、场景类，共2000条人工筛选标注样本，可作为RIG任务的严格压力测试。
### 关键结果
对SOTA UGM、图像/视频生成模型的大规模评测显示存在显著的推理-生成gap：模型常输出局部视觉合理但全局逻辑矛盾的结果，该基准可作为诊断框架指导下一代逻辑对齐的UGM、世界模拟器研发。
