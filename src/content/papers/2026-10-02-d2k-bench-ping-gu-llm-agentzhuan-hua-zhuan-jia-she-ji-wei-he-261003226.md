---
title: 'D2K-Bench: Can LLM Agents Turn Expert Designs into Efficient GPU Kernels?'
title_zh: D2K-Bench：评估LLM Agent转化专家设计为高效GPU内核的基准
authors:
- Daifeng Li
- Huiqiang Jiang
- Chengruidong Zhang
- Wei Wu
- Xudong Guo
- Jianhong Tu
- Jianwei Zhang
- Binhang Yuan
- Dayiheng Liu
affiliations:
- HKUST
- Alibaba Group
- USTC
arxiv_id: '2610.03226'
url: https://arxiv.org/abs/2610.03226
pdf_url: https://arxiv.org/pdf/2610.03226
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent GPU内核生成能力诊断评估
tags:
- LLM Agent
- GPU Kernel
- Benchmark
- Code Generation
- Expert Guidance
one_liner: 构建含三层专家指导的GPU内核生成诊断基准，量化指导对LLM Agent生成效果的提升
practical_value: '- 开发代码生成类Agent（如大模型推荐系统推理算子优化Agent）时，可复用L1算法/L2数据流/L3底层优化的三层分层指导范式，大幅提升生成代码的正确性和性能

  - 评估Agent代码生成能力时，可参考D2K-Bench的配对控制变量实验+LLM盲评代码实现度的评估框架，避免仅靠运行时指标评估的片面性

  - 对于需要优化LLM推理/训练算子的业务场景，可引入专家分层指导的Agent流程，仅付出30%左右的额外API成本即可获得超30%的算子性能提升'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent生成的GPU内核性能远低于专家实现，但仅靠运行时指标无法定位差距来自设计发现能力不足还是实现能力不足，现有基准也无法关联设计指导、实现细节和最终性能，无法为Agent优化提供明确方向。

### 方法关键点
- 构建包含26个LLM场景核心算子任务、85个负载的基准集，覆盖Attention、MoE、量化、采样等LLM训练推理常用算子
- 专家设计指导分为三层：L1高等级算法洞察、L2数据流设计、L3底层优化技巧，标注层级依赖关系，全程不提供专家源码
- 评估采用配对控制变量实验（有无指导两组其他条件完全一致），结合运行时性能指标+LLM盲评设计/实现完整度的评估体系，屏蔽运行时数据避免评估偏差

### 关键实验结果
在NVIDIA B200上测试5款主流大模型：
1. 130组模型-任务对的正确性从93.1%提升到98.5%
2. 整体性能得分从1.46提升到1.95，提升幅度33.9%
3. 三款全任务正确的前沿模型几何平均加速比从1.69×提升到2.49×，超过专家实现的2.33×水平
4. 整体实现完整度得分从57/100提升到70/100

### 核心结论
给LLM Agent提供分层的专家设计指导，是当前落地Agent代码生成任务投入产出比最高的路径之一
